# checking out namespaces

def test_scope() :

    def do_local() :
        spam = "local spam"
        
    def do_nonlocal() :
        nonlocal spam
        spam = "nonlocal spam"
        
    def do_global() :
        global spam
        spam = "global spam"
        
    spam = "test spam"
    do_local()
    print ("After local ass: ", spam)
    do_nonlocal()
    print ("After nonlocal ass: ", spam)
    do_global()
    print ("After global ass: ", spam)
    
test_scope()
print ("In global scope: ", spam)