def convert_to_abnt(name):
    LAST_NAMES = ['FILHO', 'FILHA', 'NETO', 'NETA', 'SOBRINHO', 'SOBRINHA', 'JUNIOR']
    ARTICLES = ['do', 'da', 'dos', 'das', 'dos']

    splited_name_capitalized = [x.capitalize() for x in name.split(' ') if x not in ARTICLES]
    if splited_name_capitalized and len(splited_name_capitalized) == 1:
        return splited_name_capitalized[0].upper()
    
    last_name = splited_name_capitalized.pop().upper()
    if last_name in LAST_NAMES:
        return last_name + ' ' + splited_name_capitalized.pop().upper() + ', ' + ' '.join(splited_name_capitalized)
    
    names = ' '.join(splited_name_capitalized)
    converted_name = last_name + ', ' + names
    
    return converted_name
