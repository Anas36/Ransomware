import subprocess

def create_executable(file_path):
    # Set the path to your Python script
    script_path = '/Users/anas/Desktop/SecurityProj/client.py'
    
    # Set the options for auto-py-to-exe
    options = [
        "--onefile",
        "--windowed",
        "--icon=icon.ico",
        f"--output-file={file_path}",
        script_path
    ]
    
    # Call auto-py-to-exe with the specified options
    subprocess.call(["auto-py-to-exe"] + options)

create_executable('/Users/anas/Desktop/newFile.exe')