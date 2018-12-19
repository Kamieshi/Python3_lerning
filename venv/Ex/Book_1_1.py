zero = ["  ****  ",
        " **  ** ",
        "**    **",
        " **  ** ",
        "  ****  "]

one = ["   **   ",
       "   **   ",
       "   **   ",
       "   **   ",
       "   **   "]

two = ["  ***** ",
       " **  ** ",
       "    **  ",
       "  **    ",
       " ****** "]

three = ["  ***** ",
         "     ** ",
         "   **   ",
         "     ** ",
         "  ***** "]

fore = [" **  ** ",
        " **  ** ",
        " ****** ",
        "     ** ",
        "     ** "]

five = [" ****** ",
        " **     ",
        " ****** ",
        "     ** ",
        " ****** "]

six = [" ****** ",
       " **     ",
       " ****** ",
       " **  ** ",
       " ****** "]

seven = [" ****** ",
         "     ** ",
         "   **   ",
         "  **    ",
         " **     "]

eight = [" ****** ",
         " **  ** ",
         " ****** ",
         " **  ** ",
         " ****** "]

nine = [" ****** ",
        " **  ** ",
        " ****** ",
        "     ** ",
        " ****** "]
point = ["        ",
         "        ",
         "        ",
         "   **   ",
         "   **   "]

numbers_list = [zero, one, two, three, fore, five, six, seven, eight, nine,point]


def convert_print(number):
    try:
        float(number)
    except Exception as e:
        print("Введите число типа float(12.5)")
        return e
    number = str(number)
    line_out = ""
    index_line = 0
    while index_line < len(numbers_list[0]):
        for item in number:
            try:
                line_out += numbers_list[int(item)][index_line]
            except ValueError:
                line_out += numbers_list[10][index_line]
        index_line += 1
        print(line_out)
        line_out = ""

    return 0

