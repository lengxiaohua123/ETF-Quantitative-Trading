class EventHandler:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def handle_events(self):
        for event in self.events:
            # 事件处理逻辑
            pass