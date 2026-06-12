academic_data = {
    "attendance": "Minimum 75% attendance is required to appear for semester examinations.",

    "mid_semester": "Mid Semester Exams start on 15 August 2026.",

    "end_semester": "End Semester Exams start on 10 December 2026.",

    "dbms": "DBMS syllabus includes ER Models, Relational Algebra, SQL, Normalization, Transactions and Indexing.",

    "python": "Python syllabus includes Variables, Functions, OOP, File Handling and Exception Handling."
}


def get_attendance_rule():
    return academic_data["attendance"]


def get_exam_schedule():
    return {
        "mid_semester": academic_data["mid_semester"],
        "end_semester": academic_data["end_semester"]
    }


def get_subject_syllabus(subject):
    return academic_data.get(
        subject.lower(),
        "Syllabus not available."
    )