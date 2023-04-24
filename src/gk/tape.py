class GkTape:
    def __init__(self):
        self._m_clips = []
        self._m_sources = []
        self._m_labels = []

    def createSource(self, _src_path):
        source = GkSource(self, _src_path)
        self._m_sources.append(source)
        source._m_labels.extend(self._m_labels)
        return source
    
    def addClip(self, _clip):
        self._m_clips.append(_clip)
        _clip._m_labels.extend(self._m_labels)
    
    def addLabel(self, _label):
        self._m_labels.append(_label)
        for source in self._m_sources:
            source.addLabel(_label)
        return self


class GkSource:
    def __init__(self, _tape, _src_path=""):
        self._m_tape = _tape
        self._m_path = _src_path
        self._m_clips = []
        self._m_labels = []

    def createClip(self, _start_sec, _end_sec):
        clip = GkClip(self, _start_sec, _end_sec)
        self._m_clips.append(clip)
        self._m_tape.addClip(clip)
        clip._m_labels.extend(self._m_labels)
        return clip
    
    def addLabel(self, _label):
        self._m_labels.append(_label)
        for clip in self._m_clips:
            clip.addLabel(_label)
        return self

    def getClips(self):
        return self._m_clips


class GkClip:
    def __init__(self, _source=None, _start_sec=0, _end_sec=0):
        self._m_source = _source
        self._m_start_sec = _start_sec
        self._m_end_sec = _end_sec
        self._m_labels = []

    def setSource(self, _source):
        self._m_source = _source
        return self
    
    def setStart(self, _start_sec):
        self._m_start_sec = _start_sec
        return self
    
    def setEnd(self, _end_sec):
        self._m_end_sec = _end_sec
        return self
    
    def addLabel(self, _label):
        self._m_labels.append(_label)
        return self
    
    def hasLabel(self, _label):
        return _label in self._m_labels
    

