class Human:
    def __init__(self, text):
        self.text = text

    def print_msg(self):
        print("Este "+self.text)

obj = Human("Man")
obj.print_msg()