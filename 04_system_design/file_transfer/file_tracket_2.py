from collections import defaultdict

class FileCollectionTracker:
    def __init__(self):
        # file_name -> (size, set(collections))
        self.file_metadata = {}
        self.col_sizes = defaultdict(int)
        self.col_counts = defaultdict(int)
        self.total_system_size = 0

    def addFile(self, name, size, collections):
        # 1. Handle Updates (Idempotency)
        if name in self.file_metadata:
            old_size, old_cols = self.file_metadata[name]
            self._update_stats(old_size, old_cols, increment=False)

        # 2. Add New Data
        new_cols = set(collections) # Use set to avoid duplicate counts
        self.file_metadata[name] = (size, new_cols)
        self._update_stats(size, new_cols, increment=True)

    def _update_stats(self, size, collections, increment=True):
        m = 1 if increment else -1
        self.total_system_size += (size * m)
        
        for c in collections:
            self.col_sizes[c] += (size * m)
            self.col_counts[c] += (1 * m)
            
            # Clean up empty collections to keep memory lean
            if self.col_counts[c] <= 0:
                self.col_sizes.pop(c, None)
                self.col_counts.pop(c, None)

    def getTotalFileSize(self):
        return self.total_system_size

    def getTopCollections(self, strategy):
        # strategy 0: Size, strategy 1: Count
        data = self.col_sizes if strategy == 0 else self.col_counts
        
        # KEY LOGIC: Sort by -value (descending) then by name (ascending)
        # This handles the "lexicographic tie-break" requirement perfectly.
        sorted_cols = sorted(
            data.items(), 
            key=lambda x: (-x[1], x[0])
        )
        
        return [name for name, _ in sorted_cols[:10]]

# --- Scenario Test ---
if __name__ == "__main__":
    tracker = FileCollectionTracker()
    tracker.addFile("file1.txt", 400, ["col1", "travel"])
    tracker.addFile("file2.txt", 100, ["col1"])
    tracker.addFile("file3.txt", 200, ["travel", "work"])
    
    print(f"Total Size: {tracker.getTotalFileSize()}") # 700
    print(f"Top by Size: {tracker.getTopCollections(0)}") # ['travel', 'col1', 'work']
    
    # Update file1 to smaller size and different collection
    tracker.addFile("file1.txt", 50, ["work"]) 
    print(f"Total after update: {tracker.getTotalFileSize()}") # 350