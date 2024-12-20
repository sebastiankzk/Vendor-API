from fastapi import APIRouter, HTTPException
from app.controllers.vendor_controller import VendorController

router = APIRouter()
vendor_controller = VendorController()

# Vendor Profile
@router.get("/vendor_profile/get/{user_id}")
def get_vendor(user_id: int):
    vendor_profile = vendor_controller.get_vendor_profile(user_id)
    if vendor_profile is None:
        raise HTTPException(status_code=404, detail="Vendor profile not found")
    return vendor_profile

# All Vendor Profile
@router.get("/vendor_profile/get/all/")
def get_all_vendors():
    vendor_profile = vendor_controller.get_all_vendors()
    if vendor_profile is None:
        raise HTTPException(status_code=404, detail="Vendor profile not found")
    return vendor_profile

# Vendor Menu by user id
@router.get("/menu_items/get/user_id/{user_id}", description="Retrieve menu items for vendor")
def get_menu_items_by_user_id(user_id: int):
    menu = vendor_controller.get_menu_items_by_user_id(user_id)
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return menu

# Vendor Menu by vendor id
@router.get("/menu_items/get/{vendor_profile_id}", description="Retrieve menu items for vendor")
def get_menu_items_by_vendor_id(vendor_profile_id: int):
    menu = vendor_controller.get_menu_items_by_vendor(vendor_profile_id)
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return menu   

# Vendor promotion
@router.get("/promotion/get/{user_id}", description="Retrieve promotions for vendor")
def get_promotion(user_id: int):
    try:
        promotion = vendor_controller.get_promotions(user_id)
    except Exception as ex:
        raise HTTPException(status_code=404, detail="promotion not found")
    return promotion

# Vendor opening hours
@router.get("/opening_hours/get/{user_id}", description="Retrieve opening hours for vendor")
def opening_hours(user_id: int):
    try:
        openinghours = vendor_controller.get_opening_hours(user_id)
    except Exception as ex:
        raise HTTPException(status_code=404, detail="promotion not found")
    return openinghours