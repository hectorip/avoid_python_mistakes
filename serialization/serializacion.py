import pickle


class Person:
    def __init__(self, name="Fulano"):
        self.name = name


amigo_1 = Person("Héctor")
amigo_guardado = pickle.dumps(amigo_1)


class Person:
    def __init__(self, name="Fulano", age="33"):
        self.name = name
        self.age = age


amigo_2 = Person("Iván", 34)
amigo_recuperado = pickle.loads(amigo_guardado)

print(amigo_2.age)
print(amigo_recuperado.age)  # 'Person' object has no attribute 'age'
