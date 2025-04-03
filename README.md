#X Comments

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. 

First, if you haven't already, install CrewAI:

```bash
poetry install
```
```
### Customizing


**Set in the `.env` file variables:**
- OPENAI_API_KEY -  API Key for OpenAI
- SOURCE_DIR - input folder for xlsx-files with a text that needs to be paraphrased
- RESULT_DIR - output folder where will be created two subflders: `processed` - the processed xslx-file will be moved to this directory, `result` - folder for json-files with results


## Running the Project

1. Prepare one or more xslsx files of the following format in the input directory:
First column - text for paraphrasing
Second column - number of variants required

2. Run this from the root folder of the project:

```bash
$ crewai run
```

