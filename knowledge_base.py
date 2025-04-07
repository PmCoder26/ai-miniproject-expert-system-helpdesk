# knowledge_base.py

# Knowledge base storing issues and their corresponding solutions
knowledge_base = {
    "internet": [
        "Check if your router is turned on.",
        "Restart your router and try again.",
        "Reset network settings if the issue persists.",
        "Try switching to a different Wi-Fi channel.",
        "Check if your device is too far from the router.",
        "Ensure your Wi-Fi driver is up to date.",
        "Disable and re-enable the Wi-Fi adapter.",
        "Check your router’s firmware and update it.",
        "Contact your ISP if the connection issue persists."
    ],
    "computer_not_starting": [
        "Ensure the power cable is properly connected.",
        "Try using a different power outlet or adapter.",
        "Remove external devices and try again.",
        "Hold the power button for 10 seconds and restart.",
        "Check the power supply unit (PSU) if using a desktop.",
        "Ensure the motherboard and CPU are properly seated.",
        "Listen for beeping sounds during boot to diagnose hardware failure.",
        "Try booting from a live USB to check if the issue is OS related."
    ],
    "slow_computer": [
        "Close unnecessary background applications.",
        "Run a disk cleanup and check for malware.",
        "Upgrade your RAM if the issue persists.",
        "Perform a full system scan for viruses and malware.",
        "Check disk space, and clear temp files and caches.",
        "Defragment your hard drive (HDD), or optimize your SSD.",
        "Disable unnecessary startup programs.",
        "Check for overheating, as it can slow down your system.",
        "Check your system's performance settings and adjust them for better speed."
    ],
    "software_crash": [
        "Restart the application.",
        "Check for software updates.",
        "Reinstall the application if the issue continues.",
        "Clear the application’s cache or reset settings.",
        "Run the application as an administrator.",
        "Check for conflicts with other software or antivirus programs.",
        "Ensure your operating system is up-to-date with patches.",
        "Check your system's hardware for failures affecting software performance."
    ],
    "printer_issue": [
        "Ensure the printer is properly connected to the computer.",
        "Check if the correct printer driver is installed.",
        "Try restarting both the printer and computer.",
        "Check for paper jams or ink issues.",
        "Ensure the printer is set as the default printer.",
        "Check the printer’s network settings if it's a network printer.",
        "Ensure you have the latest printer driver installed.",
        "Try printing from a different device to isolate the issue."
    ],
    "bluetooth_issue": [
        "Ensure Bluetooth is turned on in your device settings.",
        "Try turning Bluetooth off and then on again.",
        "Ensure your device is discoverable and in pairing mode.",
        "Check if the device is too far away or in interference zones.",
        "Update Bluetooth drivers or firmware if needed.",
        "Remove and re-pair the Bluetooth device.",
        "Check if the Bluetooth device has sufficient battery.",
        "Check Bluetooth compatibility with your operating system."
    ],
    "email_issue": [
        "Ensure the email server settings (SMTP/IMAP/POP3) are correct.",
        "Check if your email client is connected to the internet.",
        "Ensure your email inbox is not full.",
        "Check the email account’s security settings and password.",
        "Try using a different email client or web interface.",
        "Check if you are able to send/receive emails from other accounts.",
        "Ensure that your email provider is not experiencing downtime.",
        "Check your email account's spam filter settings."
    ],
    "overheating_shutdown": [
        "Ensure the laptop/PC has proper ventilation.",
        "Use a cooling pad or elevate the laptop to improve airflow.",
        "Clean the fan and internal components to remove dust.",
        "Update the BIOS/firmware to improve power management.",
        "Check if your power settings are adjusted for performance or cooling.",
        "Ensure that your CPU or GPU drivers are up to date.",
        "Monitor the system temperature using software tools.",
        "Check for any overclocking that could be causing overheating."
    ],
    "software_installation_error": [
        "Check if your system meets the software’s minimum requirements.",
        "Ensure there is enough disk space for installation.",
        "Disable antivirus software that might block installation.",
        "Try running the installer as an administrator.",
        "Check for operating system compatibility issues.",
        "Ensure that there is no system corruption preventing installation.",
        "Check for any previously installed versions that might conflict.",
        "Try installing the software in safe mode."
    ],
    "blue_screen_of_death": [
        "Note the error code and search for solutions online.",
        "Restart your computer and boot into safe mode.",
        "Check for hardware issues such as failing RAM or HDD.",
        "Update your graphics card and motherboard drivers.",
        "Check if any recent software or hardware changes caused the issue.",
        "Run a system restore to a point before the issue started.",
        "Test the system’s RAM and hard drive for errors.",
        "Check for overheating and ensure your cooling system is functioning properly."
    ],
    "wifi_not_detecting_network": [
        "Ensure that your Wi-Fi is turned on.",
        "Check if the Wi-Fi adapter is working properly.",
        "Restart your router and modem.",
        "Ensure that the network is not hidden (SSID broadcast).",
        "Update your Wi-Fi drivers.",
        "Check if the device is within range of the router.",
        "Try restarting your computer or device.",
        "Reset network settings on your device."
    ],
    "slow_wifi": [
        "Restart your router and modem.",
        "Check for network congestion or bandwidth hogs.",
        "Switch to a different Wi-Fi channel on your router.",
        "Use a Wi-Fi extender to increase coverage.",
        "Check if other devices are using the same bandwidth.",
        "Use the 5GHz Wi-Fi band for less interference.",
        "Contact your ISP if the issue persists."
    ]
}

# Keywords associated with each issue to help match user input
issue_keywords = {
    "internet": ["internet", "wifi", "network", "connection", "not connecting", "no signal"],
    "computer_not_starting": ["power", "not starting", "won't turn on", "boot", "black screen", "dead", "won't boot"],
    "slow_computer": ["slow", "lagging", "freezing", "hang", "performance", "not responding", "too slow"],
    "software_crash": ["crash", "not responding", "stopped working", "error", "closing", "application failure"],
    "printer_issue": ["printer", "not printing", "paper jam", "ink", "not detected", "printer offline"],
    "bluetooth_issue": ["bluetooth", "pairing", "connect", "device not found", "bluetooth not working", "connection issue"],
    "email_issue": ["email", "not sending", "can't receive", "email issue", "inbox full", "SMTP", "IMAP", "POP3"],
    "overheating_shutdown": ["overheating", "shutdown", "fan noise", "overheats", "laptop shutdown", "high temperature"],
    "software_installation_error": ["installation error", "not installing", "can't install", "setup failed", "installation issue", "setup error"],
    "blue_screen_of_death": ["blue screen", "BSOD", "stop error", "system crash", "critical error", "stop code"],
    "wifi_not_detecting_network": ["wifi not detecting", "network not found", "no network", "cannot connect", "wifi not working"],
    "slow_wifi": ["slow wifi", "wifi lag", "network lag", "low speed", "wifi congestion", "bandwidth issues"]
}