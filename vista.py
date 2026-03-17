import tkinter as tk


class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas ")

        self.root.geometry("350x400")
        self.root.config(bg="#f5f5f5")

        self.label = tk.Label(root, text="Mis Tareas 📝", font=("Arial", 14, "bold"), bg="#f5f5f5")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        self.boton_agregar = tk.Button(root, text="Agregar tarea")
        self.boton_agregar.pack(pady=5)

        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.pack(pady=10)

        self.boton_eliminar = tk.Button(root, text="Eliminar tarea")
        self.boton_eliminar.pack(pady=5)
