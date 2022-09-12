
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # list comprehensions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    print("all_python_devs_comp",all_python_devs)

    # high order
    all_python_devs_high = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs_high = list(map(lambda x: x["name"], all_python_devs_high))
    print("all_python_devs_high",all_python_devs_high)

    # list comprehensions
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    print("all_platzi_workers",all_platzi_workers)

    # high order
    all_platzi_workers_high = list(filter(lambda x: x["organization"] == "Platzi", DATA))
    all_platzi_workers_high = list(map(lambda x: x["name"], all_platzi_workers_high))
    print("all_platzi_workers_high",all_platzi_workers_high)

    # high order
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    print("adults", adults)

    old_people = list(map(lambda worker: worker | { "old": worker["age"] > 70 }, DATA))
    print("old_people", old_people)

if __name__ == "__main__":
    run()