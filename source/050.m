ps = primes(1000000);
found = false;
number = 0;
len = length(ps);
maxp = ps(len);
for l = len:-1:1
    for i = 1:len-l+1
        number = sum(ps(i:i+l-1));
        if (number > maxp)
            break;
        end

        if (any(ps(:) == number))
            printf('%d\n', number);
            found = true;
            break;
        end;    
    end

    if (found == true)
        break;
    end
end
