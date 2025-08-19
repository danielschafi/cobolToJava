import subprocess
import json


def parse_cobol(file_path, format="fixed"):
    cmd = [
        "java",
        "-cp",
        "CobolAstExporter.jar:proleap-cobol.jar:antlr-4.13.1-complete.jar:gson-2.10.1.jar",
        "CobolAstExporter",
        file_path,
        format,
    ]
    output = subprocess.check_output(cmd, text=True)
    return json.loads(output)


# Example usage
ast = parse_cobol("example.cbl", format="fixed")
print(ast)
