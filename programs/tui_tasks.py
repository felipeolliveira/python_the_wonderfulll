import os
from typing import Callable

tasks: list[dict[str, str | bool]] = []

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BG_BLUE = "\033[44m"
BG_GREEN = "\033[42m"
BG_RED = "\033[41m"


def print_header(text: str, color: str = CYAN) -> None:
    """Prints a stylized header"""
    width = 60
    print(f"\n{color}{BOLD}{'═' * width}{RESET}")
    print(f"{color}{BOLD}║{text.center(width - 2)}║{RESET}")
    print(f"{color}{BOLD}{'═' * width}{RESET}\n")


def print_box(text: str, color: str = BLUE) -> None:
    """Prints a stylized box"""
    width = 60
    print(f"{color}{'─' * width}{RESET}")
    print(f"{color}│{RESET} {text}")
    print(f"{color}{'─' * width}{RESET}")


def add_task() -> None:
    list_tasks()
    print_header("➕ ADICIONAR TAREFA", GREEN)
    name = input(f"{CYAN}📝 Digite o nome da tarefa: {RESET}")
    task: dict[str, str | bool] = {"name": name, "completed": False}
    tasks.append(task)
    print(f"\n{GREEN}✓ Tarefa adicionada com sucesso!{RESET}")


def list_tasks() -> None:
    clear_terminal()
    print_header("📋 Tarefas", MAGENTA)

    if not tasks:
        print(f"{YELLOW}⚠ Nenhuma tarefa encontrada.{RESET}\n")
    else:
        completed_count = sum(1 for task in tasks if task["completed"])
        total_count = len(tasks)

        print(
            f"{CYAN}Total: {BOLD}{total_count}{RESET}{CYAN} | Concluídas: {BOLD}{completed_count}{RESET}{CYAN} | Pendentes: {BOLD}{total_count - completed_count}{RESET}\n"
        )

        for index, task in enumerate(tasks):
            if task["completed"]:
                status = f"{GREEN}✓{RESET}"
                task_color = f"{GREEN}"
                task_name = f"{task['name']}"
            else:
                status = f"{RED}✗{RESET}"
                task_color = f"{WHITE}"
                task_name = f"{task['name']}"

            print(
                f"{BLUE}{index + 1:2d}.{RESET} {status} {task_color}{task_name}{RESET}"
            )


def complete_task() -> None:
    list_tasks()
    print(f"\n{print_header('✅ CONCLUIR TAREFA', GREEN)}")
    position = int(input(f"{CYAN}Digite a posição da tarefa: {RESET}"))
    if 0 <= position - 1 < len(tasks):
        tasks[position - 1]["completed"] = True
        print(f"\n{GREEN}✓ Tarefa marcada como concluída!{RESET}")
    else:
        print(f"\n{RED}✗ Posição inválida!{RESET}")


def update_task() -> None:
    list_tasks()
    print(f"\n{print_header('✏️  ATUALIZAR TAREFA', YELLOW)}")
    position = int(input(f"{CYAN}Digite a posição da tarefa: {RESET}"))
    new_name = input(f"{CYAN}Digite o novo nome: {RESET}")
    if 0 <= position - 1 < len(tasks):
        tasks[position - 1]["name"] = new_name
        print(f"\n{GREEN}✓ Tarefa atualizada com sucesso!{RESET}")
    else:
        print(f"\n{RED}✗ Posição inválida!{RESET}")


def delete_task() -> None:
    list_tasks()
    print(f"\n{print_header('🗑️  DELETAR TAREFA', RED)}")
    position = int(input(f"{CYAN}Digite a posição da tarefa: {RESET}"))
    if 0 <= position - 1 < len(tasks):
        del tasks[position - 1]
        print(f"\n{GREEN}✓ Tarefa deletada com sucesso!{RESET}")
    else:
        print(f"\n{RED}✗ Posição inválida!{RESET}")


def clear_completed_tasks() -> None:
    for index in range(0, len(tasks) - 1):
        if tasks[index]["completed"]:
            del tasks[index]
    print(f"\n{GREEN}✓ Tarefas concluídas removidas!{RESET}")


def list_commands() -> None:
    print(f"\n{CYAN}{BOLD}{'─' * 60}{RESET}")

    for key, value in available_commands.items():
        print(f"  {YELLOW}{BOLD}[{key}]{RESET} {value[2]} {WHITE}{value[0]}{RESET}")

    print()
    print(f"  {CYAN}{BOLD}Press CTRL-C to Exit{RESET}")
    print(f"{CYAN}{BOLD}{'─' * 60}{RESET}\n")


def clear_terminal() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def bye() -> None:
    print(f"\n{CYAN}{BOLD}👋 Saindo do Gerenciador de Tarefas. Até logo!{RESET}\n")
    exit()


def invalid_command() -> None:
    print(f"\n{RED}{BOLD}✗ Comando inválido!{RESET} Por favor, tente novamente.\n")
    input(f"{YELLOW}Pressione Enter para continuar...{RESET}")
    clear_terminal()


available_commands: dict[int, tuple[str, Callable, str]] = {
    0: ("Listar Comandos", list_commands, "📜"),
    1: ("Adicionar Tarefa", add_task, "➕"),
    2: ("Concluir Tarefa", complete_task, "✅"),
    3: ("Atualizar Tarefa", update_task, "✏️"),
    4: ("Deletar Tarefa", delete_task, "🗑️"),
    5: ("Limpar Tarefas Concluídas", clear_completed_tasks, "🧹"),
}

available_commands_list: list[int] = list(available_commands.keys())
first_command: int = available_commands_list[0]
last_command: int = available_commands_list[-1]

clear_terminal()

while True:
    try:
        list_tasks()
        list_commands()
        input_command = input(
            f"\n{BOLD}{GREEN}➜{RESET} Digite o comando ({YELLOW}{first_command}-{last_command}{RESET}): "
        )
        input_command = int(input_command)

        if input_command < first_command or input_command > last_command:
            invalid_command()
            continue

        command = available_commands.get(input_command)
        if command is not None:
            command[1]()

    except ValueError:
        invalid_command()

    except KeyboardInterrupt:
        bye()

    except Exception as e:
        clear_terminal()
        print(f"\n{RED}{BOLD}⚠ Ocorreu um erro: {e}{RESET}\n")
        input(f"{YELLOW}Pressione Enter para continuar...{RESET}")
        clear_terminal()
