from collections import defaultdict, Counter
import re

sentence = 'the quick brown fox jumps over the lazy dog'

mydict = defaultdict(int)
for c in sentence:
    mydict[c] += 1

print(mydict)

counter = Counter()
for c in sentence:
    counter[c] += 1

c1 = Counter('able was I ere i saw elba')
print(c1)

sentence ='''
This course is an in-depth look at Python dictionaries.

Dictionaries are ubiquitous in Python. Classes are essentially dictionaries, modules are dictionaries, namespaces are dictionaries, sets are dictionaries and many more.

In this course we'll take an in-depth look at:

associative arrays and how they can be implemented using hash maps

hash functions and how we can leverage them for our own custom classes

Python dictionaries and sets and the various operations we can perform with them

specialized dictionary structures such  as OrderedDict and how it relates to the built-in Python3.6+ dict

Python's implementation of multi-sets, the Counter class

the ChainMap class

how to create custom dictionaries by inheriting from the UserDict class

how to serialize and deserialize dictionaries to JSON

the use of schemas in custom JSON deserialization

a brief introduction to some useful libraries such as JSONSchema, Marshmallow, PyYaml and Serpy



***** Prerequisites *****

Please note that this is a relatively advanced Python course, and a strong knowledge of some topics in Python is required. 

Beyond the basics of Python (loops, conditional statements, exception handling, built-in data types, creating classes, etc), you should also have an in-depth understanding of the following topics:

functions and functional programming (recursion, *args, **kwargs, zip, map, sorted, any, all, etc)
'''

words = re.split('\W', sentence)
word_count = Counter(words)
print(word_count)


c = Counter()
for i in range(1, 11):
    c[i] = i

print(list(c.elements()))


def get_elements(cc):
    for key in cc:
        for _ in range(1, cc[key] + 1):
            yield key


print(get_elements(c))
for var in get_elements(c):
    print(var)

