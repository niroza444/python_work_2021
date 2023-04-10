def linear_search(list_env_key,key):
    is_Found = False
    for env in list_env_key:
        if env == key:
            is_Found = True
    return is_Found        
