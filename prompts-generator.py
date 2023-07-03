import json
from jinja2 import Template
import constants
from prompts_zh_input import data

template_str = '''
[{% for item in items %}
  {
    "act": "{{ item.act }}",
    "prompt": "{{ item.prompt }}\\n{% if item.common_format_on %} {{ common_format }} {% endif %}\\n{% if item.use_chinese %} {{ use_chinese }} {% endif %}\\n{% if item.use_english %} {{ use_english }} {% endif %}",
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
