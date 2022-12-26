## Python module that formats Persian number to Latin
## Github: https://github.com/Kourva/ChNumber


class ChNumber:
    """
    :: Converts Farsi numbers to Latin"
    """

    def format(number):
        """
        :: format method:
             -> Usage:
                    ChNumber.format(number)
             -> Example:
                    ChNumber.format("۰۹۱۴۶۵۷۹۸۱۴")
             -> Result:
                    "09146579814"
        """
        data = {
            "۱": "1",
            "۲": "2",
            "۳": "3",
            "۴": "4",
            "۵": "5",
            "۶": "6",
            "۷": "7",
            "۸": "8",
            "۹": "9",
            "۰": "0",
        }
        temp = number
        for digit in temp:
            if digit in data:
                temp = temp.replace(digit, data[digit])
        return temp
