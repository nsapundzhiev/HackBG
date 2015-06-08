class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender
        """if check_email:
                                    self.email = email
                                else:
                                    raise ValueError("Not Valid email!")
                                self.list_of_friends = []"""

    def name(self):
        return self.name

    def email(self):
        return self.email

    def gender(self):
        return self.gender

    def __str__(self):
        return "The panda {} is {}.".format(self.name, self.gender)

    def __eq__(self, other):
        equal_names = self.name == other.name
        equal_emails = self.email == other.email
        equal_genders = self.gender == other.gender
        return equal_emails and equal_genders and equal_names

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def isMale(self):
        return self.gender == "male"

    def isFemale(self):
        return self.gender == "female"
