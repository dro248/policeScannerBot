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
        # print(self.__dict__['_args'])

        # print("stream_url: ", stream_url)
        # print("dest_file: ", dest_file)
        
        self.x = ffmpeg.input(stream_url).output(dest_file)
        self.x.run(quiet=True)

class StreamRecorder:
    def __init__(self, page_url: str):
        self.recording_process = None
        self.page_url = page_url
        self.stream_url = UrlFetcher.fetch_url(self.page_url)

    def record_to(self, dest_file: str):
        if self.recording_process is not None:
                # terminate recorder process
                self.stop()
        
        # Create new process (RecorderProcess)
        self.recording_process = RecorderProcess(target=None, args=(self.stream_url, dest_file))  # type: Process
        self.recording_process.start()

        # We want to continue recording the stream, even if the url changes


    def stop(self):
        print("STOPPING NOW!")
        # self.record_thread._stop()
        self.recording_process.terminate()
        print("FINISHED STOPPING. =D")
    
    def start(self):
        """
        The start function will begin a Poll-Check-Restart loop
        """
        while True:
            # poll
            fresh_stream_url = UrlFetcher.fetch_url(self.page_url)

            # Check
            if self.stream_url != fresh_stream_url:
                self.stream_url = fresh_stream_url

                curr_time = time.strftime('%M_%S')
                # Restart
                self.record_to("out" + curr_time + ".mp3")



# src_url = UrlFetcher.fetch_url('https://www.broadcastify.com/listen/feed/18656/web')
s = StreamRecorder('https://www.broadcastify.com/listen/feed/18656/web')
s.record_to("out1.mp3")  # type: StreamRecorder


s.stop()
# print(help(s.__dict__))