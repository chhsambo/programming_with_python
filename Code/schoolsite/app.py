from models import *


csharp = Course(
    title='C# for Beginner', 
    price=70, 
    duration=60, 
    requirements='C ឬ C++',
    syllabus='String, datetime')

python = Course(
    title='Programming with Python',
    price=70,
    duration=48
)

csharp.description = 'C# is a modern programming created by Microsoft.'
print(csharp.description)
print(csharp.discount_price)
print(csharp.show_details())
print(f'C# weekend: {csharp.duration_weekend} weeks')
print(f'Python weekend: {python.duration_weekend} weeks')

# calculate how many weeks for csharp
# calculate how many weeks for python

cpp = ProgrammingCourse('C++', 59)
cpp.require_testing()