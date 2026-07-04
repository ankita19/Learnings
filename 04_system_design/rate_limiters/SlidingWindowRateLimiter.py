import time

class SlidingWindowRateLimiter:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        # Store user_id -> list of timestamps [t1, t2, t3...]
        self.history = {}

    def is_allowed(self, user_id):
        now = time.time()
        
        if user_id not in self.history:
            self.history[user_id] = [now]
            return True
        
        # 1. Add current request timestamp
        user_timestamps = self.history[user_id]
        user_timestamps.append(now)
        
        # 2. Filter out timestamps outside the sliding window
        # We only keep timestamps that are > (now - window)
        expiry_limit = now - self.window
        
        # This list comprehension is the "Clean Python" way to filter
        self.history[user_id] = [t for t in user_timestamps if t > expiry_limit]
        
        # 3. Check if we are within limits
        if len(self.history[user_id]) <= self.limit:
            return True
        
        return False

if __name__ == "__main__":
    # Allow 2 requests per 5-second sliding window
    limiter = SlidingWindowRateLimiter(limit=2, window=5)
    
    print(f"Req 1: {limiter.is_allowed('user1')}") # True
    print(f"Req 2: {limiter.is_allowed('user1')}") # True
    print(f"Req 3: {limiter.is_allowed('user1')}") # False
    
    print("Waiting 6 seconds...")
    time.sleep(6)
    
    print(f"Req 4: {limiter.is_allowed('user1')}") # True (Window moved!)