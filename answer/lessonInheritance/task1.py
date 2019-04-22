"""
課題 継承
"""
class Boss:
  def __init__(self):
    self.otakara = "お宝の在りかは大阪上本町の上の方だよ！"
  def show_otakara(self):
    print(self.otakara)

class Kobun(Boss):
    def __init__(self):
      super().__init__()

kobun = Kobun()
kobun.show_otakara()