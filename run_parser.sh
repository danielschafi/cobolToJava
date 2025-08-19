#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <cobol-file-path>"
    exit 1
fi

java -cp ".:lib/*" CobolAstToJson "$1"
