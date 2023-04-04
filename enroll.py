class Cart:
    def __init__(self):
        self.__cart = []

    def add_cart(self, will_enrolled):
        self.__cart.append(will_enrolled)

    def get_cart(self):
        return self.__cart

    def remove_cart(self, will_removed):
        self.__cart.remove(will_removed)

    def enrolled(self, user, cart):
        for i in cart:
            user.set_enrolled_course('enroll', i)


class Enroll:
    def __init__(self, will_enrolled, enrolled):
        self.__will_enrolled = will_enrolled
        self.__enrolled = enrolled

    def check_enroll(self):
        if self.__will_enrolled in self.__enrolled:
            return False
        else:
            return True
