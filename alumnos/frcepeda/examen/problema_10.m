d = double([10000, 10001, 10002]);
s = single(d);
% no hay floats de 16 bits en octave .-.

var1 = @(a) sum((a - mean(a)) .^ 2) / (columns(a) - 1);
var2 = @(a) (sum(a .^ 2) - sum(a) ^ 2 / columns(a)) / (columns(a) - 1);

var1s = var1(s) % 1
var2s = var2(s) % 0
var1d = var1(d) % 1
var2d = var2(d) % 1
