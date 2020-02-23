from rest_framework import serializers
from .models import Course
from .models import Evaluation


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "course_code",
            "course_name",
            "course_professor",
            "course_semester",
            "created_at",
            "updated_at",
        )


class EvluationSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Evaluation
        fields = (
            "id",
            "course",
            "grade",
            "review",
            "password",
            "created_at",
            "updated_at",
        )

