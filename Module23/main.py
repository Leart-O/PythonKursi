from typing import Optional, Union, Any, List

def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name())

def process_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Integer: {value}"
    return f"String: {value}"

print(process_value("DS"))

def process_anything(value: Any) -> str:
    return f"Value: {value}"

print(process_anything("Any string"))

def sum_list(numbers: List[int]) -> int:
    return sum(numbers)

numbers: List[int] = [1, 2, 3]
result: int = sum_list(numbers)
print(result)