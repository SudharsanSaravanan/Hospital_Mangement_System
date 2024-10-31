# Patient Priority Management System

A **Patient Priority Management System** developed as a **Data Structures and Algorithms (DSA) project**, aimed at prioritizing patient care based on illness severity, age, and other criteria. This project simulates a hospital's patient management and room allocation system, utilizing multiple data structures to efficiently manage patient flow, room vacancies, and patient data.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Data Structures Used](#data-structures-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributors](#contributors)
- [License](#license)

---

## Overview

In healthcare facilities, managing patient priority and room allocation can be a challenging task, especially during high-demand times. This project addresses this by developing a **Patient Priority Management System** that:
1. Prioritizes patients based on illness severity, age, and arrival time.
2. Allocates rooms based on availability and proximity.
3. Provides patient search capabilities by unique ID and condition.

This project leverages multiple data structures to ensure optimal efficiency and response times for each feature.

## Features

- **Patient Prioritization**: Patients are sorted and retrieved based on severity, age, and arrival time using a min-heap priority queue.
- **Room Allocation**: Rooms are allocated based on vacancy and shortest path using graph traversal.
- **Search by ID or Condition**: Enables quick search of patients by their unique ID or condition using a Binary Search Tree.
- **Manage Same-Severity Patients**: Lists patients with the same severity, ordered by arrival time.
- **Patient Log**: Maintains a record of admitted and discharged patients.

## Data Structures Used

### 1. Min-Heap (Priority Queue)
   - **Purpose**: Manages patient priority based on severity, age, and arrival time.
   - **Complexity**: Insertion and retrieval are both \(O(\log n)\).

### 2. Graph (Hospital Layout & Vacancy Management)
   - **Purpose**: Models the hospital layout for room allocation and vacancy management.
   - **Complexity**: Uses Dijkstra’s algorithm for shortest path search, with a time complexity of \(O((V + E) \log V)\).

### 3. Binary Search Tree (BST)
   - **Purpose**: Allows fast search and retrieval of patients by unique ID.
   - **Complexity**: Average-case complexity for insertion and search is \(O(\log n)\).

### 4. Doubly Linked List
   - **Purpose**: Manages patients of the same severity.
   - **Complexity**: Constant time for insertion and deletion at known positions.

### 5. Array
   - **Purpose**: Stores logs of admitted and discharged patients.
   - **Complexity**: Provides constant time for appending and linear time for retrieval.

