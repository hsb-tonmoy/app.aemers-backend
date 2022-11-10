import io
import wave
from django.core.files import File as DjangoFile
from .models import MockVisaInterviewAnswer


def concatenate_audio(audio_clip_paths):
    audio = [io.BytesIO(x.read()) for x in audio_clip_paths]
    params_set = False
    temp_file = io.BytesIO()
    with wave.open(temp_file, 'wb') as temp_input:
        for audio_file in audio:
            with wave.open(audio_file, 'rb') as w:
                if not params_set:
                    temp_input.setparams(w.getparams())
                    params_set = True
                temp_input.writeframes(w.readframes(w.getnframes()))

    temp_file.seek(0)
    return temp_file


def save_full_recording(session):
    audio_clip_paths = []
    for answer in MockVisaInterviewAnswer.objects.filter(session=session):
        question_audio = answer.question.question_audio
        if question_audio:
            audio_clip_paths.append(question_audio)
        audio_clip_paths.append(answer.answer)
    full_recording = concatenate_audio(audio_clip_paths)
    full_recording_file = DjangoFile(
        name='full_recording.wav', file=full_recording)
    session.full_recording = full_recording_file
    session.save()
