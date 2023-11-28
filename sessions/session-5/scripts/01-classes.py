# Definir une classe:
class Etudiant:
    def __init__(self, name, age = 18, **kwargs) -> None:
        self.name = name
        self.age = age
        self.note_histoire = kwargs.get("note_histoire", 10)
        self.note_maths = kwargs.get("note_maths", 10)
        self.note_francais = kwargs.get("note_francais", 10)

    def get_info(self) -> str:
        return f"{self.name} a {str(self.age)} ans."
    
    def get_average(self) -> int:
        return (self.note_histoire + self.note_maths + self.note_francais) / 3

# Une sous classe:
class EtudiantES(Etudiant):
    def __init__(self, name, age=18, **kwargs) -> None:
        super().__init__(name, age, **kwargs)

        self.note_ses = kwargs.get("note_ses", 10)

    def get_average(self) -> int:
        return (super().get_average() + self.note_ses) / 2


# Créer des instance d'une classe:
etudiant1 = Etudiant("Bob", 18)
etudiant2 = EtudiantES("Jacob", note_maths = 20)

# Changer des attributs:
etudiant1.age = 25

# Utiliser des méthodes:
print(etudiant1.get_info())
print(etudiant2.get_info())

print(etudiant1.get_average())
print(etudiant2.get_average())