class DNABase:
    valid_bases = {'a':'adenine',
                   'c':'cytosine',
                   'g':'guanine',
                   't':'thymine'}

    def __init__(self, nucleotide):
        self.base = nucleotide

    def __repr__(self):
        return f'DNABase(nucleotide={self.base})'

    def set_base(self, nctd):
        if nctd.lower() not in [v for k in self.__class__.valid_bases.items() for v in k]:
            raise ValueError("Invalid nucleotide base.")
        elif nctd.lower() in self.__class__.valid_bases.keys():
            self._base = self.__class__.valid_bases[f'{nctd.lower()}']
        else:
            self._base = nctd.lower()

    def get_base(self):
        return self._base

    base = property(fset=set_base, fget=get_base)


b = DNABase('A')
print(b.base)
b.base = 'tHYMine'
print(b.base)