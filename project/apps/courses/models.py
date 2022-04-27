from django.db import models
from project.apps.accounts.models import Transaction

from project.settings import AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self) -> str:
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='own_courses')
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=2000, null=False, blank=False)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_photo = models.ImageField(upload_to="courses/", null=True, blank=True)
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    
    def __str__(self) -> str:
        return self.title


class CourseMembership(models.Model):
    """ Many to Many relationship between Course and User """
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='memberships')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='members')
    date_joined = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Course membership'
        verbose_name_plural = 'Memberships of courses'
    
    def __str__(self) -> str:
        return str(self.course)


class CourseCategory(models.Model):
    """ Many to Many realtionship between Course and Category """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    
    class Meta:
        verbose_name = 'Course category'
        verbose_name_plural = 'Categories of courses'
    
    def __str__(self) -> str:
        return str(self.course)


class Lesson(models.Model):
    """ Each course have some lessons """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=300, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    videolink = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
    
    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """ User can write comment to lessons """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='comments_to_lessons')
    text = models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self) -> str:
        return self.text


class Review(models.Model):
    """ User can write course review and put it's rating """
    GREAT = 5
    GOOD = 4
    NORMAL = 3
    BAD = 2
    AWFUL = 1
    
    RATING_CHOICES = [
        (GREAT, 'Great'),
        (GOOD, 'Good'),
        (NORMAL, 'Normal'),
        (BAD, 'Bad'),
        (AWFUL, 'Awful'),
    ]
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='reviews_of_courses')
    text = models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(choices=RATING_CHOICES, default=GREAT)
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    
    def __str__(self) -> str:
        return self.text


class Wish(models.Model):
    """ 
    User can save courses to wishlist in order to buy them later.
    Uses Many to Many relationship between User and Course. 
    """
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishes')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='in_wishlist_of_users')
    
    class Meta:
        verbose_name = 'Wish'
        verbose_name_plural = 'Wishes'
    
    def __str__(self) -> str:
        return str(self.course)

