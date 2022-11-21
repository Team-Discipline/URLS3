from S3.models import Word, CombinedWord


def __check_duplicated_combined_words(word1: str, word2: str) -> bool:
    """
    If combinations of words are exists,
    return `True`
    else
    return `False`

    `False` mean 'it is unique'
    """
    words = CombinedWord.objects.filter(first_word__word__iexact=word1, second_word__word__iexact=word2)
    if words.count() > 0:
        return True
    else:
        return False


def get_combined_words(word1: str | None = None, word2: str | None = None) -> CombinedWord:
    while True:
        w1, w2 = Word(), Word()  # Create empty queryset
        if word1 is None:
            w1 = Word.objects.filter(is_noun=False).order_by('?')[0]
            word1 = w1.word
        if word2 is None:
            w2 = Word.objects.filter(is_noun=True).order_by('?')[0]
            word2 = w2.word

        if not __check_duplicated_combined_words(word1, word2):
            break

    return CombinedWord.objects.create(first_word=w1, second_word=w2)
