from task1.dictionary import phonemes, allophones
import sys


def synthesize(underlying):
    surface = ''

    # Reverse string to compute voiced attribute easier
    underlying = underlying[::-1]

    for i, phoneme in enumerate(underlying):

        # Vowel
        if phoneme == 'a':
            surface += phoneme
            continue

        if phoneme not in phonemes:
            raise ValueError('Wrong input')

        # Rules application
        voiced = phonemes[phoneme]['voiced']
        place = phonemes[phoneme]['place']
        fricative = False

        if i == 0:
            voiced = False

        if i < len(underlying) - 1 and \
                underlying[i + 1] == 'a' and \
                (i == 0 or underlying[i - 1] == 'a'):
            fricative = True

        if len(surface) > 0 and surface[-1] != 'a':
            voiced = allophones[surface[-1]]['voiced']

        # Allophone decision
        next_surface = ''
        for allophone in allophones:
            if allophones[allophone]['voiced'] == voiced and \
                    allophones[allophone]['place'] == place and \
                    allophones[allophone]['fricative'] == fricative:
                next_surface = allophone
                break

        assert next_surface
        surface += next_surface

    # Reverse string back
    return surface[::-1]


if __name__ == "__main__":
    assert len(sys.argv) == 2
    print(synthesize(sys.argv[1]))
