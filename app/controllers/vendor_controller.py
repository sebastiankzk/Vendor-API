from app.models.menu_item import MenuItem
from app.models.promotion import Promotion

from app.services.vendor_profile_service import VendorProfileService
from app.services.menu_service import MenuService
from app.services.promotion_service import PromotionService
from app.services.opening_hours_service import OpeningHoursService

class VendorController:
    def __init__(self):
        self.vendor_service = VendorProfileService()
        self.menu_service = MenuService()
        self.promotion_service = PromotionService()
        self.opening_hours = OpeningHoursService()

    def get_vendor_profile(self, userId: int):
        return self.vendor_service.get_vendor_profile(userId)
    
    def get_all_vendors(self):
        return self.vendor_service.get_all_vendors()

    def get_menu_items_by_user_id(self, userId: int):
        user_profile = self.vendor_service.get_vendor_profile(userId)
        if (user_profile is None):
            return []
        
        menuItems = self.menu_service.get_menu_items_for_vendor(user_profile.vendorProfileID)

        if len(menuItems) < 1:
            return []

        result: list[MenuItem] = []
        for i in menuItems:
            item : MenuItem = i
            result.append(item)
            
        return result

    def get_menu_items_by_vendor(self, vendorProfileId: int):
        menuItems = self.menu_service.get_menu_items_for_vendor(vendorProfileId)

        if len(menuItems) < 1:
            return []

        result: list[MenuItem] = []
        for i in menuItems:
            item : MenuItem = i
            result.append(item)
            
        return result

    def get_promotions(self, userId: int):
        user_profile = self.vendor_service.get_vendor_profile(userId)
        if (user_profile is None):
            return []
        promo = self.promotion_service.get_promotions_for_vendor(user_profile.vendorProfileID)
        if (promo is None):
            return []

        return promo
    
    def get_opening_hours(self, userId: int):
        user_profile = self.vendor_service.get_vendor_profile(userId)        
        if (user_profile is None):
            return []
        openinghours = self.opening_hours.get_opening_hours(user_profile.vendorProfileID)
        if (openinghours is None):
            return []

        return openinghours
    