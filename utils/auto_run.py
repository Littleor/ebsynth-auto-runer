import os

import pyautogui
from pyautogui import Point


def launch_ebsynth_with_file(file_path: str, software_path=None) -> bool:
    """
    launch ebsynth with file
    :param file_path:
    :param software_path:
    :return:
    """
    # TODO Need support for windows
    if os.path.exists(file_path):
        os.system(f"open -a {software_path if software_path is not None else 'EbSynth'} {file_path}")

        # subprocess.Popen(["/usr/bin/open", "-a", software_path if software_path is not None else "EbSynth", file_path])
        return True
    return False


def get_scaling_factor() -> float:
    actual_size = pyautogui.size()
    screen_size = pyautogui.screenshot().size
    scaling_factor = screen_size[0] / actual_size[0]
    return scaling_factor


def find_all_location(image_path: str, scaling_factor=1, **kwargs) -> [Point]:
    """
    find all location
    :param image_path:
    :return:
    """
    try:
        boxes = pyautogui.locateAllOnScreen(image_path, **kwargs)
        locations = []
        for box in boxes:
            location = pyautogui.center(box)
            actual_location = pyautogui.Point(x=location.x / scaling_factor, y=location.y / scaling_factor)
            locations.append(actual_location)
    except Exception as e:
        locations = []
    return locations


def find_location(image_path, scaling_factor=1, **kwargs) -> Point:
    try:
        location = pyautogui.locateCenterOnScreen(image_path, **kwargs)
        actual_location = pyautogui.Point(x=location.x / scaling_factor, y=location.y / scaling_factor)
    except Exception as e:
        print("Find location error:", e)
        actual_location = None
    return actual_location


def find_and_click(image_path: str, scaling_factor=1, **kwargs) -> bool:
    location = find_location(image_path, scaling_factor=scaling_factor, **kwargs)
    if location is not None:
        pyautogui.click(location)
        return True
    else:
        print(f"Image {image_path} not found on screen.")
        return False
