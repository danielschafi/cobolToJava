from simple_cobol_ast_parser import CobolASTParser

parser = CobolASTParser()
ast = parser.parse_cobol_file("/home/schafhdaniel@edu.local/cobolToJava/in_cob_file.cbl")
print(ast)