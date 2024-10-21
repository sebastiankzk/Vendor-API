from app.database import SessionLocal
from app.models import user
from sqlalchemy.orm import Session

from app.models.vendor_profile import VendorProfile

class VendorProfileService:
    def __init__(self):
        self.db = SessionLocal()

    def get_vendor_profile(self, userId: int):
        try:
            vendor_profile = self.db.query(VendorProfile).filter(VendorProfile.userID == userId).first()
            if not vendor_profile:
                return None
            return vendor_profile
        except Exception as e:
            self.db.rollback()
            print(f"Error: {e}")
            raise e

    def get_all_vendors(self):
        try:
            vendor_profile_list = self.db.query(VendorProfile).all()
            if not vendor_profile_list:
                return None
            return vendor_profile_list
        except Exception as e:
            self.db.rollback()
            print(f"Error: {e}")
            raise e