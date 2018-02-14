from mozscape import Mozscape
from datetime import datetime
import time
import bokeh_code as bc
import optimization as ozt

moz_client = Mozscape('', '')

""" Stream Functions """

# create writes
# create a function which only handles writes
# it should only write to the database for that specific url
# or the variables to be loaded onto the plot for most recent
# could these writes go into an array? .push()?


def call_and_assign_data(url):
    try:
        time.sleep(1)
        print("sleeping..zzz.")
        external_root_domain_links = ozt.return_external_root_domain_links(url)
        return external_root_domain_links
        # return total root domain links
    except Exception as e:
        print("Error Occured during call_and_assign_data")
        print(e)

# replace all functions beneath, with a single function taking the address of the ColumnDataSources being written to
def stream_client(timestamp, links):
    try:
        new_client_data = dict(time=[timestamp], ext_root_dom_links=[links])
        bc.client_erdl.stream(new_client_data, rollover=10)
    except Exception as e:
        print(e)
        print("There was an error with client writes")
        new_client_data = dict(time=[timestamp], ext_root_dom_links=[0])
        bc.client_erdl.stream(new_client_data, rollover=10)


def stream_first_competitor(timestamp, links):
    try:
        new_first_data = dict(time=[timestamp], ext_root_dom_links=[links])
        bc.c1_erdl.stream(new_first_data, rollover=10)
    except Exception as e:
        print(e)
        print("There was an error with first writes")
        new_first_data = dict(time=[timestamp], ext_root_dom_links=[0])
        bc.c1_erdl.stream(new_first_data, rollover=10)


def stream_second_competitor(timestamp, links):
    try:
        new_second_data = dict(time=[timestamp], ext_root_dom_links=[links])
        bc.c2_erdl.stream(new_second_data, rollover=10)
    except Exception as e:
        print(e)
        print("There was an error with second writes")
        new_second_data = dict(time=[timestamp], ext_root_dom_links=[0])
        bc.c2_erdl.stream(new_second_data, rollover=10)


#    bc.d_one.stream(new_client_data, rollover=10)
#    bc.d_two.stream(new_first_data, rollover=10)
#    bc.d_thr.stream(new_second_data, rollover=10)
#    print(bc.d_one.data)
#    print(bc.d_two.data)
#    print(bc.d_thr.data)
