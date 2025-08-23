import os
import re
def get_file_path(filename):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, filename)

    
    extracted_numbers = []
    count = 0
    with open (file_path, "r", encoding="utf-8") as f:
     for line in f:
        extracted_numbers = re.findall("\[0-9.]+", line)
        for num in extracted_numbers:
         val = float (num)
        extracted_numbers.append(val)
        count += val

    print ("total summation: ", count)




