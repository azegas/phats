class programming_languages():
    def __init__(self, difficulity, interest):
        self.difficulity = difficulity
        self.interest = interest

# both objects have different self which
# contain their attributes

    def tell_me_about_it(self):
        print("Difficulity is", self.difficulity)
        print("Interest is", self.interest)

python = programming_languages("lengva", "idomu")
javascript = programming_languages("sunku", "boring")

python.tell_me_about_it()       # same
programming_languages.tell_me_about_it(python)  # same

javascript.tell_me_about_it()   # same
programming_languages.tell_me_about_it(javascript)  # same


#############
# example 2 #
#############


class this_is_class:
    def __init__(in_place_of_self):
        print("we have used another parameter name in place of self")

object = this_is_class()
