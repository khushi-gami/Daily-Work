import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from abc import ABC, abstractmethod

# ----------------------------------- Colors -----------------------------------
BG = "#f1f5f9"
SIDEBAR = "#1e293b"
PRIMARY = "#f97316"
GREEN = "#16a34a"
RED = "#dc2626"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GRAY = "#64748b"
WHITE = "#ffffff"


# ----------------------------------- OOP Classes -----------------------------------
class MenuItem(ABC):
    def __init__(self, name, item_id, price):
        self.name = name
        self.item_id = item_id
        self.__price = price
        self.__is_available = True

    def get_price(self):
        return self.__price

    def get_is_available(self):
        return self.__is_available

    def set_is_available(self, is_available):
        self.__is_available = is_available

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def item_type(self):
        pass

    def status_text(self):
        return "Available" if self.get_is_available() else "Ordered"


class FoodItem(MenuItem):
    def __init__(self, name, item_id, price, spice_level, is_vegetarian):
        super().__init__(name, item_id, price)
        self.spice_level = spice_level
        self.is_vegetarian = is_vegetarian

    def item_type(self):
        return "Food"

    def short_details(self):
        return f"Spice: {self.spice_level} | Veg: {self.is_vegetarian}"

    def display(self):
        return (
            "---- Food Item Details ----\n\n"
            f"Name         : {self.name}\n"
            f"Item ID      : {self.item_id}\n"
            f"Price        : Rs. {self.get_price():.2f}\n"
            f"Spice Level  : {self.spice_level}\n"
            f"Vegetarian   : {self.is_vegetarian}\n"
            f"Status       : {self.status_text()}"
        )


class Colddrink(MenuItem):
    def __init__(self, name, item_id, price, volume_ml, is_alcoholic):
        super().__init__(name, item_id, price)
        self.volume_ml = volume_ml
        self.is_alcoholic = is_alcoholic

    def item_type(self):
        return "Cold Drink"

    def short_details(self):
        return f"{self.volume_ml} ml | Alcoholic: {self.is_alcoholic}"

    def display(self):
        return (
            "---- Cold Drink Details ----\n\n"
            f"Name         : {self.name}\n"
            f"Item ID      : {self.item_id}\n"
            f"Price        : Rs. {self.get_price():.2f}\n"
            f"Volume (ml)  : {self.volume_ml}\n"
            f"Alcoholic    : {self.is_alcoholic}\n"
            f"Status       : {self.status_text()}"
        )


# ----------------------------------- GUI App -----------------------------------
class RestaurantApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurant Management System")
        self.geometry("1100x650")
        self.minsize(950, 580)
        self.configure(bg=BG)

        self.items = {}  # item_id -> MenuItem
        self._setup_style()
        self._build_header()
        self._build_sidebar()
        self._build_menu_table()
        self._build_bill_panel()
        self._build_statusbar()
        self.refresh()

    # ---------- styling ----------
    def _setup_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", rowheight=32, font=("Segoe UI", 10),
                        background=WHITE, fieldbackground=WHITE, borderwidth=0)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"),
                        background=PRIMARY, foreground=WHITE, relief="flat")
        style.map("Treeview.Heading", background=[("active", "#ea580c")])
        style.map("Treeview", background=[("selected", "#fed7aa")],
                  foreground=[("selected", "#000000")])

    def _build_header(self):
        header = tk.Frame(self, bg=PRIMARY, height=70)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(header, text="🍽  Restaurant Management System", bg=PRIMARY, fg=WHITE,
                 font=("Segoe UI", 20, "bold")).pack(side="left", padx=25)
        tk.Label(header, text="Python OOP Project", bg=PRIMARY, fg="#ffedd5",
                 font=("Segoe UI", 11)).pack(side="right", padx=25)

    def _make_button(self, parent, text, color, command):
        btn = tk.Button(parent, text=text, command=command, bg=color, fg=WHITE,
                        activebackground=color, activeforeground=WHITE,
                        font=("Segoe UI", 11, "bold"), relief="flat", bd=0,
                        cursor="hand2", anchor="w", padx=18, pady=10)
        btn.pack(fill="x", padx=15, pady=6)
        btn.bind("<Enter>", lambda e: btn.config(bg=self._shade(color)))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))
        return btn

    @staticmethod
    def _shade(hex_color):
        r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
        r, g, b = (max(0, int(c * 0.85)) for c in (r, g, b))
        return f"#{r:02x}{g:02x}{b:02x}"

    def _build_sidebar(self):
        side = tk.Frame(self, bg=SIDEBAR, width=250)
        side.pack(side="left", fill="y")
        side.pack_propagate(False)
        tk.Label(side, text="OPERATIONS", bg=SIDEBAR, fg="#94a3b8",
                 font=("Segoe UI", 10, "bold")).pack(pady=(25, 10))

        self._make_button(side, "🍛  Add Food Item", GREEN, lambda: self.add_item("food"))
        self._make_button(side, "🥤  Add Cold Drink", BLUE, lambda: self.add_item("drink"))
        self._make_button(side, "🛒  Place Order", PRIMARY, self.place_order)
        self._make_button(side, "❌  Cancel Order", RED, self.cancel_order)
        self._make_button(side, "📋  Show Details", PURPLE, self.show_details)
        self._make_button(side, "🚪  Exit", GRAY, self.on_exit)

    def _build_menu_table(self):
        center = tk.Frame(self, bg=BG)
        center.pack(side="left", fill="both", expand=True, padx=(20, 10), pady=20)

        tk.Label(center, text="Menu Items", bg=BG, fg=SIDEBAR,
                 font=("Segoe UI", 15, "bold")).pack(anchor="w", pady=(0, 8))

        cols = ("id", "name", "type", "price", "details", "status")
        self.tree = ttk.Treeview(center, columns=cols, show="headings", selectmode="browse")
        widths = {"id": 70, "name": 150, "type": 90, "price": 80, "details": 200, "status": 90}
        for c in cols:
            self.tree.heading(c, text=c.title())
            self.tree.column(c, width=widths[c], anchor="center")
        self.tree.tag_configure("available", background="#dcfce7")
        self.tree.tag_configure("ordered", background="#fee2e2")
        self.tree.pack(side="left", fill="both", expand=True)

        sb = ttk.Scrollbar(center, orient="vertical", command=self.tree.yview)
        sb.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.bind("<Double-1>", lambda e: self.show_details())

    def _build_bill_panel(self):
        right = tk.Frame(self, bg=WHITE, width=280, highlightbackground="#e2e8f0",
                         highlightthickness=1)
        right.pack(side="right", fill="y", padx=(10, 20), pady=20)
        right.pack_propagate(False)

        tk.Label(right, text="🧾  Current Bill", bg=SIDEBAR, fg=WHITE,
                 font=("Segoe UI", 14, "bold"), pady=10).pack(fill="x")

        self.bill_box = tk.Text(right, bg=WHITE, fg=SIDEBAR, font=("Consolas", 10),
                                relief="flat", state="disabled", padx=12, pady=10)
        self.bill_box.pack(fill="both", expand=True)

        self.total_label = tk.Label(right, text="Total : Rs. 0.00", bg=PRIMARY, fg=WHITE,
                                    font=("Segoe UI", 14, "bold"), pady=12)
        self.total_label.pack(fill="x")

    def _build_statusbar(self):
        self.status = tk.Label(self, text="Welcome! Add a menu item to begin.", bg=SIDEBAR,
                               fg="#e2e8f0", anchor="w", padx=15, font=("Segoe UI", 10))
        self.status.pack(side="bottom", fill="x")

    # ---------- helpers ----------
    def set_status(self, msg):
        self.status.config(text=msg)

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        for it in self.items.values():
            tag = "available" if it.get_is_available() else "ordered"
            self.tree.insert("", "end", iid=it.item_id, tags=(tag,),
                             values=(it.item_id, it.name, it.item_type(),
                                     f"{it.get_price():.2f}", it.short_details(),
                                     it.status_text()))

        ordered = [i for i in self.items.values() if not i.get_is_available()]
        total = sum(i.get_price() for i in ordered)

        self.bill_box.config(state="normal")
        self.bill_box.delete("1.0", "end")
        if not ordered:
            self.bill_box.insert("end", "No orders yet.")
        for i in ordered:
            self.bill_box.insert("end", f"{i.name[:16]:<16} {i.get_price():>8.2f}\n")
        self.bill_box.config(state="disabled")
        self.total_label.config(text=f"Total : Rs. {total:.2f}")

    def get_target_item(self, action):
        """Selected row ya Item ID poochh kar item return karta hai."""
        if not self.items:
            messagebox.showwarning("No Items", "No any item is added..")
            return None
        sel = self.tree.selection()
        item_id = sel[0] if sel else simpledialog.askstring(
            action, f"Enter Item ID to {action.lower()} :", parent=self)
        if not item_id:
            return None
        item = self.items.get(item_id.strip())
        if item is None:
            messagebox.showerror("Not Found", "This Item ID does not Exist..!!")
        return item

    # ---------- actions ----------
    def add_item(self, kind):
        win = tk.Toplevel(self)
        win.title("Add Food Item" if kind == "food" else "Add Cold Drink")
        win.configure(bg=WHITE)
        win.resizable(False, False)
        win.grab_set()

        color = GREEN if kind == "food" else BLUE
        tk.Label(win, text="🍛 Food Item" if kind == "food" else "🥤 Cold Drink",
                 bg=color, fg=WHITE, font=("Segoe UI", 14, "bold"),
                 pady=10).grid(row=0, column=0, columnspan=2, sticky="ew")

        fields = [("Item Name", "name"), ("Item ID", "id"), ("Price", "price")]
        if kind == "food":
            fields += [("Spice Level", "spice"), ("Is Vegetarian", "extra")]
        else:
            fields += [("Volume (ml)", "volume"), ("Is Alcoholic", "extra")]

        widgets = {}
        for r, (label, key) in enumerate(fields, start=1):
            tk.Label(win, text=label, bg=WHITE, font=("Segoe UI", 10, "bold"),
                     anchor="w").grid(row=r, column=0, padx=20, pady=8, sticky="w")
            if key == "spice":
                w = ttk.Combobox(win, values=["Mild", "Medium", "Hot"], state="readonly", width=23)
                w.set("Medium")
            elif key == "extra":
                w = ttk.Combobox(win, values=["yes", "no"], state="readonly", width=23)
                w.set("no")
            else:
                w = ttk.Entry(win, width=26)
            w.grid(row=r, column=1, padx=20, pady=8)
            widgets[key] = w

        def save():
            name = widgets["name"].get().strip()
            item_id = widgets["id"].get().strip()
            if not name or not item_id:
                messagebox.showerror("Error", "Name and Item ID are required.", parent=win)
                return
            if item_id in self.items:
                messagebox.showerror("Error", "This Item ID already exists.", parent=win)
                return
            try:
                price = float(widgets["price"].get())
                if price < 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Enter a valid price.", parent=win)
                return

            if kind == "food":
                item = FoodItem(name, item_id, price, widgets["spice"].get(),
                                widgets["extra"].get())
            else:
                try:
                    volume = int(widgets["volume"].get())
                except ValueError:
                    messagebox.showerror("Error", "Enter a valid volume.", parent=win)
                    return
                item = Colddrink(name, item_id, price, volume, widgets["extra"].get())

            self.items[item_id] = item
            self.refresh()
            self.set_status(f"{item.item_type()} created : {name} (ID {item_id})")
            win.destroy()

        tk.Button(win, text="Save Item", command=save, bg=color, fg=WHITE,
                  font=("Segoe UI", 11, "bold"), relief="flat", cursor="hand2",
                  pady=8).grid(row=len(fields) + 1, column=0, columnspan=2,
                               sticky="ew", padx=20, pady=18)

    def place_order(self):
        item = self.get_target_item("Order")
        if item is None:
            return
        if item.get_is_available():
            item.set_is_available(False)
            self.refresh()
            self.set_status(f"Order placed for {item.name} ({item.item_id}).")
        else:
            messagebox.showinfo("Already Ordered", f"{item.name} is already ordered.")

    def cancel_order(self):
        item = self.get_target_item("Cancel")
        if item is None:
            return
        if not item.get_is_available():
            item.set_is_available(True)
            self.refresh()
            self.set_status(f"Order cancelled for {item.name} ({item.item_id}).")
        else:
            messagebox.showinfo("Not Ordered", f"{item.name} is not currently ordered.")

    def show_details(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Select Item", "Please select an item from the menu first.")
            return
        messagebox.showinfo("Item Details", self.items[sel[0]].display())

    def on_exit(self):
        if messagebox.askyesno("Exit", "Exiting the Programme. Goodbye!\n\nDo you want to exit?"):
            self.destroy()


if __name__ == "__main__":
    RestaurantApp().mainloop()