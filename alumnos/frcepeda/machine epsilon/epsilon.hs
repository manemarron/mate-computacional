import Data.Maybe
import Data.List

twoPows :: [Double]
twoPows = 1 : map (/ 2) twoPows
main = print . fromJust . findIndex (== 1) $ map (1+) twoPows
