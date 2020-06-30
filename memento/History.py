from memento.EditorState import EditorState



class History():
    def __init__(self) -> None:
        self.__states = []

    def push(self, state: EditorState) -> None:
        self.__states.append(state)

    def pop(self) -> EditorState:
        if len(self.__states) > 1:
            last_state = self.__states.pop()
            return last_state
        elif len(self.__states) == 1:
            return self.__states[0]
        return None

