from app import db, create_app
from app.models import User
from app.models import Role
from app.models import Menu
from app.models import SubMenu


def seed_menu():
    app = create_app()
    with app.app_context():
        count = Menu.query.count()
        if count>0:
            print(f'There are {count} records in Menu Table.')
        else:
            m1 = Menu(code = "m001", name = "Admin", icon='<i class="bi bi-gear-fill"></i>',order = 1)
            m2 = Menu(code = "m002", name = "Auth", icon='<i class="bi bi-person-square"></i>',order = 2)
            db.session.add_all([m1,m2])
            db.session.commit()
            print(f'Menu added.')

def see_submenu():
    app = create_app()
    with app.app_context():
        count = SubMenu.query.count()
        if count>0:
            print(f"There are {count} records in SubMenu table.")
        else:
            s1 = SubMenu(code="s001",admin_menu_id=1, name="Menu", icon='<i class="bi bi-file-earmark"></i>', end_point="admin_bp.menu_bp.index", order = 1)
            s2 = SubMenu(code="s002",admin_menu_id=2, name="Change password", icon='<i class="bi bi-file-earmark"></i>', end_point="auth_bp.password_bp.change_password", order = 2)
            db.session.add_all([s1,s2])
            db.session.commit()
            print(f"SubMenu added.")

def seed_role():
    app = create_app()
    with app.app_context():
        role_count = Role.query.count()
        if role_count>0:
            print(f"There are {role_count} records in the AuthRole table.")
        else:
            role = Role(name = "admin")
            db.session.add(role)
            db.session.commit()
            print("Admin role added.")
def seed_users():
    app = create_app()
    with app.app_context():
        user_count = User.query.count()
        if user_count > 0:
            print(f"There are {user_count} records in the User table.")
        else:
            print("Seeding User table")
            # Create multiple user instances
            user1 = User(username='admin', auth_role_id=1, password='', email='admin@ihub.science')
            user1.set_password('Rupp2357.!')

            user2 = User(username='bunchhun', auth_role_id=1,password='', email='bunchhun@ihub.science')
            user2.set_password('Rupp2357.!')

            # Add multiple users to the session
            db.session.add_all([user1, user2])

            # Commit the session to the database
            db.session.commit()

            print("Multiple users inserted successfully.")
            
if __name__ == "__main__":
    seed_menu()
    see_submenu()
    seed_role()
    seed_users()