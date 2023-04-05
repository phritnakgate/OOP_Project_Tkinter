class CourseExam:
     def __init__(self, course_name):
        self._course_name = course_name
        self._exam_list = []
     
     def add_question_ans(self, questionlist):
          self._exam_list.extend(questionlist)
          
     def show_exam(self):
          for i, question in enumerate(self._exam_list):
               print(f"{i+1}. {question['question']}")
          
     def do_exam(self, student_answers):
          score = 0
          for i, question in enumerate(self._exam_list):
               if student_answers[i].lower() == question['answer'].lower():
                    score += 1
          return score

class ExamItem:
     def __init__(self,question,answer):
          self.__question = question
          self.__answer = answer
            
class CouseProgression:
    def __init__(self):
        pass
