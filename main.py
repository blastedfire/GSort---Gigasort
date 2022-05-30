def Sort(ilist):
    if not type(ilist) == list:
        return "Invalid input. It must be a list."

    sorted = ilist
    for i in range(len(ilist) - 1):
        for ii in range(i + 1, len(ilist)):
            if sorted[i] > sorted[ii]:
              
                var = sorted[i]
                sorted[i] = sorted[ii]
                sorted[ii] = var

    return sorted
