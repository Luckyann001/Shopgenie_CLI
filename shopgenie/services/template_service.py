from shopgenie.database.config import session
from shopgenie.models.template import Template

class TemplateService:

    @staticmethod
    def create_template(name, content, category_id, user_id):
        template = Template(
            name=name,
            content=content,
            category_id=category_id,
            user_id=user_id
        )
        session.add(template)
        session.commit()
        return template

    @staticmethod
    def list_templates():
        return session.query(Template).all()

    @staticmethod
    def generate_from_prompt(prompt):
        # Very simple AI logic for MVP
        return f"AI-Generated Layout for: {prompt}"
