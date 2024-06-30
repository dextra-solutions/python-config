import ast


def try_convert_string(string):
    try:
        if string == 'true':
            return True
        elif string == 'false':
            return False
        else:
            return ast.literal_eval(string)
    except Exception as e:
        return string
