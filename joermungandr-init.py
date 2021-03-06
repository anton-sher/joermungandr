magic = r"""
def quote(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def python():
    return "magic = r\"\"\"" + magic + "\"\"\"\n\n" + magic


def bash(s):
    return "printf \"" + quote(s.replace('\\', '\\\\')) + "\" > joermungandr.py"


def cpp(s):
    return "#include <iostream>\n#include <fstream>\nint main(){std::ofstream f;\nf.open(\"joermungandr.sh\");\nf << \"" + quote(s) + "\";\nf.close();\nreturn 0;\n}"


def c(s):
    return "#include <stdio.h>\nint main() {\nFILE *f = fopen(\"joermungandr.cpp\", \"w\");\nfprintf(f, \"" + quote(s) + "\");\nfclose(f);\nreturn 0;\n}"


def java(s):
    return "import java.io.PrintStream; public class joermungandr {public static void main(String... a) throws Exception {try(PrintStream out = new PrintStream(\"joermungandr.c\")){out.print(\"" + quote(s) + "\");}}}"


def nodejs(s):
    return "require(\"fs\").writeFile(\"joermungandr.java\", \"" + quote(s) + "\");"


def groovy(s):
    return "new File(\"joermungandr.js\").text = \"" + quote(s) + "\""


def scala(s):
    return "scala.tools.nsc.io.File(\"joermungandr.groovy\").writeAll(\"" + quote(s) + "\")"


def go(s):
    return ("package main\n\nimport (\n    \"io\"\n    \"os\"\n)\n\nfunc main() {\n    file, _ := os.Create(\"joermungandr.scala\")\n    io.WriteString(file, \"" + quote(s) + "\")\n    file.Close()\n}")


def ruby():
    with open("joermungandr.rb", mode='w') as f:
        print("File.write('joermungandr.go', \"" + quote(go(scala(groovy(nodejs(java(c(cpp(bash(python()))))))))) + "\")", file=f)


ruby()"""


def quote(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def python():
    return "magic = r\"\"\"" + magic + "\"\"\"\n\n" + magic


def bash(s):
    return "printf \"" + quote(s.replace('\\', '\\\\')) + "\" > joermungandr.py"


def cpp(s):
    return "#include <iostream>\n#include <fstream>\nint main(){std::ofstream f;\nf.open(\"joermungandr.sh\");\nf << \"" + quote(s) + "\";\nf.close();\nreturn 0;\n}"


def c(s):
    return "#include <stdio.h>\nint main() {\nFILE *f = fopen(\"joermungandr.cpp\", \"w\");\nfprintf(f, \"" + quote(s) + "\");\nfclose(f);\nreturn 0;\n}"


def java(s):
    return "import java.io.PrintStream; public class joermungandr {public static void main(String... a) throws Exception {try(PrintStream out = new PrintStream(\"joermungandr.c\")){out.print(\"" + quote(s) + "\");}}}"


def nodejs(s):
    return "require(\"fs\").writeFile(\"joermungandr.java\", \"" + quote(s) + "\");"


def groovy(s):
    return "new File(\"joermungandr.js\").text = \"" + quote(s) + "\""


def scala(s):
    return "scala.tools.nsc.io.File(\"joermungandr.groovy\").writeAll(\"" + quote(s) + "\")"


def go(s):
    return ("package main\n\nimport (\n    \"io\"\n    \"os\"\n)\n\nfunc main() {\n    file, _ := os.Create(\"joermungandr.scala\")\n    io.WriteString(file, \"" + quote(s) + "\")\n    file.Close()\n}")


def ruby():
    with open("joermungandr.rb", mode='w') as f:
        print("File.write('joermungandr.go', \"" + quote(go(scala(groovy(nodejs(java(c(cpp(bash(python()))))))))) + "\")", file=f)


ruby()