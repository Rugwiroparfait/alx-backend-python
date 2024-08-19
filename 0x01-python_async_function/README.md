# 🚀 Python Async Project - README

## 📚 Project Overview

Welcome to the **Python Async** project! This project dives into the world of asynchronous programming in Python, helping you master key concepts like `async` and `await`, running concurrent coroutines, creating asyncio tasks, and using the `random` module for handling delays.

## 📝 Tasks Overview

### Task 0: The Basics of Async
- **File:** `0-basic_async_syntax.py`
- **🔧 Description:** Create `wait_random`, an asynchronous coroutine that waits for a random delay (between 0 and `max_delay` seconds) and returns the delay. Perfect for getting started with async!

### Task 1: Execute Multiple Coroutines Concurrently
- **File:** `1-concurrent_coroutines.py`
- **🔧 Description:** Build `wait_n`, an async function that spawns `wait_random` multiple times and returns a list of delays in ascending order. Get hands-on with concurrency!

### Task 2: Measure the Runtime
- **File:** `2-measure_runtime.py`
- **🔧 Description:** Implement `measure_time`, a function that calculates the total execution time for `wait_n(n, max_delay)` and returns the average time per coroutine. Time to measure your async skills!

### Task 3: Create asyncio Tasks
- **File:** `3-tasks.py`
- **🔧 Description:** Develop `task_wait_random`, a function that creates and returns an `asyncio.Task` for `wait_random`. Learn how to handle tasks like a pro!

### Task 4: Concurrent Tasks
- **File:** `4-tasks.py`
- **🔧 Description:** Transform `wait_n` into `task_wait_n`, using `task_wait_random` to run multiple tasks concurrently and return a sorted list of delays. Take your concurrency skills to the next level!

## ⚙️ Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Rugwiroparfait/alx-backend-python.git
   cd 0x01-python_async_function
   ```

2. Run the test files for each task:
   ```bash
   ./<task-number>-main.py
   ```

## 👤 Author

This project is crafted by NSANZIMANA RUGWIRO Dominique Parfait. © 2024 ALX, All rights reserved. Enjoy your async journey! 🚀
