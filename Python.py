#Assalomu alaykum , bu vazifalar ro'yxati dasturi

todo_list = []

def show_menu():
    print("\nVazifa ro'yxati dasturiga xush kelibsiz!")
    print("1. Vazifa qo'shish")
    print("2. Vazifalarni ko'rish")
    print("3. Vazifani o'chirish")
    print("4. Dasturdan chiqish")

def add_task():
    task = input("Yangi vazifa kiriting: ")
    todo_list.append(task)
    print(f'"{task}" vazifasi ro\'yxatga qo\'shildi.')

def view_tasks():
    if not todo_list:
        print("Ro'yxatda hech qanday vazifa yo'q.")
    else:
        print("\nVazifalar ro'yxati:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("O'chirmoqchi bo'lgan vazifa raqamini kiriting: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f'"{removed_task}" vazifasi o\'chirildi.')
        else:
            print("Noto'g'ri raqam kiritildi.")
    except ValueError:
        print("Iltimos, raqam kiriting.")

def main():
    while True:
        show_menu()
        choice = input("Tanlovingizni kiriting (1-4): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Dasturdan chiqmoqda...")
            break
        else:
            print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")

if __name__ == "__main__":
    main()
