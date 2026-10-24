def show_status(case_data):
    print(case_data["status"])

def open_case(case_data):
    if case_data["status"] == "NEW":
        print("This case is new")  
        case_data["status"] = "OPEN"   
    else:
        print("This case is not new")

def get_status(case_data):
    return case_data["status"]

case_a = {"title": "Review sample invoice", "description": "Fictional invoice", "status": "NEW"}
case_b = {"title": "Another sample invoice", "description": "Imaginary invoice", "status": "NEW"}

open_case(case_a)
show_status(case_a)
show_status(case_b)

open_case(case_b)
show_status(case_a)
show_status(case_b)

status_a = get_status(case_a)
if status_a == "OPEN":
    print("This case is ready for processing")