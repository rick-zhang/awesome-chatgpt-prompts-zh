import json
from jinja2 import Template
import constants
from prompts_zh_input import data

template_str = '''
[{% for item in items %}
  {
    "act": {{ item.act | tojson }},
    "prompt": {{ (
        item.prompt
        + (("\\n" + avoid_introductory) if item.avoid_introductory else "")
        + (("\\n" + scientific_format) if item.scientific_format_on else "")
        + (("\\n" + common_format) if item.common_format_on else "")
        + (("\\n" + below_h3_title) if item.below_h3_title_on else "")
        + (("\\n" + table_format) if item.table_format_on else "")
        + (("\\n" + diagram_format) if item.diagram_format_on else "")
        + (("\\n" + use_chinese) if item.use_chinese else "")
        + (("\\n" + use_english) if item.use_english else "")
        + (("\\n" + continue_generating) if item.continue_generating else "")
    ) | tojson }},
    {% if item.cmd %}
    "cmd": {{ item.cmd | tojson }},
    {% endif %}
    {% if item.enable %}
    "enable": {{ item.enable | tojson }},
    {% endif %}
    "tags": ["user-sync"]
  }{% if not loop.last %},{% endif %}{% endfor %}
]'''

template = Template(template_str)
rendered_output = template.render(items=data, **constants.__dict__)

# 将 JSON 转换为 Python 字典，然后保存为 JSON，确保格式正确
with open('prompts-zh-output.json', 'w', encoding='utf-8') as f:
    json.dump(json.loads(rendered_output), f, indent=2, ensure_ascii=False)
