
class ContentMgr(object):
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def show(self):
        print("show method")
        print("except",1/0)

with ContentMgr() as mgr:

    mgr.show()