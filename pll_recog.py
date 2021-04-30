pll = {
    "Aa": "brrggbrogobobrr",
    "Ab": "orrggobobrbgorr",
    "E": "grbrgobogobrgrb",
    "F": "gggorbrboborggg",
    "Ga": "ogobrrggobrbgogo",
    "Gb": "gbgorbroobgrgbg",
    "Gc": "rgrgbobrgoobrgr",
    "Gd": "gbgogbrroborgbg",
    "H": "orobgbrorgbgoro",
    "Ja": "gggoobrrobbrggg",
    "Jb": "gggobbroobrrggg",
    "Na": "gbbroobggorrgbb",
    "Nb": "ggbrrobbgoorggb",
    "Ra": "ogobbrgrbrogogo",
    "Rb": "rgrgrobogobbrgr",
    "T": "gbgoobrgobrrgbg",
    "Ua": "bbbrgrgogorobbb",
    "Ub": "bbbrorgrgogobbb",
    "V": "roobbgogrgrbroo",
    "Y": "rrobggobrgobrro",
    "Z": "gogogobrbrbrgog"
}

def next_colour(colour: str) -> str:
    next = {
        "g": "o",
        "o": "b",
        "b": "r",
        "r": "g"
    }
    return next[colour]

def rotate(text: str) -> str:
    rotated = ""
    for colour in text:
        rotated += next_colour(colour)
    return rotated

def check_pll(text: str) -> str:
    for key in pll:
        for _ in range(4):
            if text in pll[key]:
                return key + " perm"
            else:
                text = rotate(text)
    return "not pll"


while True:
    print(check_pll(input("Enter 6 letter string: ").replace(" ", "").lower()))
