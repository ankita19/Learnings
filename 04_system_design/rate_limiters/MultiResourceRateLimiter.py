import time

class MultiResourceRateLimiter:
    def __init__(self, limits_config):
        # limits_config = {"GET": {"limit": 100, "window": 60}, "POST": {"limit": 5, "window": 60}}
        self.limits_config = limits_config
        self.history = {} # Key: (user_id, resource_type), Value: [timestamps]

    def is_allowed(self, user_id, resource_type):
        # 1. Check if the resource type is valid
        if resource_type not in self.limits_config:
            return True # Or throw error, but usually allow if undefined
            
        config = self.limits_config[resource_type]
        limit = config["limit"]
        window = config["window"]
        
        now = time.time()
        key = (user_id, resource_type)
        
        # 2. Initialize if first time
        if key not in self.history:
            self.history[key] = [now]
            return True
            
        # 3. Sliding Window Logic
        timestamps = self.history[key]
        expiry_limit = now - window
        
        # Filter out old timestamps
        updated_timestamps = [t for t in timestamps if t > expiry_limit]
        
        # 4. Check limit and update
        if len(updated_timestamps) < limit:
            updated_timestamps.append(now)
            self.history[key] = updated_timestamps
            return True
        else:
            self.history[key] = updated_timestamps # Save filtered list even if blocked
            return False

# --- Practice Testing ---
if __name__ == "__main__":
    # Define our rules
    configs = {
        "GET": {"limit": 5, "window": 10},
        "POST": {"limit": 2, "window": 10}
    }
    
    limiter = MultiResourceRateLimiter(configs)
    
    # Test POST (Strict)
    print(f"POST 1: {limiter.is_allowed('user_1', 'POST')}") # True
    print(f"POST 2: {limiter.is_allowed('user_1', 'POST')}") # True
    print(f"POST 3: {limiter.is_allowed('user_1', 'POST')}") # False (Blocked!)
    
    # Test GET (More generous)
    print(f"GET 1: {limiter.is_allowed('user_1', 'GET')}")  # True (Independent of POST)
    print(f"GET 2: {limiter.is_allowed('user_1', 'GET')}")  # True