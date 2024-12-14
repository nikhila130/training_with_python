class Paint:
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def details(self,opacity:int):
        print("this is {self.color} paint and it is of {self.type} medium paint and has a default opacity of {self.opacity}")
        self.opacity = opacity
colour1=Paint( color :"cyan",type:"watercolours")
colour2=Paint( color :"blue",type:"gouchae")

colour1.details(120)
colour2.details()