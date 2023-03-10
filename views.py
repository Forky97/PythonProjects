def index():
    with open('templates/index.html','r') as index:
        return index.read()



def blog():
    with open('templates/blog.html','r') as blog:
        return blog.read()
