from django.contrib.auth.models import User, Group

from rest_framework import serializers


from .models import Task, Article


"""
    voi class Serializer chung ta phai code lai tat ca methods nhu ben duoi
    cac arguments phai dung so luong de nhan value tuong ung
    return dung voi chuc nang cua name method
    
    voi class Serializer chung ta co the code theo y minh

"""
# class ArticleSerializer(serializers.Serializer):
#     """
#         khi inheritance Serializer co

#         self.validated_data = dict(**form)
#     """

#     """
#         # .save() will create a new instance.
#         serializer = ArticleSerializer(data=request.data)

#         # .save() will update the existing `article` instance.
#         serializer = ArticleSerializer(article, data=request.data)

#         article_or_article_update = serializer.save()


#         # voi partial=True chi update 1 field content='foo bar'
#         # 
#         serializer = CommentSerializer(comment, data={'content': 'foo bar'}, partial=True)
#         serializer.save()

#     """

#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateTimeField()


#     def create(self, validated_data):
#         # validated_data = dict(**form)=nhan tu form

#         return Article.objects.create(validated_data)


#     def update(self, instance, validated_data):
#         # instance = Article()

#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()

#         return instance

""" 
        def save(self):
            title = self.validated_data['title']
            author = self.validated_data['author']
            send_email(from=email, message=message) 
            
            # default
            # return create() or update()

    
        # check field truoc khi dung
        def validate_title(self, title):
            # title = field = str

            if 'django' not in field.lower():
                raise serializers.ValidationError("Blog post is not about Django")
            return title

        # more...
    """


# ========================================================================

"""
    ModelSerializer da defined
        def create(self, validated_data)
        def update(self, instance, validated_data)
"""

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields =  '__all__' # ['id', 'title', 'author']
        # exclude = ['author'] # bo qua field 'author'
        # read_only_fields = ['author'] # read only 


class TaskSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'


# from rest_framework.validators import UniqueValidator


# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )

#     username = serializers.CharField(
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )

#     password = serializers.CharField(min_length=8)

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             validated_data['username'],
#             validated_data['email'],
#             validated_data['password']
#             )

#         return user

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']