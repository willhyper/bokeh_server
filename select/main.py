from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure


# initialize
from data_source import get_data
data = get_data()
source = ColumnDataSource(data=dict(date=[], t1=[], t2=[]))
source.data = source.from_df(data[['x', 'y']])


# set up plots
corr = figure(plot_width=350, plot_height=350, tools='box_select,reset')
corr.circle('x', 'y', size=2, source=source, selection_color="orange", alpha=0.6, nonselection_alpha=0.1, selection_alpha=0.4)


def selection_change(attrname, old, new):
    selected = source.selected.indices
    if selected:

        xs = source.data['x'][selected]
        ys = source.data['y'][selected]

        xy = [(x, y) for x, y in zip(xs, ys)]
        print(xy)


source.on_change('selected', selection_change)



layout = column(corr)
curdoc().add_root(layout)
curdoc().title = "Selection"
