# Illumio QA Back-end Coding Challenge

### Code Design and Implementation 

I chose Python 3 as a development environment. I created a class called url_implementation and created two methods: query_url and enter_url. When you initialize the class, the constructer will construct a dictionarary(hashmap) to store the the urls.

query_url: a method takes a string of url, page number, number_of_rows and output the json list with the correct page number with the number of rows in it. The reason to do this is that I find out that the given dummy website returns the whole json files which is large. In this way,we can only output small portion of it. However, this is not the perfect way to solve this problem. The website itself can divided its output into pages by providing the options for us to choose pages when we generating the urls. I also save the entered url in a dictionary in this step due to the fact that we can check for duplicates using the dictionary in O(1). 

enter_url: I adapt the pattern matching provded in the instruction and used it to validate if the input Url is correct. If the user input an invalid url, the user will have to more chances to enter it correctly. Otherwise, the session will expire. 

### Test Process
I created a test automation script. The script can perform user input by using the url.txt file provided. Basically, the test script checks for all functions such as url storage, page_num and user input for valid urls.
To run the page test script, input the following command in the command window:
#### python test_url.py < url.txt ####
The test cases focus on corner cases such as first page/ last page of the data, valid/invalid Urls in different sequences. The correct outcome of is based on the logic of the code. 

### Future Improvements 
1. Currently, the data structure of storing the Urls is not perfect. I think it depends on the purpose of the usage of the Urls. If we want to have fast look up, dictionary is ideal. However, if we want to find the most recent searched Url, a LRU (least recently used cache) is an optimal datastructure since it can keep track of the most recent entered Url.
2. Due to time limitation, the code of test automation is not reusable. It is better to construct a class to handle this type of jobs If we have more clear objectives of the code. 

