import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import qrcode


class QRCodeGeneratorApp:

  def __init__(self, root):
    self.root = root
    self.root.title("SUPANGAT QR Generator")
    self.root.geometry("500x420")
    self.root.resizable(False, False)

    self.file_path = ""
    self.df = None
    self.excel_file = None

    self.create_widgets()

  def create_widgets(self):
    # 1. Pilih File
    frame_file = tk.LabelFrame(
        self.root, text=" 1. Pilih File Excel / CSV ", padx=10, pady=10
    )
    frame_file.pack(fill="x", padx=15, pady=5)

    self.btn_browse = tk.Button(
        frame_file, text="Cari File...", command=self.load_file
    )
    self.btn_browse.pack(side="left")

    self.lbl_file = tk.Label(
        frame_file, text="Belum ada file dipilih", fg="gray", anchor="w"
    )
    self.lbl_file.pack(side="left", fill="x", expand=True, padx=10)

    # 2. Pilih Sheet
    frame_sheet = tk.LabelFrame(
        self.root, text=" 2. Pilih Sheet (Khusus Excel) ", padx=10, pady=10
    )
    frame_sheet.pack(fill="x", padx=15, pady=5)

    self.combo_sheet = ttk.Combobox(frame_sheet, state="disabled")
    self.combo_sheet.pack(fill="x")
    self.combo_sheet.bind("<<ComboboxSelected>>", self.on_sheet_changed)

    # 3 & 4. Pilih Kolom
    frame_cols = tk.LabelFrame(
        self.root, text=" 3 & 4. Pilih Kolom ", padx=10, pady=10
    )
    frame_cols.pack(fill="x", padx=15, pady=5)

    tk.Label(frame_cols, text="Kolom Isi QR Code:").grid(
        row=0, column=0, sticky="w", pady=2
    )
    self.combo_qr_col = ttk.Combobox(frame_cols, state="disabled")
    self.combo_qr_col.grid(row=0, column=1, sticky="ew", padx=5, pady=2)

    tk.Label(frame_cols, text="Kolom Nama File:").grid(
        row=1, column=0, sticky="w", pady=2
    )
    self.combo_name_col = ttk.Combobox(frame_cols, state="disabled")
    self.combo_name_col.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

    frame_cols.columnconfigure(1, weight=1)

    # Tombol Generate
    self.btn_generate = tk.Button(
        self.root,
        text="Generate QR Code",
        bg="#4CAF50",
        fg="white",
        font=("Helvetica", 10, "bold"),
        command=self.generate_qrcodes,
        state="disabled",
    )
    self.btn_generate.pack(pady=15, fill="x", padx=15)

  def load_file(self):
    path = filedialog.askopenfilename(
        title="Pilih File Excel atau CSV",
        filetypes=[
            ("Excel & CSV Files", "*.xlsx *.xls *.csv"),
            ("Excel Files", "*.xlsx *.xls"),
            ("CSV Files", "*.csv"),
        ],
    )
    if not path:
      return

    self.file_path = path
    self.lbl_file.config(text=os.path.basename(path), fg="black")

    # Reset Combobox
    self.combo_sheet.config(state="disabled", values=[])
    self.combo_qr_col.config(state="disabled", values=[])
    self.combo_name_col.config(state="disabled", values=[])

    if path.endswith(".csv"):
      try:
        # Pemutakhiran di sini: otomatis mendeteksi separator/pemisah CSV
        self.df = pd.read_csv(path, sep=None, engine="python")
        self.combo_sheet.set("File CSV (Tanpa Sheet)")
        self.update_column_comboboxes()
      except Exception as e:
        messagebox.showerror("Error", f"Gagal membaca CSV: {e}")
    else:
      try:
        self.excel_file = pd.ExcelFile(path)
        sheets = self.excel_file.sheet_names
        self.combo_sheet.config(state="readonly", values=sheets)
        self.combo_sheet.set(sheets[0])
        self.on_sheet_changed(None)
      except Exception as e:
        messagebox.showerror("Error", f"Gagal membaca Excel: {e}")

  def on_sheet_changed(self, event):
    if self.excel_file:
      selected_sheet = self.combo_sheet.get()
      self.df = pd.read_excel(self.excel_file, sheet_name=selected_sheet)
      self.update_column_comboboxes()

  def update_column_comboboxes(self):
    if self.df is not None:
      columns = list(self.df.columns)
      self.combo_qr_col.config(state="readonly", values=columns)
      self.combo_name_col.config(state="readonly", values=columns)

      if len(columns) > 0:
        self.combo_qr_col.set(columns[0])
        self.combo_name_col.set(
            columns[1] if len(columns) > 1 else columns[0]
        )

      self.btn_generate.config(state="normal")

  def sanitize_filename(self, name):
    return "".join(c for c in str(name) if c.isalnum() or c in (" ", "_", "-")).strip()

  def generate_qrcodes(self):
    qr_col = self.combo_qr_col.get()
    name_col = self.combo_name_col.get()

    if not qr_col or not name_col:
      messagebox.showwarning("Peringatan", "Pilih kedua kolom terlebih dahulu!")
      return

    output_dir = filedialog.askdirectory(
        title="Pilih Folder Penyimpanan QR Code"
    )
    if not output_dir:
      return

    success_count = 0
    total = len(self.df)

    for idx, row in self.df.iterrows():
      qr_data = str(row[qr_col]) if pd.notna(row[qr_col]) else ""
      filename_raw = (
          str(row[name_col]) if pd.notna(row[name_col]) else f"qr_{idx+1}"
      )

      if not qr_data.strip():
        continue

      safe_filename = self.sanitize_filename(filename_raw)
      if not safe_filename:
        safe_filename = f"qr_{idx+1}"

      filepath = os.path.join(output_dir, f"{safe_filename}.png")

      qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=6,
          border=2,
      )

      qr.add_data(qr_data)
      qr.make(fit=True)

      img = qr.make_image(fill_color="black", back_color="white")
      img.save(filepath)
      success_count += 1

    messagebox.showinfo(
        "Selesai",
        f"Berhasil membuat {success_count} dari {total} QR Code tersimpan"
        f" di:\n{output_dir}",
    )


if __name__ == "__main__":
  root = tk.Tk()
  app = QRCodeGeneratorApp(root)
  root.mainloop()