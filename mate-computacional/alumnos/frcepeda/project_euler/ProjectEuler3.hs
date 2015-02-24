-- An infinite list of all primes.
-- A prime number only has one nontrivial factor.
primes = 2 : filter (null . tail . primeFactors) [3,5..]

-- A dumb, slow way of factorizing an integer.
-- It works fast enough, though. This will return a list with each
-- prime factor listed only once, regardless of multiplicity.
primeFactors :: Int -> [Int]
primeFactors n | n > 1 = factorize n primes -- try factorizing with all primes in order
    where factorize n (p:ps)
            -- if n is greater than the square of the candidate, n is prime
            -- (the following primes will only be greater than p.)
            | p * p > n      = [n]
            -- if p divides n, add p to the list
            | n `mod` p == 0 = p : factorize (n `div` p) ps
            -- otherwise, try with the next prime
            | otherwise      = factorize n ps

-- I will be using this sieve quite a lot. There are other ways of making
-- sieves in purely functional languages. This (awesome) paper outlines them.
-- http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf

main = print . maximum . primeFactors $ 600851475143
