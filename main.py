def show_status(case_data):
    print(case_data["status"])

def open_case(case_data):
    if is_new_case(case_data):
        case_data["status"] = "OPEN"
        return True
    else:
        return False    

def get_status(case_data):
    return case_data["status"]

def is_new_case(case_data):
    return case_data["status"] == "NEW"

def create_case(title,description=""):
    if not isinstance(title, str):
        raise TypeError("Title must be a string")
    
    title = title.strip()
    
    if title == "":
        raise ValueError("Title cannot be empty")

    if not isinstance(description, str):
        raise TypeError("Description must be a string")
    
    case_data = {
        "title": title,
        "description": description,
        "status": "NEW"
    }
    return case_data

case_a = create_case("  Review sample invoice  ", "Fictional invoice")
case_b = create_case("Check sample delivery", "Fictional delivery")

print(case_a)
print(case_b)

opening_succeeded = open_case(case_a)
if opening_succeeded:
    print("The case was opened successfully")
else:
    print("The case was not opened successfully")

second_opening_succeeded = open_case(case_a)
if second_opening_succeeded:
    print("The case was opened successfully")
else:
    print("The case was not opened successfully")

open_case(case_a)
show_status(case_a)
show_status(case_b)

open_case(case_b)
show_status(case_a)
show_status(case_b)

status_a = get_status(case_a)
if status_a == "OPEN":
    print("This case is ready for processing")
    
try:
    print(create_case("Review invoice"))
except ValueError as error:
    print("Case creation failed:", error)
except TypeError as error:
    print("Case creation failed:", error)
    
print("Validation check completed")