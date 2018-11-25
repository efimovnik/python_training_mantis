from model.project import Project
import random
import string
import os.path
import jsonpickle
import getopt
import sys


def generate_project_data():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
    except getopt.GetoptError as err:
        getopt.usage()
        sys.exit(2)


    n = 1
    f = "data/projects.json"

    for o, a in opts:
        if o == "-n":
            n = int(a)
        elif o == "-f":
            f = a


    def random_string(prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


    def random_boolean():
        return random.choice([False, True])


    def random_status():
        return random.choice(['development', 'release', 'stable', 'obsolete'])


    def random_view_status():
        return random.choice(['public', 'private'])


    testdata = [Project(name=random_string("name", 10), status=random_status(),
                        inherit_global=random_boolean, view_status=random_view_status(),
                        description=random_string("Title", 5))
                for i in range(n)
    ]

    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


    with open(file, "w") as out:
        jsonpickle.set_encoder_options("json", indent=2)
        out.write(jsonpickle.encode(testdata))