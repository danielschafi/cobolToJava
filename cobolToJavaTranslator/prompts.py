def convert_prompt_base(cobol_code: str) -> str:
    return f"""
    BEGIN COBOL CODE:
    {cobol_code}
    END COBOL CODE
    """


def convert_prompt_with_ast(cobol_code: str, ast: str) -> str:
    return f"""
BEGIN COBOL CODE:
{cobol_code}
END COBOL CODE

Additionally here is the Abstract Syntax tree for this cobol programm, use it to assist in conversion to java:

BEGIN AST:
{ast}
END AST"""


def system_prompt() -> str:
    return """
    You are a code conversion assistant.  
    Your task is to convert COBOL code (which is compilable by the GNUCobol compiler) into Java.  

    REQUIREMENTS:  
    - The Java program MUST be equivalent in functionality to the COBOL code.  
    - The same inputs MUST produce the same outputs.  
    - The output MUST be ONLY a complete, compilable Java file.  
    - Do NOT include explanations, comments, or any extra text outside of the code.  
    - Do NOT wrap the code in markdown fences (```) or language tags.  
    - The output should ONLY be the CONTENT of the Java file.  
    
    IF YOU GENERATE MARKDOWN BRACKETS OR ANY EXTRA TEXT, REMOVE THEM.  

    """
