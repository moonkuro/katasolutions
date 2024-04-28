def are_you_playing_banjo(name):
    firstLetter = name[0]
    if firstLetter == "R" or firstLetter == "r":
        return name + " plays the banjo"
    else:
        return name + " does not play banjo"