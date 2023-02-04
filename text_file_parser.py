class TextFileParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def search(self, search_string=None, start_pattern=None, end_pattern=None, before=0, after=0, as_json=False, as_list=False):
        """
        Search the text file for lines containing the specified search string or between start and end patterns and return the matched lines.
        Optionally include a specified number of lines before and/or after each matched line.
        Return the lines in either JSON, list, or multi-line string format.

        Args:
            search_string (str, optional): The string to search for in the file.
            start_pattern (str, optional): The string to search for as the start pattern.
            end_pattern (str, optional): The string to search for as the end pattern.
            before (int, optional): The number of lines to include before each matched line. Defaults to 0.
            after (int, optional): The number of lines to include after each matched line. Defaults to 0.
            as_json (bool, optional): Return the lines in JSON format. Defaults to False.
            as_list (bool, optional): Return the lines in list format. Defaults to False.

        Returns:
            Union[str, List[str], dict]: The matched lines in the specified format.
        """
        result = []
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            start = 0
            end = len(lines)
            if start_pattern:
                for i, line in enumerate(lines):
                    if start_pattern in line:
                        start = i
                        break
            if end_pattern:
                for i, line in enumerate(lines[start:]):
                    if end_pattern in line:
                        end = start + i + 1
                        break
            if search_string:
                for i, line in enumerate(lines[start:end]):
                    if search_string in line:
                        start_i = max(start, i - before)
                        end_i = min(end, i + after + 1)
                        result.append(lines[start_i:end_i])
            else:
                result.append(lines[start:end])

        if as_json:
            return {"lines": result}
        elif as_list:
            return result
        else:
            return "\n".join(["".join(line) for line in result])
