"""
課題 継承
"""
class Boss:
  def __init__(self):
    self.kobun_salary = 200000
  def get_salary(self):
    return self.kobun_salary

class Kobun(Boss):
    def __init__(self):
      super().__init__()
    def show_my_salary(self):
      print("My salary is %d." % super().get_salary())

kobun = Kobun()
kobun.show_my_salary()