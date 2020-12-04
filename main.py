import json


class GetWikiLinks:

    def __init__(self, source):
        with open(str(source)) as file:
            self.countries = json.load(file)
        self.start = -1
        self.end = len(self.countries)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        name = self.countries[self.start]['name']['common']
        return f'Country name: {name}, ' \
               f'Wiki Link: https://en.wikipedia.org/wiki/{name.replace(" ", "_").replace(",", "_")} \n'


def hash_generator(filename):
    file = open(str(filename))
    for line in file.readline():
        yield hash(line)
    file.close()


if __name__ == '__main__':
    with open('countries-links.txt', 'w', encoding='utf-8') as f:
        for country in GetWikiLinks('countries.json'):
            f.write(country)

    for lh in hash_generator('countries-links.txt'):
        print(lh)
