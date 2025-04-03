#!/usr/bin/env python
import os
import json
import warnings

from datetime import datetime
from pathlib import Path

from multiply_x_comments.crew import LatestAiDevelopment
from multiply_x_comments.helpers.format_result_helper import format_result
from multiply_x_comments.helpers.xls_helper import read_xslsx_file

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    source_dir = Path(os.getenv("SOURCE_DIR"))
    source_dir.mkdir(parents=True, exist_ok=True)

    result_dir = Path(os.getenv("RESULT_DIR"))
    processed_files = result_dir / "processed"
    result_files = result_dir / "result"
    
    processed_files.mkdir(parents=True, exist_ok=True)
    result_files.mkdir(parents=True, exist_ok=True)

    for input_file in source_dir.glob("*.xlsx"):
        try:
            inputs = [{ 'topic': row[0].replace("\n", ""), "number": row[1]} for row in read_xslsx_file(str(input_file))]
            raw_result = LatestAiDevelopment().crew().kickoff_for_each(inputs=inputs)        
            json_result = format_result(input_list=inputs, output_list=raw_result)
            output_file = result_files / f"{input_file.stem}_{datetime.now().strftime('%Y%m%d%H%M%S.json')}"
            with open(str(output_file), "w") as f:
                json.dump(json_result, f, indent=4)
            destination_file = processed_files / input_file.name    
            input_file.rename(destination_file)    
        except Exception as e:
            raise Exception(f"An error occurred while running the crew: {e} for file `{input_file}`")