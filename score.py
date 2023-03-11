import voice


class Score:
    def __init__(self):
        self._voices = []

    def add_voice(self, voice_type):
        new_voice = voice.Voice(voice_type)
        self._voices.append(new_voice)
        return new_voice

    def get_voices(self):
        return self._voices
