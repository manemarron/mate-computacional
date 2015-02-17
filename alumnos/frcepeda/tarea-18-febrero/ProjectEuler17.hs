{-
 - f :: Int -> String turns a number into a string following the british rules.
 - It was easier to implement it this way since I could spot mistakes quickly.
 - Map f over the range required, then concat all the strings and get the length.
 -}

units = ["", "one","two","three","four","five","six","seven","eight","nine"]
teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

f n
    | n < 10 = units !! n
    | n < 20 = teen !! (mod n 10)
    | n < 100 = let (q,r) = quotRem n 10 in tens !! q ++ f r
    | n < 1000 = let (q,r) = quotRem n 100 in
                    units !! q ++ "hundred" ++
                    if r == 0 then "" else "and" ++ f r
    | otherwise = "onethousand"

main = print . length . concatMap f $ [1..1000]
