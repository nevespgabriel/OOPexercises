from math import ceil

class Contact:
    def __init__(self, name, last_name,
                 phone=0, email='',
                 display_mode="masked"):
        self.name = name
        self.last_name = last_name
        self.display_mode = display_mode
        self.phone = phone
        self.email = email

    @staticmethod
    def _obfuscate(text):
        half_lenght = ceil(len(text)/2)
        return text[:half_lenght] + '*' * half_lenght

    def __repr__(self):
        if self.display_mode == "masked":
            return f"Contact(name={self._obfuscate(self.name)}, last_name={self._obfuscate(self.last_name)})"
        else:
            return f"Contact(name='{self.name}', last_name='{self.last_name}', email='{self.email}', phone={self.phone})"

    def __str__(self):
        return f"{self.last_name[0]+self.name[0]}"

    def __format__(self, format_spec):
        if format_spec == "masked":
            return f"Contact(name={self._obfuscate(self.name)}, last_name={self._obfuscate(self.last_name)})"
        else:
            return f"Contact(name='{self.name}', last_name='{self.last_name}', email='{self.email}', phone={self.phone})"

    def __eq__(self, other):
        if isinstance(other, Contact):
            if self.email == other.email and self.email != '':
                return True
            if self.phone == other.phone and self.phone != 0:
                return True
            return self.name == other.name and self.last_name == other.last_name
        else:
            return False

    def __hash__(self):
        return ((self.name, self.last_name))
