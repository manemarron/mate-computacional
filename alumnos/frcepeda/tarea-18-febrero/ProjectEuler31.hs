{-
 - We use dynamic programming to solve the classical coin change problem.
 - Let the coins' denominations in cents be a_0, a_1, ..., a_{c+1}, and let
 - f(n, i) = how many ways to represent n cents using coins from the set
 - {a_i, a_{i+1}, ...}.
 - Notice that f(0, c) = 1 and f(x, c) = 0 for all other x.
 - Also, f(n, i) = 0 if n < 0.
 - Finally, f(n, i) = f(n - a_i, i) + f(n, i+1).
 - The following code computes f(200,0) using a fold over a list of lists.
 -}

knapsack xs n = last (foldr f (1:replicate n 0) xs)
    where f k xs = xs'
            where xs' = zipWith (+) xs ((replicate k 0) ++ xs')

main = print (knapsack [1,2,5,10,20,50,100,200] 200)
