def find_longest_word(words):
    return max(words, key=len)

def print_top(word_len, north):
    top="─".ljust(word_len,"─")
    empty=" ".ljust(word_len)
    north_justed=(north + " (N)" if north else "").center(word_len)

    print(f"┌{top}┬{top}┬{top}┐") 
    print(f"│{empty}│{north_justed}│{empty}│")
    print(f"├{top}┼{top}┼{top}┤")

def print_middle(word_len,west, east):
    west_justed=(west + " (W)" if west else "").center(word_len)
    east_justed=(east + " (E)" if east else "").center(word_len)
    here="X".center(word_len)

    print(f"│{west_justed}│{here}│{east_justed}│")

def print_bottom(word_len, south):
    top="─".ljust(word_len,"─")
    south_justed=(south + " (S)" if south else "").center(word_len)
    empty=" ".ljust(word_len)

    print(f"├{top}┼{top}┼{top}┤")
    print(f"│{empty}│{south_justed}│{empty}│")
    print(f"└{top}┴{top}┴{top}┘")

def print_map(current):
    directions = {"n": "", "s":"", "e":"", "w":""}

    for key in directions:
        directions[key]=current["options"].get(key,"")
        
    print_top(40,directions["n"])
    print_middle(40,directions["w"], directions["e"])
    print_bottom(40,directions["s"])
