import subprocess

def compile(c_file):
    # Compilation command
    dll_path = 'low_level_python/__llp_cdll__/'
    command = f'gcc -fPIC -shared -o {dll_path}{c_file}.o {c_file}.c'

    try:
        # Execute the command
        result = subprocess.run(command, 
                                shell=True, 
                                check=True, 
                                capture_output=True, 
                                text=True)
        
        # Print the output
        print("Compilation successfull.")
        if result.stdout:
            print("Standard output:")
            print(result.stdout)
        
        # If there's any error output, print it as well
        if result.stderr:
            print("Standard error:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        print("Error output:")
        print(e.stderr)

    except Exception as e:
        print(f"An error occurred: {e}")