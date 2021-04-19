import os

def file_test(filename, action):
    """The below code first checks the file mode like read or write"""

    if action == "r":
        """If it is read mode, it checks whether the input is a file path and also file exists."""

        if os.path.isfile(filename):
            """If the file exists, it then checks if the file is empty or not"""

            if os.path.getsize(filename) != 0:

                filedata = open(filename, action)
                words = filedata.read().split()
                max_leng = len(max(words, key=len))
                max_words = [word for word in words if len(word) == max_leng]
                transposed_list = [word[::-1] for word in max_words]

                return max_words, transposed_list

            else:
                return "File is empty"

        else:
            return "File doesnot exist or invalid file name or invalid file path"

    else:
        return "Check file options"