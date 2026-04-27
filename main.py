from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.clock import Clock

Window.clearcolor = (0, 0, 0, 1)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.tap_count = 0
        self.hidden_unlocked = False
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title (tappable for easter egg)
        self.title = Button(
            text='[color=ff0000]⚠ BEYOND 9 ⚠[/color]\n[size=14][color=ffff00]Reality Breach Protocol[/color][/size]',
            markup=True,
            size_hint=(1, 0.15),
            font_size='32sp',
            background_color=(0, 0, 0, 0)
        )
        self.title.bind(on_press=self.secret_tap)
        layout.add_widget(self.title)
        
        # Mode selector
        self.normal_modes = (
            '👁️ Entity Detection',
            '🔴 VHS Glitch',
            '💀 Digital Corruption',
            '🌈 RGB Shift',
            '⚡ Datamosh',
            '📺 Static',
            '☠️ CHAOS'
        )
        
        self.hidden_modes = (
            '🌌 UV Vision',
            '🔥 Infrared',
            '👻 Spirit Vision',
            '✨ Aura Mode',
            '⚡ Electromagnetic',
            '🌀 Quantum View',
            '🌊 Dimensional Shift',
            '🌟 Astral Vision'
        )
        
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
        
        # Status
        self.status = Label(
            text='[color=ff0000]⚠ SYSTEM READY\nWARNING: May detect entities invisible to human eye[/color]',
            markup=True,
            size_hint=(1, 0.4),
            font_size='14sp'
        )
        layout.add_widget(self.status)
        
        # Info
        info = Label(
            text='[color=666666]APK v1.0 | Camera integration in progress[/color]',
            markup=True,
            size_hint=(1, 0.15),
            font_size='10sp'
        )
        layout.add_widget(info)
        
        self.add_widget(layout)
    
    def secret_tap(self, instance):
        """Triple tap to unlock hidden modes"""
        self.tap_count += 1
        if self.tap_count == 3 and not self.hidden_unlocked:
            self.unlock_hidden_modes()
        Clock.schedule_once(lambda dt: self.reset_tap_count(), 2)
    
    def reset_tap_count(self):
        self.tap_count = 0
    
    def unlock_hidden_modes(self):
        """Unlock secret vision modes"""
        self.hidden_unlocked = True
        all_modes = self.normal_modes + self.hidden_modes
        self.mode_spinner.values = all_modes
        
        self.title.text = '[color=00ff00]⚠ BEYOND 9 ⚠[/color]\n[size=14][color=00ffff]HIDDEN VISION UNLOCKED[/color][/size]'
        self.status.text = '[color=00ff00]🔓 HIDDEN MODES UNLOCKED!\n👁️ You can now see what humans cannot see[/color]'
        
        Clock.schedule_once(lambda dt: self.flash_unlock(), 0.5)
    
    def flash_unlock(self):
        self.status.text = '[color=ff00ff]⚡ DIMENSIONAL BARRIERS REMOVED ⚡\n🌌 UV | 🔥 IR | 👻 SPIRIT | ✨ AURA | ⚡ EM | 🌀 QUANTUM | 🌊 DIMENSIONAL | 🌟 ASTRAL[/color]'
    
    def start_recording(self, instance):
        mode = self.mode_spinner.text
        self.status.text = f'[color=ffff00]⚡ {mode} MODE ACTIVATED\n📱 Preparing reality breach...[/color]'
        
        Clock.schedule_once(lambda dt: self.show_ready(), 2)
    
    def show_ready(self):
        self.status.text = '[color=00ff00]✓ MODE READY\n⚠ Camera integration coming in next update\n[color=666666]For now, use Termux version for full features[/color][/color]'

class Beyond9App(App):
    def build(self):
        self.title = 'Beyond 9 - Reality Breach'
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    Beyond9App().run()
