from django.test import TestCase # Django fornece isolamento entre os testes que acessam o banco
from .models import Task

# Create your tests here.
class TaskModelTests(TestCase):

    def test_create_task(self):
        task = Task.objects.create(
            title="Aprender Testcontainers"
        )

        saved_task = Task.objects.get(pk=task.pk)

        self.assertEqual(
            saved_task.title,
            "Aprender Testcontainers",
        )

        self.assertFalse(saved_task.completed)

    def test_update_task(self):
        task = Task.objects.create(
            title="Estudar Django"
        )

        task.completed = True
        task.save()

        updated_task = Task.objects.get(pk=task.pk)

        self.assertTrue(updated_task.completed)