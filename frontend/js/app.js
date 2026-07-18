/*
=========================================
Application Controller
=========================================
*/

const button = document.getElementById("createBtn");
const textarea = document.getElementById("query");


/*
=========================================
Load Tasks
=========================================
*/

async function loadTasks() {

    try {

        showLoading();

        const tasks = await getTasks();

        renderTaskList(tasks);

    }

    catch (error) {

        showError(error.message);

    }

    finally {

        hideLoading();

    }

}


/*
=========================================
Create Task
=========================================
*/

async function createNewTask() {

    const query = textarea.value.trim();

    if (query === "") {

        showToast("Please enter a task.", false);

        return;

    }

    try {

        showLoading();

        button.disabled = true;

        button.innerHTML = "⏳ Creating...";

        await createTask(query);

        textarea.value = "";

        await loadTasks();

        showToast("✅ Task created successfully!");

    }

    catch (error) {

        showError(error.message);

    }

    finally {

        hideLoading();

        button.disabled = false;

        button.innerHTML = "➕ Create Task";

    }

}


/*
=========================================
Events
=========================================
*/

button.addEventListener(
    "click",
    createNewTask
);


/*
=========================================
Ctrl + Enter Shortcut
=========================================
*/

textarea.addEventListener(
    "keydown",
    (event) => {

        if (event.ctrlKey && event.key === "Enter") {

            event.preventDefault();

            createNewTask();

        }

    }
);


/*
=========================================
Page Load
=========================================
*/

window.addEventListener(
    "load",
    loadTasks
);