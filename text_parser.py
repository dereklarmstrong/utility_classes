import json

class TextParser:
    """A class to parse text files and retrieve matching patterns

    Attributes:
        file_path (str): path to the text file to be parsed
        start_pattern (str): start pattern to be searched in the text file
        end_pattern (str): end pattern to be searched in the text file

    Methods:
        parse_file: retrieves all text in the text file that lies between start and end patterns
    """

    def __init__(self, file_path: str, start_pattern: str = None, end_pattern: str = None):
        """Initialize the class with file path and start and end patterns to be searched"""
        self.file_path = file_path
        self.start_pattern = start_pattern
        self.end_pattern = end_pattern

    def parse_file(self, return_format: str = "string"):
        """Retrieve all text in the text file that lies between start and end patterns

        Args:
            return_format (str): format in which the matching text should be returned (default: "string")
                                 options: "string", "json", "list"

        Returns:
            str/list/dict: matching text based on the specified return format
        """
        matching_text = []
        start_found = False
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    if self.start_pattern and self.end_pattern:
                        if self.start_pattern in line:
                            start_found = True
                        if start_found:
                            matching_text.append(line.strip())
                            if self.end_pattern in line:
                                break
                    elif self.start_pattern:
                        if self.start_pattern in line:
                            matching_text.append(line.strip())
                            break
                    else:
                        matching_text.append(line.strip())
            
            if return_format == "string":
                return "\n".join(matching_text)
            elif return_format == "list":
                return matching_text
            elif return_format == "json":
                return json.dumps(matching_text)
            else:
                print("Error: Invalid return format. Choose either 'string', 'list', or 'json'.")
                return None
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
