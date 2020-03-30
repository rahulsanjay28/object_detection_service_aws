import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler

class VideosWatcher:
    def __init__(self, src_path):
        self.__src_path = src_path
        self.__event_handler = VideosEventHandler()
        self.__event_observer = Observer()

    def run(self):
        self.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )

class VideosEventHandler(RegexMatchingEventHandler):
    VIDEOS_REGEX = [r".*\.h264$"]

    def __init__(self):
        super().__init__(self.VIDEOS_REGEX)

    def on_created(self, event):
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            print("File is in process of creation")
            file_size = os.path.getsize(event.src_path)
            time.sleep(1)
        self.process(event)

    def process(self, event):
        print("File created")
        video_file_path = event.src_path
        print(video_file_path)


if __name__ == "__main__":
    src_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    VideosWatcher(src_path).run()
