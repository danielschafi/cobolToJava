1. Literaturrecherche
2. Überlegen, wie die evaluation gemacht werden könnte.
    - Alle cobol scripts so schreiben, dass die Parameter mit argumenten übergeben werden können.
    - Dann für jedes Argument eine Range von Werten definieren
    - All diese Kombinationen in das COBOL programm füttern und die Outputs aufzeichnen
    - Alles in einem JSON speichern
    - Programm übersetzen, sollte mit gleichen inputs zu gleichen outputs führen.
    - Das sollte auf Equivalenz testen

    - Zusätzlich auch noch statische code analysen durchführen, readability etc.

3. Suche nach Datset
    - Nicht wirklich erfolgreich, habe zwei potentielle gefunden. Eines recht klein, das andere bis jetzt nicht zum laufen gekriegt.
    - Was kann man hier machen? Ideen?

4. Wie kann ich von python aus COBOL programme compilieren und ausführen, ihre outputs einfangen?
    - Cobol compiler installieren, dann einfach über subprocess.run(cobx ....)
5. Wie kann ich von python aus Java programme compilieren und ausführen, ihre outputs einfangen?
    - Auch compiler installieren, und über subprocess.run(javac ...), capture_output=True

6. LLM Abstraction layer
    - Einfaches laden von verschiedenen LLMs, setzen von system, user prompts, nur noch llm.predict(cobol_code)

7. Programm zur umwandlung von COBOL zu Java mit hilfe eines local LLM (Qwen2.5-coder-instruct-7B)
    - Base
    - Mit AST

8. proleap-cobol-parser verwenden, um den AST von COBOL zu extrahieren
    - Ist ein Java programm
    - Das aufrufbar machen, so dass man nur noch parser.getAST(code_file) machen muss
    - Wrapper darum -> Extrac Java file
    - python class um die interaktion damit zu handeln.
    - Hat lange gedauert das einzubinden
    - Danke Claude <3