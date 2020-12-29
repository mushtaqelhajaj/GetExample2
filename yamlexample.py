import yaml
from yaml import load, load_all

stream = open('sample.yaml','r')
documents = pip install pyyaml
load_all(stream, Loader=yaml.FullLoader)

print(type(documents))

for doc in documents:
    print(type(doc))

    print(doc['people'][1]['LastName'])



    