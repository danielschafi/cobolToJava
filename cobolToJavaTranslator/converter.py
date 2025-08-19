import os
from dotenv import load_dotenv
import shutil

load_dotenv()

# Logging Setup
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
# Other Imports
from datasets import load_dataset
import pandas as pd


from utils.llm import LLM
from cobolToJavaTranslator.prompts import (
    convert_prompt_base,
    convert_prompt_with_ast,
    system_prompt,
)

import datetime
from pathlib import Path
from enum import Enum
import subprocess
import re


class ConversionType(Enum):
    BASE = 0
    AST = 1


class ConverterHelper:
    def __init__(
        self,
        llm: LLM,
        conversion_type: ConversionType = ConversionType.BASE,
        output_dir: str = Path(os.getcwd()) / "out_dir",
    ):
        self.llm = llm
        self.conversion_type = conversion_type
        self.system_prompt = system_prompt()
        self.output_dir = output_dir

    def _get_conversion_prompt(self, cobol_code: str, ast: str = None) -> str:
        """
        Builds the conversion prompt and returns it according to the selected conversion type
        """
        if self.conversion_type == ConversionType.BASE:
            return convert_prompt_base(cobol_code)
        elif self.conversion_type == ConversionType.AST:
            return convert_prompt_with_ast(cobol_code, ast)

    def cob_2_java(self, cobol_code: str | Path, ast: str = None) -> Path:
        """
        Converts the cobol code to java using an llm and outputs the resulting java file
        The conversion is done accoding to the specified ConversionType

        Args:
            cobol_code (str|Path): the cobol code that is to be converted as string OR the path to the file containing the code
            ast (str) optional; abstract syntax tree representation of cobol code. Required if ConversionType.AST is set
        Returns:
            Path: The path of the generated *.java file
        """
        if self.conversion_type == ConversionType.AST:
            if ast is None:
                raise ValueError(
                    "Parameter ast is None. Is required, if conversion_type AST is selected."
                )

        if os.path.exists(cobol_code):
            with open(cobol_code, "r") as cobol_file:
                src = cobol_file.read()
        else:
            src: str = cobol_code

        self.conversion_prompt = self._get_conversion_prompt(src, ast)
        java_code = self.llm.predict(
            prompt=self.conversion_prompt, system_prompt=self.system_prompt
        )
        logger.info("Conversion cob2Java complete")

        # save the generated code
        os.makedirs(self.output_dir, exist_ok=True)
        output_filename = self._get_java_class_name(java_code) + ".java"
        self.java_filepath = Path(self.output_dir) / output_filename

        logger.info(f"Saving the generated java code to: {self.java_filepath}")
        if os.path.exists(self.java_filepath):
            logger.info(f"File: {self.java_filepath} already exists. Overwriting...")
            os.remove(self.java_filepath)

        with open(self.java_filepath, "w") as java_file:
            java_file.write(java_code)

        if (
            os.path.exists(self.java_filepath)
            and os.path.getsize(self.java_filepath) > 1
        ):
            logger.info(
                f"Successfully written generated java code to {self.java_filepath}"
            )
        else:
            raise ValueError(
                f"Generated java file {self.java_filepath} could not be found or was empty"
            )

        return self.java_filepath

    def _get_java_class_name(self, java_code: str) -> str:
        """
        Extracts the public class name from Java Code snippet.

        Args:
            java_file (str): the java source code

        Returns:
            str: Public class name
        """

        if len(java_code) == 0:
            raise ValueError(
                "No Java Code was generated, could not extract class name."
            )

        # Regex to match 'public class ClassName'
        match = re.search(r"public\s+class\s+([A-Za-z_][A-Za-z0-9_]*)", java_code)

        if match:
            return match.group(1)
        else:
            raise ValueError(f"No public class found in {java_code}")

    def compile(self, java_filepath: Path) -> Path:
        """
        Compiles the .java file at the specified filepath. returns the path of the compiled programm

        Args:
            java_filepath (Path): path of the .java file that should be compiled

        Returns:
            Path: Path to the compiled programm
        """
        try:
            logging.info(f"Attempting to compile: {java_filepath}")
            compile_result = subprocess.run(
                ["javac", java_filepath], capture_output=True, text=True
            )
            if compile_result.returncode != 0:
                logger.warning(
                    f"Compilation failed of {java_filepath} \n{compile_result.stderr}"
                )
            else:
                logger.info(f"Compilation of {java_filepath} successfull")
                return java_filepath.with_suffix("")
        except Exception as e:
            logger.error(f"Compilation of {java_filepath} failed: {e}")
            raise

    def run_java_programm(self, java_prog_path: Path):
        """
        runs a Java programm and captures the output

        Args:
            java_prog_path (Path): _description_
        """
        try:
            logging.info(f"Attempting to run: {java_prog_path}")
            dir = java_prog_path.parent
            filename = java_prog_path.stem

            result_programm = subprocess.run(
                ["java", "-cp", dir, filename], capture_output=True, text=True
            )
            print(result_programm.stdout)
        except Exception as e:
            logger.error(f"Running of {java_prog_path} failed: {e}")
            raise

    def convert_compile_run(
        self,
        cobol_code: str | Path,
    ):
        java_filepath = self.cob_2_java(
            cobol_code,
        )
        java_programm_path = self.compile(java_filepath)
        self.run_java_programm(java_programm_path)


def main():
    # llm = LLM()
    # converter = ConverterHelper(llm, ConversionType.BASE)
    cobol_code_path = Path("/home/schafhdaniel@edu.local/cobolToJava/in_cob_file.cbl")
    # java_filepath = converter.cob_2_java(
    #     cobol_code=cobol_code_path,
    # )
    # java_programm_path = converter.compile(java_filepath)
    # converter.run_java_programm(java_programm_path)

    # converter.convert_compile_run(cobol_code_path)

    # converter_ast = ConverterHelper(llm, ConversionType.AST)
    # converter_ast.convert_compile_run(cobol_code_path, ast)

    # with open(cobol_code_path, "r") as file:
    # result = parse_file(cobol_code_path)
    # print(result)


if __name__ == "__main__":
    main()
