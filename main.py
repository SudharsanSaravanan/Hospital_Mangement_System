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

    def __lt__(self, other):
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

    def find_nearest_vacant_room(self, start_room_id):
        distances = {room_id: float('inf') for room_id in self.rooms}
        distances[start_room_id] = 0
        min_heap = [(0, start_room_id)]

        while min_heap:
            current_distance, current_room_id = heapq.heappop(min_heap)

            # If the nearest vacant room is found, return it
            current_room = self.rooms[current_room_id]
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

    def get_next_patient(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None


# Managing patient room admission based on vacancy
class HospitalManagementSystem:
    def __init__(self):
        self.pq = PriorityQueue()
        self.hospital_graph = HospitalGraph()

    def add_patient(self, patient):
        self.pq.add_patient(patient)

    def admit_patient(self, patient, start_room_id):
        vacant_room = self.hospital_graph.find_nearest_vacant_room(start_room_id)
        if vacant_room:
            vacant_room.vacancy = False
            print(f"Patient {patient.name} admitted to room {vacant_room.room_id}.")
        else:
            print("No vacant rooms available at this time.")

    def discharge_patient(self, room_id):
        if room_id in self.hospital_graph.rooms:
            room = self.hospital_graph.rooms[room_id]
            room.vacancy = True
            print(f"Room {room_id} is now vacant.")


# Testing the Hospital Management System
hospital_system = HospitalManagementSystem()

# Set up rooms and corridors
hospital_system.hospital_graph.add_room("Room1", vacancy=True)
hospital_system.hospital_graph.add_room("Room2", vacancy=True)
hospital_system.hospital_graph.add_room("Room3", vacancy=False)  # Already occupied room

hospital_system.hospital_graph.add_corridor("Room1", "Room2", 5)
hospital_system.hospital_graph.add_corridor("Room2", "Room3", 10)

# Creating and adding patients
patient1 = Patient(1, "John Doe", 3, "Flu", 65, "Male")
hospital_system.add_patient(patient1)

# Admit patient to nearest vacant room
hospital_system.admit_patient(patient1, "Room1")

# Discharge a patient from a room
hospital_system.discharge_patient("Room1")

# Re-attempt to admit another patient
patient2 = Patient(2, "Jane Smith", 2, "Pneumonia", 70, "Female")
hospital_system.add_patient(patient2)
hospital_system.admit_patient(patient2, "Room2")
