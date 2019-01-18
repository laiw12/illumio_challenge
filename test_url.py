#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:19:54 2019

@author: csking
"""
from url_implementation  import url_implementation 
import urllib.request, json 


if __name__ == "__main__":
    
    obj = url_implementation()  
    test_url = "http://dummy.restapiexample.com/api/v1/employees"
    print("-------------testing url storage -----------------------------------------")
    response = obj.query_url("http://dummy.restapiexample.com/api/v1/employees",0,5)
    if test_url in obj.url_stored:
        print("url stored succeccfull")
    print("------------testing if page number is correct -----------------------------")
    request_url =  urllib.request.urlopen(test_url)
    data = json.loads(request_url.read().decode())
   
    if response == data[0:5]:
        print("case1: 0 page passed")
    else:
        print("case1: 0 page not pass")
    response = obj.query_url("http://dummy.restapiexample.com/api/v1/employees",10000,1000)
    if response == data[(len(data)-1000):]:
        print("case2: last page passed")
    else:
        print("case2: last page not pass")
    response = obj.query_url("http://dummy.restapiexample.com/api/v1/employees",5,10)
    if response == data[50:60]:
        print("case3: page in the middle passed")
    else:
        print("case3: page in the middle not pass")
    
    print("------------testing if enter url is correct -----------------------------")
    output = obj.enter_url()
    if output == "Valid":
        print("case1: Enter Correct URL PASSED")
    else: 
        print("case1: Enter Correct URL Not PASSED")
    output = obj.enter_url()
    if output == "Session Expire":
        print("case2: Enter Incorrect URL Passed")
    else:
        print("case2: Enter Incorrect URL Not Passed")
    
    print("--------------performing a sequence of 4 additional test cases -----------")
    output1 =  obj.enter_url()
    output2 =  obj.enter_url()
    output3 =  obj.enter_url()
    output4 =  obj.enter_url()
    if [output1,output2,output3,output4] == ["Valid","Valid","Valid","Session Expire"]:
        print("All Test Casess Passed")
    else:
        print("For additional case not passed")
        
    
 
    
        
    
    
    
    
    
    