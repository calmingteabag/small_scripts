def json_extractor(json_obj, dict_key):
    '''
    NOT MY IDEA, but this script can possibly save my life in the future
    I'm gonna try to explain it

    What it does is, given a dict key, iterate over NESTED dictionaries and return
    all values from key.
    '''

    value_list = []

    # extraction function
    def json_iterator(json_obj, value_list, dict_key):

        if isinstance(json_obj, dict):
            '''
            If the object IS a dictionary, start iterating...
            '''
            for key, value in json_obj.items():

                if isinstance(value, (dict, list)):
                    json_iterator(value, value_list, dict_key)
                    '''
                    IF the iterator sees either a dict or a list, put it as an argument and
                    call the function again to start iterating over the nested dict or list
                    '''
                elif key == dict_key:
                    value_list.append(value)
                    '''
                    If the iterator doesnt see a dict or a list, it means that it's a dict
                    entry. Then it just checks if the key matches the key you are looking
                    for and adds into the list.
                    '''
# new stuff
        elif isinstance(json_obj, list):
            '''
            Now this is interesting
            What usually happens in nested dicts, is having a list containing a dict inside it. So
            it goes through the same procedure as above (function call with iterator as values) because
            we need to extract the dictionaries from the list
            '''

            for item in json_obj:
                extract(item, value_list, dict_key)

        return value_list

    # extraction function call
    values = json_iterator(json_obj, value_list, dict_key)
    return values
