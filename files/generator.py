import os
def listingPath(path):
    for item in os.listdir(path):
        yield item
        if os.path.isdir(path+"/"+item):
            for x in listingPath(path+"/"+item):
                yield f" {x}"

for x in listingPath("C:/Users/Liya Keidar/PycharmProjects/"):
    print(x)