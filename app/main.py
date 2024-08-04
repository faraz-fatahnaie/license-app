import os

from fastapi import FastAPI, HTTPException, Depends, Header, Request
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from database import get_db
from schemas import CreateLicenseRequest, ActivateLicenseRequest, ValidateLicenseRequest
from crud import create_user, create_license, get_user_by_tarabari_id, get_license_by_activation_code
from utils import compare_dates
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()


@app.post("/api/create_license")
async def create_license_endpoint(request: CreateLicenseRequest,
                                  req: Request,
                                  db: Session = Depends(get_db)):
    api_key = str(os.getenv('REG_API_KEY'))
    if api_key != req.headers['REG_API_KEY']:
        raise HTTPException(status_code=401, detail="Unauthorized")

    tarabari_id = request.tarabari_id
    additional_days = request.additional_days

    user = get_user_by_tarabari_id(db, tarabari_id)
    if not user:
        user = create_user(db, tarabari_id)

    license = create_license(db, tarabari_id, additional_days)
    return {"activation_code": license.activation_code,
            "message": "License created. Activate it to set expiry date."}


@app.post("/api/activate_license")
async def activate_license_endpoint(request: ActivateLicenseRequest,
                                    req: Request,
                                    db: Session = Depends(get_db)):
    api_key = os.getenv('API_KEY')
    if api_key != req.headers['API_KEY']:
        raise HTTPException(status_code=401, detail="Unauthorized")

    activation_code = request.activation_code
    hardware_unique_id = request.hardware_unique_id

    license = get_license_by_activation_code(db, activation_code)
    if not license:
        raise HTTPException(status_code=404, detail="License not found")

    if license.status == 'active':
        return {"status": "success",
                "message": "License already activated",
                "start_date": license.activate_date,
                "duration": license.duration,
                "expiry_date": license.expiry_date}

    curr_datetime = datetime.now()

    license.status = 'active'
    license.activate_date = curr_datetime
    license.hardware_unique_id = hardware_unique_id
    license.expiry_date = curr_datetime + timedelta(days=license.duration)
    db.commit()

    return {"status": "success",
            "message": "License activated and hardware ID linked",
            "start_date": curr_datetime,
            "duration": license.duration,
            "expiry_date": license.expiry_date}


@app.post("/api/validate_license")
async def validate_license_endpoint(request: ValidateLicenseRequest,
                                    req: Request,
                                    db: Session = Depends(get_db)):
    api_key = os.getenv('API_KEY')
    if api_key != req.headers['API_KEY']:
        raise HTTPException(status_code=401, detail="Unauthorized")

    activation_code = request.activation_code
    hardware_unique_id = request.hardware_unique_id
    expiry_date = request.expiry_date

    license = get_license_by_activation_code(db, activation_code)
    curr_datetime = datetime.now().isoformat()

    if not license:
        raise HTTPException(status_code=404, detail="License not found")

    if license.status == 'inactive':
        raise HTTPException(status_code=400, detail="License is not activated yet")

    if license.hardware_unique_id != hardware_unique_id:
        raise HTTPException(status_code=400, detail="License is activated on another device.")

    activate_state, remaining_days = compare_dates(curr_datetime, expiry_date)

    if not activate_state:
        return {"status": "success",
                "message": "License is expired",
                "license_state": activate_state,
                "remaining_days": remaining_days}

    license.validation_count += 1
    db.commit()

    return {"status": "success",
            "message": f"License has {remaining_days} days remaining",
            "license_state": activate_state,
            "remaining_days": remaining_days}
