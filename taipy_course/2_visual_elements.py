"""
Creating a taipy web app.

https://github.com/Avaiga/taipy-course-gui
"""

# +---------+
# | Imports |
# +---------+

from taipy.gui import Gui
import taipy.gui.builder as tgb
import pandas as pd


# +------------+
# | Build Page |
# +------------+

# data = pl.read_csv('taipy_course/data.csv')
# chart_data = (
#     data
#     .group_by('State')
#     .agg(pl.col('Sales').sum())
#     .sort(by='Sales', descending=True)
# )

# categories = data.select(pl.col('Category').unique())
# selected_category = 'Furniture'
#
#
# def change_category(state):
#     state.data = data.filter(pl.col('Category') == 'Furniture')
#     state.chart_data = (
#         data.filter(pl.col('Category') == state.selected_category)
#     )
#     state.layout = {
#         'yaxis': {'title': 'Revenue (USD)'},
#         'title': f'Sales by State for {state.selected_category}',
#     }

data = pd.read_csv('taipy_course/data.csv')
chart_data = (
    data
    .groupby(by='State')['Sales']  # Group sales by state
    .sum()  # Total sales by state
    .sort_values(ascending=False)  # In descending order
    .head(10)  # Top-10 states
    .reset_index()  # Make state names a column instead of index
)

categories = list(data['Category'].unique())
selected_category = 'Furniture'

layout = {
    'yaxis': {'title': 'Revenue (USD)'},
    'title': 'Sales by State'
}


def change_category(state):
    state.data = data[data['Category'] == state.selected_category]
    state.chart_data = (
        state.data.groupby('State')['Sales']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    state.layout = {
        'yaxis': {'title': 'Revenue (USD)'},
        'title': f'Sales by State for {state.selected_category}',
    }


with tgb.Page() as page:
    tgb.selector(
        value='{selected_category}',
        lov=categories,
        on_change=change_category
    )
    tgb.chart(
        data='{chart_data}',
        x='State',
        y='Sales',
        type='bar',
        layout='{layout}'
    )
    tgb.html('br')
    tgb.table(data='{data}')

# +------+
# | Main |
# +------+

def main():
    pass


if __name__ == '__main__':
    # Will not work if encapsulated in main()
    Gui(page=page).run(
        title='Sales',
        dark_mode=False
    )