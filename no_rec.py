"""
FPS No Recoil by imn0
"""
from time import sleep
from pynput import mouse
from pynput import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key

ptr = Controller()
level = 3
is_running = True


def info():
    print '[i] Running' if is_running else '[i] Idle'
    print '[i] Sensitivity Levels %d\n' % level


def on_press(key):
    global level
    global is_running

    if key == Key.up:
        level += 1
    if key == Key.down:
        level -= 1
    if key == Key.f2:
        is_running = not is_running
    if key == Key.home:
        info()


def on_click(x, y, button, pressed):
    if is_running:
        while pressed:
            sleep(0.5)
            if button == Button.left:
                ptr.move(0, level)


print '###############################'
print '# FPS no Recoil Running v 0.1 #'
print '#         Enjoy Gaming        #'
print '###############################'
print '[Home] for Status'
print '[UP] for Increase'
print '[DOWN] for Decrease'

with keyboard.Listener(on_press=on_press) as k_listener, mouse.Listener(on_click=on_click) as m_listener:
    k_listener.join()
    m_listener.join()
