import pypandoc

from . import ConverterService, InputFormat, OutputFormat


class PandocConverterService(ConverterService):
    @staticmethod
    def convert_text(*, source: str, input_format: InputFormat, output_format: OutputFormat) -> str:
        return pypandoc.convert_text(source=source, format=input_format, to=output_format)
