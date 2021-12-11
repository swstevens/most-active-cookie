from os import error
import sys
import datetime
def find_most_active(argv):
	# processing flags
    i = 2
    dateflag=False
    date = ''
    while (i< len(argv)):
        if (argv[i][0]!= '-'):
            i+=1
            continue
        if ("d" in argv[i]):
            dateflag = True
            try: 
                date = datetime.date.fromisoformat(argv[i+1])
            except:
                print("Usage: ./most_active_cookie [File] -d [Date]")
                raise(error)
        i+=1



    # parse csv file based on flags from argv
    try:
        fp = open(argv[1], "r")
    except:
        raise(error)
    next(fp)
    lines = fp.readlines()
    instance_counter = {}
    if dateflag:
        for line in lines:
            arguments = line.split(",")
            # print(arguments)
            if (len(arguments) != 2):
                fp.close()
                raise(error)
            #TODO incoroporate UTC datetime for check
            arguments[1] = arguments[1].rstrip("\n")
            cookie_time = datetime.datetime.fromisoformat(arguments[1])
            if (cookie_time.date() == date):
                if arguments[0] not in instance_counter:
                    instance_counter[arguments[0]] = 1
                else:
                    instance_counter[arguments[0]] += 1

    # execute on information stored in instance_counter
    most_active_cookies = []
    max_cookie_count = 0
    for key in instance_counter:
        if instance_counter[key] > max_cookie_count:
            max_cookie_count = instance_counter[key]
            most_active_cookies = [key]
        elif instance_counter[key] == max_cookie_count:
            most_active_cookies.append(key)

    [print(item) for item in most_active_cookies]
    fp.close()
    return most_active_cookies

def main():
    # print(sys.argv)
    find_most_active(sys.argv)
    return


if __name__ == "__main__":
    main()