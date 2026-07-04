from collections import defaultdict

class FileTracker:
    def __init__(self):
        # file_id -> (size, collection)
        self.processed_files = {}

        # collection -> total size
        self.collection_sizes = defaultdict(int)

        # global total
        self.total_size = 0

    def add_file(self, file_id, size, collection):
        """
        Adds a file to the migration tracker.
        Idempotent: same file_id will not be counted twice.
        """

        if file_id in self.processed_files:
            # Idempotency guarantee
            return False  # File already processed

        # Track file
        self.processed_files[file_id] = (size, collection)

        # Update totals
        self.collection_sizes[collection] += size
        self.total_size += size

        return True

    def get_total_size(self):
        return self.total_size

    def get_collection_size(self, collection):
        return self.collection_sizes.get(collection, 0)

if __name__ == "__main__":
    # 1. normal migration
    tracker = FileTracker()

    tracker.add_file("f1", 100, "space-A")
    tracker.add_file("f2", 300, "space-B")
    tracker.add_file("f3", 200, "space-A")

    print(tracker.get_total_size())
    print(tracker.get_collection_size("space-A"))
    print(tracker.get_collection_size("space-B"))

    # 2. Idempotancy
    tracker.add_file("f1", 100, "space-A")  # duplicate
    print(tracker.get_total_size())

    # 3. large file
    tracker.add_file("f4", 10_000_000_000, "space-C")
    print(tracker.get_collection_size("space-C"))
    print(tracker.get_total_size())

    # 4. Missing collection
    print(tracker.get_collection_size("space-X"))







