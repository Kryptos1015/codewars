def solution(args):
    result = []
    start = end = args[0]
    for n in args[1:]:
        if n - end == 1:
            end = n
        else:
            if start == end:
                result.append(str(start))
            elif end - start == 1:
                result.append(f"{start},{end}")
            else:
                result.append(f"{start}-{end}")
            start = end = n
    if start == end:
        result.append(str(start))
    elif end - start == 1:
        result.append(f"{start},{end}")
    else:
        result.append(f"{start}-{end}")
    return ','.join(result)
