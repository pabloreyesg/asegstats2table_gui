# Graphical Interface for `asegstats2table`

This project provides a graphical user interface (GUI) for the `asegstats2table` command from FreeSurfer, used to generate statistical tables of FreeSurfer segmentations. The interface allows selecting input folders, choosing which measures to calculate, and specifying where to save the generated files.

## Features

- **Select `SUBJECTS_DIR`:** Allows you to choose the directory where the subject data is located.
- **Select subjects file:** Allows you to select the `listsubject.txt` file containing the list of subjects.
- **Select measures to calculate:** You can choose multiple measures (volume, standard deviation, and mean).
- **Select output directory:** Allows you to choose the directory where the generated CSV files will be saved.
- **Automatic execution of the `asegstats2table` command:** For each selected measure, the command will be run and the results saved in CSV files with the corresponding prefix.

## Requirements

This project requires Python 3.x and the following libraries:

- `tkinter` (for the GUI)
- `subprocess` (for running the `asegstats2table` command)
- `os` (for managing paths and environment variables)

Install the required dependencies using:

```bash
pip install tk

