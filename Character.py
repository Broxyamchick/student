class Character:
    name = ''
    year_of_birth = 2010
    group = 228
    GPA = 10
    old = 2022 - year_of_birth

    def __init__(self, name, year_of_birth=2010, group=228, GPA=10, old=2022-year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth
        self.group = group
        self.GPA = GPA
        self.old = old

    def __str__(self):
        return f' == {self.name} ==\n' \
            f' год рождения: {self.year_of_birth}\n' \
            f' группа: {self.group}\n' \
            f' средний балл: {self.GPA}\n' \
            f' возраст: {self.old}\n'






