import json

dict = {
    "state" : "karnataka ", "capital" : "banglore",
    "state" : "maharashtra", "capital" : "mumbai",
    "state" : "telangana",  "caital" : "hyderabad",
    "state" : "tamil nadu", "capital" : "chennai",
    "state" : "andra pradesh", "capital" : "amaravati",
    "state" : "kerala", "capital" : "thiruvanantapuram",
    "state" : "uttar pradesh", "capital" : "lucknow"
}

json_obj = json.dumps(dict, indent=8)
print(json_obj)