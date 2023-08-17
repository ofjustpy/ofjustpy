
from Browser import Browser
from datetime import date
import sys
import os
from rpyc.utils.server import ThreadedServer
import rpyc

# os.mkdir(date_str)


url = "http://nytimes.com"

class PageServer(rpyc.Service):
    _server:ThreadedServer
    
    def __init__(self, browser):
        self.browser  = browser

    @staticmethod
    def set_server(inst):
        PageServer._server = inst
        
    def on__connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        print("client connected")
        pass

    def on_disconnect(self, conn):
        print("client disconnected")
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        pass

    def exposed_load_page(self, url, label):
        print ("called load_page with url = ", url, " ", type(url))
        ph = self.browser.get_page(url, 1, label=label)
        page_loaded = ph.__next__()
        page_source = ph.__next__()
        try:
            ph.__next__() #write page_source to file
        except:
            pass
        return page_source

    # def exposed_click_button(def, button_id):
    #     pass

    # def exposed_set_value_element(self, element_id, value):
    #     return self.browser.set_value_element(element_id, value)

    def exposed_element_exists(self, element_id):
        return self.browser.element_exists(element_id)
        pass
    def exposed_set_element_text(self, element_id, text):
        return self.browser.set_element_text(element_id, text)

    
    def exposed_submit_element(self, element_id):
        return self.browser.submit_element(element_id)

    def exposed_is_selected(self, element_id):
        return self.browser.is_selected(element_id)    

    def exposed_get_element_text(self, element_id):
        return self.browser.get_element_text(element_id)

    def exposed_check_if_tag_text_pair_exists(self, tag_name, text):
        print("Called check_if_tag_text_pair_exists")
        return self.browser.check_if_tag_text_pair_exists(tag_name, text)
        #return 
    
    def exposed_get_element_attr_value(self, element_id, attr_label):
        return self.browser.get_element_attr_value(element_id, attr_label)
    
    def exposed_stop(self):
        if self._server:
            self._server.close()
        
        
if __name__ == "__main__":

    with Browser() as _b:
        server_handle = ThreadedServer(PageServer(_b), port=int(sys.argv[1]))
        PageServer.set_server(server_handle)
        server_handle.start()
        print("Shutting down proxy server")
    

        
