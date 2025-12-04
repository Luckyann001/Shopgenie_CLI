import click
from shopgenie.menus.menu import main_menu
from shopgenie.services.user_service import UserService
from shopgenie.services.template_service import TemplateService
from shopgenie.services.category_service import CategoryService

@click.command()
def start():
    while True:
        choice = main_menu()

        if choice == "1":
            name = input("Enter name: ")
            role = input("Role (developer/entrepreneur): ")
            UserService.create_user(name, role)
            print("User created!")

        elif choice == "2":
            for u in UserService.list_users():
                print(u)

        elif choice == "3":
            prompt = input("Enter prompt: ")
            content = TemplateService.generate_from_prompt(prompt)
            print("\nGenerated Template:")
            print(content)

        elif choice == "4":
            for t in TemplateService.list_templates():
                print(t)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
