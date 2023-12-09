#write functions here, don't add input('') statements here!
def get_most_likely_ancestor_consensus(string1, string2):
    index_value = []
    for i in range(len(string1) - len(string2) + 1):
        if string1[i:i+len(string2)] == string2:
            index_value.append(i + 1)

    return tuple(index_value)

def validate_string_length(string1):
    if len(string1) < 8 or len(string1) > 16:
        return 'Invalid'

def validate_substring_length(string2):
    if len(string2) != 4:
        return 'Invalid'

