# enables writing to the document
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.models.widgets import Button, TextInput
from bokeh.layouts import layout
from datetime import datetime
# import test.py
import test as ts
# NOTE: database still needs to be configured into this prototype to make subtle api calls to prevent throttle


# assign hover to an assignment of an attribute of
# popup to a HoverTool function
p1_hover = HoverTool(tooltips="""
    <div>
        <div>

        <div>
            <span style="font-size: 12px; color: #696;">Time Stamp: @time</span><br>
            <span style="font-size: 12px; color: #696;">Amount of External Root Domain Links: @ext_root_dom_links</span><br>
        </div>
    </div>
""")

# create Tools object to assign to tools attribute into the fiture
# figure object
first_plot_tools = [p1_hover]
# figure declarations
f = figure(x_axis_type='datetime', tools=first_plot_tools)
# format our xaxis
"""Bokeh Code For All Data -- removing c_blocks_linked"""
# client root domain links
client_erdl = ColumnDataSource(data=dict(time=[], ext_root_dom_links=[]))
# first root domain links
c1_erdl = ColumnDataSource(data=dict(time=[], ext_root_dom_links=[]))
# second root domain links
c2_erdl = ColumnDataSource(data=dict(time=[], ext_root_dom_links=[]))


"""Bokeh Code For Figure 'f'"""
# plot for external root domain links
# client
f.line(x='time', y='ext_root_dom_links', line_color='red', line_width=2, source=client_erdl)
f.circle(x='time', y='ext_root_dom_links', line_color='red', line_alpha=.5, fill_color=None, line_width=4, source=client_erdl)
# first competitor
f.line(x='time', y='ext_root_dom_links', line_color='green', line_width=2, source=c1_erdl)
f.circle(x='time', y='ext_root_dom_links', line_color='green', line_alpha=.5, fill_color=None, line_width=4, source=c1_erdl)
# second competitor
f.line(x='time', y='ext_root_dom_links', line_color='blue', line_width=2, source=c2_erdl)
f.circle(x='time', y='ext_root_dom_links', line_color='blue', line_alpha=.5, fill_color=None, line_width=4, source=c2_erdl)
"""Bokeh Code For Figure 'f_c_blocks'"""


def stream_new_data_from_api():
    call_timestamp = datetime.now()

    client_links = ts.call_and_assign_data(cli_addr.value)
    new_client_data = dict(time=[call_timestamp], ext_root_dom_links=[client_links])

    first_c_links = ts.call_and_assign_data(comp_one_addr.value)
    new_first_data = dict(time=[call_timestamp], ext_root_dom_links=[first_c_links])

    second_c_links = ts.call_and_assign_data(comp_two_addr.value)
    new_second_data = dict(time=[call_timestamp], ext_root_dom_links=[second_c_links])
    try:
        # stream data to ColumnDataSources
        client_erdl.stream(new_client_data, rollover=10)
        c1_erdl.stream(new_first_data, rollover=10)
        c2_erdl.stream(new_second_data, rollover=10)
    except Exception as e:
        print(e)
        print("Writing to ColumnDataSources was throttled -- error is in stream_new_data_from_api() function")

    # on_click() - we then go through 'test' object - we execute the api function with the url's entered into the TextInput widgets


cli_addr = TextInput(title="Client Full Url")
comp_one_addr = TextInput(title="First Competitor Full Url")
comp_two_addr = TextInput(title="Second Competitor Full Url")


button = Button(label="Call Data")
button.on_click(stream_new_data_from_api)
# format our ticker for x_axis

lay_out_variable = layout([[f], [button, cli_addr, comp_one_addr, comp_two_addr]])
curdoc().add_root(lay_out_variable)
