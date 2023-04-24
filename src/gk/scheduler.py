from collections import OrderedDict

class GkScheduler:
    def __init__(self):
        self._m_criteria = []
        self._m_sources = []

    def addCriteria(self, _criteria):
        self._m_criteria.append(_criteria)

    def addSources(self, _sources):
        self._m_sources.append(_sources)

    def schedule(self):
        # Prioritize the criteria
        self._m_criteria.sort(key=lambda crit: crit._m_priority)

        # TODO I need to rethink this. Applying the label weights is fine, because
        # it lets us weed out the 0s. However, we can't apply the timing weights until
        # we're actually scheduling... all we can do up front is calculate the occur_pct
        # of each clip. So we need to save both the weights and the occur_pct... is there 
        # a better way to structure / store this information?
        timeline = {}
        for criteria in self._m_criteria:
            for source in self._m_sources:
                clipWeights = OrderedDict.fromkeys(source.getClips(), 1.0)
                clipWeights = criteria.applyLabelWeights(clipWeights)

        

class GkCriteria:
    def __init__(self):
        self._m_priority = 0

        self._m_chooseOnlyOnce = True
        self._m_startTimeSec = 0
        self._m_endTimeSec = 0
        self._m_reoccurFreqSec = 0
        self._m_randomSec = 0

        self._m_labelWeightsDict = {}

        self._m_chooseRandomly = False
        self._m_windowPct = 0
        self._m_weightCurve = 0
        self._m_chooseBackwards = False

    def applyLabelWeights(self, _clipWeights):
        labelWeights = self._m_labelWeightsDict.copy()
        elseWeight = labelWeights.pop("else", None)
        matchedClips = []

        for clip in _clipWeights:
            for label in labelWeights:
                if clip.hasLabel(label):
                    _clipWeights[clip] *= labelWeights[label]
                    matchedClips.append(clip)

        # replace all unmatched clip weights with the else weight
        if elseWeight != None:  
            newWeights = OrderedDict.fromkeys(_clipWeights, elseWeight)
            for clip in matchedClips:
                newWeights[clip] = _clipWeights[clip]
            _clipWeights = newWeights.copy()

        # remove all instances of 0s
        newWeights = OrderedDict()
        for k,v in _clipWeights:
            if v > 0:
                newWeights[k] = v

        return newWeights


    def setPriority(self, _priority):
        """Sets the priority of this criteria. Higher priority criteria are used first for scheduling clips.
        
        If multiple criteria exist with the same priority, they are used in declaration order.
        @param _priority: Integer indicating what order this criteria should be used by the scheduler.
        """
        self._m_priority = 0

    def setChoiceTime(self, _startTimeSec):
        """Specifies that a single clip matching this criteria should be chosen and shown at the specified time.
        
        @param _startTimeSec: Add the chosen clip at this time, or the nearest available time thereafter.
        @returns: self
        """
        self._m_chooseOnlyOnce = True
        self._m_startTimeSec = _startTimeSec
        self._m_endTimeSec = 0
        self._m_reoccurFreqSec = 0
        self._m_randomSec = 0
        return self


    def setChoiceTimeframe(self, _startTimeSec, _endTimeSec, _reoccurFreqSec=0, _randomSec=0):
        """Specifies the timeline timespan during which the clips matching this criteria may be added.
        
        @param _startTimeSec: Add the chosen clips at this time, or the nearest available time thereafter.
        @param _endTimeSec: Don't add any clips past this time.
        @param _reoccurFreqSec: Add subsequent clips this many seconds after the previous clip was started.
        @param _randomSec: Add a random number of seconds to the reoccur time, up to _randomSec.
        @returns: self
        """
        self._m_chooseOnlyOnce = False
        self._m_startTimeSec = _startTimeSec
        self._m_endTimeSec = _endTimeSec
        self._m_reoccurFreqSec = _reoccurFreqSec
        self._m_randomSec = _randomSec
        return self
    
    def setLabelWeights(self, _labelWeightDict):
        """When choosing clips to play, the listed labels should have their probability weight
        adjusted by the specified amounts. When multiple weights match one clip, their values are multiplied.
        All clips are weighted 1.0 until otherwise matched.

        Using the label "else" will apply the specified weight to all clips not matched specifically.
        Values greater than 0 and less than 1 only matter when using chooseRandomlyByOccuranceWindow.

        @param _labelWeightDict: Dictionary mapping label strings to their assigned weights.
        """
        self._m_labelWeightsDict = _labelWeightDict

    def chooseOrdered(self, _backwards=False):
        """Clips are chosen in the order that they are provided to the scheduler, or in backwards order.

        Any weights specified with setLabelWeights are applied before choosing clips, and any clips with a 
        weight of 0 are skipped.

        @param _backwards: Choose clips starting with the last clip in the scheduler and working towards the
        first. Default: False
        """
        self._m_chooseRandomly = False
        self._m_chooseBackwards = _backwards

    def chooseRandomlyByOccuranceWindow(self, _windowPct=0, _weightCurve=0):
        """Clips are chosen based on how far the scheduler has progressed in the choice timeframe (set with 
        setChoiceTimeframe) compared to when the clip occurred in the original source media.

        @param _windowPct: If non-zero, clips will be randomly chosen for the timeline so long as they are
        no more than _windowPct different from the scheduler's current progress percentage for the criterea.
        This random choice will take into account the weights specified with setLabelWeights.
        If set to 0, the clips will not be randomly chosen. Instead, the scheduler will identify the clip with
        the nearest occurrence percentage and attempt to schedule it for play at the nearest possible opportunity.
        Default: 0

        @param _weightCurve: If non-zero, the clips in the window will have their weights adjusted based on how
        far they are from the scheduler's current criteria progress. This weight is applied in a circular curve 
        starting at 0 at the edges of the window and approaching 1 at the center of the window.
        A curve of 1 is completely curved (only 1 at the very center of the window) and steepest at the edges of
        the window, resembling a semi-circle.
        A curve less than one will plateau at the center of the window.
        A curve of zero is completely flat and is weighted 1.0 throughout the window and 0.0 outside it.
        A negative curve will approach the center in a concave, asymptotic fashion such that it's steepest at
        the center of the window approaching 1 and flattest at the edges of the window approaching 0.
        """
        self._m_chooseRandomly = True
        self._m_windowPct = _windowPct
        self._m_weightCurve = _weightCurve

    def allowPlayBehind(self, _startBehind, _endBehind):
        
