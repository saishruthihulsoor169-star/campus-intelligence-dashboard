from servers.academic_server import get_attendance_rule, get_exam_schedule, get_subject_syllabus
from servers.placement_server import get_all_placements, search_company, get_company_package
from ai_brain import ask_campus_ai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from servers.library_server import search_book, get_all_books
from servers.cafeteria_server import get_menu_by_day, get_timings
from servers.events_server import get_all_events, get_events_by_category, search_event

app = FastAPI(title="Campus Intelligence Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Campus Dashboard is running!"}

# Library routes
@app.get("/library/books")
def all_books():
    return get_all_books()

@app.get("/library/search")
def search(book: str):
    return search_book(book)

# Cafeteria routes
@app.get("/cafeteria/menu")
def menu(day: str):
    return get_menu_by_day(day)

@app.get("/cafeteria/timings")
def cafe_timings():
    return get_timings()

# Events routes
@app.get("/events/all")
def all_events():
    return get_all_events()

@app.get("/events/category")
def events_by_category(category: str):
    return get_events_by_category(category)

@app.get("/events/search")
def events_search(query: str):
    return search_event(query)
@app.get("/ask")
def ask(question: str):
    return ask_campus_ai(question)