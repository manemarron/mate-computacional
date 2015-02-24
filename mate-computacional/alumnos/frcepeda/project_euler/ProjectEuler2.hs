-- The awesomest way to write the fibonacci sequence.
-- Yes, this is an infinite list. You may want to read up on zipWith.
fib = 0 : 1 : zipWith (+) fib (tail fib)

main = print . sum . filter even . takeWhile (< 4000000) $ fib
