import synping.synping
import sys

def test():
    try:
        synping.synping.ping("127.0.0.1",1,3)
    except Exception as ex:
        if 'Err' in str(ex) or '-2' in str(ex) or 'not known' in  str(ex):
            print("Test Failed on localhost port: 1 ")
            sys.exit(1)
        else:
            print("Looks Good,")


test()
sys.exit(0)