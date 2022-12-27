from faker import Faker
from random import randint, random
from random import choice

from mimesis import Datetime

MAX_N = 1000
MAX_COUNTRY = 200

datetime = Datetime()
t_pos = ["goalkeeper", "defender", "midfielder", "forward"]


def generate_country():
    faker = Faker()
    f = open('country.csv', 'w')
    co_set = set()
    cap_set = set()
    for i in range(MAX_COUNTRY):
        name = faker.country()
        while name in co_set:
            name = faker.country()
        co_set.add(name)
        capital = faker.city()
        while name in cap_set:
            capital = faker.country()
        cap_set.add(capital)
        square = 1 + random() * 20 * 1e6
        population = 1 + random() * 1.5 * 1e9
        line = "{0};{1};{2};{3}\n".format(
            name,
            capital,
            square,
            population)
        f.write(line)
    f.close()




def generate_footballer():
    faker = Faker()
    f = open('footballer.csv', 'w')
    for i in range(MAX_N):
        name = faker.name()
        name = name.split(' ')
        surname = str(name[1])
        country = faker.country()
        position = choice(t_pos)
        price = randint(1, 200) * 1e6
        line = "{0};{1};{2};{3};\n".format(
            surname,
            country,
            position,
            price)
        f.write(line)
    f.close()


def generate_contract():
    f = open('contract.csv', 'w')
    for i in range(MAX_N):
        footballer = randint(1, MAX_N)
        agent = randint(1, MAX_N)
        date = datetime.date(start=2020, end=2022)
        duration = randint(1, 5)
        line = "{0};{1};{2};{3}\n".format(
            footballer,
            agent,
            date,
            duration)
        f.write(line)
    f.close()

def generate_coach():
    faker = Faker()
    f = open('coach.csv', 'w')
    for i in range(MAX_N):
        name = faker.name()
        name = name.split(' ')
        name_res = str(name[0])
        surname = str(name[1])
        country = randint(1, MAX_COUNTRY)
        club = randint(1, MAX_N)
        birth_data = datetime.date(start=1930, end=2000)
        line = "{0};{1};{2};{3};{4}\n".format(
            name_res,
            surname,
            country,
            club,
            birth_data)
        f.write(line)
    f.close()

if __name__ == "__main__":
    # generate_country() #done
    # generate_league() #done
    # generate_agent() #done
    # generate_club() #done
    generate_footballer() #done
    #generate_contract()  # done
    #generate_coach() #defend
