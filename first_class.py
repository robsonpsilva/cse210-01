class Person:
    '''A code template for the category of things known as Person. The
    responsibility of a Person is to hold and display personal information.
    '''

    def __init__(self):
        '''A special method, called a constructor, that initializes two
        attributes. It is invoked using the class name followed by parentheses.
        '''
        self.given_name = ""
        self.family_name = ""

    def show_eastern_name(self):
        '''A method that displays the person's full name as used in eastern 
        countries or <family name, given name>.
        '''
        print(f"{self.family_name}, {self.given_name}")

    def show_western_name(self):
        '''A method that displays the person's full name as used in western
        countries or <given name family name>.
        '''
        print(f"{self.given_name} {self.family_name}")