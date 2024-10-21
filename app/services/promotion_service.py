from app.database import SessionLocal
from app.models import user
from sqlalchemy.orm import Session

from app.models.promotion import Promotion

class PromotionService:
    def __init__(self):
        self.db = SessionLocal()

    def get_promotions_for_vendor(self, vendorProfileID: int):
        try:
            promotion = self.db.query(Promotion).filter(Promotion.vendorProfileID == vendorProfileID, Promotion.isValid).first()
            if not promotion:
                return None
            return promotion
        except Exception as e:
            self.db.rollback()
            print(f"Error: {e}")
            raise e
