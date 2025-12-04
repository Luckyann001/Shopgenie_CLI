from shopgenie.utils.formatters import title, line
from shopgenie.services.user_service import UserService
from shopgenie.services.template_service import TemplateService
from shopgenie.services.category_service import CategoryService

def main_menu():
    title("📦 ShopGenie CLI")

    print("1. Register User")
    print("2. List Users")
    print("3. Generate Template (AI)")
    print("4. List Templates")
    print("5. Exit")

    return input("\nChoose an option: ")
