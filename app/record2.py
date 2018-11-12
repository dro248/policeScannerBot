import ffmpeg
from threading import Thread
from url_fetcher import UrlFetcher
import time

class RecorderThread(Thread):
    def run(self):
        args = self.__dict__['_args']
        stream_url = args[0]
        dest_file = args[1]
        # print(self.__dict__['_args'])

        # print("stream_url: ", stream_url)
        # print("dest_file: ", dest_file)
        
        self.x = ffmpeg.input(stream_url).output(dest_file)
        self.x.run(quiet=True)


class StreamRecorder:
    def __init__(self):
        self.record_thread = None

    def record(self, stream_url: str, dest_file):
        if self.record_thread is not None:
                # Join thread
                self.record_thread.join()
        
        # Create new thread
        self.record_thread = RecorderThread(target=None, args=(stream_url, dest_file), name="recorderThread")  # type: Thread
        self.record_thread.start()

    def stop(self):
        print("STOPPING NOW!")
        self.record_thread._stop()
        # self.record_thread.join()
        print("FINISHED STOPPING. =D")

src_url = UrlFetcher.fetch_url('https://www.broadcastify.com/listen/feed/18656/web')
s = StreamRecorder()
s.record(src_url, "out1.mp3")  # type: StreamRecorder

for i in range(10):
    print("hello: " + str(i))
    time.sleep(1)

print(help(s.__dict__))