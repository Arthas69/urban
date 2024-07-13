def count_calls():
    global calls
    calls += 1


def string_info(string: str) -> tuple[int, str, str]:
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(st: str, strings: list) -> bool:
    count_calls()
    return st.lower() in map(str.lower, strings)


if __name__ == '__main__':
    calls = 0

    print(string_info('Capybara'))
    print(string_info('Armageddon'))
    print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
    print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
    print(calls)