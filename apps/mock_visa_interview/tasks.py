import io
import wave
from django.core.files import File as DjangoFile
from .models import MockVisaInterviewAnswer


# def concatenate_audio(audio_clip_paths):
#     output = io.BytesIO()
#     data = []
#     for clip in audio_clip_paths:
#         w = wave.open(clip, "rb")
#         data.append([w.getparams(), w.readframes(w.getnframes())])
#         w.close()
#     output = wave.open(output, "wb")
#     output.setparams(data[0][0])
#     for clip in data:
#         output.writeframes(clip[1])
#     output.close()
#     return output

def concatenate_audio(audio_clip_paths):
    audio = [io.BytesIO(x) for x in audio_clip_paths]
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


def save_full_recording(session):
    audio_clip_paths = []
    for answer in MockVisaInterviewAnswer.objects.filter(session=session):
        question_audio = answer.question.question_audio
        if question_audio:
            audio_clip_paths.append(question_audio)
        audio_clip_paths.append(answer.answer)
    # output_path = f'mock_visa_interview/sessions/{session.id}/full_recording.wav'
    full_recording = concatenate_audio(audio_clip_paths)
    # full_recording_file = DjangoFile(
    #     open(full_recording, mode='rb'), name='full_recording.wav')
    session.full_recording = full_recording.read()
    session.save()
