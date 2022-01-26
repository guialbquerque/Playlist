class Program:
    def __init__(self, name, year, likes):
        self._name = name
        self._year = year
        self._likes = likes
    
    @property
    def name(self):
        return f'Name: {self._name}'
    
    @property
    def year(self):
        return f'Year: {self._name}'
    
    @property
    def likes(self):
        return f' Likes: {self._likes}'