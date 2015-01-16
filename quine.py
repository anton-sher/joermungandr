magic = r"""
def q():
    return "magic = r\"\"\"" + magic + "\"\"\"\n\n" + magic


with open("quine1.py", mode='w') as f:
    print(q(), file=f)"""


def q():
    return "magic = r\"\"\"" + magic + "\"\"\"\n\n" + magic


with open("quine1.py", mode='w') as f:
    print(q(), file=f)