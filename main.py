def show_status(case_data):
    print(case_data["status"])

def open_case(case_data):
    if case_data["status"] == "NEW":
        print("This case is new")  
        case_data["status"] = "OPEN"   
    else:
        print("This case is not new")
               
case = {"title": "Review sample invoice", "description": "Fictional invoice", "status": "NEW"}

show_status(case)
open_case(case)    
show_status(case)