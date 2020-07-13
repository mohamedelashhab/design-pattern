from visitor.Operation import Operation


class PlaintextOperation(Operation):
    def apply(self, node) -> None:
        print("Plaintext-{}".format(node.__class__.__name__))
