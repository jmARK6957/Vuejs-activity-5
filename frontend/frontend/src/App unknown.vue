<template>
  <main>
    <h1>{{ message }}</h1>

    <form @submit.prevent="addTask">
      <label>
        New Task
        <input v-model="newTask" name="newTask" />
      </label>
      <div class="button-container">
        <button type="submit" :disabled="newTask.trim() === ''">Add</button>
      </div>
    </form>

    <ul class="task-list">
      <li
        v-for="task in tasks"
        :key="task.id"
        :class="{ completed: task.completed, editing: editingTask && editingTask.id === task.id }"
      >
        <input type="checkbox" v-model="task.completed" />

        <span v-if="editingTask && editingTask.id === task.id">
          <input v-model="editingTask.text" @keyup.enter="saveEdit" />
        </span>
        <span v-else>
          {{ task.text }}
        </span>

        <div class="task-actions">
          <button
            class="edit-btn"
            @click="startEditing(task)"
            v-if="!editingTask || editingTask.id !== task.id"
            title="Edit"
          >
            ✏️
          </button>

          <button
            class="edit-btn"
            @click="saveEdit"
            v-if="editingTask && editingTask.id === task.id"
            title="Save"
          >
            💾
          </button>

          <button class="delete-btn" @click="deleteTask(task.id)" title="Delete">
            🗑️
          </button>
        </div>
      </li>
    </ul>
  </main>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

interface Task {
  id: number;
  text: string;
  completed: boolean;
}

const message = ref('Tasks');
const newTask = ref('');
const tasks = ref<Task[]>([

]);

const editingTask = ref<Task | null>(null);

function addTask() {
  const trimmedText = newTask.value.trim();
  if (trimmedText === '') return;

  const newId = tasks.value.length > 0 ? Math.max(...tasks.value.map(t => t.id)) + 1 : 1;
  tasks.value.push({
    id: newId,
    text: trimmedText,
    completed: false,
  });
  newTask.value = '';
}

function deleteTask(id: number) {
  tasks.value = tasks.value.filter(task => task.id !== id);
}

function startEditing(task: Task) {
  editingTask.value = { ...task };
}

function saveEdit() {
  if (!editingTask.value || editingTask.value.text.trim() === '') return;

  const taskIndex = tasks.value.findIndex(t => t.id === editingTask.value!.id);
  if (taskIndex !== -1) {
    tasks.value[taskIndex].text = editingTask.value.text.trim();
  }
  editingTask.value = null;
}
</script>

<style scoped>
main {
  max-width: 800px;
  margin: 1rem auto;
}

.button-container {
  display: flex;
  justify-content: end;
  margin-top: 1rem;
}

.task-list {
  list-style: none;
  padding: 0;
}

.task-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 0;
  border-bottom: 1px solid #ccc;
}

.task-list li.com pleted span {
  text-decoration: line-through;
  color: #888;
}

.task-list li.editing {
  background-color: #f0f8ff;
}

.task-actions {
  display: flex;
  gap: 0.5rem;
}

input[type="text"] {
  padding: 0.5rem;
  width: 100%;
}

input[type="checkbox"] {
  margin-right: 0.5rem;
}

/* Button styles */
button {
  padding: 0.4rem 0.75rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.edit-btn {
  background-color: #4CAF50;
}

.delete-btn {
  background-color: #f44336;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
