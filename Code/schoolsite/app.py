from models import Course


c1 = Course(
    title='C# for Beginner', 
    description='​សម្រាប់​អ្នក​ចង់ក្លាយជា​អ្នក​បង្កើត​កម្មវិធី និង គេហទំព័រដោយ​ប្រើ​ភាសា C# ។', 
    price=70, 
    duration=60, 
    requirements='C ឬ C++',
    syllabus='String, datetime')

c2 = Course(
    title='Programming with Python',
    price=70
)

print(c1.show_details())
print(c1)

print(c2.show_details())
print(c2)