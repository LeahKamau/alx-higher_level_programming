#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = ""
    for ch in range(len(str)):
        if ch != n:
            str_cpy = str_cpy + str[ch]
    return (str_cpy)
