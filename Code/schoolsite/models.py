class Course:

    def __init__(self, title, price, duration=None, description=None, syllabus=None, requirements=None):
        self.title = title
        self.price = price
        self.duration = duration
        self.description = description
        self.syllabus = syllabus
        self.requirements = requirements

    def __str__(self):
        return f'<Course: {self.title}>'

    def show_details(self):
        print(
            f'{self.title}\n'
            f'Price: {self.price}\n'
            f'Duration: {self.duration}\n'
        )