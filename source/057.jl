num, den = BigInt(1), BigInt(2)
res = 0
lim = 1000

for i = 1:lim
    if length(string(num + den)) > length(string(den))
        res += 1
    end

    hold = num + 2 * den
    num = den
    den = hold
end

println(res)
