# Cafeteria MCP Server

menu = {
    "monday": {
        "breakfast": ["Poha", "Chai", "Banana"],
        "lunch": ["Dal Rice", "Paneer Butter Masala", "Roti", "Salad"],
        "dinner": ["Chole", "Rice", "Roti", "Raita"]
    },
    "tuesday": {
        "breakfast": ["Idli", "Sambar", "Coconut Chutney"],
        "lunch": ["Rajma Rice", "Mix Veg", "Roti"],
        "dinner": ["Dal Makhani", "Jeera Rice", "Naan"]
    },
    "wednesday": {
        "breakfast": ["Paratha", "Curd", "Pickle"],
        "lunch": ["Kadhi Rice", "Aloo Gobi", "Roti"],
        "dinner": ["Palak Paneer", "Rice", "Roti"]
    },
    "thursday": {
        "breakfast": ["Upma", "Chai", "Boiled Eggs"],
        "lunch": ["Sambar Rice", "Rasam", "Papad"],
        "dinner": ["Matar Mushroom", "Roti", "Rice", "Salad"]
    },
    "friday": {
        "breakfast": ["Puri Bhaji", "Chai"],
        "lunch": ["Veg Biryani", "Raita", "Papad"],
        "dinner": ["Paneer Tikka", "Butter Naan", "Dal"]
    },
    "saturday": {
        "breakfast": ["Dosa", "Sambar", "Chutney"],
        "lunch": ["Special Thali", "Sweet"],
        "dinner": ["Fried Rice", "Manchurian", "Soup"]
    },
    "sunday": {
        "breakfast": ["Chole Bhature", "Lassi"],
        "lunch": ["Special Sunday Meal", "Kheer"],
        "dinner": ["Roti", "Dal", "Rice", "Ice Cream"]
    }
}

timings = {
    "breakfast": "7:30 AM - 9:30 AM",
    "lunch": "12:00 PM - 2:30 PM",
    "dinner": "7:00 PM - 9:30 PM"
}

def get_menu_by_day(day: str):
    day = day.lower()
    if day not in menu:
        return {"found": False, "message": f"No menu found for '{day}'"}
    return {"day": day, "menu": menu[day], "timings": timings}

def get_timings():
    return {"timings": timings}