import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import add_task, complete_task, remove_task, list_tasks


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tasks = []

    def test_add_task(self):
        task = add_task(self.tasks, "Estudar DevOps")
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(task["description"], "Estudar DevOps")
        self.assertFalse(task["done"])

    def test_add_task_increments_id(self):
        add_task(self.tasks, "Primeira tarefa")
        second = add_task(self.tasks, "Segunda tarefa")
        self.assertEqual(second["id"], 2)

    def test_complete_task(self):
        task = add_task(self.tasks, "Fazer commit")
        result = complete_task(self.tasks, task["id"])
        self.assertTrue(result)
        self.assertTrue(self.tasks[0]["done"])

    def test_complete_task_not_found(self):
        result = complete_task(self.tasks, 999)
        self.assertFalse(result)

    def test_remove_task(self):
        task = add_task(self.tasks, "Tarefa temporaria")
        result = remove_task(self.tasks, task["id"])
        self.assertTrue(result)
        self.assertEqual(len(self.tasks), 0)

    def test_list_tasks_format(self):
        add_task(self.tasks, "Abrir PR")
        lines = list_tasks(self.tasks)
        self.assertEqual(len(lines), 1)
        self.assertIn("Abrir PR", lines[0])


if __name__ == "__main__":
    unittest.main()

