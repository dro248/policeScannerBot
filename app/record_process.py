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

        self.x = ffmpeg.input(stream_url).output(dest_file)
        self.x.run(quiet=True, overwrite_output=True)

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
        self.recording_process = RecorderProcess(target=None, args=(self.stream_url, dest_file))
        
        # We want to continue recording the stream, even if the url changes
        self.recording_process.run()


    def stop(self):
        print("Turning off Recorder...")
        try:
            self.recording_process.terminate()
        except Exception as e:
            pass
        print("Stopped Recording. =D")
    

    def _run(self):
        """
        The start function will begin a Poll-Check-Restart loop. 
        This should never be called externally (hence the _ prefix).
        """
        # poll
        while True:
            fresh_stream_url = UrlFetcher.fetch_url(self.page_url)

            # Check if current stream url is different from the new one
            if self.stream_url != fresh_stream_url:
                self.stream_url = fresh_stream_url

                curr_time = time.strftime('%M_%S')
                
                # Restart
                self.record_to("out" + curr_time + ".mp3")

                # Wait 30s
                time.sleep(30)


try:
    s = StreamRecorder('https://www.broadcastify.com/listen/feed/18656/web')
    s.record_to("out1.mp3")  # type: StreamRecorder
except KeyboardInterrupt:
    print("Caught KeyboardInterrupt signal")
    s.stop()
