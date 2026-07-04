import unittest
import time

'''
1. Given : total_request x in window_size y. if cross limit then return false

input : user_id

Cases:
    A : if new user_id  => true
    B : B.1 : if user_id exist and total_request < limit_request => update total_request and return true
        B.2 : if user_is exist and request_time - last_request_time < window_size :  reset=> update new request time and request count and return true  
    C : Return false


 API:
 is_allow(user_id) -> bool

 DataStructure:
 HashMap/Dictionary
 
Validation:
valid user validation?
request source validation? 

TestCases:
1. empty input => throw error
2. new user => return true
3. exsiting user => total_request_count > limit => false
4. existing user => 

'''



class RateLimiterPractice:
    def __init__(self, limit , window):
        self.limit = limit
        self.window = window
        self.history = {}

    def is_allowed(self, user_id):
        now = time.time()

        # if user is new, initialize them
        if user_id not in self.history:
            self.history[user_id] =  [1, now]
            return True

        # get current data for exsiting user
        count, start_time = self.history[user_id]
        
        # 1. check if the window has passed
        if now - start_time > self.window:
            self.history[user_id] = [1, now] #reset
            return  True
        
        #2. check if under limit 
        if count < self.limit:
            self.history[user_id][0] += 1 
            return True
        
        return False # over limit
    
if __name__ == "__main__":
    limiter = RateLimiterPractice(limit=2 , window=5)

    print(limiter.is_allowed('A'))
    print(limiter.is_allowed('A'))
    print(limiter.is_allowed('A'))





