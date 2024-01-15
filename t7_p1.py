def makeHomepage(name, hobby):
    f = open("my_homepage.html", 'w')
    f.write(f"Name: {name}"+'\n')
    f.write(f"Hobby: {hobby}"+'\n\n\n')
    f.close()

makeHomepage("Michael", "Basketball")