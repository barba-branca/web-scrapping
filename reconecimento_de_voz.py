import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# arquivos

audio_mp3 = 'Vicios_e_Virtudes.mp3'
audio_wav = 'Vicios_e_Virtudes.wav'

# conversão de mp3 para wav

sound = AudioSegment.from_mp3(audio_mp3)
sound.export(audio_wav, format='wav')

# selecionando audio

audio = AudioSegment.from_file(audio_wav, 'wav')

# Tamanho em milisegundos
tamanho = 30000

# divisao do audio em partes

partes = make_chunks (audio,tamanho)
partes_audio =[]
for i, parte in enumerate(partes):
    # enumerando arquivo particionado
    parte_name = 'Vicios{0}.wav'.format(i)
    
    #Guardando os nomes das partiçoes e, ima lista
    partes_audio.append(parte_name)
    
    # Exportando arquivos
    parte.export(parte_name,format='wav')
    
def transcreve_audio(nome_audio):
    # selecione o audio para reconecimento
    r = sr.Recognizer()
    with sr.Audio(nome_audio) as source:
        audio = r.record(source) # leitura do arquivo de audio
        
    # Reconhecimento usando o Google Speech Recognition
    try:
        print('Google Speech recognition: ' + r.recognize_google(audio, language='pt-BR'))
        texto = r.recognize_google(audio,language='pt-BR')
    except sr.UnknownValueError:
        print('Google Speech Recognition: ')
        texto =''
    except sr.RequestError as e:
        print('Erro ao solicitar resultados do serviço Google Speech Recognition; {0}'.format(e))
        texto=''
    return texto

# transformando audio em texto
texto=''
for parte in partes_audio:
    texto = texto + '' + transcreve_audio(parte)