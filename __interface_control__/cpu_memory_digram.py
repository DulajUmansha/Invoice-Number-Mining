import psutil
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide6.QtCore import QThread, Signal


class WorkerThread(QThread):
    update_signal = Signal(list, list)

    def run(self):
        cpu_data = []
        memory_data = []
        while True:
            cpu_percent, memory_percent = self.get_usage()
            cpu_data.append(cpu_percent)
            memory_data.append(memory_percent)
            cpu_data = cpu_data[-50:]
            memory_data = memory_data[-50:]
            self.update_signal.emit(cpu_data, memory_data)
            self.msleep(500)  # Sleep for 500 milliseconds

    def get_usage(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        return cpu_percent, memory_percent

# Function to update the plot
def update_plot(cpu_data, memory_data, cpu_sc, memory_sc):
    # Update CPU usage plot
    cpu_sc.axes.clear()
    cpu_sc.axes.set_facecolor('#424242')
    cpu_sc.axes.grid(color='white', linestyle='--', linewidth=0.5)
    cpu_sc.axes.spines['bottom'].set_color('white')
    cpu_sc.axes.spines['top'].set_color('white')
    cpu_sc.axes.spines['right'].set_color('white')
    cpu_sc.axes.spines['left'].set_color('white')
    cpu_sc.axes.xaxis.label.set_color('white')
    cpu_sc.axes.yaxis.label.set_color('white')
    cpu_sc.axes.title.set_color('white')
    cpu_sc.axes.tick_params(axis='x', colors='white')
    cpu_sc.axes.tick_params(axis='y', colors='white')
    cpu_sc.axes.plot(cpu_data, label="CPU Usage", color="blue")
    cpu_sc.axes.set_ylim(0, 100)
    cpu_sc.axes.set_xlabel("Time (s)")
    cpu_sc.axes.set_ylabel("CPU Usage (%)")
    cpu_sc.axes.set_xticks([])
    cpu_sc.axes.legend()
    cpu_sc.draw()

    # Update memory usage plot
    memory_sc.axes.clear()
    memory_sc.axes.set_facecolor('#424242')
    memory_sc.axes.grid(color='white', linestyle='--', linewidth=0.5)
    memory_sc.axes.spines['bottom'].set_color('white')
    memory_sc.axes.spines['top'].set_color('white')
    memory_sc.axes.spines['right'].set_color('white')
    memory_sc.axes.spines['left'].set_color('white')
    memory_sc.axes.xaxis.label.set_color('white')
    memory_sc.axes.yaxis.label.set_color('white')
    memory_sc.axes.title.set_color('white')
    memory_sc.axes.tick_params(axis='x', colors='white')
    memory_sc.axes.tick_params(axis='y', colors='white')
    memory_sc.axes.plot(memory_data, label="Memory Usage", color="green")
    memory_sc.axes.set_ylim(0, 100)
    memory_sc.axes.set_xlabel("Time (s)")
    memory_sc.axes.set_ylabel("Memory Usage (%)")
    memory_sc.axes.set_xticks([])
    memory_sc.axes.legend()
    memory_sc.draw()

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi,facecolor="#424242")
        self.axes = self.fig.add_subplot(111)

        # Set the spines and ticks explicitly
        self.axes.spines['bottom'].set_color('white')
        self.axes.spines['top'].set_color('white')
        self.axes.spines['right'].set_color('white')
        self.axes.spines['left'].set_color('white')
        self.axes.xaxis.label.set_color('white')
        self.axes.yaxis.label.set_color('white')
        self.axes.title.set_color('white')
        self.axes.tick_params(axis='x', colors='white')
        self.axes.tick_params(axis='y', colors='white')

        super(MplCanvas, self).__init__(self.fig)

        # Set the background color of the canvas
        self.setStyleSheet("background-color: #424242;")
