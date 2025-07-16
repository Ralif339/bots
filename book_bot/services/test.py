def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punctuation_marks = ',.!:;?'
    end = start+size
    
    if end >= len(text):
        return text, len(text)
    
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

text = 'Раз. Окей паренек, сходим куда нибудь!?'

print(_get_part_text(text, 5, 9), sep=',')