all: most_active_cookie

most_active_cookie: most_active_cookie.c
    gcc most_active_cookie.c -o most_active_cookie

clean:
    rm -f *.o most_active_cookie