path = "limericks.txt"

f = open(path, "r", encoding="utf-8")
new_path = "limericks_clean.txt"
new_file = open(new_path, "w", encoding="utf-8")
for line in f:
    res_line = line.replace(".", "")
    new_file.write(res_line)
f.close()
new_file.close()
