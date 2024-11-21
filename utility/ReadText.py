class ReadText:
    def __init__(self):
        pass
    
    def read(self, path="idea.txt"):
        """
        Reads the content of a text file at the specified path.

        Parameters:
        path (str): The file path to read from.

        Returns:
        str: The content of the file as a string, or an error message if the file cannot be read.
        """
        try:
            with open(path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return f"Error: The file at {path} was not found."
        except IOError:
            return f"Error: An error occurred while trying to read the file at {path}."

# Only run the following if this script is executed directly
if __name__ == "__main__":
    path = input("Enter the path to the text file: ")
    reader = ReadText()
    result = reader.read()
    print(result)
