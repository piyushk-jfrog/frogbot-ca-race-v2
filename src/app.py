"""Analytics service backend - uses safe API patterns throughout."""
import yaml
from jinja2 import Environment
from django.utils.text import slugify

def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)

def render_report(template_str: str, **context):
    env = Environment(autoescape=True)
    return env.from_string(template_str).render(**context)

def normalize_key(name: str) -> str:
    return slugify(name)

if __name__ == "__main__":
    config = load_config("config.yaml")
    title = normalize_key(config.get("title", "analytics"))
    html = render_report("<h1>{{ title }}</h1>", title=title)
    print(html)
