import os
import sys


BOOK_PATH = 'C:\\Users\\sarim\\OneDrive\\Рабочий стол\\python\\book_bot\\books\\book.txt'
PAGE_SIZE = 1050


book: dict[int, str] = {}

def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punctuation_marks = ',.!:;?'
    end = start+size
    
    if end >= len(text):
        return text[start:], len(text)
    
    part_text = text[start:end]
    text = text + '  '
    last_symbol_index = 0
    
    for symbol in punctuation_marks:
        last_symbol = part_text.rfind(symbol)
        if last_symbol > last_symbol_index:      
            if text[last_symbol+start+1] not in ',.!:;?':
                last_symbol_index = last_symbol
            else:
                part_text = part_text[:last_symbol] + " " + part_text[last_symbol+1:]
                
                last_symbol = part_text.rfind(symbol)
                
                if last_symbol > last_symbol_index:
                    last_symbol_index = last_symbol
    
    if last_symbol_index <= 0:
        return part_text, len(part_text)
    part_text = text[start:last_symbol_index+start+1]
    
    return part_text, len(part_text)


def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    
    data_length = len(data)
    prepared_book: dict[int, str] = {}
    i = 1
    start = 0
    
    while start < data_length:
        new_data = data[start:]
        text, text_length = _get_part_text(text=new_data, start=0, size=page_size)
        prepared_book[i] = text.strip()
        start += text_length
        i += 1
    
    return prepared_book