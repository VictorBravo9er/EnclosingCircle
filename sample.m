function sample()
    load("data.txt");
    cent = mean(data);
    [i, point, dist] = farthestPoint(data, cent);
    disp(data(1:10,:));
    disp(i);
    disp(point);
    disp(dist(1:10));
end;

function [dist] = distanceSq(A, B)
    dist = sum((A - B) .^ 2, 2);
end;

function [dist] = distance(A, B)
    dist = (sum((A - B) .^ 2, 2)) .^ (0.5);
end;

function [idx, point, dist] = farthestPoint(A, B)
    dist = distance(A, B);
    [_, idx] = max(dist);
    point = A(idx, :);
end;
