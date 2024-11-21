class ReadWriteTextFile:
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
    
    def write(self, content, file_name=None):
        """
        Save the given content into a text file.
        
        :param content: The text content to save.
        :param file_name: Optional file name to save the content to.
        """
        file_to_save = file_name if file_name else self.file_name
        
        try:
            with open(file_to_save, 'w') as file:
                file.write(content)
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")

# Only run the following if this script is executed directly
if __name__ == "__main__":
    path = input("Enter the path to the text file: ")
    reader = ReadWriteTextFile()
    result = reader.read()
    print(result)
