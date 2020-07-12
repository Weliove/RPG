def set_stored_items(list_widget, stored_items, total_list):
    for item in stored_items:
        if item in stored_items:
            item_index = total_list.index(item)
            list_widget.select_set(item_index)
