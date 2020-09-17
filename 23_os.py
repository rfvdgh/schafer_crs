import os
from datetime import datetime

os.chdir("/home/poopmonkey")

# os.mkdir('OS-Demo-2')
# os.makedirs("OS-Demo-2/Sub-Dir-1")  # will make sub dirs unlike previous

# os.rmdir("OS-Demo-2")
# os.removedirs("OS-Demo-2/Sub-Dir-1")  # will delete sub dirs unlike previous

# os.rename("test.txt", "demo.txt")
# mod_time = os.stat("demo.txt").st_mtime
# print(datetime.fromtimestamp(mod_time))

# print(os.listdir())

# does'nt work
# for dirpath, dirnames, filenames in os.walk("\home\poopmonkey"):
#     print("Current Path:", dirpath)
#     print("Directories:", dirnames)
#     print("Files:", filenames)
#     print()

# print(os.environ.get("HOME"))

# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)

print(os.path.basename("/tmp/test.txt"))  # fake path
print(os.path.dirname("/tmp/test.txt"))  # fake path
print(os.path.split("/tmp/test.txt"))  # fake path
print(os.path.exists("/tmp/test.txt"))
print(os.path.isfile("/tmp/test.txt"))
print(os.path.isdir("/tmp/test.txt"))
print(os.path.splitext("/tmp/test.txt"))  # separates the extension
