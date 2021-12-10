from os import error
import sys
def find_most_active(argv):
    if (len(argv) != 4):
        print("Usage: py most-active-cookie.py [file] -d [date]")
        return


    # parse csv file
    try:
        fp = open(argv[1], "r")
    except:
        raise(error)
    next(fp)
    lines = fp.readlines()
    instance_counter = {}
    for line in lines:
        arguments = line.split(",")
        # print(arguments)
        if (len(arguments) != 2):
            raise(error)
            return []
        time_arguments = arguments[1].split("T")
        if (time_arguments[0] == argv[3]):
            if arguments[0] not in instance_counter:
                instance_counter[arguments[0]] = 1
            else:
                instance_counter[arguments[0]] += 1

    # execute on information stored in instance_counter
    most_active_cookies = []
    cookie_count_max = 0
    for key in instance_counter:
        if instance_counter[key] > cookie_count_max:
            cookie_count_max = instance_counter[key]
            most_active_cookies = [key]
        elif instance_counter[key] == cookie_count_max:
            most_active_cookies.append(key)

    [print(item) for item in most_active_cookies]
    fp.close()
    return most_active_cookies

def main():
    print(sys.argv)
    find_most_active(sys.argv)
    return


if __name__ == "__main__":
    main()