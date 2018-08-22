def select_from_menu(menu_options: dict,):
    selection = input('Make selection: ')
    action = menu_options.get(int(selection), None)
    if action is None:
        print('Invalid selectin')
    else:
        print('')
        action()
        print('')

