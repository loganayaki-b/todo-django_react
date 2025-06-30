
import React, { useEffect, useState } from "react";

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTitle, setNewTitle] = useState("");
  const [newDesc, setNewDesc] = useState("");

  const BASE_URL = "http://127.0.0.1:8000/tasks";

  // Fetch all tasks (GET)
  const fetchTasks = async () => {
    try {
      const res = await fetch(BASE_URL);
      const data = await res.json();
      setTasks(data);
    } catch (error) {
      console.error("Error fetching tasks:", error);
    }
  };

  // Add new task (POST)
  const addTask = async () => {
    if (!newTitle || !newDesc) return;
    try {
      await fetch(BASE_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: newTitle,
          description: newDesc,
          completed: false,
        }),
      });
      setNewTitle("");
      setNewDesc("");
      fetchTasks();
    } catch (error) {
      console.error("Error adding task:", error);
    }
  };

  // Toggle task completed (PUT)
  const toggleComplete = async (task) => {
    try {
      await fetch(`${BASE_URL}/${task.id}/`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: task.title,
          description: task.description,
          completed: !task.completed,
        }),
      });
      fetchTasks();
    } catch (error) {
      console.error("Error updating task:", error);
    }
  };

  // Delete task (DELETE)
  const deleteTask = async (id) => {
    try {
      await fetch(`${BASE_URL}/${id}/`, {
        method: "DELETE",
      });
      fetchTasks();
    } catch (error) {
      console.error("Error deleting task:", error);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>📝 To-Do List</h2>

      <input
        type="text"
        placeholder="Enter title"
        value={newTitle}
        onChange={(e) => setNewTitle(e.target.value)}
        style={{ marginBottom: 8, padding: 5 }}
      />
      <br />
      <input
        type="text"
        placeholder="Enter description"
        value={newDesc}
        onChange={(e) => setNewDesc(e.target.value)}
        style={{ marginBottom: 8, padding: 5 }}
      />
      <br />
      <button onClick={addTask} style={{ padding: 6, marginBottom: 20 }}>
        ➕ Add Task
      </button>

      <ul>
        {tasks.map((task) => (
          <li key={task.id} style={{ marginBottom: 10 }}>
            <span>
              <b>{task.title}</b>: {task.description} -{" "}
              {task.completed ? "✅ Done" : "❌ Not done"}
            </span>
            <br />
            <button onClick={() => toggleComplete(task)} style={{ marginRight: 5 }}>
              🔄 Toggle
            </button>
            <button onClick={() => deleteTask(task.id)}>🗑️ Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
