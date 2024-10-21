from app.database import SessionLocal
from app.models import user
from sqlalchemy.orm import Session

from app.models.menu_item import MenuItem
from app.models.vendor_profile import VendorProfile

class MenuService:
    def __init__(self):
        self.db = SessionLocal()

    def get_menu_items_for_vendor(self, vendorProfileId: int):
        try:
            menu =  self.db.query(MenuItem).filter(MenuItem.vendorProfileID == vendorProfileId).all()
            if not menu:
                return None
            return menu
        except Exception as e:
            self.db.rollback()
            print(f"Error: {e}")
            raise e