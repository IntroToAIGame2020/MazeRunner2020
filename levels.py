

def get_maze(index):
    level_1 = [
    "X   ",
    "   X",
    "X   "
    ]

    level_2 = [
    "XX   X",
    "   X  ",
    "  XX  ",
    " X  X ",
    "X   X ",
    "  X  X",
    "XX   X",
    "   X  "
    ]

    level_3 = [
    "  X X  ",
    "      X",
    "X    XX",
    "   X XX",
    "  X XXX",
    "   X   ",
    "X    XX",
    ]

    level_4 = [
    "XXXXXXXX",
    "   XX   ",
    "X  X X X",
    "   XXX  ",
    "X  X XX ",
    "XX X  X ",
    " X X X  ",
    "X    XX ",
    "   X XXX",
    "X  XX  X",

    ]

    level_5 = [
    "XXXXXXXXXXXX",
    "X      XX  X",
    "X    XXX   X",
    "X  XX X X X ",
    "XX XXXX X  X ",
    "X  XX X   XX",
    "XX  XXXX XXX",
    "X        XXX",
    "X   X      X",
    "XX   XXX  XX"
    ]

    if index == 1:
        return level_1
    elif index == 2:
        return level_2
    elif index == 3:
        return level_3
    elif index == 4:
        return level_4
    elif index == 5:
        return level_5
    
