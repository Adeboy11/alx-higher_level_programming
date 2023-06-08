#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    cases = dir(hidden_4)
    for case in cases:
        if case[:2] != "__":
            print(case)
