import os
import json
from groq import Groq
from dotenv import load_dotenv
from servers.library_server import search_book, get_all_books
from servers.cafeteria_server import get_menu_by_day, get_timings
from servers.events_server import get_all_events, get_events_by_category, search_event
from servers.academic_server import(
    get_attendance_rule,
    get_exam_schedule,
    get_subject_syllabus
)
from servers.placement_server import (
    get_all_placements,
    search_company,
    get_company_package
)  
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Define tools — these tell the AI what functions it can call
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_book",
            "description": "Search for a book in the campus library by title or author name",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The book title or author name to search for"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_menu_by_day",
            "description": "Get the cafeteria menu for a specific day of the week",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "string",
                        "description": "Day of the week e.g. monday, tuesday"
                    }
                },
                "required": ["day"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_timings",
            "description": "Get cafeteria opening and closing timings",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_event",
            "description": "Search for campus events by name or keyword",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Event name or keyword to search"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_events_by_category",
            "description": "Get campus events filtered by category like technical, cultural, sports, workshop",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Category: technical, cultural, sports, workshop"
                    }
                },
                "required": ["category"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_all_events",
            "description": "Get all upcoming campus events",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name":"get_attendance_rule",
            "description":"Get attendamce requirements"
        }
    },
    {
        "type":"function",
        "function":{
            "name":"get_exam_schedule",
            "description":"Get_exam_schedule"
        }
    },
    {
    "type": "function",
    "function": {
        "name": "get_subject_syllabus",
        "description": "Get syllabus for a subject",
        "parameters": {
            "type": "object",
            "properties": {
                "subject": {
                    "type": "string",
                    "description": "Subject name"
                }
            },
            "required": ["subject"]
        }
    }
    },
    {
    "type": "function",
    "function": {
        "name": "get_all_placements",
        "description": "Get all placement drives",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
    },
    {
    "type": "function",
    "function": {
        "name": "search_company",
        "description": "Search placement drive by company name",
        "parameters": {
            "type": "object",
            "properties": {
                "company": {
                    "type": "string"
                }
            },
            "required": ["company"]
        }
    }
    },
    {
    "type": "function",
    "function": {
        "name": "get_company_package",
        "description": "Get package offered by a company",
        "parameters": {
            "type": "object",
            "properties": {
                "company": {
                    "type": "string"
                }
            },
            "required": ["company"]
        }
    }
    },
]


# Map function names to actual Python functions
function_map = {
    "search_book": lambda args: search_book(args["query"]),
    "get_menu_by_day": lambda args: get_menu_by_day(args["day"]),
    "get_timings": lambda args: get_timings(),
    "search_event": lambda args: search_event(args["query"]),
    "get_events_by_category": lambda args: get_events_by_category(args["category"]),
    "get_all_events": lambda args: get_all_events(),

    "get_attendance_rule": lambda args: get_attendance_rule(),

    "get_exam_schedule": lambda args: get_exam_schedule(),

    "get_subject_syllabus": lambda args: get_subject_syllabus(
        args["subject"]
    ),
    "get_all_placements": lambda args: get_all_placements(),
    "search_company": lambda args: search_company(
        args["company"]
    ),
    "get_company_package": lambda args: get_company_package(
          args["company"]
    ),

}

def ask_campus_ai(question: str):
    messages = [
        {
            "role": "system",
            "content": """You are a helpful campus assistant for a college. 
            You help students find information about the library, cafeteria, and campus events.
            Always be friendly and give clear, concise answers.
            Use the available tools to fetch real data before answering."""
        },
        {
            "role": "user",
            "content": question
        }
    ]

    # First call — AI decides which tool to use
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    response_message = response.choices[0].message

    # If AI wants to call a tool
    if response_message.tool_calls:
        tool_call = response_message.tool_calls[0]
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        # Actually call the function
        tool_result = function_map[function_name](function_args)

        # Send result back to AI for final answer
        messages.append({"role": "assistant", "content": None, 
                         "tool_calls": response_message.tool_calls})
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(tool_result)
        })

        final_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        return {
            "question": question,
            "tool_used": function_name,
            "answer": final_response.choices[0].message.content
        }

    # If AI answered directly without tool
    return {
        "question": question,
        "tool_used": "none",
        "answer": response_message.content
    }