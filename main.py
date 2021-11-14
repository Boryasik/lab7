def merge(*lists):
    final_list = []

    for k in range(len(lists)):
        final_list += lists[k]

    final_list.sort()
    return final_list
