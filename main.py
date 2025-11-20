import random
import tkinter as tk
from tkinter import ttk


class PowerballGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Powerball Generator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Configure styles
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=10)
        style.configure("Title.TLabel", font=("Arial", 16, "bold"), foreground="blue")
        style.configure(
            "Numbers.TLabel", font=("Arial", 14, "bold"), foreground="darkgreen"
        )

        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Title
        title_label = ttk.Label(
            main_frame, text="Powerball Generator", style="Title.TLabel"
        )
        title_label.pack(pady=(0, 15))

        # Main numbers label
        main_label = ttk.Label(main_frame, text="Main Numbers:", font=("Arial", 12))
        main_label.pack(anchor=tk.W, pady=5)

        # Main numbers display
        self.main_numbers_var = tk.StringVar()
        main_display = ttk.Label(
            main_frame, textvariable=self.main_numbers_var, style="Numbers.TLabel"
        )
        main_display.pack(pady=5)

        # Powerball label
        power_label = ttk.Label(main_frame, text="Powerball:", font=("Arial", 12))
        power_label.pack(anchor=tk.W, pady=5)

        # Powerball display
        self.powerball_var = tk.StringVar()
        power_display = ttk.Label(
            main_frame, textvariable=self.powerball_var, style="Numbers.TLabel"
        )
        power_display.pack(pady=5)

        # Generate button
        generate_button = ttk.Button(
            main_frame, text="Generate Numbers", command=self.generate_numbers
        )
        generate_button.pack(pady=(20, 10))

        # Initialize with first set of numbers
        self.generate_numbers()

    def generate_numbers(self):
        """Generate random Powerball numbers without duplicates"""
        # Generate 5 unique main numbers from 1-69
        main_numbers = random.sample(range(1, 70), 5)
        main_numbers.sort()

        # Generate 1 powerball number from 1-26
        powerball = random.randint(1, 26)

        # Update display
        self.main_numbers_var.set(", ".join(map(str, main_numbers)))
        self.powerball_var.set(str(powerball))


def main():
    root = tk.Tk()
    app = PowerballGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
