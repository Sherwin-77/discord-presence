import pypresence

import asyncio
import json
import time


# change below for other json path
JSON_PATH = "config.json"


# TODO: Implement this with tkinter
class App:
    def __init__(self, loop):
        self.loop = loop

        self.setting: dict = {}
        self.client_id = None
        self.presence = None

    def load_setting(self) -> None:
        with open(JSON_PATH) as f:
            self.setting = json.load(f)
        self.client_id = self.setting.get("client_id", None)

    def update_presence(self) -> None:
        # Modify from this code if you want instead of using config json
        self.presence.update(
            state=self.setting.get("state", None),
            details=self.setting.get("details", None),
            start=self.setting.get("start", time.time()),
            large_image=self.setting.get("large_image", None),
            large_text=self.setting.get("large_text", None),
            small_image=self.setting.get("small_image", None),
            small_text=self.setting.get("small_text", None),
            party_size=self.setting.get("party_size", None),
            buttons=[self.setting.get("button_1", None), self.setting.get("button_2", None)]
        )

    def connect(self) -> None:
        if self.presence is None:
            self.presence = pypresence.Presence(self.client_id, loop=self.loop)
        self.presence.connect()

    def close(self) -> None:
        self.presence.close()


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = App(loop=loop)
    app.load_setting()
    app.connect()
    print("Connected!")

    while True:
        app.update_presence()
        time.sleep(30)


if __name__ == '__main__':
    main()
