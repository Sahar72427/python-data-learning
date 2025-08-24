import os
import re
def get_file_path(filename):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file = open("filename.txt", "r")
    extracted_numbers = []
    count = 0
    for line in file:
        extracted_numbers = re.findall("\[0-9.]+", line)
        for s in extracted_numbers:
            try:
                num = float(s)
                extracted_numbers.append(num)
                count += num
            except:
                pass
    print("total summation:", count)
