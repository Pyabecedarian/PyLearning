# The module is designed for the main logic process
import sys
import functions as f

id_list = []

# load id from file
f.load_info(id_list)

# main program circulation
while True:
    # Main page
    f.main_page()

    usr_cmd = input("请选择执行的操作: ")
    print("\n您选择的功能: " + usr_cmd)

    if usr_cmd == '1':
        # 1> Add Id
        f.add_id(id_list)

    elif usr_cmd == '2':
        # 2> Show details
        f.show_all(id_list)

    elif usr_cmd == '3':
        # 3> Search info
        f.search_info(id_list)

    elif usr_cmd == '0':
        # 4> quit
        print("欢迎再次使用[名片管理系统]")
        sys.exit()

    else:
        print("\n输入有误, 请重新输入!")
