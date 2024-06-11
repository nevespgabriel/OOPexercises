from collections import UserDict

class BidirectionalDict(UserDict):

    def __len__(self):
        return int(len(self.nrm_dict)/2)

    def __delitem__(self, key):
        super().__delitem__(self[key])
        super().__delitem__(key)

    def __setitem__(self, key, value):
        if key in self.keys():
            del self[key]
        if value in self.keys():
            del self[value]
        super().__setitem__(key, value)
        super().__setitem__(value, key)


bd = BidirectionalDict({"Eu": "massa", "Ele": "nada"})
bd.update([("Eu", "lenda")])
print(bd)
