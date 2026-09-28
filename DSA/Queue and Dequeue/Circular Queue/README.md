front == -1
        ↓
Queue Empty

front == rear
        ↓
মাত্র ১টা element

(rear + 1) % size == front
        ↓
Queue Full

rear = (rear + 1) % size
        ↓
Circular movement