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

class Movies(Program):
    def __init__(self, name, year, likes, duration):
        super().__init__(name, year, likes)
        self._duration = duration
    
    @property
    def duration(self):
        return f'Duration: {self._duration} min'
    
    def __str__(self):
        return f'Name: {self._name}\nYear: {self._year}\nDuration: {self._duration} min\nLikes: {self._likes}\n'

class Series(Program):
    def __init__(self, name, year, likes, season):
        super().__init__(name, year, likes)
        self._season = season
    
    @property
    def season(self):
        return f' Seasons: {self.season}'

    def __str__(self):
        return f'Name: {self._name}\nYear: {self._year}\nSeasons: {self._season}\nLikes: {self._likes}\n'

