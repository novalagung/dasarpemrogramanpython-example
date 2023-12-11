quotes = [
    "never let anyone live in your head rent free",
    "if others can do it, then why should I?",
    "\n".join([
        "I'm sick of following my dreams, man.",
        "I'm just going to ask where they're going and hook up with 'em later."
    ]),
]

from random import randint

def print_random_quote():
    """
    function `print_random_quote()`:
        print one random quote,
        so nothing special
    """

    i = randint(0, len(quotes)-1)
    print(quotes[i])

class Quote:
    """
    class `Quote`:
        A class Quote represent a quote.
        It has the following two attributes:
            - class attribute `note`
            - instance method `print_quote()`
    """

    note = "A class to represent quote"
    """
        instance method `print_quote()`:
            Responsible to print specific quote by index
    """ 

    @classmethod
    def print_quote(cls, i):
        """
        instance method `print_quote()`:
            Responsible to print specific quote by index
        """

        print(quotes[i])
