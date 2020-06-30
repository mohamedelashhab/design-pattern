from memento.Editor import Editor
from memento.History import History


if __name__ == '__main__':
    editor   = Editor()
    history  = History()

    editor.content = "a"
    history.push(editor.createState())

    editor.content = "b"
    history.push(editor.createState())

    editor.content = "c"
    history.push(editor.createState())
    editor.restore(history.pop())
    editor.restore(history.pop())

    print(repr(editor.content))

