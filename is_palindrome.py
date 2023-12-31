def is_palindrom(word):
    """ Function that cheks word for palindrome. """

    if word == word[::-1]:
         print("True")
    else:
         print("False")

if __name__ == "__main__":
    n = 'racecar'
    s = 'top'
    is_palindrom(n)
    is_palindrom(s)
    