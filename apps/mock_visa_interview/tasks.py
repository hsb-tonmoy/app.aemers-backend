import io
import wave
from .models import MockVisaInterviewAnswer


def concatenate_audio(audio_clip_paths):
    output = io.BytesIO()
    data = []
    for clip in audio_clip_paths:
        w = wave.open(clip, "rb")
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
    output = wave.open(output, "wb")
    output.setparams(data[0][0])
    for clip in data:
        output.writeframes(clip[1])
    output.close()
    return output


def save_full_recording(session):
    audio_clip_paths = []
    for answer in MockVisaInterviewAnswer.objects.filter(session=session):
        question_audio = answer.question.question_audio
        if question_audio:
            audio_clip_paths.append(question_audio)
        audio_clip_paths.append(answer.answer)
    # output_path = f'mock_visa_interview/sessions/{session.id}/full_recording.wav'
    full_recording = concatenate_audio(audio_clip_paths)
    session.full_recording = full_recording
    session.save()
