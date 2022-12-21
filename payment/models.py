from django.db import models
from schedule.models import Subject
from users.models import Student


class Payment(models.Model):
    pay_types = (
        ("cash", "cash"),
        ("card", "card"),
        ("click", "click"),
        ("payme", "payme"),
    )
    student = models.ForeignKey(Student, related_name='student_payment', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=15, choices=pay_types, default="cash")
    amount = models.FloatField()
    payment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.user.phone + ' | ' + str(self.amount)
