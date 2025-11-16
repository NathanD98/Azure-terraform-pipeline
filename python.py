import subprocess
import sys
import os


def run_black_on_file(filepath):
    """
    Runs the 'black' code formatter on the specified file using
    'python -m black' for robust environment handling.

    Note: The 'black' package must be installed in your current environment
    (e.g., using `pip install black`).

    Args:
        filepath (str): The path to the file to be formatted.
    """
    # Check if the file exists before attempting to format
    if not os.path.exists(filepath):
        print(f"Error: File not found at '{filepath}'")
        sys.exit(1)

    # Use sys.executable (which is 'python' or 'python3') and '-m black'
    # for robust execution within the current environment.
    command = [sys.executable, "-m", "black", filepath]

    print(f"Attempting to run black on: {filepath}")
    print(f"Executing command: {' '.join(command)}")

    try:
        # subprocess.run executes the command.
        # check=True raises CalledProcessError if black exits with a non-zero code
        # (e.g., if there's a syntax error or if the 'black' module is not found).
        result = subprocess.run(command, check=True, text=True, capture_output=False)

        # If we reach this point, the command successfully executed.
        if result.returncode == 0:
            print(f"\nBlack formatting command finished on '{filepath}'.")

    except subprocess.CalledProcessError as e:
        # This catches errors reported by the black tool or environment issues
        # (like 'No module named black' if it's not installed).
        print(f"\nAn error occurred while running black: {e}")
        print("Please check if 'black' is installed in the current environment.")
        sys.exit(1)


run_black_on_file("C:\\Users\\Nate\\Azure-terraform-pipeline\\")
