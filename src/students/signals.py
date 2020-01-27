from django.db.models.signals import pre_save
from django.dispatch import receiver
from students.models import Student


@receiver(pre_save, sender=Student)
def pre_save_student(sender, instance, **kwargs):
    instance.email = instance.email.lower()
    print(sender)
    print(kwargs)
    print(instance)

    if instance.id is None:
        print('Object is created!')
        import inspect
        print(inspect.stack())