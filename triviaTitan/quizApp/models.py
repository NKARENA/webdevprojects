from django.db import models

# Create your models here.


class Quiz(models.Model):
    topic = models.CharField(max_length=70)

    question1 = models.CharField(max_length=250)
    option_1_q1 = models.CharField(max_length=150)
    option_2_q1 = models.CharField(max_length=150)
    option_3_q1 = models.CharField(max_length=150)
    option_4_q1 = models.CharField(max_length=150)
    answer_for_q1 = models.CharField(max_length=150)

    question2 = models.CharField(max_length=250)
    option_1_q2 = models.CharField(max_length=150)
    option_2_q2 = models.CharField(max_length=150)
    option_3_q2 = models.CharField(max_length=150)
    option_4_q2 = models.CharField(max_length=150)
    answer_for_q2 = models.CharField(max_length=150)

    question3 = models.CharField(max_length=250)
    option_1_q3 = models.CharField(max_length=150)
    option_2_q3 = models.CharField(max_length=150)
    option_3_q3 = models.CharField(max_length=150)
    option_4_q3 = models.CharField(max_length=150)
    answer_for_q3 = models.CharField(max_length=150)

    question4 = models.CharField(max_length=250)
    option_1_q4 = models.CharField(max_length=150)
    option_2_q4 = models.CharField(max_length=150)
    option_3_q4 = models.CharField(max_length=150)
    option_4_q4 = models.CharField(max_length=150)
    answer_for_q4 = models.CharField(max_length=150)

    question5 = models.CharField(max_length=250)
    option_1_q5 = models.CharField(max_length=150)
    option_2_q5 = models.CharField(max_length=150)
    option_3_q5 = models.CharField(max_length=150)
    option_4_q5 = models.CharField(max_length=150)
    answer_for_q5 = models.CharField(max_length=150)

    question6 = models.CharField(max_length=250)
    option_1_q6 = models.CharField(max_length=150)
    option_2_q6 = models.CharField(max_length=150)
    option_3_q6 = models.CharField(max_length=150)
    option_4_q6 = models.CharField(max_length=150)
    answer_for_q6 = models.CharField(max_length=150)

    question7 = models.CharField(max_length=250)
    option_1_q7 = models.CharField(max_length=150)
    option_2_q7 = models.CharField(max_length=150)
    option_3_q7 = models.CharField(max_length=150)
    option_4_q7 = models.CharField(max_length=150)
    answer_for_q7 = models.CharField(max_length=150)

    question8 = models.CharField(max_length=250)
    option_1_q8 = models.CharField(max_length=150)
    option_2_q8 = models.CharField(max_length=150)
    option_3_q8 = models.CharField(max_length=150)
    option_4_q8 = models.CharField(max_length=150)
    answer_for_q8 = models.CharField(max_length=150)

    question9 = models.CharField(max_length=250)
    option_1_q9 = models.CharField(max_length=150)
    option_2_q9 = models.CharField(max_length=150)
    option_3_q9 = models.CharField(max_length=150)
    option_4_q9 = models.CharField(max_length=150)
    answer_for_q9 = models.CharField(max_length=150)

    question10 = models.CharField(max_length=250)
    option_1_q10 = models.CharField(max_length=150)
    option_2_q10 = models.CharField(max_length=150)
    option_3_q10 = models.CharField(max_length=150)
    option_4_q10 = models.CharField(max_length=150)
    answer_for_q10 = models.CharField(max_length=150)
