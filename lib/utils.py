def print_items(items):
    for item in items:
        print(f'\t\t{item}')


def print_result(items, context):
    print(
        '\n\t',
        f'---------   Creating your {context}  ---------'
    )
    print_items(items)
    print(f'\t -----------   {context} Created!   -----------\n')


def validate_is_number(how_many=None, attempt=0):
    if how_many is None:
        how_many = input('How Many? ')
    try:
        return int(how_many)
    except ValueError:
        print("input must be a number")
        if attempt > 1:
            print("too many attempts!")
        else:
            validate_is_number(how_many=None, attempt=attempt + 1)
