def partial_sums(*args):
    sums = [0]
    for i, x in enumerate(args):
        sums.append(x + sums[i])
    return sums


print(partial_sums(13))
