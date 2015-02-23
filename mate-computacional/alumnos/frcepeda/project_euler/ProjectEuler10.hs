-- Same old sieve as before.
primes = 2 : filter (null . tail . primeFactors) [3,5..]

primeFactors n = factorize n primes
            where factorize n (p:ps)
                        | p * p > n      = [n]
                        | n `mod` p == 0 = p : factorize (n `div` p) ps
                        | otherwise      = factorize n ps

-- It's slowish. But meh, really. 2 seconds isn't that bad and
-- most of the code is reused from the last problem, anyway.
-- You may want to compile this with -O2.
main = print . sum . takeWhile (< 2000000) $ primes
