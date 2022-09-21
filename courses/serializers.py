from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import Category, Course, Lesson, Tag, Action, Rating, User, Comment


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    image = SerializerMethodField(source='image')

    def get_image(self, course):
        request = self.context['request']
        name = course.image.name
        if name.startswith("/static"):
            path = '/static/%s' % name

            return request.build_absolute_uri(path)

    class Meta:
        model = Course
        fields = ["id", "subject", "created_date", "image", "category"]


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'created_date', 'updated_date', 'course', 'tags']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class LessonDetailSerializer(LessonSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content', 'tags']


class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "type", "created_date"]


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id','username', 'password', 'first_name',
                  'last_name', 'email','date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class CommentSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_date', 'updated_date', 'user']


class CreateCommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_date', 'updated_date']



class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "type", "created_date"]