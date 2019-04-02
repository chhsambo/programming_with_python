from enums import *

class Course:
    school = 'ANT Training'

    def __init__(self, title, price, duration=None, syllabus=None, requirements=None):
        self.title = title
        self.price = price
        self.duration = duration
        self.syllabus = syllabus
        self.requirements = requirements

    def __str__(self):
        return f'<Course: {self.title}>'

    @property
    def discount_price(self):
        discount = self.price * DISCOUNT
        return self.price - discount

    @property
    def duration_weekend(self):
        weeks = self.duration // STUDY_HOURS_WEEKEND
        return weeks

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    def show_details(self):
        print(
            f'{self.title}\n'
            f'Price: {self.price}\n'
            f'Duration: {self.duration}\n'
        )


class ProgrammingCourse(Course):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def require_testing(self):
        print('Please come to our center to test')


class WebDevelopment(Course):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        