def initiator_of_discount(data):
    # sanitize the data
    if type(data) == str:
        data_list = data.split()
    elif type(data) == list:
        data_list = data
    else:
        return 0
    
    first_element = data_list[0]

    for i in range(1, len(data_list)):
        # compare current data with first element and previous data
        if data_list[i] < first_element and data_list[i] < data_list[i-1]:
            return i
        
    return 0