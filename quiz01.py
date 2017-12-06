def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    base = 2
    number = 1
    while True:
        if a==1 and b==1:
            return number
        elif a%base==0:
            number = number*base
            a=a/base
            if b%base==0:
                b=b/base
        elif b%base==0 :
            number = number*base
            b=b/base
        else:
            base=base+1




def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    m=0
    unique=0

    while n != 0:
        if has_digit(m,n%10) == False:
            unique = unique+1
            m = m*10+ n%10
        n=n/10

    return unique


def has_digit(m,k):
    while m!=0:
        if m%10==k:
            return True
        else:
            m=m/10
    return False

