import functions
import time

now = time.strftime("%b %d, %Y %I:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()  # removes input whitespace

    # if 'add' in user_action or 'new' in user_action:
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"  # splice after 'add' till the end

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)
    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index + 1} - {todo}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            start_index = 0
            end_index = len(todos) - 1

            if number < start_index or number > end_index:
                raise IndexError()

            new_todo = input("Enter new todo text: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Enter a number to edit")
            continue
        except IndexError:
            print(
                f"Please enter a number to edit from {start_index + 1} to {end_index + 1}"
            )
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.get_todos()

            start_index = 0
            end_index = len(todos) - 1

            if number < start_index or number > end_index:
                raise IndexError()

            todo_to_remove = todos.pop(number)

            functions.write_todos(todos)

            print(f"Todo {todo_to_remove.strip('\n')} was removed.")
        except ValueError:
            print("Enter a number to edit")
            continue
        except IndexError:
            print(
                f"Please enter a number to complete from {start_index + 1} to {end_index + 1}"
            )
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
