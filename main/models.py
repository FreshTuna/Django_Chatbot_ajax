from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="질문")
    answer = models.CharField(max_length=100, verbose_name="답")

    def __str__(self):
        return self.question_text

    class Meta:
        db_table = 'questions' # 테이블명 지정
        verbose_name = 'Qs'
        verbose_name_plural='Qs'
