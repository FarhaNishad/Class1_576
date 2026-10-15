from fastapi import FastAPI
app = FastAPI(title="farha")

students = [
    {"id" : 1, "name":"a", "dept":"python"},
    {"id" : 2, "name":"b", "dept":"c"},
    {"id" : 3, "name":"c", "dept":"java"},
    {"id" : 4, "name":"d", "dept":"python"},
    {"id" : 5, "name":"e", "dept":"c"}
]

#path paarmeters
@app.get("/students/{student_id}")

def get_student_id(student_id:int):
    print(student_id)
    print(type("id"))
    for i in students:
        if i["id"] == student_id:
            return i
        return{"msg":"id is invalid"}

# if i givr the dept name,i want all the students in tthat dept

@app.get("/students")
def get_student_id(dept:str):
    result = []
    for i in students:
        if i["dept"]  == dept:
            result.append(i)
        return result

    
        

@app.get("/")
def home():
    return {"message" : "Hi FastAPI" }

@app.get("/name")
def name():
    return {"batch -576"}

            