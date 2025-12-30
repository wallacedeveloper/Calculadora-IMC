"""
Graphical User Interface for BMI Calculator using Tkinter.
"""
import tkinter as tk
from tkinter import messagebox
from .calculator import calcular_imc, classificar_imc


class IMCCalculatorGUI:
    """GUI Application for BMI Calculator."""
    
    def __init__(self, root):
        """Initialize the GUI."""
        self.root = root
        self.root.title("Calculadora de IMC")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create and layout GUI widgets."""
        # Title
        title_label = tk.Label(
            self.root, 
            text="Calculadora de IMC", 
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=20)
        
        # Weight input
        weight_frame = tk.Frame(self.root)
        weight_frame.pack(pady=10)
        
        tk.Label(weight_frame, text="Peso (kg):", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        self.weight_entry = tk.Entry(weight_frame, font=("Arial", 12), width=15)
        self.weight_entry.pack(side=tk.LEFT, padx=5)
        
        # Height input
        height_frame = tk.Frame(self.root)
        height_frame.pack(pady=10)
        
        tk.Label(height_frame, text="Altura (m):", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        self.height_entry = tk.Entry(height_frame, font=("Arial", 12), width=15)
        self.height_entry.pack(side=tk.LEFT, padx=5)
        
        # Calculate button
        calculate_btn = tk.Button(
            self.root,
            text="Calcular IMC",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.calculate_bmi,
            cursor="hand2"
        )
        calculate_btn.pack(pady=20)
        
        # Result label
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            fg="#333"
        )
        self.result_label.pack(pady=10)
    
    def calculate_bmi(self):
        """Calculate and display BMI result."""
        try:
            peso = float(self.weight_entry.get())
            altura = float(self.height_entry.get())
            
            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)
            
            self.result_label.config(
                text=f"Seu IMC é: {imc}\nClassificação: {classificacao}",
                fg="#2196F3"
            )
            
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {e}")


def main():
    """Launch the GUI application."""
    root = tk.Tk()
    app = IMCCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
