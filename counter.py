# 动作计数器
class RepetitionCounter(object):

    def __init__(self, class_name, enter_threshold=6, exit_threshold=4):
        self._class_name = class_name

        self._enter_threshold = enter_threshold
        self._exit_threshold = exit_threshold

        self._pose_entered = False

        self._n_repeats = 0

    @property
    def n_repeats(self):
        return self._n_repeats

    def __call__(self, pose_classification):
        pose_confidence = 0.0
        if self._class_name in pose_classification:
            pose_confidence = pose_classification[self._class_name]
        if not self._pose_entered:
            self._pose_entered = pose_confidence > self._enter_threshold
            return self._n_repeats
        if pose_confidence < self._exit_threshold:
            self._n_repeats += 1
            self._pose_entered = False

        return self._n_repeats
