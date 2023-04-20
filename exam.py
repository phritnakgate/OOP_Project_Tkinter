class CourseExam:
    def __init__(self, course_name):
        self._course_name = course_name
        self._exam_list = []
        self._score = None

    def add_question_ans(self, questionlist):
        q_list = []
        for q , a in questionlist.questions:
             q_list.append(ExamItem(q[1], a[1]))
        self._exam_list.extend(q_list)

    def get_exams(self):
        return self._exam_list   
   
    def edit_exam(self, number, body:dict):
          if(number <= len(self._exam_list)):
               self._exam_list[number-1].set_ques(body['question'])
               self._exam_list[number-1].set_ans(body['answer'])
               return {'Exam Updated'}
          else:         
               return {'Not found'}     

class ExamItem:
    def __init__(self, question, answer):
        self.__question = question
        self.__answer = answer

    def get_ques(self):
        return self.__question

    def get_ans(self):
        return self.__answer

    def set_ques(self, q):
        self.__question = q

    def set_ans(self, a):
        self.__answer = a


class CourseProgression:
    def __init__(self, username, course):
        self.__username = username
        self.__refcode = refcode
        self.__progression = None
        self.__exam = None
        
     def set_exam(self, exam):
          self.__exam = exam   
          
     def do_exam(self, student_answers):
          list_q = [q.get_ans() for q in self.__exam]
          # Check the index of each element in student_ans
          x = [i for i in range(len(student_answers)) if student_answers[i] == list_q[i]]
          percent_correct = (len(x) / len(self.__exam)) * 100 if len(x) > 0 else 0
          self.__progression = percent_correct
          
     def get_progress(self): 
          return self.__progression
     
     def get_refcode(self):
          return self.__refcode
