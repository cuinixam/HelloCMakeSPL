from typing import Callable


class TextGenerator:
    def __init__(self, *, generator: Callable[[], str] = None, content: str = ''):
        self.generator = generator if generator else TextGenerator.make_generator(content)

    def update_content(self, new_content: str):
        self.generator = self.make_generator(new_content)

    def generate_text(self) -> str:
        return self.generator()

    @staticmethod
    def make_generator(content: str) -> Callable[[], str]:
        def generator() -> str:
            return content or ''

        return generator
