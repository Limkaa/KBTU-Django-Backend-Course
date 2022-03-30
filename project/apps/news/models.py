from django.db import models

from project.settings import COURSE_MODEL

class News(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    text = models.CharField(max_length=2000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
    
    def __str__(self) -> str:
        return self.title


class CourseNews(News):
    course = models.ForeignKey(COURSE_MODEL, on_delete=models.CASCADE, related_name='news')
    
    class Meta:
        verbose_name = 'Course news'
        verbose_name_plural = 'Courses news'
    
    def __str__(self) -> str:
        return self.title