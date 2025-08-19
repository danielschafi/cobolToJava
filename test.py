from cobolToJavaTranslator.cobolAstParser import CobolASTParser

parser = CobolASTParser()
ast = parser.parse_cobol_file("/home/schafhdaniel@edu.local/cobolToJava/in_cob_file.cbl")
print(ast)