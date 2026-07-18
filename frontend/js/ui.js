/*
=========================================
UI Rendering
=========================================
*/

const taskList = document.getElementById("taskList");
const taskCount = document.getElementById("taskCount");
const loadingOverlay = document.getElementById("loadingOverlay");
const toast = document.getElementById("toast");


function formatDate(dateString) {

    if (!dateString) return "Not Available";

    return new Date(dateString).toLocaleString(
        "en-IN",
        {
            timeZone: "Asia/Kolkata",
            day: "2-digit",
            month: "short",
            year: "numeric",
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
            hour12: true,
        }
    );

}


function formatDueDate(dateString) {

    if (!dateString) {

        return "Not Specified";

    }

    return new Date(dateString).toLocaleDateString(
        "en-IN",
        {
            day: "2-digit",
            month: "short",
            year: "numeric",
        }
    );

}


function renderTask(task) {

    const card = document.createElement("div");

    card.className = "task";

    card.innerHTML = `

        <h3>${task.title}</h3>

        <p>

            <strong>📅 Due Date:</strong>

            ${formatDueDate(task.due_date)}

        </p>

        <p>

            <strong>Priority:</strong>

            <span class="badge ${task.priority.toLowerCase()}">

                ${task.priority.toUpperCase()}

            </span>

        </p>

        <small>

            Created:
            ${formatDate(task.created_at)}

        </small>

        <div class="actions">

            <button
                class="delete-btn"
                onclick="deleteTask(${task.id})">

                🗑 Delete

            </button>

        </div>

    `;

    taskList.prepend(card);

}


function renderTaskList(tasks) {

    taskList.innerHTML = "";

    taskCount.textContent =
        `${tasks.length} Task${tasks.length !== 1 ? "s" : ""}`;

    if (tasks.length === 0) {

        taskList.innerHTML = `

            <div class="empty">

                📭

                <h3>No Tasks Yet</h3>

                <p>Create your first AI task.</p>

            </div>

        `;

        return;

    }

    tasks.forEach(renderTask);

}


/*
=========================================
Loading
=========================================
*/

function showLoading() {

    loadingOverlay.classList.remove("hidden");

}

function hideLoading() {

    loadingOverlay.classList.add("hidden");

}


/*
=========================================
Toast
=========================================
*/

function showToast(message, success = true) {

    toast.innerText = message;

    toast.style.background =
        success ? "#22c55e" : "#ef4444";

    toast.classList.add("show");

    setTimeout(() => {

        toast.classList.remove("show");

    }, 3000);

}


/*
=========================================
Errors
=========================================
*/

function showError(message) {

    hideLoading();

    showToast(message, false);

}


/*
=========================================
Delete Task
=========================================
*/

async function deleteTask(id) {

    if (!confirm("Delete this task?")) {

        return;

    }

    try {

        await apiDeleteTask(id);

        showToast("Task Deleted");

        loadTasks();

    }

    catch (err) {

        showError(err.message);

    }

}