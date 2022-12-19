import os
import subprocess

def start():
    os.system('cls')

    print("-----------------------------")
    print("starting new project...")
    print("-----------------------------")

    dir = input("name - ")
    parent = input("location - ")

    path = os.path.join(parent, dir)
    templates_path = os.path.join(f"{parent}/{dir}", "templates")
    static_path = os.path.join(f"{parent}/{dir}", "static")
    css_path = os.path.join(f"{parent}/{dir}/static", "css")
    js_path = os.path.join(f"{parent}/{dir}/static", "js")
    os.mkdir(path)
    os.mkdir(templates_path)
    os.mkdir(static_path)
    os.mkdir(css_path)
    os.mkdir(js_path)

    os.system('cls')
    print("-----------------------------")
    print(f"directory {dir} created...")
    print(f"directory templates created...")

    create_flask_app = open(f"{parent}/{dir}/app.py", 'w')
    flask_app_temp = open("templates/flask_app.py", "r")
    flask_app_write = open(f"{parent}/{dir}/app.py", 'a')
    flask_app_write.write(f"{flask_app_temp.read()}")
    flask_app_write.close()

    print("app.py created...")

    create_base_html = open(f"{parent}/{dir}/templates/base.html", 'w')
    base_html_temp = open("templates/base_temp.html", "r")
    base_html_write = open(f"{parent}/{dir}/templates/base.html", 'a')
    base_html_write.write(f"{base_html_temp.read()}")
    base_html_write.close()

    print("base.html created...")

    create_home_html = open(f"{parent}/{dir}/templates/home.html", 'w')
    home_html_temp = open("templates/home_temp.html", "r")
    home_html_write = open(f"{parent}/{dir}/templates/home.html", 'a')
    home_html_write.write(f"{home_html_temp.read()}")
    home_html_write.close()

    print("home.html created...")

    create_home_css = open(f"{parent}/{dir}/static/css/home.css", 'w')
    home_css_temp = open("templates/home.css", "r")
    home_css_write = open(f"{parent}/{dir}/static/css/home.css", 'a')
    home_css_write.write(f"{home_css_temp.read()}")
    home_css_write.close()

    print("home.css created...")

    subprocess.Popen(rf'explorer /select,"{parent}\{dir}\."')
    print("opening directory...")

    input()


function_dict = {'start': start}

if __name__ == "__main__":
    print("-----------------------------")
    print("flask automation by zeqdev")
    print("-----------------------------")

    prefix = '$'

    user = input("cmd - ")

    if prefix in user:
        pass
    else:
        input("command not found...")
        exit()

    try:
        cmd, arg = user.split()
    except:
        cmd = user

    cmd = cmd.replace(prefix, "")

    function_dict[cmd]()