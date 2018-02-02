from creatures import (
    dactylostylis,
    discerceis,
    disconectes,
    dynamenella,
    dynamene,
)

def report():
    print "These are some little buggers"
    print "-----------------------------"
    print "-", dactylostylis.Dactylostylis()
    print "-", discerceis.Discerceis()
    print "-", disconectes.Disconectes()
    print "-", dynamenella.Dynamenella()
    print "-", dynamene.Dynamene()

if __name__ == '__main__':
    report()
