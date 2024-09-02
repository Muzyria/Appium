




import subprocess
import time

def long_press_key(keycode: int, duration: int = 5) -> None:
    for i in range(100):

        subprocess.run(['adb', 'shell', 'input', 'keyevent', str(keycode)])
        # Задержка для длительного нажатия


# Пример использования
long_press_key(3)  # KEYCODE_HOME


