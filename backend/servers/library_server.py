# This is the Library MCP Server
# It holds all book data and search logic

books_database = [
    {
        "id": 1,
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "available": True,
        "copies": 3,
        "location": "Section A, Shelf 2"
    },
    {
        "id": 2,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "available": True,
        "copies": 2,
        "location": "Section B, Shelf 1"
    },
    {
        "id": 3,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "available": False,
        "copies": 0,
        "location": "Section C, Shelf 4"
    },
    {
        "id": 4,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "available": True,
        "copies": 1,
        "location": "Section C, Shelf 1"
    },
    {
        "id": 5,
        "title": "Atomic Habits",
        "author": "James Clear",
        "available": False,
        "copies": 0,
        "location": "Section D, Shelf 3"
    }
]

def search_book(query: str):
    query = query.lower()
    results = []

    for book in books_database:
        if query in book["title"].lower() or query in book["author"].lower():
            results.append(book)

    if not results:
        return {"found": False, "message": f"No books found for '{query}'"}

    return {"found": True, "count": len(results), "books": results}

def get_all_books():
    return {"total": len(books_database), "books": books_database}