# Patient Priority Management System

A **Patient Priority Management System** developed as a **Data Structures and Algorithms (DSA) project**, aimed at prioritizing patient care based on illness severity, age, and other criteria. This project simulates a hospital's patient management and room allocation system, utilizing multiple data structures to efficiently manage patient flow, room vacancies, and patient data.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Data Structures Used](#data-structures-used)
- [Methods and Usage](#methods-and-usage)
- [Time Complexity](#time-complexity)
- [Contributors](#contributors)
- [License](#license)

---

## Overview

In healthcare facilities, managing patient priority and room allocation can be a challenging task, especially during high-demand times. This project addresses this by developing a **Patient Priority Management System** that:

1. Prioritizes patients based on severity, age, and arrival time.
2. Allocates rooms based on availability and proximity.
3. Provides patient search capabilities by unique ID and condition.

This project leverages multiple data structures to ensure optimal efficiency and response times for each feature.

---

## Features

- **Patient Prioritization**: Patients are sorted and retrieved based on severity, age, and arrival time using a min-heap priority queue.
- **Room Allocation**: Rooms are allocated based on vacancy and shortest path using graph traversal.
- **Search by ID or Condition**: Enables quick search of patients by their unique ID or condition using a Binary Search Tree.
- **Manage Same-Severity Patients**: Lists patients with the same severity, ordered by arrival time.
- **Patient Log**: Maintains a record of admitted and discharged patients.

---

## Data Structures Used

1. **Min-Heap Priority Queue**
   - **Purpose**: Manages patient priority based on severity, age, and arrival time.
   - **Implementation**: Python's `heapq` library, with patients stored in a list and sorted by custom comparison operators.

2. **Graph (Adjacency List)**
   - **Purpose**: Represents hospital rooms and corridors, with nodes as rooms and edges as corridors.
   - **Implementation**: `RoomNode` objects store room connections and vacancies. Shortest path is found using **Dijkstra’s algorithm**.

3. **Binary Search Tree (BST)**
   - **Purpose**: Stores patients by unique ID for efficient searching.
   - **Implementation**: Standard BST structure with patient nodes containing IDs for fast retrieval and lookup.

---

## Methods and Usage

1. **`add_patient(self, patient)`**
   - **Description**: Adds a new patient to the priority queue.
   - **Returns**: None

2. **`admit_patient(self, patient)`**
   - **Description**: Finds the nearest vacant room from "Reception" and assigns it to the patient.
   - **Returns**: None

3. **`discharge_patient(self, room_id)`**
   - **Description**: Frees a room and removes the patient from the priority queue.
   - **Returns**: None

4. **`find_nearest_vacant_room(self, start_room_id)`**
   - **Description**: Uses Dijkstra's algorithm to find the nearest vacant room from the starting point.
   - **Returns**: `RoomNode` (nearest vacant room)

5. **`remove_patient(self, patient_id)`**
   - **Description**: Removes a patient from the priority queue.
   - **Returns**: None

6. **`display_patients_in_priority_order(self)`**
   - **Description**: Prints all patients in the priority queue in ascending order.
   - **Returns**: None

7. **`room_assigned(self)`**
   - **Description**: Displays the current room assignments and vacancy status.
   - **Returns**: None

---

## Time Complexity

- **`add_patient(self, patient)`**: **O(log n)** - Insertion in a min-heap requires maintaining heap order.
- **`admit_patient(self, patient)`**: **O(E + V log V)** - Uses Dijkstra's algorithm to find the nearest vacant room, where *V* is the number of rooms and *E* is the number of corridors.
- **`discharge_patient(self, room_id)`**: **O(n)** - Rebuilds the heap after removing a patient, requiring traversal of all patients in the priority queue.
- **`find_nearest_vacant_room(self, start_room_id)`**: **O(E + V log V)** - Dijkstra's algorithm for finding the shortest path to a vacant room.
- **`remove_patient(self, patient_id)`**: **O(n)** - Searches and rebuilds the heap after removing a patient by ID.
- **`display_patients_in_priority_order(self)`**: **O(n log n)** - Displays patients in priority order, requiring sorting of the min-heap.
- **`room_assigned(self)`**: **O(V)** - Traverses the list of rooms to display assignments, where *V* is the number of rooms.

---

## Contributors

- [Chirag Keshav](https://github.com/Chirag-Keshav)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--- 
