from random import getrandbits, choice

class Virus:
    def __init__(self, name, reproduction_rate, resistance):
        self.name = name
        self.reproduction_rate = reproduction_rate
        self.load = 1
        self.host = None

    def infect(self, host):
        self.host = host

    def reproduce(self):
        if self.host is not None:
            self.load *= (1 + self.reproduction_rate)
            self.should_mutate = getrandbits(1)
            print(f'Should mutate = {self.should_mutate}')
            if self.should_mutate:
                try:
                    self.mutate()
                except AttributeError:
                    pass
            return True, f'Virus reproduced in {self.host}. Viral load =  {self.load}'

        raise AttributeError("The virus needs to infect a host before being able to reproduce.")


class RNAVirus(Virus):
    genome = 'ribonucleic'

    def reproduce(self): #defining this reproduce behaviour in the child class, we'll start by calling the parent class, and if our application is successful, we'll notify the user acordingly
        success, status = super().reproduce(self)

        if success:
            print(f'{self.name} just replicated in the citoplasm of {self.host} cells.') #everything that happens here is specific for RNAVirus


class DNAVirus(Virus):
    genome = 'deoxyribonucleic'

    def reproduce(self):
        success, status = super().reproduce(self)

        if success:
            print(f'{self.name} just replicated in the nucleus of {self.host} cells.')


class CoronaVirus(RNAVirus):
    pass


class SARSCov2(CoronaVirus):
    def mutate(self):
        print(f'The {self.name} virus just mutated its spike protein')


class FunnyDict(dict):
    not_found = ["404", "Wait, what?", "Try again, or don't!"]

    def __getitem__(self, item):
        if not item in self:
            return choice(self.not_found)
        return super().__getitem__(item)


population = FunnyDict({
    "CAN": 38,
    "USA": 329,
    "IND": 1380
})

#cv = SARSCov2("original", 2.9, 1.2)
#cv.infect("Tobi")
#for _ in range(4):
    #print(cv.reproduce(), "\n")
