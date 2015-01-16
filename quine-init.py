magic = r"""
def quote(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def q():
    return "magic = r\"\"\"" + magic + "\"\"\"\n\n" + magic


def ruby():
    with open("quine.rb", mode='w') as f:
        print("print \"" + quote(q()) + "\"", file=f)


ruby()"""


def quote(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def q():
    return "magic = r\"\"\"" + magic + "\"\"\"\n\n" + magic


def ruby():
    with open("quine.rb", mode='w') as f:
        print("print \"" + quote(q()) + "\"", file=f)


ruby()