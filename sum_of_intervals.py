def sum_of_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = []
    for i in intervals:
        if not merged:
            merged.append(i)
        else:
            last_i = merged[-1]
            if i[0] <= last_i[1]:
                merged[-1] = (last_i[0], max(last_i[1], i[1]))
            else:
                merged.append(i)
    return sum(end - start for start, end in merged)
