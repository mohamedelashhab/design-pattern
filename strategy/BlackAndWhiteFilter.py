from strategy.Filter import Filter


class BlackAndWhiteFilter(Filter):
    def apply(self, fileName: str) -> None:
        print("Applying B&W filter on {}".format(fileName))