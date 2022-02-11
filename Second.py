PHONE_REMOVE_CHARACTERS = '()-.'

def remove_extra_characters(text):
    cleaned_text = text
    for char in PHONE_REMOVE_CHARACTERS:
        cleaned_text = cleaned_text.replace(char, '')
    return cleaned_text

def remove_additional_code(text):
    for header_value_pair in text:
        entity = header_value_pair.split(':')
        header = entity[0]
        value = entity[1]
        for v in value:
            v = v.split('x')[0]
        new_pair = header + ':' + value
    return new_pair

with open('calls.txt', 'r') as f:
    calls = f.readlines()

with open('suspects.txt', 'r') as f:
    suspects = f.readlines()

with open('cleared_calls.txt' 'w') as f:
    for call in calls:
        new_call = remove_extra_characters(calls)
        new_call = call.split('|')
        for entity in new_call:
            entity = remove_additional_code(entity)
    f.write(new_call)

with open('cleared_suspects.txt' 'w') as f:
    for suspect in suspects:
    new_suspect = remove_extra_characters(suspect)
    for number in new_suspect:
        number = number.split('x')[0]
    f.write(new_suspectl)







