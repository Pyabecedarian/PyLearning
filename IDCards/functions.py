# The module designated for specific design of functions imported
# in the main module

file_name = 'id_cards.json'


def load_info(id_list):
    """load ID stored in file"""

    try:
        with open(file_name) as f_obj:
            lines = f_obj.readlines()

    except FileNotFoundError:
        fp = open(file_name, 'w')
        fp.close()

    else:
        num = int(len(lines) / 4)
        while num > 0:
            sub_list = []
            current_id_dict = {}
            i = 0
            while i < 4:
                sub_lines = lines.pop()
                sub_list.append(sub_lines)
                i += 1

            for key_value_str in sub_list:
                [key, value] = key_value_str.split()
                current_id_dict[key] = value
            id_list.append(current_id_dict)
            del current_id_dict
            num -= 1


def write_info(name, phone, qq, email):
    """write id to file"""

    with open(file_name, 'a') as f_obj:
        f_obj.write('name %s\n' % name)
        f_obj.write('phone %s\n' % phone)
        f_obj.write('qq %s\n' % qq)
        f_obj.write('email %s\n' % email)


def main_page():
    """Show menu page"""
    print()
    print("*" * 50)
    print("欢迎使用[名片管理系统] V1.0\n")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片\n")
    print("0. 退出系统")
    print("*" * 50)
    print()


def add_id(id_list):
    """Add id to dictionary"""
    current_id_dict = {}

    print("功能: 新建名片")
    name = input("请输入姓名: ")
    phone = input("请输入电话: ")
    qq = input("请输入QQ号码: ")
    email = input("请输入邮箱: ")

    # write ID to file
    write_info(name, phone, qq, email)

    # Store ID in dictionary
    current_id_dict['name'] = name
    current_id_dict['phone'] = phone
    current_id_dict['qq'] = qq
    current_id_dict['email'] = email
    id_list.append(current_id_dict)
    print("添加 " + name + " 的名片成功")


def header():
    """print header"""

    print("\n姓名\t\t\t\t电话\t\t\t\tQQ\t\t\t\t邮箱")
    print("=" * 66)


def show_all(id_list):
    """Show details"""

    if id_list:
        # 打印表头
        header()
        # 打印列表
        for id_dict in id_list:
            show_info(id_dict)
        print("-" * 66)
    else:
        print("提示: 没有任何名片记录")


def edit_id(find_name, id_dict, id_list):
    """Edit info"""

    name = input("请输入姓名 (回车不修改此项): ")
    phone = input("请输入电话 (回车不修改此项): ")
    qq = input("请输入QQ (回车不修改此项): ")
    email = input("请输入邮箱 (回车不修改此项): ")

    if name:
        id_dict['name'] = name
    if phone:
        id_dict['phone'] = phone
    if qq:
        id_dict['qq'] = qq
    if email:
        id_dict['email'] = email

    print(find_name + " 的名片修改成功.")
    # Refresh file list
    refresh_file(id_list)

    header()
    show_info(id_dict)
    print('-' * 66)


def delete_id(find_name, id_dict, id_list):
    """delete info"""

    id_list.remove(id_dict)
    print(find_name + " 已从名片中删除!")
    # Refresh file list
    refresh_file(id_list)


def search_info(id_list):
    """find specific info"""

    print("功能: 查询名片")
    find_name = input("请输入查询的姓名: ")

    for id_dict in id_list:
        # 如果找到
        if find_name == id_dict['name']:
            while True:
                header()
                show_info(id_dict)
                print("-" * 66)

                msg = "请输入对名片的操作: 1.修改 / 2.删除 / 0.返回上一级"
                usr_cmd = input(msg)
                if usr_cmd == '1':
                    # Edit ID info
                    edit_id(find_name, id_dict, id_list)
                    break
                elif usr_cmd == '2':
                    # Delete ID info
                    delete_id(find_name, id_dict, id_list)
                    break
                elif usr_cmd == '0':
                    return
                else:
                    print("输入错误. 请重新输入")

            break
    # 没有找到
    else:
        print("没有找到 " + find_name)


def refresh_file(id_list):
    """Refresh file info"""

    with open(file_name, 'w') as f_obj:
        for id_dict in id_list:
            if id_dict:
                f_obj.write('name %s\n' % id_dict['name'])
                f_obj.write('phone %s\n' % id_dict['phone'])
                f_obj.write('qq %s\n' % id_dict['qq'])
                f_obj.write('email %s\n' % id_dict['email'])


def show_info(id_dict):
    """显示一个ID"""

    print(id_dict['name'] + '\t\t\t', end='')
    print(id_dict['phone'] + '\t\t\t\t', end='')
    print(id_dict['qq'] + '\t\t\t\t', end='')
    print(id_dict['email'])
