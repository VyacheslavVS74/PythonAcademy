class Student:
    def __init__(self, name, model, cpu, ram):
        self.name = 'Roman'
        self.ps = self.Ps(model, cpu, ram)

    def show(self):
        print(self.name, '=>', end=' ')

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    class Ps:
        def __init__(self, model, cpu, ram):
            self.model = model
            self.cpu = cpu
            self.ram = ram

        def display(self):
            print(self.model, self.cpu, self.ram)


st = Student('Roman', 'HP', 'i7', 16)  #
st.show()
d1 = st.ps
d1.display()

st.set_name('Vladimir')

st.show()
d1.display()


