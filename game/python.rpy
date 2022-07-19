init python:   
    showitems = True
   
    def display_items_overlay():
        if showitems:
            inventory_show = "Inventory: "
            for i in range(0, len(inventory)):
                item_name = inventory[i].title()
                if i > 0:
                    inventory_show += ", "
                inventory_show += item_name
            ui.frame()
            ui.text(inventory_show)
    config.overlay_functions.append(display_items_overlay)

    def keyCheck():
        if("Master Key" in inventory):
            return True
        return False