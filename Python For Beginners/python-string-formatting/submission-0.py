def say_goodbye(name: str, hour: int) -> str:
    return f"Goodbye, {name}. See you again at {hour} o'clock."

    # Another solution:
    # return "Goodbye, {}. See you again at {} o'clock.".format(name, hour)


# do not modify below this line
print(say_goodbye("Bob", 12))
print(say_goodbye("Jane", 4))
print(say_goodbye("NeetCode", 9))
