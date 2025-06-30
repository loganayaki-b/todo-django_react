import React, { useEffect, useState } from "react";

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTitle, setNewTitle] = useState("");
  const [newDesc, setNewDesc] = useState("");

  // GET all tasks
  const fetchTasks = () => {
    fetch("http://127.0.0.1:8000/")
      .then((res) => res.json())
      .then((data) => setTasks(data));
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  // POST - Add task
  const addTask = () => {
    fetch("http://127.0.0.1:8000/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: newTitle, description: newDesc, completed: false }),
    }).then(() => {
      setNewTitle("");
      setNewDesc("");
      fetchTasks();
    });
  };

  // PUT - Toggle complete
  const toggleComplete = (task) => {
    fetch(`http://127.0.0.1:8000/
      ${task.id}/`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title: task.title,
        description: task.description,
        completed: !task.completed,
      }),
    }).then(() => fetchTasks());
  };

  // DELETE - Delete task
  const deleteTask = (id) => {
    fetch(`http://127.0.0.1:8000/
      ${id}/`, {
      method: "DELETE",
    }).then(() => fetchTasks());
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>To-Do List</h2>
      <input
        type="text"
        placeholder="Title"
        value={newTitle}
        onChange={(e) => setNewTitle(e.target.value)}
      />
      <br />
      <input
        type="text"
        placeholder="Description"
        value={newDesc}
        onChange={(e) => setNewDesc(e.target.value)}
      />
      <br />
      <button onClick={addTask}>Add Task</button>

      <ul style={{ marginTop: 20 }}>
        {tasks.map((task) => (
          <li key={task.id}>
            <b>{task.title}</b>: {task.description} -{" "}
            {task.completed ? "✅ Done" : "❌ Not done"}
            <button onClick={() => toggleComplete(task)} style={{ marginLeft: 10 }}>
              Toggle
            </button>
            <button onClick={() => deleteTask(task.id)} style={{ marginLeft: 5 }}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
