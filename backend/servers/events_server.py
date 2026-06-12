# Events MCP Server

events = [
    {
        "id": 1,
        "name": "Tech Fest 2026",
        "category": "technical",
        "date": "June 20, 2026",
        "time": "10:00 AM",
        "venue": "Main Auditorium",
        "description": "Annual technical festival with coding competitions and workshops",
        "registration_open": True
    },
    {
        "id": 2,
        "name": "AI/ML Workshop",
        "category": "workshop",
        "date": "June 15, 2026",
        "time": "2:00 PM",
        "venue": "CS Department Lab",
        "description": "Hands-on workshop on Machine Learning fundamentals",
        "registration_open": True
    },
    {
        "id": 3,
        "name": "Cultural Night",
        "category": "cultural",
        "date": "June 22, 2026",
        "time": "6:00 PM",
        "venue": "Open Air Theatre",
        "description": "Annual cultural evening with music, dance and drama",
        "registration_open": False
    },
    {
        "id": 4,
        "name": "Hackathon 2026",
        "category": "technical",
        "date": "June 28, 2026",
        "time": "9:00 AM",
        "venue": "Innovation Centre",
        "description": "24-hour hackathon open to all students",
        "registration_open": True
    },
    {
        "id": 5,
        "name": "Sports Meet",
        "category": "sports",
        "date": "July 1, 2026",
        "time": "8:00 AM",
        "venue": "Sports Ground",
        "description": "Inter-department sports competition",
        "registration_open": True
    }
]

def get_all_events():
    return {"total": len(events), "events": events}

def get_events_by_category(category: str):
    category = category.lower()
    filtered = [e for e in events if e["category"] == category]
    if not filtered:
        return {"found": False, "message": f"No events found for category '{category}'"}
    return {"found": True, "count": len(filtered), "events": filtered}

def search_event(query: str):
    query = query.lower()
    results = [e for e in events if query in e["name"].lower() 
               or query in e["description"].lower()]
    if not results:
        return {"found": False, "message": f"No events found for '{query}'"}
    return {"found": True, "count": len(results), "events": results}