#System volume control using python
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def get_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    return current_volume

def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level, None)

def change_volume(change):
    current_volume = get_volume()
    new_volume = current_volume + change
    new_volume = max(0.0, min(1.0, new_volume))  # Ensure the volume stays within 0.0 to 1.0
    set_volume(new_volume)
    print(f"Volume changed to: {new_volume * 100:.2f}%")

if __name__ == "__main__":
    change = float(input("Enter volume change (-0.1 to decrease by 10%, 0.1 to increase by 10%): "))
    change_volume(change)
