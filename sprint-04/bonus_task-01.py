class SubscriptionService:

    def __init__(self, service_name):
        self.service_name = service_name


    def __repr__(self):
        return f"{self.service_name}" 



class User:

    def __init__(self, name):
        self.name = name
        self.subscriptions = set()


    def subscribe(self, service):
        self.subscriptions.add(service)


    def unsubscribe(self, service):
        self.subscriptions.remove(service)


    def common_services(self, user):
        shared_objects = set(self.subscriptions) & set(user.subscriptions)
        return [service.service_name for service in shared_objects]



# Creating services
netflix = SubscriptionService("Netflix")
spotify = SubscriptionService("Spotify")
github = SubscriptionService("GitHub")

# Creating users
anna = User("Anna")
bob = User("Bob")

anna.subscribe(netflix)
anna.subscribe(spotify)

bob.subscribe(spotify)
bob.subscribe(github)

print(anna.common_services(bob)) # ['Spotify']

anna.unsubscribe(spotify)
print(anna.common_services(bob)) # []
print(anna.subscriptions) # {Netflix}