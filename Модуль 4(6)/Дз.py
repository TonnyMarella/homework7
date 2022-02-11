from typing import List

lst: list[int] = [1]


def main(lst: List[int]) -> List[str]:
    result = []
    for i in lst:
        result.append(str(i))
    return result


print(type(main(lst)))
print(type(main(lst)[0]))
