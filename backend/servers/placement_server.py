placement_data = [
    {
        "company": "Infosys",
        "package": "6 LPA",
        "date": "20 July 2026",
        "eligibility": "60% throughout academics"
    },
    {
        "company": "TCS",
        "package": "7 LPA",
        "date": "25 July 2026",
        "eligibility": "65% throughout academics"
    },
    {
        "company": "Wipro",
        "package": "5.5 LPA",
        "date": "28 July 2026",
        "eligibility": "60% throughout academics"
    },
    {
        "company":"Google",
        "package":"45 LPA",
        "date":"15 August 2026",
        "eligibility":"8 CGPA"
    }
]


def get_all_placements():
    return placement_data


def search_company(company):
    company = company.lower()

    for drive in placement_data:
        if company in drive["company"].lower():
            return drive

    return {"message": "Company not found"}


def get_company_package(company):
    company = company.lower()

    for drive in placement_data:
        if company in drive["company"].lower():
            return {
                "company": drive["company"],
                "package": drive["package"]
            }

    return {"message": "Package not found"}