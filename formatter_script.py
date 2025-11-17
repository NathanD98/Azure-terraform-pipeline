import subprocess
import sys
import os

def run_black_on_dir(dirpath):
    """
    Runs the 'black' code formatter on the specified directory (recursively) 
    using 'python -m black' for robust environment handling.

    Args:
        dirpath (str): The path to the directory containing files to be formatted.
    """
    # Check if the path exists before attempting to format
    if not os.path.exists(dirpath):
        # We don't exit here if the path doesn't exist, as it might be a valid 
        # scenario (e.g., no code yet), but we log a warning.
        print(f"Warning: Directory not found at '{dirpath}'. Skipping black formatting.")
        return

    # Use sys.executable (which is 'python' or 'python3') and '-m black'
    # for robust execution within the current environment.
    # We pass the directory path, and black will format all files recursively.
    command = [sys.executable, "-m", "black", dirpath]

    print(f"Attempting to run black on directory: {dirpath}")
    print(f"Executing command: {' '.join(command)}")

    try:
        # subprocess.run executes the command.
        # check=True raises CalledProcessError if black exits with a non-zero code
        # (e.g., if there's a syntax error or if the 'black' module is not found).
        # We also pass the --check --diff flags if you only want to verify formatting 
        # instead of applying it, but here we run the actual formatting.
        subprocess.run(command, check=True, text=True, capture_output=False)

        # If we reach this point, the command successfully executed.
        print(f"\n✅ Black formatting command finished successfully on '{dirpath}'.")

    except subprocess.CalledProcessError as e:
        # This catches errors reported by the black tool (e.g., syntax errors) 
        # or environment issues.
        print(f"\n❌ An error occurred while running black: {e}")
        print("Review the black output above for details (e.g., syntax errors or module not found).")
        sys.exit(e.returncode)


if __name__ == "__main__":
    # Check if a positional argument (the directory path) was provided
    if len(sys.argv) < 2:
        print("Error: Missing required directory path argument.")
        print("Usage: python my_script.py <directory_path>")
        # Exit with a standard error code
        sys.exit(1)

    # sys.argv[0] is the script name ('my_script.py')
    # sys.argv[1] is the first positional argument passed from the pipeline
    directory_to_format = sys.argv[1]

    # Run the formatter function
    run_black_on_dir(directory_to_format)