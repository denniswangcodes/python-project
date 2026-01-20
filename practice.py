def clean_numbers(nums: list[int]) -> list[int]:
    return [n for n in nums if n > 0 and n % 2 == 0 ]

def everage(nums: list[float]) -> float:
    if not nums:
        raise ValueError("Not a list of numbers")
    return sum(nums) / len(nums)

def safe_get(d: dict, key: str, default=None):
    return d.get(key, default)

