class Tablet:
    supported_types = {"lite": (32, 2),
                       "pro": (64, 3),
                       "max": (128, 4)}

    def __init__(self, model, storage=0):
        self.model = model
        self.added_storage = 0
        self._base_storage = self.supported_types[self.model][0]
        self.storage = storage
        self._memory = self.supported_types[self.model][1]

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, m):
        if m.lower() not in self.supported_types.keys():
            raise ValueError(f"Invalid model {m} specified.")
        self._model = m

    @property
    def base_storage(self):
        return self._base_storage

    @property
    def memory(self):
        return self._memory

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, val):
        if val > 1024 or val < self._base_storage:
            raise ValueError("Invalid storage value. It must be between the base storage and 1024")
        self.add_storage(val - self._base_storage)

    def add_storage(self, value):
        if value + self._base_storage > 1024:
            raise ValueError("Total storage exceeded. The maximum storage is 1024GB.")
        self.added_storage+=value
        self._storage = self.added_storage + self._base_storage

    def __repr__(self):
        return f"Tablet(model='{self._model}', base_storage={self._base_storage}, added_storage={self.added_storage}, memory={self._memory})"


t1 = Tablet("lite", 41025)
print(t1)
