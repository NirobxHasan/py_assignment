class Storage:

	def __init__(self):
		self.tasks = {} # Changed: List to dictionary for optimization and simplicity

	def save_task(self, task): #O(1) -> O(1)
		self.tasks[task.title] = task  # store title as key and task as value
 
	def update_task(self, updated_task): # O(N) -> O(1)
		if updated_task.title in self.tasks:   #constant-time lookup O(1)
			self.tasks[updated_task.title] = updated_task

	def get_task(self, title): # O(N) -> O(1)     
		return self.tasks.get(title, None) # The task object will return if title match, otherwise it will return None

	def get_all_tasks(self): #O(N) -> O(N)
		return list(self.tasks.values())

	def clear_all_tasks(self): #O(1) -> O(1)
		self.tasks.clear()
