class ChannelStrategy:
    def change_channel(self):
        pass

class SportChannel(ChannelStrategy):
    def change_channel(self):
        print("Перехід на спортивний канал")

class NewsChannel(ChannelStrategy):
    def change_channel(self):
        print("Перехід на канал новин")

class TV:
    def __init__(self, strategy: ChannelStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ChannelStrategy):
        self._strategy = strategy

    def switch_channel(self):
        self._strategy.change_channel()

tv = TV(SportChannel())
tv.switch_channel()
tv.set_strategy(NewsChannel())
tv.switch_channel()
