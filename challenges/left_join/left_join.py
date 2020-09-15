def left_join(table1, table2):
    output = []
    for item in table1:
        try:
            table2_item = table2.get(item[0][0])
            new_entry = [item[0][0], item[0][1], table2_item]
            output.append(new_entry)
        except TypeError:
            if item:
                output.append(item)
    return output
