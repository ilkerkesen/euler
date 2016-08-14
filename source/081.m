load p081_matrix.txt;
matrix = p081_matrix;
[m, n] = size(matrix);

for i = 1:m
    for j = 1:n
        if (i == 1 && j == 1)
            continue;
        elseif (i == 1)
            matrix(i, j) += matrix(i, j-1);
        elseif (j == 1)
            matrix(i, j) += matrix(i-1, j);
        else
            matrix(i, j) += min(matrix(i, j-1), matrix(i-1, j));
        end
    end
end

printf('%d\n', matrix(m, n));
