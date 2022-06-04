# Created by vidit.singh at 09-03-2022

# Counters
from collections import Counter


def main():
    list1 = [111, 22, 333, 45, 22, 44, 3, 2, 222, 33, 44, 111, 55, 66, 44, 33, 111, 23]
    print(Counter(list1))  # Counts the repeated elements
    common = Counter(list1)  # Ge the most common repeated elements
    print(common.most_common(2))
    # Convert to list again
    list(common)


from collections import defaultdict

d = {'key1': "Vidit"}
print(f"Dictionary : {d['key1']}")
print(d.get('ke2','key not present'))

d = defaultdict(lambda: "default value")

print(d['wrong key'])

# Named tuple -> can be given name to each element.

from collections import namedtuple

Dog = namedtuple('Dog', ['name', 'age', 'breed'])
sammy = Dog(name='Sam', age=5, breed='husky')

print(sammy)
print(sammy.breed)

if __name__ == '__main__':
    main()
