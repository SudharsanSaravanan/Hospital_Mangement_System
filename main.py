import heapq
import time

# Patient class (updated with age and gender attributes)
class Patient:
    def __init__(self, patient_id, name, severity, disease, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.severity = severity
        self.arrival_time = time.time()
        self.disease = disease
        self.age = age
        self.gender = gender

    def __lt__(self, other):  # Comparison based on severity, age, and arrival time
        if self.severity == other.severity:
            if self.age == other.age:
                return self.arrival_time < other.arrival_time
            return self.age > other.age
        return self.severity < other.severity


# Graph Node representing a hospital room
class RoomNode:
    def __init__(self, room_id, vacancy=True):
        self.room_id = room_id
        self.vacancy = vacancy
        self.neighbors = {}
        self.patient_assigned = None  # Track the patient assigned to this room

    def add_neighbor(self, neighbor_room, distance):
        self.neighbors[neighbor_room] = distance


# Hospital Graph with Dijkstra's Algorithm
class HospitalGraph:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_id, vacancy=True):
        self.rooms[room_id] = RoomNode(room_id, vacancy)

    def add_corridor(self, room1_id, room2_id, distance):
        if room1_id in self.rooms and room2_id in self.rooms:
            self.rooms[room1_id].add_neighbor(self.rooms[room2_id], distance)
            self.rooms[room2_id].add_neighbor(self.rooms[room1_id], distance)

    def find_nearest_vacant_room(self, start_room_id="Reception"):
        distances = {room_id: float('inf') for room_id in self.rooms}
        distances[start_room_id] = 0
        min_heap = [(0, start_room_id)]

        while min_heap:
            current_distance, current_room_id = heapq.heappop(min_heap)
            current_room = self.rooms[current_room_id]

            # If the nearest vacant room is found, return it
            if current_room.vacancy:
                return current_room

            for neighbor, weight in current_room.neighbors.items():
                distance = current_distance + weight
                if distance < distances[neighbor.room_id]:
                    distances[neighbor.room_id] = distance
                    heapq.heappush(min_heap, (distance, neighbor.room_id))
        return None  # No vacant rooms found


# PriorityQueue class using min-heap for priority-based patient management
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def add_patient(self, patient):
        heapq.heappush(self.heap, patient)
        print(f"Patient {patient.name} with severity {patient.severity} added to priority queue.")

    def remove_patient(self, patient_id):
        # Rebuild the heap without the discharged patient
        self.heap = [patient for patient in self.heap if patient.patient_id != patient_id]
        heapq.heapify(self.heap)  # Restore heap property

    def get_next_patient(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None
    
    def display_patients_in_priority_order(self):
        print("Patients in priority order:")
        for patient in heapq.nsmallest(len(self.heap), self.heap):
            print(f"Patient ID: {patient.patient_id}, Name: {patient.name}, Severity: {patient.severity}, Age: {patient.age}, Arrival Time: {patient.arrival_time}")


# Managing patient room admission based on vacancy
class HospitalManagementSystem:
    def __init__(self):
        self.pq = PriorityQueue()
        self.hospital_graph = HospitalGraph()
        self.hospital_graph.add_room("Reception", vacancy=False)  # Adding a reception room

    def add_patient(self, patient):
        self.pq.add_patient(patient)

    def admit_patient(self, patient):
        # Start the search from "Reception" to find the nearest vacant room
        vacant_room = self.hospital_graph.find_nearest_vacant_room("Reception")
        if vacant_room:
            vacant_room.vacancy = False
            vacant_room.patient_assigned = patient  # Assign the patient to this room
            print(f"Patient {patient.name} admitted to room {vacant_room.room_id}.")
        else:
            print("No vacant rooms available at this time.")

    def discharge_patient(self, room_id):
        if room_id in self.hospital_graph.rooms:
            room = self.hospital_graph.rooms[room_id]
            if room.patient_assigned:
                patient_id = room.patient_assigned.patient_id
                room.vacancy = True
                room.patient_assigned = None  # Remove the patient from the room
                print(f"Room {room_id} is now vacant.")

                # Remove the patient from the priority queue
                self.pq.remove_patient(patient_id)
                print(f"Patient with ID {patient_id} has been discharged and removed from the hospital (priority queue).")
            else:
                print(f"No patient is currently assigned to room {room_id}.")

    def room_assigned(self):
        print("Room Assignments:")
        for room_id, room in self.hospital_graph.rooms.items():
            if room.patient_assigned:
                patient = room.patient_assigned
                print(f"Room {room_id} -> Patient ID: {patient.patient_id}, Name: {patient.name}, Severity: {patient.severity}")
            else:
                print(f"Room {room_id} is currently vacant.")


# Testing the Hospital Management System
hospital_system = HospitalManagementSystem()

# Set up rooms and corridors
hospital_system.hospital_graph.add_room("Room1", vacancy=True)
hospital_system.hospital_graph.add_room("Room2", vacancy=True)
hospital_system.hospital_graph.add_room("Room3", vacancy=False)  # Already occupied room

hospital_system.hospital_graph.add_corridor("Reception", "Room1", 3)
hospital_system.hospital_graph.add_corridor("Room1", "Room2", 5)
hospital_system.hospital_graph.add_corridor("Room2", "Room3", 10)

# Creating and adding patients
patient1 = Patient(1, "John Doe", 3, "Flu", 65, "Male")
hospital_system.add_patient(patient1)

# Admit patient to nearest vacant room from the reception
hospital_system.admit_patient(patient1)

# Show room assignments
hospital_system.room_assigned()

# Discharge a patient from a room
hospital_system.discharge_patient("Room1")

# Admit another patient
patient2 = Patient(2, "Jane Smith", 2, "Pneumonia", 70, "Female")
hospital_system.add_patient(patient2)
hospital_system.admit_patient(patient2)

# Display all patients in priority order
hospital_system.pq.display_patients_in_priority_order()

# Show updated room assignments
hospital_system.room_assigned()
