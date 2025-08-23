import re
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else input("Enter filename: ").strip()
with open(filename, "r", encoding="utf-8") as f:
    nums = [int(n) for n in re.findall(r"\d+", f.read())]

print("Sum =", sum(nums))





