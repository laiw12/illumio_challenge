import re
import urllib.request, json 


class query_url:
    
    def __init__(self):
        
        self.url_stored = {}
        self.pattern = re.compile(r'^(?:http|ftp)s?://' # http:// or https://
                                  r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                                  r'localhost|' #localhost...
                                  r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                                  r'(?::\d+)?' # optional port
                                  r'(?:/?|[/?]\S+)$', re.IGNORECASE)
                                  
   
                                   
    def query_url(self,url,page_num,rows_per_page):
        """A method that can stor URLs in hashmap and return the query result based on page number """
        
        if url not in self.url_stored:
            self.url_stored[url] = 0
            
        start_element = page_num * rows_per_page 
        end_element = page_num * rows_per_page  + rows_per_page 
        request_url =  urllib.request.urlopen(url)
        data = json.loads(request_url.read().decode())
        
        if len(data) <  rows_per_page:
            return data
            
        elif end_element > len(data):
           
            return data[(len(data)- rows_per_page):]
            
        return data[start_element: end_element]
       
        
    
    def enter_url(self):
        """ A method that asks the user to input a valid URL"""
       
        input_url = input("Please enter your valid URL: ")
        number_of_times_tried = 0
        while True:
            if re.match(self.pattern,  input_url):
                print("you entered a valid URL")
                return "Valid"
            else:
                input_url= input("please enter your valid URL: ")
                number_of_times_tried  += 1
            if number_of_times_tried  == 2:
                print("Session Expires, too many invalid inputs")
                return "Session Expire" 
    
    
    

                

        
  




