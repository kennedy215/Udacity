class Parent():
    def __init__(self,last_name,eye_color):
        #print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name -"+self.last_name)
        print("Eye Color -"+self.eye_color)

class Child(Parent):
    ("child constructor called")
    def __init__(self,last_name,eye_color,fighting_style):
        Parent.__init__(self,last_name,eye_color)
        self.fighting_style = fighting_style

#test normall this would be in a seperate file... Example is not on a seperate
#file

