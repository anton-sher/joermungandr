magic = r"""
def quote(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def python():
    return "magic = r\"\"\"" + magic + "\"\"\"\n\n" + magic


def bash(s):
    return "printf \"" + quote(s.replace('\\', '\\\\')) + "\" > joermungandr.py"


def nodejs(s):
    return "require(\"fs\").writeFile(\"joermungandr.sh\", \"" + quote(s) + "\");"


def groovy(s):
    return "new File(\"joermungandr.js\").text = \"" + quote(s) + "\""


def ruby():
    with open("joermungandr.rb", mode='w') as f:
        print("File.write('joermungandr.groovy', \"" + quote(groovy(nodejs(bash(python())))) + "\")", file=f)


ruby()"""


def quote(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def python():
    return "magic = r\"\"\"" + magic + "\"\"\"\n\n" + magic


def bash(s):
    return "printf \"" + quote(s.replace('\\', '\\\\')) + "\" > joermungandr.py"


def nodejs(s):
    return "require(\"fs\").writeFile(\"joermungandr.sh\", \"" + quote(s) + "\");"


def groovy(s):
    return "new File(\"joermungandr.js\").text = \"" + quote(s) + "\""


def ruby():
    with open("joermungandr.rb", mode='w') as f:
        print("File.write('joermungandr.groovy', \"" + quote(groovy(nodejs(bash(python())))) + "\")", file=f)


ruby()