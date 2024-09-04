import time

class Room:
    def __init__(self, name):
        self.name = name
        self.dirty = True

    def clean(self):
        print(f"Vacuum cleaner in Room {self.name}: Sucking dirt...")
        self.dirty = False

    def is_dirty(self):
        return self.dirty

class VacuumCleaner:
    def __init__(self):
        self.room_a = Room("A")
        self.room_b = Room("B")
        self.current_room = self.room_a

    def move_to_room(self, room):
        self.current_room = room
        print(f"Moving to Room {self.current_room.name}...")

    def clean_current_room(self):
        if self.current_room.is_dirty():
            self.current_room.clean()
        else:
            print(f"Room {self.current_room.name} is already clean.")

    def clean_rooms_monday_tuesday(self):
        for day in ["Monday", "Tuesday"]:
            print(f"\n--- {day} ---")
            self.move_to_room(self.room_a)
            self.clean_current_room()
            time.sleep(1) 
            
            self.move_to_room(self.room_b)
            self.clean_current_room()
            time.sleep(1)  
            self.room_a.dirty = True
            self.room_b.dirty = True

if __name__ == "__main__":
    vacuum = VacuumCleaner()
    vacuum.clean_rooms_monday_tuesday()
