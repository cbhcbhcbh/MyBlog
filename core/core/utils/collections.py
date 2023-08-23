def deep_update(base_dict, update_with):
    for key, value in update_with.items():
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)

            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            else:
                base_dict[key] = value
        else:
            base_dict[key] = value

    return base_dict


if __name__ == '__main__':
    base_dict = {'A': {'B': 'B'}, 'C':'C'}
    update_with = {'A': {'B': 'D'}, 'C':'F'}
    new_base_dict = deep_update(base_dict, update_with)
    print(new_base_dict)
