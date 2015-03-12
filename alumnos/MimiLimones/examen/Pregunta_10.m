

varianza= @(n) (sum((n-((1.0/n)*sum(n)))**2))/(n-1);

doub=double([10000,10001,10002]);
sin=single([10000,10001,10001]);

varianzar1=varianza(doub)
varianzar2=varianza(sin)


