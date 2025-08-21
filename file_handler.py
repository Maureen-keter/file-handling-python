def file_handler():
    file=input("Enter the name of the file: ")
    try:
        with open(file,"r") as f:
            data=f.read()

            modified_content=data.upper()

            output_file="modified_" + file
            with open(output_file, "w") as f:
                f.write(modified_content)
            print(f"File modified successfully and saved as {output_file}!")
    except FileNotFoundError:
        print("Error:File does not exist")
    except PermissionError:
        print("Error:You can't access this file")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


file_handler()