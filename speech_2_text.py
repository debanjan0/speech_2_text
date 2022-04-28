from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import sounddevice as sd
from scipy.io.wavfile import write


def speech2test(seconds=7):
    fs = 44100  # Sample rate
    """
    create and generate the api & url from the link -
    https://cloud.ibm.com/catalog/services/speech-to-text
    
    """
    apikey = <APIKEY>
    url = <URL>

    #record the audio
    my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, my_recording)  # Save as WAV file

    #authenticate with ibm cloud
    authenticator = IAMAuthenticator(apikey)
    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url(url)

    with open('output.wav', 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/wav', model='en-US_NarrowbandModel').get_result()
    text = res['results'][0]['alternatives'][0]['transcript']

    print(text)
    return text


speech2test()
