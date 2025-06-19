# Graphical Interface for `asegstats2table`

This project provides a graphical user interface (GUI) for the `asegstats2table` command from FreeSurfer, which is used to generate statistical tables from FreeSurfer segmentations. The interface allows users to select the input directories, choose the measures to calculate, and specify where to save the generated files.

## Features

- **Select `SUBJECTS_DIR`:** Allows you to choose the directory where the subject data is located.
- **Select subjects file:** Allows you to select the `listsubject.txt` file containing the list of subjects.
- **Select measures to calculate:** You can choose multiple measures (volume, standard deviation, and mean).
- **Select output directory:** Allows you to choose the directory where the generated CSV files will be saved.
- **Automatic execution of the `asegstats2table` command:** For each selected measure, the command will be executed and the results saved in CSV files with the corresponding prefix.

## Requirements

This project requires Python 3.x and the following libraries:

- `tkinter` (for the GUI)
- `subprocess` (for running the `asegstats2table` command)
- `os` (for managing paths and environment variables)

Install the required dependencies using:

```bash
pip install tk
```

## How to use

```bash
piython asegui.py
```

## Example Workflow:
1. Click "Select SUBJECTS_DIR folder" to choose the directory where your subject data is stored.
2. Click "Select file" to choose your listsubject.txt file.
3. Select the measures you want to calculate (e.g., Volume and Standard Deviation (std)).
4. Click "Select output directory" to choose where the results should be saved.
5. Finally, click "Run" to generate the CSV files.



