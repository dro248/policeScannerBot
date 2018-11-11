from url_fetcher import UrlFetcher
import subprocess


class StreamRecorder:
    def record(self, stream_url: str, dest_file):
        #  bash stream_recorder.sh -s http://relay.broadcastify.com/7sth0nfg9y5pcjq.mp3 -d out.mp3
        x = subprocess.call(["bash", "./bash/stream_recorder.sh", "-s", stream_url, "-d", dest_file], 
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        print('hi')
        print(x.stdout)

StreamRecorder().record(UrlFetcher.fetch_url('https://www.broadcastify.com/listen/feed/18656/web'), 'out.mp3')