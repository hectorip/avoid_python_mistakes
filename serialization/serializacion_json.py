import json


class Person:
    def __init__(self, name="Fulano"):
        self.name = name


amigo_1 = Person("Héctor")

# ni modo, más trabajo
amigo_guardado = json.dumps({"name": amigo_1.name})


class Person:
    def __init__(self, name="Fulano", age="33"):
        self.name = name
        self.age = age


amigo_2 = Person("Iván", 34)
# igual más trabajo
amigo_recuperado_data = json.loads(amigo_guardado)
amigo_recuperado = Person(amigo_recuperado_data["name"])


print(amigo_2.age)
print(amigo_recuperado.age)  # 'Person' object has no attribute 'age'
