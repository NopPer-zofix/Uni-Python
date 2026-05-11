
class B1:
    __name  = "Name"
    def __init__(self, i, word):
        self.value = i
        self.name = word

    def laugh(self):
        print(f"so funny, u -{self.name}, re retard {self.value}")

    def __str__(self):
        return "what do you want?"

line = []


# with open("text.txt", 'r') as f:
#     print([line.rstrip() for line in f.readlines()])


# a =["12", "11", "13"]
# a[0] =  'erre'
# b = [i + "wew" for i in a]
# print(b)


str(B1)
a = B1(12, "Alex")
print(a.value)
a.laugh()