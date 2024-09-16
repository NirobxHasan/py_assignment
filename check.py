from task_manager import TaskManager
from storage import Storage


def main():
    storage = Storage()
    manager = TaskManager(storage)

    manager.add_task('Task 1', 'Task 1 Descriptions')
    manager.add_task('Task 2', 'Task 2 Descriptions')
    manager.add_task('Task 3', 'Task 3 Descriptions')
    print(manager.generate_report())

    manager.complete_task('Task 2')
    print(manager.generate_report())


    [print(i.title, i.completed, i.description) for i in manager.list_tasks(include_completed=True)]

    



if __name__ == "__main__":
    main()