'''
Creating a taipy web app.

https://github.com/Avaiga/taipy-course-gui
'''

# +---------+
# | Imports |
# +---------+

from taipy.gui import Gui
import taipy.gui.builder as tgb
import pandas as pd

from taipy_course.chart import generate_map


# +---------+
# | Backend |
# +---------+

data = pd.read_csv('taipy_course/data.csv')
chart_data = (
    data
    .groupby(by='State')['Sales']  # Group sales by state
    .sum()  # Total sales by state
    .sort_values(ascending=False)  # In descending order
    .head(10)  # Top-10 states
    .reset_index()  # Make state names a column instead of index
)

categories = data['Category'].unique().tolist()
selected_category = 'Furniture'

selected_subcategory = 'Bookcases'
subcategories = (
    data.loc[data['Category'] == selected_category, 'Sub-Category']
    .unique()
    .tolist()
)

layout = {
    'yaxis': {'title': 'Revenue (USD)'},
    'title': 'Sales by State'
}

start_date = pd.to_datetime('2015-01-01')
end_date = pd.to_datetime('2018-12-31')

map_fig = generate_map(data)


def change_category(state):
    state.subcategories = (
        data.loc[data['Category'] == state.selected_category, 'Sub-Category']
        .unique()
        .tolist()
    )
    state.selected_subcategory = state.subcategories[0]  # Auto-select a sub-cat


def apply_changes(state):
    # Filter by order dates w/i start & end date
    state.data = data[
        (
            pd.to_datetime(data['Order Date'], format='%d/%m/%Y')
            >= pd.to_datetime(start_date, format='%Y-%m-%d')
        )
        & (
            pd.to_datetime(data['Order Date'], format='%d/%m/%Y')
            <= pd.to_datetime(end_date, format='%Y-%m-%d')
        )
    ]

    # Filter by category
    state.data = data[data['Category'] == state.selected_category]

    # Filter by sub-category
    state.data = (
        state.data[state.data['Sub-Category'] == state.selected_subcategory]
    )

    # Generate state-wise sales chart data from order data
    state.chart_data = (
        state.data.groupby('State')['Sales']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    # Bar chart layout
    state.layout = {
        'yaxis': {'title': 'Revenue (USD)'},
        'title': (f'Sales by State for {state.selected_category} '
                  f'- {state.selected_subcategory}'),
    }

    # Regenerate map based on filtered data
    state.map_fig = generate_map(state.data)


# +------------+
# | Build Page |
# +------------+

with tgb.Page() as page:

    # Apply styling only to elements within 'container' part
    with tgb.part(class_name='container'):
        tgb.text('# Sales by **State**', mode='md')

        with tgb.part(class_name='card'):

            # Distribute elements across width in a 1:2:1 width ratio
            with tgb.layout(columns='1 2 1'):

                # Start & end date selector
                with tgb.part():
                    tgb.text('From **Date**', mode='md')
                    tgb.date('{start_date}')
                    tgb.text('To **Date**', mode='md')
                    tgb.date('{end_date}')

                # Category & sub-category selector
                with tgb.part():
                    tgb.text('Product **Category**', mode='md')
                    tgb.selector(
                        value='{selected_category}',
                        lov=categories,  # Static list to show all categories
                        dropdown=True,  # Dropdown list
                        on_change=change_category
                    )

                    tgb.text('Product **Subcategory**', mode='md')
                    tgb.selector(
                        value='{selected_subcategory}',
                        lov='{subcategories}',  # Dynamic list of sub-cats
                        dropdown=True,  # Dropdown list
                    )

                # Center text in the right-most column
                with tgb.part(class_name='text-center'):
                    tgb.button(
                        'Apply',
                        class_name='plain apply_button',
                        on_action=apply_changes
                    )

                    # tgb.button(
                    #     'Reset',
                    #     class_name='reset button'
                    # )

        tgb.html('br')  # Break for vertical spacing

        # Adjacent chart & map figs
        with tgb.layout(columns='1 1'):

            with tgb.part():
                # Chart of top-10 sales by state
                tgb.chart(
                    data='{chart_data}',
                    x='State',
                    y='Sales',
                    type='bar',
                    layout='{layout}'
                )

            with tgb.part():
                tgb.chart(
                    figure='{map_fig}',
                )

            # Map of sales by state

        tgb.html('br')  # Break for vertical spacing

        # Table of source data by selected category
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
        # dark_mode=False
        port='auto',  # choose any free port
        use_reloader=True  # safe for notebooks
    )