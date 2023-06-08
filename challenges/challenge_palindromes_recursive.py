def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    # condição de parada
    if low_index >= high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    # chamada recursiva
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    # raise NotImplementedError
    # ajuda de Joseane Oliveira
