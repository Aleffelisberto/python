mat, hourglassSum, maxSum = [], 0, -63
for _ in range(6):
    mat.append(list(map(int, input().rstrip().split())))

for i in range(4):
    for j in range(4):
        hourglassSum, maxK, maxL = 0, i+3, j+3
        for k in range(i, maxK):
            for l in range(j, maxL):
                if k == i+1:
                    if l == j+1:
                        hourglassSum += mat[k][l]
                    else:
                        continue
                else:
                    hourglassSum += mat[k][l]
        if hourglassSum > maxSum:
            maxSum = hourglassSum

print(maxSum)
