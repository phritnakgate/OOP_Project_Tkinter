class Review:
    def __init__(self, user, write_review, write_comment):
        self.__user = user
        self.__write_review = write_review
        self.__write_comment = write_comment
        
    def get_write_review(self):
        return self.__write_review

    def get_write_comment(self):
        return self.__write_comment