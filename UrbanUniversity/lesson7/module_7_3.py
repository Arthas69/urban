import re


class WordsFinder(object):
    def __init__(self, *file_names):
        self.file_names = file_names
        self.words = {}

    def get_all_words(self):
        if not self.words:
            all_words = []
            for file_name in self.file_names:
                with open(file_name, 'r', encoding='utf-8') as file:
                    for line in file:
                        all_words.extend(
                            [x for x in re.sub(
                                r'[,.=!?;:]',
                                '',
                                line.replace(' - ', ' ')
                            ).lower().split()])
                    self.words[file_name] = all_words
        return self.words

    def find(self, word):
        result = {}
        for file, words in self.get_all_words().items():
            if (wl := word.lower()) in words:
                result[file] = words.index(wl) + 1
        return result

    def count(self, word):
        result = {}
        for file, words in self.get_all_words().items():
            if (wl := word.lower()) in words:
                result[file] = words.count(wl)
        return result


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
