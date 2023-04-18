class CourseExam:
    def __init__(self, course_name):
        self._course_name = course_name
        self._exam_list = []
        self._score = None

     def add_question_ans(self, questionlist):
        q_list = []
        for q , a in questionlist.questions:
             print(q)
             print(a)
             q_list.append(ExamItem(q[1], a[1]))
        self._exam_list.extend(q_list)

    def get_exams(self):
        return self._exam_list   
                             
class ExamItem:
     def __init__(self,question,answer):
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
     def __init__(self,username,course):
        self.__username = username
        self.__course = course
        self.__progression = None
        self.__exam = None
        self._indices = None
        
     def set_exam(self, exam):
          self.__exam = exam   
          
     def do_exam(self, student_answers):
          list_q = [q.get_ans() for q in self.__exam]
          # Check the index of each element in student_ans
          self._indices = [i for i in range(len(student_answers)) if student_answers[i] == list_q[i]]

     def get_progress(self):
          # Calculate the percentage of correct answerss
          percent_correct = (len(self._indices) / len(self.__exam)) * 100 if len(self._indices) > 0 else 0
          self.__progression = percent_correct
          return self.__progression
