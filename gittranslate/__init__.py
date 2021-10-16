from .documents import PandocConverterService

result = PandocConverterService.convert_text(source='<h1>Lol</h1>', input_format='html', output_format='markdown')
print(result)
