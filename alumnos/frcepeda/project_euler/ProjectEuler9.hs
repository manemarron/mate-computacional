n = 1000

-- Yeah, it's slow. So what?
triple = [[a,b,c] | a <- [1..n], b <- [a..n], let c = n - a - b, c*c == a*a + b*b]

main = print . product . head $ triple
