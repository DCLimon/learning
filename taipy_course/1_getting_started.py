"""
Creating a taipy web app.

https://github.com/Avaiga/taipy-course-gui
"""

# +---------+
# | Imports |
# +---------+

from taipy.gui import Gui
import taipy.gui.builder as tgb
from math import cos, exp


# +------------+
# | Build Page |
# +------------+

value = 10


# Cosine decay function
def compute_data(decay: int) -> list:
    return [cos(i/6) * exp((-i*decay) / 600) for i in range(100)]


# Define update fxn for when GUI slider is moved
def slider_moved(state):
    state.data = compute_data(state.value)


# Define page elements for GUI
with tgb.Page() as page:
    tgb.text(value='# Taipy Getting Started', mode='md')
    tgb.text(value='**Value:** {value}', mode='md')
    tgb.slider(value='{value}', on_change=slider_moved)
    tgb.chart(data='{data}')

data = compute_data(value)


# +------+
# | Main |
# +------+

def main():
    pass


if __name__ == '__main__':
    # Will not work if encapsulated in main()
    Gui(page=page).run(
        title="Cosine damping demo",
        port='auto',  # choose any free port
        use_reloader=False  # safe for notebooks
    )
