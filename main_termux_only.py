from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.clock import Clock
import subprocess
import os
import json
from datetime import datetime
from pathlib import Path

Window.clearcolor = (0, 0, 0, 1)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Easter egg: tap counter
        self.tap_count = 0
        self.hidden_unlocked = False
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Title with warning (tappable for easter egg)
        self.title = Button(
            text='[color=ff0000]⚠ BEYOND 9 ⚠[/color]\n[size=14][color=ffff00]Reality Breach Protocol[/color][/size]',
            markup=True,
            size_hint=(1, 0.15),
            font_size='32sp',
            background_color=(0, 0, 0, 0)
        )
        self.title.bind(on_press=self.secret_tap)
        layout.add_widget(self.title)

        # Mode selector (will update when hidden modes unlock)
        self.normal_modes = ('👁️ Entity Detection', '🔴 VHS Glitch',
                            '💀 Digital Corruption', '🌈 RGB Shift',
                            '⚡ Datamosh', '📺 Static', '☠️ CHAOS')
        
        self.hidden_modes = ('🌌 UV Vision', '🔥 Infrared',
                            '👻 Spirit Vision', '✨ Aura Mode',
                            '⚡ Electromagnetic', '🌀 Quantum View',
                            '🌊 Dimensional Shift', '🌟 Astral Vision')
        
        self.mode_spinner = Spinner(
            text='👁️ Entity Detection',
            values=self.normal_modes,
            size_hint=(1, 0.1),
            background_color=(0.5, 0, 0, 1)
        )
        layout.add_widget(self.mode_spinner)

        # Record button
        record_btn = Button(
            text='🔴 CAPTURE REALITY',
            size_hint=(1, 0.2),
            background_color=(0.5, 0, 0, 1),
            font_size='24sp'
        )
        record_btn.bind(on_press=self.start_recording)
        layout.add_widget(record_btn)

        # AI Analysis button
        ai_btn = Button(
            text='🧠 AI ENTITY SCAN',
            size_hint=(1, 0.15),
            background_color=(0.3, 0, 0.5, 1),
            font_size='20sp'
        )
        ai_btn.bind(on_press=self.analyze_with_ai)
        layout.add_widget(ai_btn)

        # Status with warnings
        self.status = Label(
            text='[color=ff0000]⚠ SYSTEM READY\nWARNING: May detect entities invisible to human eye[/color]',
            markup=True,
            size_hint=(1, 0.25),
            font_size='14sp'
        )
        layout.add_widget(self.status)

        # Disclaimer
        info = Label(
            text='[color=666666]Use at own risk | Not responsible for what you see[/color]',
            markup=True,
            size_hint=(1, 0.15),
            font_size='10sp'
        )
        layout.add_widget(info)

        self.add_widget(layout)

    def secret_tap(self, instance):
        """Easter egg: Triple tap to unlock hidden vision modes"""
        self.tap_count += 1
        
        if self.tap_count == 3 and not self.hidden_unlocked:
            self.unlock_hidden_modes()
        
        # Reset counter after 2 seconds
        Clock.schedule_once(lambda dt: self.reset_tap_count(), 2)
    
    def reset_tap_count(self):
        self.tap_count = 0
    
    def unlock_hidden_modes(self):
        """Unlock secret vision modes"""
        self.hidden_unlocked = True
        
        # Add hidden modes to spinner
        all_modes = self.normal_modes + self.hidden_modes
        self.mode_spinner.values = all_modes
        
        # Update title
        self.title.text = '[color=00ff00]⚠ BEYOND 9 ⚠[/color]\n[size=14][color=00ffff]HIDDEN VISION UNLOCKED[/color][/size]'
        
        # Show unlock message
        self.status.text = '[color=00ff00]🔓 HIDDEN MODES UNLOCKED!\n👁️ You can now see what humans cannot see[/color]'
        
        # Flash effect
        Clock.schedule_once(lambda dt: self.flash_unlock(), 0.5)
    
    def flash_unlock(self):
        self.status.text = '[color=ff00ff]⚡ DIMENSIONAL BARRIERS REMOVED ⚡\n🌌 UV | 🔥 IR | 👻 SPIRIT | ✨ AURA | ⚡ EM | 🌀 QUANTUM | 🌊 DIMENSIONAL[/color]'

    def start_recording(self, instance):
        mode = self.mode_spinner.text
        self.status.text = f'[color=ffff00]⚡ RECORDING {mode}...\nReality distortion in progress[/color]'

        # Launch camera
        subprocess.Popen([
            'am', 'start',
            '-n', 'app.grapheneos.camera/.ui.activities.VideoCaptureActivity'
        ])

        # Schedule processing
        Clock.schedule_once(lambda dt: self.process_video(mode), 5)

    def analyze_with_ai(self, instance):
        self.status.text = '[color=ff00ff]🧠 SCANNING FOR ENTITIES...\n⚠ SYSTEM MAY BECOME UNSTABLE[/color]'

        try:
            # Find newest video
            result = subprocess.run(
                ['sh', '-c', 'find /sdcard/DCIM -name "*.mp4" -type f -mmin -10 -exec ls -t {} + 2>/dev/null | head -1'],
                capture_output=True,
                text=True
            )

            if result.stdout.strip():
                video = result.stdout.strip()
                Clock.schedule_once(lambda dt: self.run_ai_analysis(video), 1)
            else:
                self.status.text = '[color=ff0000]❌ NO VIDEO FOUND[/color]'
        except Exception as e:
            self.status.text = f'[color=ff0000]⚠ ERROR: {e}[/color]'

    def run_ai_analysis(self, video_path):
        """Use Ollama to analyze video for entities"""

        # Extract frame from video
        frame_path = '/sdcard/beyond9_frame.jpg'
        subprocess.run([
            'ffmpeg', '-i', video_path,
            '-vf', 'select=eq(n\\,0)',
            '-vframes', '1',
            '-y', frame_path
        ], capture_output=True)

        # Analyze with Ollama
        try:
            result = subprocess.run([
                'curl', '-X', 'POST',
                'http://localhost:11434/api/generate',
                '-d', json.dumps({
                    'model': 'llava',
                    'prompt': 'Analyze this image for anomalies, entities, or anything unusual that should not be there. Describe what you see in detail.',
                    'images': [self.encode_image(frame_path)]
                })
            ], capture_output=True, text=True)

            response = json.loads(result.stdout)
            analysis = response.get('response', 'Unknown')

            self.status.text = f'[color=00ff00]🧠 AI ANALYSIS:\n{analysis[:200]}...[/color]'

        except Exception as e:
            self.status.text = f'[color=ff0000]⚠ AI BREACH: {e}\nREALITY UNSTABLE[/color]'

    def encode_image(self, image_path):
        """Encode image to base64 for Ollama"""
        import base64
        with open(image_path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')

    def process_video(self, mode):
        try:
            result = subprocess.run(
                ['sh', '-c', 'find /sdcard/DCIM -name "*.mp4" -type f -mmin -10 -exec ls -t {} + 2>/dev/null | head -1'],
                capture_output=True,
                text=True
            )

            if result.stdout.strip():
                newest = result.stdout.strip()

                # Check if it's a hidden mode
                if any(hidden in mode for hidden in ['UV', 'Infrared', 'Spirit', 'Aura', 'Electromagnetic', 'Quantum', 'Dimensional']):
                    self.apply_hidden_vision(newest, mode)
                elif '👁️' in mode:
                    self.apply_beyond9_effect(newest)
                else:
                    self.apply_glitch(newest, mode)
            else:
                self.status.text = '[color=ff0000]❌ NO VIDEO FOUND[/color]'
        except Exception as e:
            self.status.text = f'[color=ff0000]⚠ ERROR: {e}[/color]'

    def apply_hidden_vision(self, video_path, mode):
        """Apply hidden vision modes that see beyond human perception"""
        output_dir = '/sdcard/DCIM/Beyond9'
        os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        mode_clean = mode.split()[1] if ' ' in mode else mode
        output = f'{output_dir}/BEYOND9_HIDDEN_{mode_clean}_{timestamp}.mp4'

        # Hidden vision filters
        hidden_filters = {
            'UV': 'colorchannelmixer=.393:.769:.189:0:.349:.686:.168:0:.272:.534:.131,eq=contrast=1.3',
            'Infrared': 'pseudocolor=preset=heat,eq=saturation=1.5',
            'Spirit': 'edgedetect=low=0.1:high=0.5,negate,colorchannelmixer=0:1:0:0:0:0:1:0:1:0:0',
            'Aura': 'gblur=sigma=5,eq=brightness=0.1:saturation=2.5,colorchannelmixer=1:0:1:0:0:1:0:0:1:0:1',
            'Electromagnetic': 'edgedetect,negate,colorchannelmixer=0:0:1:0:0:1:0:0:1:0:0,eq=contrast=1.5',
            'Quantum': 'noise=alls=30:allf=t,hue=s=3,rgbashift=rh=3:bh=-3,eq=contrast=1.4',
            'Dimensional': 'setpts=0.5*PTS,rgbashift=rh=5:bh=-5,colorchannelmixer=1:0:0:0:0:1:0:0:0:0:1',
            'Astral': 'colorchannelmixer=.5:.5:.5:0:.3:.3:.3:0:.7:.7:.7,gblur=sigma=3,eq=brightness=0.2:contrast=1.4:saturation=0.5,pseudocolor=preset=magma'
        }

        filter_str = hidden_filters.get(mode_clean, hidden_filters['UV'])
        
        self.status.text = f'[color=ff00ff]⚡ APPLYING {mode_clean} VISION...\n👁️ SEEING BEYOND HUMAN PERCEPTION[/color]'

        subprocess.Popen([
            'ffmpeg', '-i', video_path,
            '-vf', filter_str,
            '-c:v', 'libx264',
            '-crf', '18',
            '-c:a', 'copy',
            '-y', output
        ])

        Clock.schedule_once(lambda dt: self.finish_hidden(output, mode_clean), 3)

    def finish_hidden(self, output, mode):
        self.status.text = f'[color=00ff00]✓ {mode} VISION COMPLETE\n👁️ {os.path.basename(output)}\n[color=ffff00]⚠ What you see cannot be unseen[/color][/color]'

    def apply_beyond9_effect(self, video_path):
        """Apply Beyond 9 entity detection overlay"""
        output_dir = '/sdcard/DCIM/Beyond9'
        os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output = f'{output_dir}/BEYOND9_{timestamp}.mp4'

        self.status.text = '[color=ff00ff]⚡ APPLYING ENTITY DETECTION...\n⚠ DIMENSIONAL BREACH IN PROGRESS[/color]'

        # Complex Beyond 9 filter with entity detection overlay
        filter_complex = (
            "split[main][detect];"
            "[detect]edgedetect=low=0.1:high=0.4[edges];"
            "[main][edges]overlay=0:0:format=rgb,"
            "drawbox=x=10:y=10:w=iw-20:h=ih-20:color=red@0.3:t=2,"
            "drawtext=fontfile=/system/fonts/DroidSansMono.ttf:text='BEYOND 9 - ENTITY SCAN':fontcolor=red:fontsize=28:x=10:y=10,"
            "drawtext=fontfile=/system/fonts/DroidSansMono.ttf:text='%{pts\\:gmtime\\:0\\:%H\\\\\\:%M\\\\\\:%S}':fontcolor=lime:fontsize=20:x=10:y=50,"
            "drawtext=fontfile=/system/fonts/DroidSansMono.ttf:text='⚠ ANOMALY DETECTED':fontcolor=red:fontsize=24:x=(w-text_w)/2:y=h-80:enable='lt(mod(t,3),1.5)',"
            "noise=alls=20:allf=t,"
            "rgbashift=rh=2:bh=-2,"
            "eq=contrast=1.3:saturation=1.2"
        )

        subprocess.Popen([
            'ffmpeg', '-i', video_path,
            '-vf', filter_complex,
            '-c:v', 'libx264',
            '-crf', '18',
            '-c:a', 'copy',
            '-y', output
        ])

        Clock.schedule_once(lambda dt: self.finish_beyond9(output), 3)

    def finish_beyond9(self, output):
        self.status.text = f'[color=00ff00]✓ ENTITY SCAN COMPLETE\n⚠ {os.path.basename(output)}\n[color=ff0000]WARNING: Review footage carefully[/color][/color]'

    def apply_glitch(self, video_path, mode):
        """Apply glitch effects"""
        output_dir = '/sdcard/DCIM/Super9Glitch'
        os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        mode_clean = mode.split()[1] if ' ' in mode else mode
        output = f'{output_dir}/SUPER9_{mode_clean}_{timestamp}.mp4'

        filters = {
            'VHS': 'rgbashift=rh=-2:gh=0:bh=2,noise=alls=20:allf=t,eq=contrast=1.2:brightness=-0.1',
            'Digital': 'noise=alls=30:allf=t+u,eq=saturation=1.5',
            'RGB': 'rgbashift=rh=5:gh=-3:bh=3:rv=2:gv=-2:bv=1',
            'Datamosh': 'noise=alls=40:allf=t,eq=contrast=1.5:saturation=0.8',
            'Static': 'noise=alls=60:allf=t+u',
            'CHAOS': 'noise=alls=45:allf=t+u,rgbashift=rh=10:gh=-5:bh=8,hue=s=2,eq=contrast=1.7'
        }

        filter_str = filters.get(mode_clean, filters['VHS'])

        self.status.text = f'[color=ffff00]⚡ APPLYING {mode_clean} GLITCH...[/color]'

        subprocess.Popen([
            'ffmpeg', '-i', video_path,
            '-vf', filter_str,
            '-c:v', 'libx264',
            '-crf', '18',
            '-c:a', 'copy',
            '-y', output
        ])

        Clock.schedule_once(lambda dt: self.finish_glitch(output), 3)

    def finish_glitch(self, output):
        self.status.text = f'[color=00ff00]✓ GLITCH COMPLETE\n{os.path.basename(output)}[/color]'

class Beyond9App(App):
    def build(self):
        self.title = 'Beyond 9 - Reality Breach'
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    Beyond9App().run()
