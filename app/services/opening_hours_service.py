from app.database import SessionLocal
from app.models import user
from sqlalchemy.orm import Session

from app.models.opening_hours import OpeningHours

class OpeningHoursService:
    def __init__(self):
        self.db = SessionLocal()

    def get_opening_hours(self, vendorProfileId : int):
        try:
            openinghours = self.db.query(OpeningHours).filter(OpeningHours.vendorProfileID == vendorProfileId).first()
            if not openinghours:
                return None
            return openinghours
        except Exception as e:
            self.db.rollback()
            print(f"Error: {e}")
            raise e
