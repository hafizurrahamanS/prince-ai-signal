import random
import datetime

def generate_signal():
    score = random.randint(0, 5)
    now = datetime.datetime.now().strftime("%I:%M %p")

    if score >= 4:
        return {'type': 'BUY', 'color': 'green', 'label': '✅ Confirmed BUY', 'time': now}
    elif 2 <= score < 4:
        return {'type': 'BUY', 'color': 'purple', 'label': '♻️ Martingale OK', 'time': now}
    else:
        return {'type': 'BUY', 'color': 'gray', 'label': '🚫 Avoid Signal', 'time': now}
