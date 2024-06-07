def single_root_words(root, *words):
    return [word for word in words if word.lower() in root.lower() or root.lower() in word.lower()]


result1 = single_root_words('rich', 'richest', 'orichalcum', 'cheers', 'riches')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
