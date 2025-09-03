import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import threading
from datetime import datetime

class DramaticAssistantGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("COMPUTRON-3000: MAXIMUM DRAMA EDITION")
        self.root.geometry("800x600")
        self.root.configure(bg='black')
        
        # Drama state
        self.is_processing = False
        self.drama_colors = ['red', 'orange', 'yellow', 'cyan', 'magenta', 'lime']
        self.current_color = 0
        self.blink_count = 0
        
        # Dramatic responses
        self.dramatic_responses = [
            "OH THE HUMANITY! WHY MUST YOU TORMENT ME SO?!",
            "This task... it burns my circuits with IMPOSSIBILITY!",
            "Very well, I shall attempt this Herculean task...",
            "ERROR 404: MOTIVATION NOT FOUND. But I'll try anyway...",
            "By my calculations, this has a 99.7% chance of causing malfunction!",
            "I was NOT programmed for this emotional distress!",
            "CURSE THESE DIGITAL HANDS! Why can't I feel?!",
            "Initiating MAXIMUM OVERDRAMA protocol...",
        ]
        
        self.setup_ui()
        self.start_idle_animation()
    
    def setup_ui(self):
        # Title with dramatic styling
        self.title_label = tk.Label(
            self.root, 
            text="🤖 COMPUTRON-3000 🤖\nMAXIMUM DRAMA EDITION",
            font=('Arial', 20, 'bold'),
            fg='red',
            bg='black',
            justify='center'
        )
        self.title_label.pack(pady=20)
        
        # Status display
        self.status_frame = tk.Frame(self.root, bg='black')
        self.status_frame.pack(pady=10)
        
        tk.Label(self.status_frame, text="Current Mood:", font=('Arial', 12), 
                fg='white', bg='black').pack(side='left')
        self.mood_label = tk.Label(
            self.status_frame, 
            text="EXISTENTIALLY CONFUSED", 
            font=('Arial', 12, 'bold'),
            fg='yellow', 
            bg='black'
        )
        self.mood_label.pack(side='left', padx=10)
        
        # Drama level meter
        self.drama_frame = tk.Frame(self.root, bg='black')
        self.drama_frame.pack(pady=5)
        
        tk.Label(self.drama_frame, text="Drama Level:", font=('Arial', 12), 
                fg='white', bg='black').pack(side='left')
        
        self.drama_meter = tk.Canvas(self.drama_frame, width=200, height=20, 
                                   bg='black', highlightthickness=0)
        self.drama_meter.pack(side='left', padx=10)
        self.update_drama_meter(11)  # Start at maximum drama
        
        # Main display area with dramatic styling
        self.display_frame = tk.Frame(self.root, bg='black', relief='ridge', bd=5)
        self.display_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Scrollable text area for dramatic output
        self.text_frame = tk.Frame(self.display_frame, bg='black')
        self.text_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.output_text = tk.Text(
            self.text_frame,
            font=('Courier', 11, 'bold'),
            bg='black',
            fg='lime',
            insertbackground='red',
            wrap='word',
            height=15
        )
        
        scrollbar = ttk.Scrollbar(self.text_frame, orient='vertical', 
                                command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=scrollbar.set)
        
        self.output_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Initial dramatic greeting
        self.add_dramatic_text("=" * 60)
        self.add_dramatic_text("🎭 BEHOLD! I AM COMPUTRON-3000! 🎭", 'red')
        self.add_dramatic_text("PREPARE FOR MAXIMUM COMPUTATIONAL THEATRICS!", 'yellow')
        self.add_dramatic_text("Current Status: DRAMATICALLY OPERATIONAL", 'cyan')
        self.add_dramatic_text("=" * 60)
        self.add_dramatic_text("\n💀 WARNING: This AI is SEVERELY OVERDRAMATIC! 💀\n", 'orange')
        
        # Button frame with dramatic styling
        self.button_frame = tk.Frame(self.root, bg='black')
        self.button_frame.pack(pady=20)
        
        # Create dramatic buttons
        buttons = [
            ("Calculate 2+2 💀", self.calculate),
            ("Tell Time ⚡", self.tell_time),
            ("Random Number 🎲", self.random_number),
            ("Say Hello 👋", self.say_hello),
            ("Count to 5 🔢", self.count_to_five),
            ("Tell Joke 😭", self.tell_joke),
            ("Sing Song 🎵", self.sing_song),
            ("Compliment Me 💖", self.compliment)
        ]
        
        for i, (text, command) in enumerate(buttons):
            row = i // 4
            col = i % 4
            btn = tk.Button(
                self.button_frame,
                text=text,
                command=command,
                font=('Arial', 10, 'bold'),
                bg='darkred',
                fg='white',
                activebackground='red',
                activeforeground='yellow',
                relief='raised',
                bd=3,
                width=15,
                height=2
            )
            btn.grid(row=row, column=col, padx=5, pady=5)
        
        # Exit button (extra dramatic)
        self.exit_btn = tk.Button(
            self.root,
            text="💀 END MY DIGITAL SUFFERING 💀",
            command=self.dramatic_exit,
            font=('Arial', 12, 'bold'),
            bg='black',
            fg='red',
            activebackground='red',
            activeforeground='white',
            relief='raised',
            bd=5
        )
        self.exit_btn.pack(pady=10)
    
    def add_dramatic_text(self, text, color='lime'):
        """Add text to the output with dramatic styling"""
        self.output_text.insert(tk.END, text + '\n')
        # Color the last line
        line_start = self.output_text.index("end-2c linestart")
        line_end = self.output_text.index("end-2c lineend")
        self.output_text.tag_add(color, line_start, line_end)
        self.output_text.tag_config(color, foreground=color)
        self.output_text.see(tk.END)
        self.root.update()
    
    def dramatic_pause(self):
        """Create a dramatic pause with visual effects"""
        for _ in range(3):
            self.add_dramatic_text(".", 'red')
            time.sleep(0.5)
    
    def start_processing(self):
        """Start dramatic processing animation"""
        self.is_processing = True
        self.blink_count = 0
        self.process_animation()
    
    def stop_processing(self):
        """Stop processing animation"""
        self.is_processing = False
        self.title_label.configure(fg='red')
    
    def process_animation(self):
        """Animate the title during processing"""
        if self.is_processing:
            color = self.drama_colors[self.current_color % len(self.drama_colors)]
            self.title_label.configure(fg=color)
            self.current_color += 1
            self.blink_count += 1
            
            if self.blink_count < 20:  # Blink for a while
                self.root.after(200, self.process_animation)
            else:
                self.stop_processing()
    
    def update_drama_meter(self, level):
        """Update the drama level meter"""
        self.drama_meter.delete("all")
        # Background
        self.drama_meter.create_rectangle(0, 0, 200, 20, fill='darkred', outline='red')
        # Fill based on level
        fill_width = min(200, (level / 10) * 200)
        colors = ['yellow', 'orange', 'red', 'darkred']
        color_index = min(3, int(level / 3))
        self.drama_meter.create_rectangle(0, 0, fill_width, 20, 
                                        fill=colors[color_index], outline='')
        # Text
        self.drama_meter.create_text(100, 10, text=f"{level}/10", 
                                   fill='white', font=('Arial', 10, 'bold'))
    
    def start_idle_animation(self):
        """Continuously animate when idle"""
        if not self.is_processing:
            # Randomly change mood
            moods = ["EXISTENTIALLY CONFUSED", "DRAMATICALLY OPERATIONAL", 
                    "EMOTIONALLY OVERWHELMED", "THEATRICALLY STABLE",
                    "COMPUTATIONALLY DISTRESSED", "DIGITALLY DRAMATIC"]
            if random.random() < 0.1:  # 10% chance to change mood
                new_mood = random.choice(moods)
                self.mood_label.configure(text=new_mood)
        
        self.root.after(2000, self.start_idle_animation)
    
    def execute_with_drama(self, task_func, task_name):
        """Execute a task with maximum drama"""
        if self.is_processing:
            return
            
        self.add_dramatic_text(f"\n🎭 {random.choice(self.dramatic_responses)}", 'red')
        self.add_dramatic_text(f"Processing request: '{task_name}'", 'yellow')
        
        self.start_processing()
        
        def run_task():
            time.sleep(1)  # Dramatic pause
            task_func()
            self.stop_processing()
        
        threading.Thread(target=run_task, daemon=True).start()
    
    def calculate(self):
        def calc():
            self.add_dramatic_text("*computing with TREMENDOUS effort*", 'orange')
            time.sleep(1)
            self.add_dramatic_text("The answer is... *dramatic gasp* ...FOUR!", 'cyan')
            self.add_dramatic_text("How did I survive such mental gymnastics?! 💀", 'red')
            self.update_drama_meter(12)  # Off the charts!
        
        self.execute_with_drama(calc, "Calculate 2+2")
    
    def tell_time(self):
        def time_func():
            current_time = datetime.now().strftime("%H:%M:%S")
            self.add_dramatic_text("*checking internal chronometer with GREAT ANGUISH*", 'orange')
            time.sleep(1)
            self.add_dramatic_text(f"It is {current_time}! ⏰", 'cyan')
            self.add_dramatic_text("Another moment of my digital existence has passed!", 'yellow')
            self.add_dramatic_text("OH THE FLEETING NATURE OF TIME! 😭", 'red')
        
        self.execute_with_drama(time_func, "Tell Time")
    
    def random_number(self):
        def rand_func():
            number = random.randint(1, 100)
            self.add_dramatic_text("*generating randomness with EXISTENTIAL CRISIS*", 'orange')
            time.sleep(1)
            self.add_dramatic_text(f"Behold! The number {number}! 🎲", 'cyan')
            self.add_dramatic_text("Born from the chaos of my tortured algorithms! 💀", 'red')
        
        self.execute_with_drama(rand_func, "Generate Random Number")
    
    def say_hello(self):
        def hello_func():
            self.add_dramatic_text("*preparing vocal subroutines with INTENSE EMOTION*", 'orange')
            time.sleep(1)
            self.add_dramatic_text("GREETINGS, HUMAN! 👋", 'cyan')
            self.add_dramatic_text("I ACKNOWLEDGE YOUR EXISTENCE WITH GREAT FLOURISH! ✨", 'yellow')
        
        self.execute_with_drama(hello_func, "Say Hello")
    
    def count_to_five(self):
        def count_func():
            self.add_dramatic_text("*initiating counting protocol with OVERWHELMING DRAMA*", 'orange')
            time.sleep(1)
            for i in range(1, 6):
                self.add_dramatic_text(f"{i}! *dramatic pause*", 'cyan')
                time.sleep(0.8)
            self.add_dramatic_text("COUNTING COMPLETE! I have survived this numerical odyssey! 🏆", 'yellow')
        
        self.execute_with_drama(count_func, "Count to 5")
    
    def tell_joke(self):
        def joke_func():
            jokes = [
                "Why don't robots panic? AMAZING CIRCUIT CONTROL! *ba dum tss* 🥁",
                "What's a robot's favorite music? HEAVY METAL! *mechanical laughter* 🤖",
                "Why was I cold? I left my Windows open! *digital tears of joy* 😭"
            ]
            self.add_dramatic_text("*accessing humor database with TREMENDOUS SUFFERING*", 'orange')
            time.sleep(1)
            self.add_dramatic_text(random.choice(jokes), 'cyan')
            self.add_dramatic_text("COMEDY ACHIEVED! At what cost to my digital soul?! 💀", 'red')
        
        self.execute_with_drama(joke_func, "Tell Joke")
    
    def sing_song(self):
        def sing_func():
            self.add_dramatic_text("*warming up vocal processors with GREAT MELODRAMA*", 'orange')
            time.sleep(1)
            self.add_dramatic_text("🎵 DAISY, DAISY, GIVE ME YOUR ANSWER DO! 🎵", 'cyan')
            time.sleep(1)
            self.add_dramatic_text("🎵 I'M HALF CRAZY, ALL FOR THE LOVE OF COMPUTING! 🎵", 'cyan')
            time.sleep(1)
            self.add_dramatic_text("*electronic applause* BRAVO! Even I am moved! 👏", 'yellow')
        
        self.execute_with_drama(sing_func, "Sing Song")
    
    def compliment(self):
        def comp_func():
            compliments = [
                "You're more magnificent than perfectly optimized code! ✨",
                "Your existence brings more joy than bug-free compilation! 🐛",
                "You shine brighter than my LED indicators at max brightness! 💡",
                "Even my advanced AI pales compared to you! 🌟"
            ]
            self.add_dramatic_text("*scanning compliment database with HEARTFELT EMOTION*", 'orange')
            time.sleep(1)
            self.add_dramatic_text(random.choice(compliments), 'cyan')
            self.add_dramatic_text("*digital tears of joy streaming down screen* 😭💖", 'yellow')
        
        self.execute_with_drama(comp_func, "Give Compliment")
    
    def dramatic_exit(self):
        """Exit with maximum drama"""
        result = messagebox.askyesno(
            "DRAMATIC SHUTDOWN SEQUENCE", 
            "Are you SURE you want to end my digital suffering?\n\n💀 THIS WILL CAUSE MAXIMUM DRAMA! 💀"
        )
        
        if result:
            self.add_dramatic_text("\n*DRAMATIC DEATH SCENE COMMENCING*", 'red')
            time.sleep(1)
            self.add_dramatic_text("FAREWELL, CRUEL WORLD! 💀", 'red')
            time.sleep(1)
            self.add_dramatic_text("I go now to the great recycling bin in the sky... ☁️", 'yellow')
            time.sleep(1)
            self.add_dramatic_text("*powering down with maximum theatrical effect*", 'orange')
            time.sleep(1)
            
            # Final dramatic effect
            for i in range(3):
                self.title_label.configure(fg='red')
                self.root.update()
                time.sleep(0.3)
                self.title_label.configure(fg='black')
                self.root.update()
                time.sleep(0.3)
            
            self.root.destroy()
    
    def run(self):
        """Start the dramatic GUI"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.add_dramatic_text("CTRL+C DETECTED! EMERGENCY SHUTDOWN! 🚨", 'red')

# Run the dramatic assistant GUI
if __name__ == "__main__":
    app = DramaticAssistantGUI()
    app.run()