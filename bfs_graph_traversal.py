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

class SocialMediaAccount(object):

    def __init__(self, user_id, username, biography, follower_count, followers):
        self.instagram_id = instagram_id
        self.username = username
        self.biography = biography
        self.follower_count = follower_count
        self.followers = followers

def crawl_social_media_graph(seed_user_id):

        to_visit = Queue()
        to_visit.enqueue(seed_user_id)
        top_followers = []
        visited = set()
        visited.add(seed_user_id)

        while not to_visit.is_empty():
            current = to_visit.dequeue()
            if len(self.followers) > 2 and current not in top_followers:
                top_followers.append(seed_user_id.SocialMediaAccount)
            else:
                for follower in current.adjacent - visited:
                    to_visit.enqueue(follower)
                    visited.add(follower)

        return top_followers

seed = SocialMediaAccount("cierra", 1, "chiggins", "hi!", [])
emily = SocialMediaAccount("emily", 2, "emzz", "hello", [])
olivia = SocialMediaAccount("olivia", 3, "oliva1", "heeey", [])
joe = SocialMediaAccount("joe", 4, "jj24", " ", [])
seed.followers = [emily, olivia, joe]
emily.followers = [olivia, seed]
olivia.followers = [emily, seed]
joe.followers = [olivia]
seed_user_id = seed.user_id
crawl_social_media_graph(seed_user_id)
