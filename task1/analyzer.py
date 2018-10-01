from task1.dictionary import phonemes, allophones
import sys


def analyze(surface):
    variants = ['']

    # Reverse string to compute voiced attribute easier
    surface = surface[::-1]

    for i, allophone in enumerate(surface):

        # Vowel
        if allophone == 'a':
            for j, variant in enumerate(variants):
                variants[j] += allophone
            continue

        if allophone not in allophones:
            raise ValueError('Wrong input')

        # Rules application
        voiced = allophones[allophone]['voiced']
        place = allophones[allophone]['place']

        if i == 0 or surface[i - 1] != 'a':
            voiced = None

        # Phoneme decision
        if voiced is not None:
            for j, variant in enumerate(variants):
                for phoneme in phonemes:
                    if phonemes[phoneme]['place'] == place and phonemes[phoneme]['voiced'] == voiced:
                        variants[j] += phoneme
            continue

        variants_copy = variants[:]
        for j, variant in enumerate(variants):
            for phoneme in phonemes:
                if phonemes[phoneme]['place'] == place:
                    if phonemes[phoneme]['voiced']:
                        variants[j] += phoneme
                    else:
                        variants_copy[j] += phoneme

        variants.extend(variants_copy)

    return [variant[::-1] for variant in variants]


if __name__ == "__main__":
    assert len(sys.argv) == 2
    for variant in analyze(sys.argv[1]):
        print(variant)
