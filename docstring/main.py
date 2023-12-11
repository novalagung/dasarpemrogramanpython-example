from quote import Quote, print_random_quote

if __name__ == '__main__':
    print_random_quote()
    Quote.print_quote(2)
    print(Quote.note)

    # # menampilkan docstring fungsi `print_random_quote()`
    # print(print_random_quote.__doc__)

    # # menampilkan docstring class `Quote`
    # print(Quote.__doc__)

    # # menampilkan docstring class method `Quote.print_quote()`
    # print(Quote.print_quote.__doc__)
