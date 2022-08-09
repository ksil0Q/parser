def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    d = {}
    for index, number in enumerate(nums):
        if d.get(number) and index + 1 - d[number] <= k:
            return True
        d[number] = index + 1
    return False


if __name__ == '__main__':
    containsNearbyDuplicate([1,0,1,1], 1)
