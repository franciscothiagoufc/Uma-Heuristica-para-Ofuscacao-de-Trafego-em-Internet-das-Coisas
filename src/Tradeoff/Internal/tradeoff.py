def tradeoff(acurracy,overhead):
    result = []
    for i,j in zip(acurracy,overhead):
        result.append((1-i)/j)
    return result