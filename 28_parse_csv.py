import csv

# example 1
# with open("28_names.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # next(csv_reader)  # generator that steps over the title

#     # copying csv file, but uses a different delimiter
#     with open("28_new_names.csv", "w") as new_file:
#         csv_writer = csv.writer(new_file, delimiter="\t")

#         for line in csv_reader:
#             csv_writer.writerow(line)

# example 2
# with open("28_names.csv", "r") as csv_file:
#     csv_reader = csv.reader(
#         csv_file, delimiter="\t"
#     )  # need to specify delimiter if you want to print out right

#     for line in csv_reader:
#         print(line)

# example 3
# more obvious what fields are being acted upon
with open("28_names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line["email"])

    with open("28_new_names.csv", "w") as new_file:
        fieldnames = ["first_name", "last_name"]

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")

        csv_writer.writeheader()

        for line in csv_reader:
            del line["email"]
            csv_writer.writerow(line)
