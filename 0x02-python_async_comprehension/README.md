# Python Async Comprehension

This project focuses on asynchronous programming in Python, particularly using asynchronous generators and comprehensions. The tasks involve creating coroutines that efficiently handle asynchronous operations, helping you understand how to work with async comprehensions and measure runtime for concurrent tasks.

## Learning Objectives

By the end of this project, you will be able to:
- Write an asynchronous generator.
- Utilize async comprehensions.
- Type-annotate asynchronous generators.

## Project Structure

- **0-async_generator.py**: Defines a coroutine that yields random numbers asynchronously.
- **1-async_comprehension.py**: Collects random numbers using async comprehension over the generator.
- **2-measure_runtime.py**: Measures the runtime of running async comprehensions in parallel.

## Requirements

- Python 3.7 or later
- All code should follow the `pycodestyle` (version 2.5.x) style guide.
- Each module and function must include documentation.
- Files should be executable and end with a new line.

## Usage

You can test the functionality of each script by running the provided main files:

```bash
$ ./0-main.py
$ ./1-main.py
$ ./2-main.py
```

## Example Output

Example output for each task is provided below:

```bash
$ ./0-main.py
[4.40, 6.91, 6.29, 4.55, 4.13, 9.99, 6.73, 9.84, 1.01, 1.38]

$ ./1-main.py
[9.86, 8.57, 1.75, 4.07, 0.55, 8.08, 8.39, 1.55, 7.71, 7.67]

$ ./2-main.py
10.02
```

## License

alx@africa

---

written by NSANZIMANA RUGWIRO Dominique Parfait
