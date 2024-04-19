import tkinter as tk

# 定义PCI_ECAM_ADDRESS宏
def PCI_ECAM_ADDRESS(Bus, Device, Function, Offset):
    return (((Offset) & 0xfff) | (((Function) & 0x07) << 12) | (((Device) & 0x1f) << 15) | (((Bus) & 0xff) << 20))

# 计算ECAM ADDR
def calculate_ecam_addr():
    ecam_base = int(ecam_base_entry.get(), 16) # 使用16进制格式输入，转换为整数
    bus = int(bus_entry.get())
    device = int(device_entry.get())
    function = int(function_entry.get())
    offset = int(offset_entry.get())

    ecam_addr = ecam_base + PCI_ECAM_ADDRESS(bus, device, function, offset)
    ecam_addr_output.config(state=tk.NORMAL)
    ecam_addr_output.delete(0, tk.END)
    formatted_ecam_addr = format(ecam_addr, '#010x')  # 以十六进制格式输出，每32位添加一个空格
    formatted_ecam_addr = ' '.join([formatted_ecam_addr[i:i+10] for i in range(2, len(formatted_ecam_addr), 10)])  # 添加空格
    ecam_addr_output.insert(tk.END, formatted_ecam_addr)
    ecam_addr_output.config(state=tk.DISABLED)

# 清除所有输入框和输出框的内容
def clear_all():
    ecam_base_entry.delete(0, tk.END)
    bus_entry.delete(0, tk.END)
    device_entry.delete(0, tk.END)
    function_entry.delete(0, tk.END)
    offset_entry.delete(0, tk.END)
    ecam_addr_output.config(state=tk.NORMAL)
    ecam_addr_output.delete(0, tk.END)
    ecam_addr_output.config(state=tk.DISABLED)

# 创建主窗口
root = tk.Tk()
root.title("ECAM ADDR Calculator")

# 创建输入框和标签
ecam_base_label = tk.Label(root, text="ECAM BASE (Hex):")  # 提示用户使用十六进制输入
ecam_base_label.grid(row=0, column=0)
ecam_base_entry = tk.Entry(root)
ecam_base_entry.grid(row=0, column=1)

bus_label = tk.Label(root, text="BUS (Decimal):")  # 提示用户使用十进制输入
bus_label.grid(row=1, column=0)
bus_entry = tk.Entry(root)
bus_entry.grid(row=1, column=1)

device_label = tk.Label(root, text="DEVICE (Decimal):")  # 提示用户使用十进制输入
device_label.grid(row=2, column=0)
device_entry = tk.Entry(root)
device_entry.grid(row=2, column=1)

function_label = tk.Label(root, text="FUNCTION (Decimal):")  # 提示用户使用十进制输入
function_label.grid(row=3, column=0)
function_entry = tk.Entry(root)
function_entry.grid(row=3, column=1)

offset_label = tk.Label(root, text="OFFSET (Decimal):")  # 提示用户使用十进制输入
offset_label.grid(row=4, column=0)
offset_entry = tk.Entry(root)
offset_entry.grid(row=4, column=1)

# 创建计算按钮
calculate_button = tk.Button(root, text="Calculate", command=calculate_ecam_addr)
calculate_button.grid(row=5, column=0, columnspan=2)

# 创建清除按钮
clear_button = tk.Button(root, text="Clear All", command=clear_all)
clear_button.grid(row=5, column=1, columnspan=2)

# 创建输出框
ecam_addr_output_label = tk.Label(root, text="ECAM ADDR (Hex):")  # 输出为十六进制格式
ecam_addr_output_label.grid(row=6, column=0)
ecam_addr_output = tk.Entry(root, state=tk.DISABLED)
ecam_addr_output.grid(row=6, column=1)

# 运行主循环
root.mainloop()
