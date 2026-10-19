case = {"title": "Review sample invoice", "description": "Fictional invoice", "status": "CLOSED"}
if case["status"] == "NEW":
    print("This case is new")  
    case["status"] = "OPEN"   
else:
    print("This case is not new")
    
print(case["status"])