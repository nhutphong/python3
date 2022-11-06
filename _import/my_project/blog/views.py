


from .models import model2 # .file cung folder bat buoc co dot<.>
from product.models import model1 #cach1

print("blog.views.py")

def blog_view1():
	print("tao la blog_view1() of blog.views.py")


def blog_view2():
	print("tao la blog_view2() of blog.views.py")


if __name__ == '__main__':
    print("blog.views.py.py tu chay")
    blog_view1()
    blog_view2()
else:
    print("blog.views.py duoc import")