class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"

def main():
    var= person("mohsen",20)
    var1=person("reza",4)
    var2=person("amirreza",17)
    var3=person("nader",21)
    print(var, var1, var2, var3, sep='\n', end='\n')
    print("name=", var.name, var1.name, var2.name, var3.name, sep=' ')
    print("age=", var.age, var1.age, var2.age, var3.age, sep=' ')
main()