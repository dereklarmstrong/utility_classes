class CreditCard:
    """A class to search a text file for credit card numbers, validate them using Luhn's algorithm, and mask them if specified

    Attributes:
        file_path (str): path to the text file to be searched
        credit_card_numbers (list): list to store all the credit card numbers found in the text file
        mask_credit_card_numbers (bool): flag to determine if found credit card numbers should be masked in the text file

    Methods:
        find_credit_card_numbers: searches the text file for credit card numbers and masks them if specified
        validate_credit_card_number: performs Luhn's algorithm to validate a credit card number
        mask_credit_card_number: masks a credit card number by leaving only the last 4 digits
    """

    def __init__(self, file_path: str, mask_credit_card_numbers: bool = False):
        """Initialize the class with the file path to be searched and masking flag"""
        self.file_path = file_path
        self.credit_card_numbers = []
        self.mask_credit_card_numbers = mask_credit_card_numbers

    def find_credit_card_numbers(self):
        """Search the text file for credit card numbers and mask them if specified"""
        try:
            with open(self.file_path, "r") as file:
                lines = file.readlines()
            with open(self.file_path, "w") as file:
                for line in lines:
                    for word in line.split():
                        if len(word) == 16 and word.isdigit():
                            if self.validate_credit_card_number(word):
                                self.credit_card_numbers.append(word)
                                if self.mask_credit_card_numbers:
                                    line = line.replace(word, self.mask_credit_card_number(word))
                    file.write(line)
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")

    def validate_credit_card_number(self, credit_card_number: str):
        """Perform Luhn's algorithm to validate a credit card number

        Args:
            credit_card_number (str): credit card number to be validated

        Returns:
            bool: True if the credit card number is valid, False otherwise
        """
        total = 0
        num_digits = len(credit_card_number)
        odd_even = num_digits & 1

        for count in range(0, num_digits):
            digit = int(credit_card_number[count])

            if not ((count & 1) ^ odd_even):
                digit = digit * 2
            if digit > 9:
                digit = digit - 9

            total = total + digit

        return (total % 10) == 0
    
    def mask_credit_card_number(credit_card_number: str):
        """Mask a credit card number by leaving only the last 4 digits visible

        Args:
            credit_card_number (str): the credit card number to be masked

        Returns:
            str: the masked credit card number with only the last 4 digits visible
        """
        masked_number = "*" * (len(credit_card_number) - 4) + credit_card_number[-4:]
        return masked_number
