from pydantic import BaseModel


class CreateLicenseRequest(BaseModel):
    tarabari_id: str
    additional_days: int


class ActivateLicenseRequest(BaseModel):
    activation_code: str
    hardware_unique_id: str


class ValidateLicenseRequest(BaseModel):
    activation_code: str
    hardware_unique_id: str
    expiry_date: str
