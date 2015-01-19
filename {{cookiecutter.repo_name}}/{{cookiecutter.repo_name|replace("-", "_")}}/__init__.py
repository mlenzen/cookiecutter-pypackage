# -*- coding: utf-8 -*-
"""
{{ cookiecutter.repo_name|replace('-', '_') }}
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.description }}

:copyright: (c) {{ cookiecutter.year }} by {{ cookiecutter.full_name }}
:licence: BSD, see LICENCE for more details
"""
from __future__ import absolute_import, unicode_literals

# Generate your own AsciiArt at:
# patorjk.com/software/taag/#f=Calvin%20S&t={{ cookiecutter.project_name }}
__banner__ = r"""
╦  ╦┌─┐┌┐┌┌─┐┬ ┬┌─┐┬─┐┌┬┐
╚╗╔╝├─┤││││ ┬│ │├─┤├┬┘ ││  by {{ cookiecutter.full_name }}
 ╚╝ ┴ ┴┘└┘└─┘└─┘┴ ┴┴└──┴┘
"""

__title__ = '{{ cookiecutter.repo_name }}'
__summary__ = '{{ cookiecutter.description }}'
__uri__ = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'

__version__ = '{{ cookiecutter.version }}'

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'

__license__ = 'BSD'
__copyright__ = 'Copyright {{ cookiecutter.year }} {{ cookiecutter.full_name }}'
