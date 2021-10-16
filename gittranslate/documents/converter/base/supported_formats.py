from typing import Literal

"""
File formats supported by ``pandoc`` for conversion inputs, 
as specified by the command: ``pandoc --list-input-formats``.
"""
InputFormat = Literal['biblatex', 'bibtex', 'commonmark', 'commonmark_x', 'creole', 'csljson', 'csv',
                      'docbook', 'docx', 'dokuwiki', 'epub', 'fb2', 'gfm', 'haddock', 'html', 'ipynb',
                      'jats', 'jira', 'json', 'latex', 'man', 'markdown', 'markdown_github', 'markdown_mmd',
                      'markdown_phpextra', 'markdown_strict', 'mediawiki', 'muse', 'native', 'odt', 'opml',
                      'org', 'rst', 'rtf', 't2t', 'textile', 'tikiwiki', 'twiki', 'vimwiki']

"""
File formats supported by ``pandoc`` for conversion outputs, 
as specified by the command: ``pandoc --list-output-formats``.
"""
OutputFormat = Literal['asciidoc', 'asciidoctor', 'beamer', 'biblatex', 'bibtex', 'commonmark', 'commonmark_x',
                       'context', 'csljson', 'docbook', 'docbook4', 'docbook5', 'docx', 'dokuwiki', 'dzslides',
                       'epub', 'epub2', 'epub3', 'fb2', 'gfm', 'haddock', 'html', 'html4', 'html5', 'icml', 'ipynb',
                       'jats', 'jats_archiving', 'jats_articleauthoring', 'jats_publishing', 'jira', 'json', 'latex',
                       'man', 'markdown', 'markdown_github', 'markdown_mmd', 'markdown_phpextra', 'markdown_strict',
                       'mediawiki', 'ms', 'muse', 'native', 'odt', 'opendocument', 'opml', 'org', 'pdf', 'plain',
                       'pptx', 'revealjs', 'rst', 'rtf', 's5', 'slideous', 'slidy', 'tei', 'texinfo', 'textile',
                       'xwiki', 'zimwiki']
