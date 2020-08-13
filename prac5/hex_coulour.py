COLOUR_DICT = dict(aliceblue="#f0f8ff", antiquewhite="#faebd7", antiquewhite1="#ffefdb", antiquewhite2="#ffefdb",
                   antiquewhite3="#cdc0b0",
                   aquamarine1="#7fffd4", aquamarine2="#76eec6", azure1="#f0ffff", azure4="	#838b8b",
                   beige="#838b8b")
print(COLOUR_DICT)
color = input("Enter the name of the color: ").lower()
while color != "":
    if color in COLOUR_DICT:
        print(color, "is", COLOUR_DICT[color])
    else:
        print("Invalid color name")
    color = input("Enter the name of the color: ").lower()