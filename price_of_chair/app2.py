import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['full_stack']
collection = database['students']

# students = collection.find({})
# student_list = []
# for student in students:
#     student_list.append(student)
# print(student_list)

# students = [student for student in collection.find({})]
# print(students)
# students_mark = [student['mark'] for student in collection.find({})]
# print(students_mark)
# students_high_mark = [student['mark'] for student in collection.find({}) if student['mark'] == 100]
# print(students_high_mark)

collection.insert({"name": "Kelly", "mark": 200})
collection.insert({"name": "Eric", "mark": 300})
collection.insert({"name": "Melly", "mark": 250})