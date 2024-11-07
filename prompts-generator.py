import json
from jinja2 import Template
import constants
from prompts_zh_input import data

template_str = '''
[{% for item in items %}
  {
    "act": "{{ item.act }}",
    "prompt": "\
{{ item.prompt }}\
{% if item.avoid_introductory %}\\n{{ avoid_introductory }}{% endif %}\
{% if item.scientific_format_on%}\\n{{ scientific_format }}{% endif %}\
{% if item.common_format_on %}\\n{{ common_format }}{% endif %}\
{% if item.table_format_on %}\\n{{ table_format }}{% endif %}\
{% if item.use_chinese %}\\n{{ use_chinese }}{% endif %}\
{% if item.use_english %}\\n{{ use_english }}{% endif %}\
{% if item.continue_generating %}\\n{{ continue_generating }}{% endif %}\
",
    {% if item.cmd %}
    "cmd": "{{ item.cmd }}",
    {% endif %}
    {% if item.enable %}
    "enable": {{ item.enable | tojson }},
    {% endif %}
    "tags": [
        "user-sync"
    ]
  }{% if not loop.last %},{% endif %}{% endfor %}
]'''

template = Template(template_str)
rendered_output = template.render(items=data, **constants.__dict__)

with open('prompts-zh-output.json', 'w', encoding='utf-8') as f:
    json.dump(json.loads(rendered_output), f, indent=2, ensure_ascii=False)
