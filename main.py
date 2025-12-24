
import tkinter as tk
from tkinter import ttk, messagebox
from settings import *
from task_manager import TaskManager

class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        
        # إعدادات الحجم
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+400+50")
        self.resizable(True, True) 
        self.minsize(400, 500)
        self.configure(bg=COLOR_BG)

        # تحميل البيانات
        self.manager = TaskManager()
        self.tasks = self.manager.load_tasks()
        self.show_completed_only = False 

        # بناء الواجهة
        self.setup_ui()
        self.refresh_list()

    def setup_ui(self):
        # --- ستايل السكرول بار (Custom Style) ---
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", 
                        background=COLOR_FRAME, 
                        troughcolor=COLOR_BG,
                        bordercolor=COLOR_BG, 
                        arrowcolor=COLOR_ACCENT,
                        gripcount=0)

        # --- الهيدر ---
        header_frame = tk.Frame(self, bg=COLOR_FRAME, height=90)
        header_frame.pack(fill=tk.X)
        
        lbl_title = tk.Label(header_frame, text="TASK MASTER", font=("Segoe UI", 26, "bold"), 
                             bg=COLOR_FRAME, fg=COLOR_TEXT)
        lbl_title.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # --- منطقة الإدخال ---
        input_frame = tk.Frame(self, bg=COLOR_BG)
        input_frame.pack(pady=20)

        self.entry_task = tk.Entry(input_frame, width=24, font=("Segoe UI", 16), 
                                   bg=COLOR_FRAME, fg=COLOR_TEXT, 
                                   insertbackground=COLOR_ACCENT, bd=0)
        self.entry_task.pack(side=tk.LEFT, ipady=8, padx=10)
        self.entry_task.focus()

        # اختصار: زر Enter للإضافة
        self.entry_task.bind('<Return>', lambda event: self.add_task())

        btn_add = tk.Button(input_frame, text="ADD", font=("Segoe UI", 11, "bold"), 
                            bg=COLOR_ACCENT, fg=COLOR_BG, width=8, bd=0, 
                            cursor="hand2", command=self.add_task)
        btn_add.pack(side=tk.LEFT, ipady=5)
        
        # زر الفلترة
        self.btn_filter = tk.Button(self, text="SHOW DONE", font=("Segoe UI", 10, "bold"), 
                                    bg=COLOR_BG, fg=COLOR_ACCENT, bd=0, 
                                    cursor="hand2", command=self.toggle_view_mode)
        self.btn_filter.pack(pady=(0, 10))

        # --- القائمة (Listbox) ---
        list_frame = tk.Frame(self, bg=COLOR_BG)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        self.listbox = tk.Listbox(list_frame, font=('Segoe UI', 15), 
                                  bg=COLOR_FRAME, fg=COLOR_TEXT, 
                                  selectbackground=COLOR_ACCENT, selectforeground=COLOR_BG,
                                  bd=0, highlightthickness=0, activestyle="none", cursor="hand2")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # اختصار: زر Delete للحذف
        self.listbox.bind('<Delete>', lambda event: self.delete_task())
        # اختصار: دبل كليك لتغيير الحالة
        self.listbox.bind('<Double-1>', self.toggle_task_status)
        # اختصار: كليك يمين للقائمة المختصرة
        self.listbox.bind('<Button-3>', self.show_context_menu)

        # السكرول بار 
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.listbox.yview, style="Vertical.TScrollbar")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # --- قائمة كليك يمين (Context Menu) ---
        self.context_menu = tk.Menu(self, tearoff=0, bg=COLOR_FRAME, fg=COLOR_TEXT, activebackground=COLOR_ACCENT)
        self.context_menu.add_command(label="Toggle Status (Done/Undo)", command=lambda: self.toggle_task_status(None))
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Delete Task", command=self.delete_task)

        # --- زر الحذف السفلي ---
        self.btn_del = tk.Button(self, text="DELETE SELECTED", 
                                 bg=COLOR_DELETE, fg="white", 
                                 font=("Segoe UI", 12, "bold"), bd=0, 
                                 cursor="hand2", command=self.delete_task)
        self.btn_del.pack(side=tk.BOTTOM, pady=30, ipadx=30, ipady=10)

        self.btn_del.bind("<Enter>", lambda e: self.btn_del.configure(bg=COLOR_DELETE_HOVER))
        self.btn_del.bind("<Leave>", lambda e: self.btn_del.configure(bg=COLOR_DELETE))

    def add_task(self):
        text = self.entry_task.get().strip()
        if text:
            new_task = {"text": text, "status": "Pending"}
            self.tasks.append(new_task)
            self.manager.save_tasks(self.tasks)
            self.refresh_list()
            self.entry_task.delete(0, tk.END)

    def toggle_task_status(self, event):
        try:
            if self.show_completed_only:
                messagebox.showinfo("Info", "Switch to 'ALL TASKS' to edit.")
                return

            # لو الاستدعاء جاي من الكيبورد أو الماوس
            if event:
                index = self.listbox.nearest(event.y)
            else:
                index = self.listbox.curselection()[0]

            current_status = self.tasks[index]['status']
            self.tasks[index]['status'] = "Done" if current_status == "Pending" else "Pending"
            
            self.manager.save_tasks(self.tasks)
            self.refresh_list()
        except (IndexError, tk.TclError):
            pass

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            
            # منطق الحذف أثناء الفلترة
            if self.show_completed_only:
                display_text = self.listbox.get(index)
                clean_text = display_text[2:].strip()
                for i, task in enumerate(self.tasks):
                    if task['text'] == clean_text and task['status'] == "Done":
                        self.tasks.pop(i)
                        break
            else:
                self.tasks.pop(index)

            self.manager.save_tasks(self.tasks)
            self.refresh_list()
        except IndexError:
            pass


    def show_context_menu(self, event):
        try:
            # تحديد العنصر اللي تحت الماوس
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(self.listbox.nearest(event.y))
            self.listbox.activate(self.listbox.nearest(event.y))
            
            # التعديل هنا: استخدمنا post بدل tk_popup
            # post بتعرض القائمة بس مش بتعمل "تجميد" للشاشة
            self.context_menu.post(event.x_root, event.y_root)
            
            # التريك: بنقول للبرنامج لو حصل أي "كليك شمال" في أي حتة، شغل دالة الإخفاء
            self.bind('<Button-1>', self.hide_context_menu)
        except:
            pass


    def hide_context_menu(self, event):
        # دالة لإخفاء القائمة
        self.context_menu.unpost()
        
        # بنلغي مراقبة الكليك عشان ميفضلش شغال عالفاضي
        self.unbind('<Button-1>')


    def toggle_view_mode(self):
        self.show_completed_only = not self.show_completed_only
        if self.show_completed_only:
            self.btn_filter.config(text="SHOW ALL", fg=COLOR_COMPLETED)
        else:
            self.btn_filter.config(text="SHOW DONE", fg=COLOR_ACCENT)
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = task['status']
            text = task['text']
            
            if self.show_completed_only and status != "Done":
                continue
            
            icon = ICON_CHECKED if status == "Done" else ICON_UNCHECKED
            display_text = f"{icon} {text}"
            
            self.listbox.insert(tk.END, display_text)
            
            if status == "Done":
                self.listbox.itemconfig(tk.END, {'fg': COLOR_COMPLETED})
            else:
                self.listbox.itemconfig(tk.END, {'fg': COLOR_TEXT})

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()