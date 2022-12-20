import collections

graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tom', 'jonny']
graph['anuj'] = graph['peggy'] = graph['jonny'] = graph['tom'] = []

print(graph)

def person_seller(pers):
    return pers[-1] == 'm'

def search(name):
    search_queue = collections.deque()
    search_queue += graph[name]
    searched = list()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_seller(person):
                print(person + ' is mango seller!')
                break
            else:
                search_queue += graph[person]
                searched.append(person)
    else:
        print('No mango sellers!')

search('you')