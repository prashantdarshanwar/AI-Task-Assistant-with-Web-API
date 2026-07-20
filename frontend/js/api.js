/*
=========================================
API Layer
Handles communication with FastAPI Backend
=========================================
*/

const BASE_URL = "http://13.207.61.163:8000";

/*
=========================================
Create Task
=========================================
*/

async function createTask(query) {

    const response = await fetch(
        `${BASE_URL}/assistant`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify({
                query: query,
            }),
        }
    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(
            data.message ||
            data.detail ||
            "Failed to create task."
        );

    }

    return data;

}

/*
=========================================
Get All Tasks
=========================================
*/

async function getTasks() {

    const response = await fetch(
        `${BASE_URL}/tasks`
    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(
            data.message ||
            "Unable to load tasks."
        );

    }

    return data;

}

/*
=========================================
Delete Task
=========================================
*/

async function apiDeleteTask(id) {

    const response = await fetch(
        `${BASE_URL}/tasks/${id}`,
        {
            method: "DELETE",
        }
    );

    if (!response.ok) {

        const data = await response.json();

        throw new Error(
            data.message ||
            "Unable to delete task."
        );

    }

    return true;

}

/*
=========================================
Update Task (Future Use)
=========================================
*/

async function updateTask(id, payload) {

    const response = await fetch(
        `${BASE_URL}/tasks/${id}`,
        {
            method: "PUT",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify(payload),
        }
    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(
            data.message ||
            "Unable to update task."
        );

    }

    return data;

}