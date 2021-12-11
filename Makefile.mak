all: most_active_cookie

most_active_cookie: test_implementation.c
    gcc test_implementation.c -o most_active_cookie

clean:
    rm -f *.o most_active_cookie