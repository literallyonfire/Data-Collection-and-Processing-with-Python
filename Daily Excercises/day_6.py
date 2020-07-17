#1. requests-6-2: If resp is a Response object returned by a call to requests.get(), which of the following is a way to extract the contents into a python dictionary or list?

# A. resp.json() and json.loads(resp.text)

#2. requests-7-1: Why is it important to use a function like make_cache_key in this caching pattern rather than just uring the full url as the key?

# A. Because when requests.get encodes URL parameters, the keys in the params dictionary might be in any order, which would make it hard to compare one URL to another later on, and you could cache the same request multiple times.

#3. requests-8-1: Why would you define a function in order to make a request to a REST API for data?

#A. Because that means you have to write less repeated code if you want to make a request to the same API more than once in the same program.
#B. Because writing functions to complete a complex process in your code makes it easier to read and easier to fix later.
#C. Because a lot of things stay the same among different requests to the same API.

#4. requests-8-3: In the runestone environment, if there is a runtime error and you don’t get a Response object back from the call to requests.get(), what should you do?

#B. look at the values you passed in to requests.get()

#5. requests-11-1: If you wanted to search for photos tagged with either river or mountains (using flickr api), rather than requiring both, what would you change in the code? (Hint: check the documentation)

#C. Set ``params_diction["tag_mode"] = "any"``