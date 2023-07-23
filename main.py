import socket
from typing import Optional
from paramiko.client import SSHClient
import dearpygui.dearpygui as dpg

dpg.create_context()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
SERVER_SESSION: Optional[SSHClient] = None

dpg.create_viewport(title="SSH CONTROLLER", decorated=True)
dpg.set_viewport_small_icon("PATH_TO_ICON")
dpg.set_viewport_large_icon("PATH_TO_ICON")
dpg.configure_viewport(0, x_pos=100, y_pos=100, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
dpg.set_viewport_max_height(WINDOW_HEIGHT)
dpg.set_viewport_max_width(WINDOW_WIDTH)


def open_auth_window():
    dpg.configure_item("main_menu", show=False)
    dpg.configure_item("auth_window", show=True)
    dpg.set_primary_window(auth_panel, value=True)


def open_transfer_file_window():
    dpg.configure_item("main_menu", show=False)
    dpg.configure_item("transfer_window", show=True)
    dpg.set_primary_window(transfer_panel, value=True)


def return_to_main_menu():
    dpg.configure_item("auth_window", show=False)
    dpg.configure_item("transfer_window", show=False)
    dpg.configure_item("main_menu", show=True)
    dpg.set_primary_window(main_menu_window, value=True)


def check_server_files():
    if SERVER_SESSION is None:
        dpg.set_value("files_status", f"STATUS: NO ACTIVE CONNECTION")
    else:
        path = dpg.get_value("folder_path")
        _, stdout, _ = SERVER_SESSION.exec_command(f"ls {path}")
        dpg.set_value("ssh_output", stdout.readlines())


def server_login_from_data():
    global SERVER_SESSION
    username = dpg.get_value("username")
    server_ip = dpg.get_value("server_ip")
    password = dpg.get_value("password")

    try:
        SERVER_SESSION = SSHClient()
        SERVER_SESSION.load_system_host_keys()
        SERVER_SESSION.connect(hostname=server_ip, username=username, password=password)
        return_to_main_menu()
        dpg.set_value("active_connection_label", f"ACTIVE CONNECTION: {'YES' if SERVER_SESSION else 'NO'}")

    except (ValueError, socket.gaierror) as error:
        print(error)


with dpg.window(label="Transfer Panel", show=False, tag="transfer_window") as transfer_panel:
    dpg.add_input_text(width=WINDOW_WIDTH - 15, height=400, show=True, tag="ssh_output", multiline=True)
    dpg.add_spacer(height=10)

    with dpg.group(horizontal=False):
        dpg.add_text(f"STATUS: MISSING", tag="files_status")
        dpg.add_text(f"PATH:")
        dpg.add_input_text(tag="folder_path")

    dpg.add_spacer(height=10)

    with dpg.group(horizontal=True):
        submit_btn = dpg.add_button(label="SUBMIT", callback=check_server_files)
        back = dpg.add_button(label="BACK", callback=return_to_main_menu)

with dpg.window(label="Authorization", show=False, tag="auth_window") as auth_panel:
    username_title = dpg.add_text("SERVER USERNAME")
    username_input = dpg.add_input_text(tag="username", default_value="ROOT", width=WINDOW_WIDTH - 0)

    server_ip_title = dpg.add_text("SERVER IP")
    server_ip_input = dpg.add_input_text(tag="server_ip", width=WINDOW_WIDTH - 30)

    password_title = dpg.add_text("PASSWORD")
    password_input = dpg.add_input_text(password=True, tag="password", default_value="", width=WINDOW_WIDTH - 30)

    dpg.add_spacer(width=100, height=15)
    dpg.add_separator()
    dpg.add_spacer(width=100, height=15)

    with dpg.group(horizontal=True):
        dpg.add_button(label="LOGIN", callback=server_login_from_data)
        dpg.add_button(label="BACK", callback=return_to_main_menu)

with dpg.font_registry():
    default_font = dpg.add_font(file="fonts/custom.ttf", size=20)
    custom_font = dpg.add_font(file="fonts/custom.ttf", size=50)

with dpg.window(label="SSH CONTROLLER", tag="main_menu", show=True) as main_menu_window:
    with dpg.group(horizontal=True):
        title = dpg.add_text(
            default_value="SSH CONTROLLER",
            pos=[WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 - 100]
        )
        dpg.bind_item_font(title, custom_font)

    with dpg.group(horizontal=True):
        dpg.add_text(
            f"ACTIVE CONNECTION: {'YES' if SERVER_SESSION else 'NO'}",
            pos=[WINDOW_WIDTH // 2 - 120, WINDOW_HEIGHT // 2 - 30],
            tag="active_connection_label"
        )

    with dpg.group(horizontal=True, pos=[WINDOW_WIDTH // 2 - 170, WINDOW_HEIGHT // 2 + 18]):
        file_btn = dpg.add_button(label="TRANSFER FILE", callback=open_transfer_file_window)
        connect_btn = dpg.add_button(label="CONNECT TO THE SERVER", callback=open_auth_window)

dpg.set_primary_window(window=main_menu_window, value=True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
