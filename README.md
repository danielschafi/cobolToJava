## Next Steps

1. Get a LLM to work
2. Define test case generation flow setup in java, cobol
3. Compare Java code generation in cobol and cobol + ast 
4. Then maybe throught compilation, LLM  assisted decompilation.


Since test case generation is not working right now but i want to have some progress to show i will just take one cobol script and then try to convert that into java with and without ast
1. Find cobol script that is good, compilable
2. Convert it to java without ast
3. try to compile and run it
4. Extract AST from cobol
5. Prompt to translate it with AST
6. convert it to java with AST
7. Try to compile and run it


Tell it to translate it to java ONLY from the COBOL AST