import ffmpeg
from multiprocessing import Process
from url_fetcher import UrlFetcher
import time

class RecorderProcess(Process):
    def run(self):
        print("HI from the PROCESS")
        args = self.__dict__['_args']
        stream_url = args[0]
        dest_file = args[1]
        print(self.__dict__['_args'])

        print("stream_url: ", stream_url)
        print("dest_file: ", dest_file)
        
        self.x = ffmpeg.input(stream_url).output(dest_file)
        self.x.run(quiet=True)

class StreamRecorder:
    def __init__(self):
        self.recording_process = None

    def record(self, stream_url: str, dest_file):
        if self.recording_process is not None:
                # Join thread
                self.recording_process.join()
        
        # Create new thread
        self.recording_process = RecorderProcess(target=None, args=(stream_url, dest_file))  # type: Process
        self.recording_process.start()
        print('hi')

    def stop(self):
        print("STOPPING NOW!")
        # self.record_thread._stop()
        self.recording_process.terminate()
        print("FINISHED STOPPING. =D")

src_url = UrlFetcher.fetch_url('https://www.broadcastify.com/listen/feed/18656/web')
s = StreamRecorder()
s.record(src_url, "out1.mp3")  # type: StreamRecorder

for i in range(10):
    print("hello: " + str(i))
    time.sleep(1)

s.stop()
# print(help(s.__dict__))