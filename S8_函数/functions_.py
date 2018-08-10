def describe_pet(animal_type, pet_name):
    """显示宠物信息
    S8_02
    """

    print("\nI have a " + animal_type.title() + '.')
    print("My " + animal_type.title() + "'s name is " +
          pet_name.title())


def get_formatted_name(first_name, last_name, middle_name=""):
    """返回整洁的姓名
    :rtype: object
    """

    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()


def make_pizza(size, *toppings):
    """
    打印顾客店的所有配料
    :param toppings: 配料
    """

    print("\nMaking a " + str(size) + "-inch pizza with the "
                                      "following toppings:")
    for topping in toppings:
        print("- " + topping)
