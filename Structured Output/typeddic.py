from typing import TypedDict, List
class Person(TypedDict):
    name: str
    age: int
    hobbies: List[str]
    
new_person: Person = {
    'name': 'Alice', 
    'age': 30, 
    'hobbies': ['reading', 'hiking', 'coding']  
}  
print(new_person) 