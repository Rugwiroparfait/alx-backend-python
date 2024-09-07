# 0x03. Unittests and Integration Tests

## Project Overview
This project focuses on understanding and applying **unit tests** and **integration tests** in Python, particularly within the context of backend development. You'll write and execute tests to verify your code's functionality and interactions across different modules.

### Unit Testing
Unit tests check individual functions or methods to ensure they return the correct results for a set of inputs. You’ll mock external function calls, such as network or database requests, to isolate and verify the logic of the function being tested.

### Integration Testing
Integration tests evaluate how different components of your code interact with each other in a more complete system. Only low-level external calls (e.g., HTTP requests, database I/O) are mocked, allowing you to test larger code paths.

## Learning Objectives
By the end of this project, you should be able to:
- Differentiate between **unit** and **integration** tests.
- Understand and apply common testing patterns such as **mocking**, **parameterization**, and **fixtures**.

## Requirements
- Files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files must end with a new line.
- First line of every file should be `#!/usr/bin/env python3`.
- Code must follow **pycodestyle** (version 2.5).
- All files must be executable.
- Document every module, class, and function.
- All functions and coroutines must be type-annotated.

## Setup and Execution

### Running Tests
Execute your unit and integration tests using the following command:
```bash
$ python -m unittest path/to/test_file.py
```

### Directory Structure
- **GitHub Repository**: `alx-backend-python`
- **Project Directory**: `0x03-Unittests_and_integration_tests`
- **Test Files**: 
  - `test_utils.py`
  - `test_client.py`

### Files Required
- `utils.py`
- `client.py`
- `fixtures.py`

## Tasks

### 0. Parameterize a Unit Test
Create a `TestAccessNestedMap` class in `test_utils.py` to test the `utils.access_nested_map` function with parameterized inputs.

### 1. Test for Exceptions
Expand your tests in `TestAccessNestedMap` to verify that a `KeyError` is raised for invalid paths.

### 2. Mock HTTP Calls
Create a `TestGetJson` class to mock HTTP requests using `unittest.mock.patch` to avoid actual external calls.

### 3. Memoization
Implement `TestMemoize` to test the `utils.memoize` decorator.

### 4. Patching as Decorators
In `test_client.py`, write tests for `client.GithubOrgClient.org`, using `@patch` to mock external HTTP calls.

### 5. Mocking a Property
Test the `client.GithubOrgClient._public_repos_url` method by patching its dependencies.

### 6. More Patching
Write tests for the `client.GithubOrgClient.public_repos` method, mocking both external requests and properties.

### 7. Parameterize Tests
Test `client.GithubOrgClient.has_license` by parameterizing different repository license inputs.

### 8. Integration Test: Fixtures
Use fixtures to test the `GithubOrgClient.public_repos` method, mocking external requests but testing end-to-end interactions.

## Resources
- **[unittest Framework](https://docs.python.org/3/library/unittest.html)**
- **[unittest.mock Library](https://docs.python.org/3/library/unittest.mock.html)**
- **[Memoization](https://en.wikipedia.org/wiki/Memoization)**
