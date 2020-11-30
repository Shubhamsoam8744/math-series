
# Explaining 1

 in case the (n) value in negative or string typye it will return the invalid message
 the 0 and 1 are the base cases that are the segnature of fibonacci
 in the normal cases lets say the input were 4, the fuction will work like this:

 fibonacci(4) = fibonacci(3)                                  +fibonacci(2)
                fibonacci(2)        +      fibonacci(1)       +fibonacci(1)+fibonacci(0)
                fibonacci(1)+fibonacci(0)+       1            +      1     +     0
                     1      +     0      +       1            +      1     +     0       =        3

 and so on

----------------------------------------------------------------

# Explaining 2

 in case the (n) value in negative or string typye it will return the invalid message
 the 2 and 1 are the base cases that are the segnature of lucas
 in the normal cases lets say the input were 4, the fuction will work like this:

 lucas(4) =     lucas(3)                          +lucas(2)
                lucas(2)        +    lucas(1)     +lucas(1)+lucas(0)
                lucas(1)+lucas(0)+     1          +    1   +   2
                   1    +   2    +     1          +    1   +   2     =      7

 and so on

----------------------------------------------------------------

# Explaining 3

in case the (n) value in negative or string typye it will return the invalid message
the 0 and 1 are the base cases with the default of the fibonacci values returned
in the normal cases lets say the input were 4 and the default left as it is, the fuction will work like this:

sum_series(4) = sum_series(3)                                   +sum_series(2)
                sum_series(2)        +      sum_series(1)       +sum_series(1)+sum_series(0)
                sum_series(1)+sum_series(0)+       1            +       1     +      0
                     1       +     0       +       1            +       1     +      0       =        3

but if v1 and v2 changed to be 10,10 it will work like this 

sum_series(4) = sum_series(3)                                   +sum_series(2)
                sum_series(2)        +      sum_series(1)       +sum_series(1)+sum_series(0)
                sum_series(1)+sum_series(0)+       10           +      10     +      10
                     10      +     10      +       10           +      10     +      10       =        50

 and so on
