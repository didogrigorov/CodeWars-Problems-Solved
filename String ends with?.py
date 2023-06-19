def solution(text, ending):
    result = []
    i = 0

    if len(ending) > len(text):
        return False

    for item in reversed(ending):
        i -= 1
        if item == text[i]:
            result.append(item)

    result.reverse()
    final_result = ''.join(result)
    return final_result == ending


print(solution('ails', 'fails'))