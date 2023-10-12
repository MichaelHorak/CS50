class Jar:
    def __init__(self, capacity=12):
        if isinstance(capacity, int) and capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError
        self._cookies = 0
    # __init__ should initialize a cookie jar with the given capacity,
    # which represents the maximum number of cookies that can fit in the
    # cookie jar.
    # If capacity is not a non-negative int, though, __init__ should instead
    # raise a ValueError.

    def __str__(self):
        return f"{self._cookies * '🍪'}"
    # __str__ should return a str with 🍪, where is the number of cookies
    # in the cookie jar. For instance, if there are 3 cookies in the cookie
    # jar, then str should return "🍪🍪🍪"

    def deposit(self, n):
        addition = self._cookies + n
        if addition > self._capacity:
            raise ValueError
        self._cookies = addition
    # deposit should add n cookies to the cookie jar. If adding that many
    # would exceed the cookie jar’s capacity, though, deposit should instead
    # raise a ValueError.

    def withdraw(self, n):
        subtraction = self._cookies - n
        if subtraction < 0:
            raise ValueError
        self._cookies = subtraction
    # withdraw should remove n cookies from the cookie jar. Nom nom nom. If
    # there aren’t that many cookies in the cookie jar, though, withdraw should
    # instead raise a ValueError.

    @property
    def capacity(self):
        return self._capacity
    # capacity should return the cookie jar’s capacity.

    @property
    def size(self):
        return self._cookies
    # size should return the number of cookies actually in the cookie jar, initially 0.


def main():
    cookie_jar = Jar(6)
    print(cookie_jar)
    cookie_jar.deposit(3)
    print(cookie_jar)
    cookie_jar.withdraw(1)
    print(cookie_jar)


if __name__ == "__main__":
    main()
