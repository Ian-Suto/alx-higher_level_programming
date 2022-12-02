#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    attribute_list = dir(hidden_4)
    for attribute in attribute_list:
        if attribute[:2] == "__":
            continue
        print("{}".format(attribute))
