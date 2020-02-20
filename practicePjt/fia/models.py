from django.db import models


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
# Create your models here.


class lecture(models.Model):
    prof = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    codeNum = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class evaluation(models.Model):
    subject = models.CharField(default='주제', max_length=50)
    star = models.IntegerField(default=5)
    text = models.TextField()
    password = models.IntegerField(default=0000, max_length=10)


class Course(TimeStampedModel):
    course_code = models.CharField(max_length=15)
    course_name = models.CharField(max_length=30)
    course_professor = models.CharField(max_length=30)
    course_semester = models.CharField(max_length=10)

    def __str__(self):
        return '%s - %s' % (self.course_code, self.course_name)


# class Evaluation(TimeStampedModel):
#     course = models.ForeignKey(
#         Course, verbose_name="course", on_delete=models.CASCADE)
#     grade = models.IntegerField()
#     review = models.TextField()
#     password = models.IntegerField(default=0000, max_length=10)
