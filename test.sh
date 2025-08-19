#!/bin/bash


echo "       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST.
       PROCEDURE DIVISION.
       DISPLAY 'Hello'.
       STOP RUN." > test.cbl

# Run the parser
./run_parser.sh test.cbl