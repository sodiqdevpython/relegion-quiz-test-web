from django.contrib.auth.models import User
from django.db import models

class QuizModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Mavzu nomi')
    tugatish = models.BooleanField(default=False)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = "Yangi test qo'shish"
        verbose_name_plural = "Yangi test tuzish"


class Question(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    name = models.TextField(verbose_name="Savolni kiriting", help_text="Agar savolingizni klaviaturada yozib bo'lmasa rasmini kiriting !")
    image_question = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name="Agar savolingizni yozib bo'lmasa rasmini kiriting", help_text="Agar klaviaturada yoza olmasangiz savolni rasmga olib faqat rasmini qo'ying")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yangi savol qo'shish"
        verbose_name_plural = "Savol qo'shish"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Test javoblari"
        verbose_name_plural = "Testlar javoblari"

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_question = models.IntegerField()
    corrent_question = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    spend_time = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return self.user.username

    @property
    def total(self):
        return round((100 * self.corrent_question) / self.total_question, 2)
    class Meta:
        ordering = ['-corrent_question']
        verbose_name = "Test natijalari"
        verbose_name_plural = "Test natijalari"
        unique_together = ['user', 'quiz']

class GroupUNI(models.Model): # Group university
    name = models.CharField(max_length=50)
    overall_ball = models.PositiveIntegerField(default=0)
    group_students = models.ManyToManyField(User)

    class Meta: 
        verbose_name = 'Gurux'
        verbose_name_plural = 'Guruxlar'
    
    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # !user ni o'zi
    overall_score = models.PositiveIntegerField(default=0) #! Jami to'plagan bali userni 
    which_group = models.ForeignKey(GroupUNI, blank=True, null=True, on_delete=models.CASCADE) #! Qaysi guruxdanligi
    image = models.ImageField(upload_to='media/', blank=True, null=True) #! Profil rasmi
    average_test_solve_time = models.PositiveIntegerField(null=True, blank=True) #! O'rtacha test ishlash vaqti user ni

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profillar'

class Theme(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Mavzu'
        verbose_name_plural = 'Mavzular'