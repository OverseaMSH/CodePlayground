// https://quera.org/college/6092/chapter/20016/lesson/248156/?comments_page=1&comments_filter=ALL&submissions_page=1
const tasks = [];

function addTask(title) {
  if (!title) {
    console.log("Task title cannot be empty.");
    return;
  }

  if (tasks.find((task) => task.title === title)) {
    console.log(`Task with title "${title}" already exists.`);
    return;
  }

  tasks.push({ title, completed: false });
  console.log(`Task "${title}" added.`);
}

function removeTask(title) {
  const taskIndex = tasks.findIndex((task) => task.title === title);

  if (taskIndex === -1) {
    console.log(`Task with title "${title}" not found.`);
    return;
  }

  tasks.splice(taskIndex, 1);
  console.log(`Task "${title}" removed.`);
}

function toggleTaskStatus(title) {
  const task = tasks.find((task) => task.title === title);

  if (!task) {
    console.log(`Task with title "${title}" not found.`);
    return;
  }

  task.completed = !task.completed;
  console.log(
    `Task "${title}" marked as ${task.completed ? "completed" : "not completed"}.`
  );
}

function listTasks(title) {
  let filteredTasks = tasks;

  if (title) {
    filteredTasks = tasks.filter((task) =>
      task.title.toLowerCase().includes(title.toLowerCase())
    );
  }

  if (filteredTasks.length === 0) {
    console.log("No tasks found.");
    return;
  }

  console.log("Tasks:");
  filteredTasks.forEach((task, index) => {
    console.log(
      `${index + 1}. ${task.title} [${task.completed ? "completed" : "not completed"}]`
    );
  });
}

function findTask(title) {
  const task = tasks.find((task) => task.title === title);

  if (!task) {
    console.log(`Task with title "${title}" not found.`);
    return;
  }

  console.log(
    `Task found: ${task.title} [${task.completed ? "completed" : "not completed"}]`
  );
}

const TaskManager = {
  tasks,
  addTask,
  removeTask,
  toggleTaskStatus,
  listTasks,
  findTask,
};

module.exports = TaskManager;
