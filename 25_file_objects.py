# File objects

# f = open("25_test.txt", "r")
# print(f.name)
# f.close()

# with open("25_test.txt", "r") as f:

# for line in f:
#     print(line, end="")

# f_contents = f.readline()
# print(f_contents, end="")
# f_contents = f.readline()
# print(f_contents, end="")

# f_contents = f.read(100)  # first 100 characters
# print(f_contents, end="")
# print(f.tell())
# f_contents = f.read(100)
# print(f_contents, end="")
# f_contents = f.read(100)  # empty string here
# print(f_contents, end="")

# size_to_read = 10
# f_contents = f.read(size_to_read)
# while len(f_contents) > 0:
#     print(f_contents, end="*")
#     f_contents = f.read(size_to_read)

# size_to_read = 10
# f_contents = f.read(size_to_read)
# print(f_contents, end="")
# f.seek(0)
# f_contents = f.read(size_to_read)
# print(f_contents)

# with open("test2.txt", "w") as f:
#     f.write("Test")

# with open("25_test.txt", "r") as rf:
#     with open(25_test_copy.txt, "w") as wf:
#         for line in rf:
#             wf.write(line)

# for pictures
# with open("25_penguin.png", "rb") as rf:
#     with open("[25]penguin_copy.png", "wb") as wf:
#         for line in rf:
#             wf.write(line)

# for more control
with open("25_penguin.png", "rb") as rf:
    with open("25_penguin_copy.png", "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
