import os

os.chdir("/home/poopmonkey/wildcards/automate_parse")

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)

    f_title, f_course, f_num = f_name.split("-")

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip().zfill(2)  # will pad 0s on the single digits

    print("{}-{}-{}{}".format(f_num, f_course, f_title, f_ext))

    # new_name = ("{}-{}-{}{}".format(f_num, f_course, f_title, f_ext))
    # os.rename(f, new_name)
