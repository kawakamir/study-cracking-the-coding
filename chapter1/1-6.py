import sys


def compression_by_numbering_continuous(sample):
    sample_len = len(sample)
    past_point = 0
    past_word = None
    compression = ""
    for i, word in enumerate(sample):
        if i == 1:
            compression = word
            past_word = word
        if i + 1 == sample_len:
            compression += str((i + 1 - past_point))
        if past_word != word:
            compression += str((i - past_point)) + word
            past_point = i
            past_word = word

    print(compression) if sample_len > len(compression) else print(sample)


if __name__ == '__main__':
    sample = sys.argv[1]
    compression_by_numbering_continuous(sample)
