#!/bin/bash

# Create lib directory
mkdir -p lib

echo "Downloading required JARs..."

# Download ANTLR4 Runtime
wget -O lib/antlr4-runtime-4.9.3.jar https://repo1.maven.org/maven2/org/antlr/antlr4-runtime/4.9.3/antlr4-runtime-4.9.3.jar

# Download Gson
wget -O lib/gson-2.10.1.jar https://repo1.maven.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.jar

echo "Please manually download the Proleap COBOL Parser JAR from:"
echo "https://github.com/uwol/proleap-cobol-parser/releases"
echo "Save it as: lib/proleap-cobol-parser.jar"
echo ""
echo "After downloading, compile with:"
echo "javac -cp \"lib/*\" CobolAstToJson.java"
echo ""
echo "And create a simple runner script..."

# Create a simple runner script
cat > run_parser.sh << 'EOF'
#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <cobol-file-path>"
    exit 1
fi

java -cp ".:lib/*" CobolAstToJson "$1"
EOF

chmod +x run_parser.sh

echo "Setup complete! Don't forget to download the Proleap COBOL Parser JAR."