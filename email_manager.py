"""
Module for sending emails.
"""

import time
from dataclasses import dataclass
import pyautogui

from templates import NormalInvite

@dataclass
class EmailPositions:
    """
    XY positions of important locations of buttons and apps.
    """

    outlook_app: tuple = (330, 980)
    new_email: tuple = (200, 110)
    to: tuple = (690, 210)
    subject: tuple = (690, 255)
    body: tuple = (690, 400)
    send: tuple = (630, 115)


outlook_positions = EmailPositions()

@dataclass
class Email:
    """
    Message details of the email that needs to be sent.
    """
    to: str
    subject: str
    body: str

def move_and_click(x: int, y: int, delay: float = 1) -> None:
    """
    Move the mouse to (x, y) and click.
    Args:
        x (int): X-coordinate on the screen.
        y (int): Y-coordinate on the screen.
        delay (float): Delay before and after clicking (default 0.5 seconds).
    """
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(delay)
    pyautogui.click()
    pyautogui.click()
    time.sleep(delay)


def start_outlook() -> None:
    """
    Clicks on the outlook app
    """
    move_and_click(*outlook_positions.outlook_app, delay=2)

def send_email(email: Email) -> None:
    """
    Takes the email and sends it.
    """
    start_outlook()
    move_and_click(*outlook_positions.new_email)
    pyautogui.write(email.to)
    move_and_click(*outlook_positions.subject)
    pyautogui.write(email.subject)
    move_and_click(*outlook_positions.body)
    pyautogui.write(email.body)
    move_and_click(*outlook_positions.send)

if __name__ == '__main__':
    speaker = 'shithead'
    co_organizer = 'sweet_fuckall'
    my_name = 'myself'

    body = NormalInvite(speaker, my_name, co_organizer)
    test_email = Email('trystanscottlambert@gmail.com', 'Invite for Seminar', body.message)

    send_email(test_email)