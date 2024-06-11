from random import choice
from string import ascii_letters, punctuation, digits

class Password:
    chars = {
        'letters': [],
        'numbers': [],
        'punctuation': []
    }

    def __init__(self, strength='mid', length=0):
        self.key = ''
        self.strength = strength
        self.generate()
        if length != 0:
            self.length = length
        self.key = self.password()


    def generate(self):
        if self.strength == 'low':
            self.length = 8
            self.characters = ascii_letters
        elif self.strength == 'mid':
            self.length = 12
            self.characters = digits+ascii_letters
        elif self.strength == 'high':
            self.length = 16
            self.characters = punctuation+ascii_letters+digits
        else:
            print("INVALID VALUE TO STRENGHT")


    def password(self):
        key = ''
        for c in range(0,self.length):
            key += choice(self.characters)
        for c in self.key:
            if c in ascii_letters:
                self.chars['letters'].append(c)
            elif c in digits:
                self.chars['numbers'].append(c)
            elif c in punctuation:
                self.chars['punctuation'].append(c)
        return key


    @classmethod
    def show_input_universe(cls):
        return cls.chars


m1 = Password('mid', 15)
m1.password()
m2 = Password('high')
m2.password()
print(m1.key, m2.key)


