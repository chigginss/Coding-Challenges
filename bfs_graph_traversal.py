
# How do you return an object
# How do you test this 

class Queue(object):

    def  __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

class InstagramAccount(object):

    def __init__(self, instagram_id, username, biography, follower_count, folloewrs):
        self.instagram_id = instagram_id
        self.username = username
        self.biography = biography
        self.follower_count = follower_count
        self.followers = [] 

def crawl_instagram_graph(seed_instagram_id):

        to_visit = Queue()
        to_visit.enqueue(seed_instagram_id)
        top_followers = []
        visited = set()
        visited.add(seed_instagram_id)

        while not to_visit.is_empty():
            current = to_visit.dequeue()
            if len(self.followers) > 2 and current not in top_followers:
                top_followers.append(seed_instagram_id.InstagramAccount)
            else:
                for follower in current.adjacent - visited:
                    to_visit.enqueue(follower)
                    visited.add(follower)

        return top_followers

seed = InstagramAccount("cierra", 1, "chiggins", "hi!", [])
emily = InstagramAccount("emily", 2, "emzz", "hello", [])
olivia = InstagramAccount("olivia", 3, "oliva1", "heeey", [])
joe = InstagramAccount("joe", 4, "jj24", " ", [])
seed.followers = [emily, olivia, joe]
emily.followers = [olivia, seed]
olivia.followers = [emily, seed]
joe.followers = [olivia]
seed_instagram_id = seed.instagram_id
crawl_instagram_graph(seed_instagram_id)
