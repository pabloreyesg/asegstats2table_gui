import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import os

# Function to check if asegstats2table is installed
def check_asegstats2table():
    try:
        # Try running the command to check if it's installed
        subprocess.run(['asegstats2table', '--help'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True  # Command is available
    except subprocess.CalledProcessError:
        return False  # Command failed, it's not available

# Function to get the value of $SUBJECTS_DIR
def get_subjects_dir():
    subjects_dir = os.getenv('SUBJECTS_DIR', 'SUBJECTS_DIR is not defined')
    return subjects_dir

# Function to update the value of SUBJECTS_DIR
def set_subjects_dir():
    # Open the folder explorer to select the directory
    selected_dir = filedialog.askdirectory(title="Select the SUBJECTS_DIR directory")
    if selected_dir:
        os.environ['SUBJECTS_DIR'] = selected_dir
        subjects_dir_label.config(text=f"Subjects directory: {selected_dir}")
        print(f"SUBJECTS_DIR updated to: {selected_dir}")

# Function to select the output directory
def set_output_dir():
    # Open the folder explorer to select the output directory
    selected_dir = filedialog.askdirectory(title="Select the output directory to save files")
    if selected_dir:
        output_dir_var.set(selected_dir)
        output_dir_label.config(text=f"Files will be saved in: {selected_dir}")
        print(f"Output directory selected: {selected_dir}")

# Function to execute the command with the selected parameters
def run_command():
    # Check if asegstats2table is installed
    if not check_asegstats2table():
        messagebox.showerror("Error", "asegstats2table is not installed. Please install it and try again.")
        return

    # Get the selected subjects file
    subjects_file = subjects_file_var.get()

    # Create the name of the CSV file with the prefix of the selected measure
    measures_selected = []
    if volume_var.get():
        measures_selected.append("volume")
    if std_var.get():
        measures_selected.append("std")
    if mean_var.get():
        measures_selected.append("mean")

    if not measures_selected:
        messagebox.showwarning("Warning", "Please select at least one measure.")
        return

    # Get the working directory
    subjects_dir = get_subjects_dir()
    output_dir = output_dir_var.get()

    if not output_dir:
        messagebox.showwarning("Warning", "Please select an output directory.")
        return

    # Execute the command for each selected measure
    for meas in measures_selected:
        tablefile = os.path.join(output_dir, f"aseg_stats_{meas}.csv")  # CSV file name based on the measure

        # Create the command
        command = f"asegstats2table --subjectsfile {subjects_file} --common-segs --meas {meas} --tablefile {tablefile} -d comma"

        # Show the working directory
        print(f"SUBJECTS_DIR value: {subjects_dir}")
        subjects_dir_label.config(text=f"Subjects directory: {subjects_dir}")

        # Run the command
        try:
            subprocess.run(command, check=True, shell=True)
            messagebox.showinfo("Success", f"Command executed successfully for the measure {meas}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error executing the command for {meas}: {e}")

# Function to open the file explorer and select the subjects file
def select_subjects_file():
    file_path = filedialog.askopenfilename(title="Select the subjects file",
                                           filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if file_path:
        subjects_file_var.set(file_path)

# Create the main window
root = tk.Tk()
root.title("Graphical Interface for asegstats2table")
root.geometry("500x600")
root.resizable(False, False)

# Use ttk theme for a more polished interface
style = ttk.Style(root)
style.theme_use('clam')

# Instructions label
instructions = ttk.Label(root, text="Select the subjects folder, file, and measures to use.")
instructions.pack(pady=10)

# Button to select the SUBJECTS_DIR folder
set_subjects_button = ttk.Button(root, text="Select SUBJECTS_DIR folder", command=set_subjects_dir)
set_subjects_button.pack(pady=5)

# Label to display the selected SUBJECTS_DIR
subjects_dir_label = ttk.Label(root, text="Subjects directory: Not defined")
subjects_dir_label.pack(pady=5)

# Label and input field for the subjects file
subjects_file_label = ttk.Label(root, text="Subjects file (listsubject.txt):")
subjects_file_label.pack(pady=5)

subjects_file_var = tk.StringVar()
subjects_file_entry = ttk.Entry(root, textvariable=subjects_file_var, width=40)
subjects_file_entry.pack(pady=5)

# Button to open file explorer to select the subjects file
browse_button = ttk.Button(root, text="Select file", command=select_subjects_file)
browse_button.pack(pady=5)

# Button to select the output directory
set_output_button = ttk.Button(root, text="Select output directory", command=set_output_dir)
set_output_button.pack(pady=10)

# Label to display the selected output directory
output_dir_var = tk.StringVar()
output_dir_label = ttk.Label(root, text="Files will be saved in: Not defined")
output_dir_label.pack(pady=5)

# Label for selecting the measures
meas_label = ttk.Label(root, text="Select the measures:")
meas_label.pack(pady=5)

# Variables for checkboxes
volume_var = tk.BooleanVar()
std_var = tk.BooleanVar()
mean_var = tk.BooleanVar()

# Checkboxes for selecting measures
volume_cb = ttk.Checkbutton(root, text="Volume", variable=volume_var)
volume_cb.pack()

std_cb = ttk.Checkbutton(root, text="Standard Deviation (std)", variable=std_var)
std_cb.pack()

mean_cb = ttk.Checkbutton(root, text="Mean", variable=mean_var)
mean_cb.pack()

# Button to run the command
run_button = ttk.Button(root, text="Run", command=run_command)
run_button.pack(pady=20)

# Display the interface
root.mainloop()

