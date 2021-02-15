class featured_rank(int):
    def __init__(self, s):
        if s == '__OFF__':
            self = -2
        elif s == '__LAST__':
            self = -1
        else:
            self = int(s)