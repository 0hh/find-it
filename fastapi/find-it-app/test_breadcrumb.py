class Item:
    def __init__(self, item_id, item_name, parent_id):
        self.item_id = item_id
        self.item_name = item_name
        self.parent_id = parent_id

ITEMS = [
    Item(1, "Abstellkammer", None),
    Item(2, "Oberstes Regal", 1),
    Item(3, "Klebeband", 2),
    Item(4, "Werkzeugkasten", 2),
    Item(5, "Hammer", 4),
    Item(6, "Zange", 4),
]

def find_item_by_id(id):
    """Find and return the item object from the list using its id."""
    for item in ITEMS:
        if item.id == id:
            return item
    return None

def get_bread_path_to_root_element(id):
    """Returns a list of the parent element, it's parent, it's parent's parent etc. until it finds the root element where parent is `None`."""
    breadcrumb = []
    current_item = find_item_by_id(id)
    
    while current_item:
        breadcrumb.append(current_item.item_name)
        if current_item.parent_id is None:
            break
        current_item = find_item_by_id(current_item.parent_id)
    
    return breadcrumb[::-1]

# Example usage
print(get_bread_path_to_root_element(6))
# Expected output: ['Abstellkammer', 'Oberstes Regal', 'Werkzeugkasten', 'Zange']
