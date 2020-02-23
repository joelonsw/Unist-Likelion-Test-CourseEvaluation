from rest_framework import serializers
from fia.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "course_code",
            "course_name",
            "course_professor",
            "course_semester",
            "subject",
            "created_at",
            "updated_at",
        )