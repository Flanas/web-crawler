import re

def count_words(title):
    # Remove symbols and count words
    return len(re.findall(r'\b\w+\b', title))

def filter_more_than_five_words(entries):
    filtered = [entry for entry in entries if count_words(entry['title']) > 5]
    return sorted(filtered, key=lambda x: x['comments'], reverse=True)

def filter_five_words_or_less(entries):
    filtered = [entry for entry in entries if count_words(entry['title']) <= 5]
    return sorted(filtered, key=lambda x: x['points'], reverse=True)
