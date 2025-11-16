import subprocess
import sys
import os
import black 


def run_black_on_file(filepath):
    """
    Runs the 'black' code formatter on the specified file.

    Note: The 'black' package must be installed in your environment
    (e.g., using `pip install black`).

    Args:
        filepath (str): The path to the file to be formatted.
    """
    # Check if the file exists before attempting to format
    if not os.path.exists(filepath):
        print(f"Error: File not found at '{filepath}'")
        sys.exit(1)

    # The simplest command to execute black on the target file.
    command = ['black', filepath]

    print(f"Attempting to run black on: {filepath}")

    try:
        # subprocess.run executes the command.
        # check=True ensures a Python error (CalledProcessError) is raised
        # if the 'black' command itself fails (e.g., if there's a syntax error in the file).
        # capture_output=False lets black print its output (e.g., "reformatted...") directly to the terminal.
        result = subprocess.run(command, check=True, text=True, capture_output=False)

        # If we reach this point, the command successfully executed.
        if result.returncode == 0:
            print(f"\nBlack formatting command finished on '{filepath}'.")

    except FileNotFoundError:
        print("\nERROR: 'black' command not found.")
        print("Please ensure 'black' is installed and accessible in your system's PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        # This catches errors reported by the black tool itself (e.g., parsing a broken file).
        print(f"\nAn error occurred while running black: {e}")
        sys.exit(1)

run_black_on_file("C:\\Users\\Nate\\Azure-terraform-pipeline\\")