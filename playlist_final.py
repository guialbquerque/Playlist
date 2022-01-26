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

class Playlists:
    def __init__(self, name, programs):
        self._name = name
        self._programs = programs
    
    def __getitem__(self, item):
        print('=*'*30)
        return self._programs[item]

Film = []
Serie = []

number_films = input('How many movies are there in the playlist?\n')
while number_films.isnumeric() == False:

    number_films = input('Please, type a numerical argument: \n')


counter = 0
likes = 0
while counter < int(number_films):
    
    
    for i in range(1, int(number_films)+1):
        counter += 1
        year = input(f'Year of the {i}º movie:\n')
        while year.isnumeric() == False or year > str(2021):
            counter = i 
            year = input(f'Wrong type of movie {i}, type a valid year:\n')
        name = input(f'Name of the {i}º movie:\n').capitalize()
        duration = input(f'Duration of the {i}º movie in minutes:\n')
        likes = input(f'Likes of the {i}º movie:\n')
        Film.append(Movies(name,year, likes, duration))

counter2 = 0

number_series = input('How many series are there in the playlist?\n')
while number_series.isnumeric() == False:

    number_series = input('Please, type a numerical argument: \n')

while counter2 < int(number_series):
    counter2 += 1
for i in range(1, int(number_series)+1):
    year = input(f'Year of the {i}º serie:\n')
    while year.isnumeric() == False or year > str(2021):
        counter2 = i
        year = input(f'Wrong type of serie {i}, type a valid year:\n')
    series = input(f'Name of the {i} serie:\n').capitalize()
    seasons = input('Number of seasons:\n')
    likes_serie = input(f'Likes of the {i}º serie:\n')
    Serie.append(Series(series, year, likes_serie, seasons))
    
            

PlaylistFinal = Film
PlaylistFinal.extend(Serie)

print('=*'*30)

print('Final Playlist: \n')
print('\n')
Weekend =  Playlists('Weekend of Fun', PlaylistFinal)

for i in Weekend:
    print(i)
    with open('Playlist.txt', 'a') as output:
        output.write(str(i))

