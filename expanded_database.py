# -*- coding: utf-8 -*-

ADDITIONAL_SOFTWARE = {
    "Zoom Bloatware": {
        "type": "Bloatware/Privacy",
        "detection": ["Zoom OEM", "Zoom Preinstalled"],
        "reason": "Video conferencing preinstalled without consent. Privacy concerns with data collection. Should be user choice."
    },
    "Discord OEM": {
        "type": "Bloatware",
        "detection": ["Discord OEM", "Discord Preinstalled"],
        "reason": "Gaming chat app preinstalled. Should be user installed when needed."
    },
    "Microsoft Sticky Notes": {
        "type": "Bloatware",
        "detection": ["Microsoft.MicrosoftStickyNotes"],
        "reason": "Basic notes app. Many better alternatives. Optional for most users."
    },
    "Weather": {
        "type": "Bloatware",
        "detection": ["Microsoft.BingWeather", "MSN Weather"],
        "reason": "Weather widget. Redundant with web browsers. Uses resources."
    },
    "Yahoo Powered": {
        "type": "Adware/Toolbar",
        "detection": ["Yahoo Powered", "Yahoo Toolbar"],
        "reason": "Yahoo toolbar changing search settings. Tracking and ads. Difficult to remove."
    },
    "Bing Bar": {
        "type": "Bloatware/Toolbar",
        "detection": ["Bing Bar", "Microsoft Bing Bar"],
        "reason": "Microsoft search toolbar. Redundant. Changes browser settings."
    },
    "PC Matic": {
        "type": "PUP/Aggressive AV",
        "detection": ["PC Matic"],
        "reason": "Aggressive antivirus with questionable detection. Fear tactics. Expensive."
    },
    "Panda Free Antivirus": {
        "type": "Bloatware/AV",
        "detection": ["Panda Free", "Panda Security"],
        "reason": "Free antivirus with aggressive upselling. Resource intensive. Privacy concerns."
    },
    "Kaspersky Trial": {
        "type": "Trialware/AV",
        "detection": ["Kaspersky Trial", "Kaspersky OEM"],
        "reason": "Trial antivirus preinstalled. Constant upgrade nags. Geopolitical concerns."
    },
    "ESET NOD32 Trial": {
        "type": "Trialware",
        "detection": ["ESET NOD32 Trial", "ESET OEM"],
        "reason": "Trial security software. Nag screens. Should be user installed."
    },
    "Trend Micro Trial": {
        "type": "Trialware/AV",
        "detection": ["Trend Micro OEM", "Trend Micro Trial"],
        "reason": "Trial antivirus with limited features. Upgrade prompts. Resource usage."
    },
    "Webroot SecureAnywhere Trial": {
        "type": "Trialware",
        "detection": ["Webroot SecureAnywhere", "Webroot OEM"],
        "reason": "Cloud-based AV trial. Limited trial period. Constant reminders."
    },
    "Sophos Home": {
        "type": "Bloatware/AV",
        "detection": ["Sophos Home"],
        "reason": "Enterprise AV for home. Overkill for consumers. Resource intensive."
    },
    "Quick Heal": {
        "type": "PUP/AV",
        "detection": ["Quick Heal"],
        "reason": "Lesser-known AV with questionable practices. Often bundled. Aggressive."
    },
    "K7 Antivirus": {
        "type": "Bloatware/AV",
        "detection": ["K7 Total Security", "K7 Antivirus"],
        "reason": "Regional AV with limited support. Better alternatives available."
    },
    "Comodo Antivirus": {
        "type": "PUP/Aggressive",
        "detection": ["Comodo", "Comodo Internet Security"],
        "reason": "Aggressive antivirus. Installs own DNS. Changes settings without clear consent."
    },
    "ZoneAlarm": {
        "type": "Bloatware/Firewall",
        "detection": ["ZoneAlarm", "Check Point ZoneAlarm"],
        "reason": "Firewall software. Windows Firewall sufficient. Nagware. Resource heavy."
    },
    "F-Secure Trial": {
        "type": "Trialware",
        "detection": ["F-Secure Trial", "F-Secure OEM"],
        "reason": "Trial security suite. Limited features. Upgrade prompts."
    },
    "G DATA": {
        "type": "Trialware/AV",
        "detection": ["G DATA", "G DATA Antivirus"],
        "reason": "Lesser-known AV trial. Nagware. Resource usage."
    },
    "BullGuard": {
        "type": "Trialware",
        "detection": ["BullGuard", "BullGuard Antivirus"],
        "reason": "Trial antivirus. Aggressive marketing. Limited trial period."
    },
    "Vipre": {
        "type": "PUP/AV",
        "detection": ["VIPRE", "ThreatTrack Security"],
        "reason": "Enterprise AV marketed to consumers. Questionable practices. Expensive."
    },
    "ByteFence": {
        "type": "PUP/Rogue",
        "detection": ["ByteFence"],
        "reason": "Rogue anti-malware. False positives. Bundled with other PUPs. Difficult to remove."
    },
    "Emsisoft": {
        "type": "Trialware",
        "detection": ["Emsisoft Anti-Malware"],
        "reason": "Trial anti-malware. Constant upgrade prompts. Expensive subscription."
    },
    "SUPERAntiSpyware": {
        "type": "PUP/Questionable",
        "detection": ["SUPERAntiSpyware"],
        "reason": "Questionable anti-spyware. False positives. Aggressive upselling."
    },
    "Malwarebytes AdwCleaner OEM": {
        "type": "Bloatware",
        "detection": ["AdwCleaner OEM"],
        "reason": "Cleanup tool preinstalled. One-time use. Shouldn't stay installed."
    },
    "PC Decrapifier": {
        "type": "Ironic Bloatware",
        "detection": ["PC Decrapifier"],
        "reason": "Bloatware remover that itself becomes bloatware if left installed."
    },
    "Should I Remove It": {
        "type": "Nagware",
        "detection": ["Should I Remove It", "Reason Company"],
        "reason": "Software advisor with constant prompts. Questionable recommendations."
    },
    "Unchecky": {
        "type": "Bloatware Post-Purpose",
        "detection": ["Unchecky"],
        "reason": "Toolbar blocker. Useful but becomes bloatware if forgotten. Can interfere with legitimate installers."
    },
    "Ninite": {
        "type": "Utility Bloatware",
        "detection": ["Ninite"],
        "reason": "Installer utility. No need to keep installed after initial setup."
    },
    "FileHippo App Manager": {
        "type": "Update Nagware",
        "detection": ["FileHippo App Manager"],
        "reason": "Software updater. Constant notifications. Manual updates better."
    },
    "Patch My PC": {
        "type": "Update Bloatware",
        "detection": ["Patch My PC"],
        "reason": "Update tool. Redundant with built-in updaters. Can cause conflicts."
    },
    "SUMo": {
        "type": "Update Nagware",
        "detection": ["SUMo", "Software Update Monitor"],
        "reason": "Software updater with nagware. Free version very limited. Constant upgrade prompts."
    },
    "Chocolatey GUI": {
        "type": "Utility Bloatware",
        "detection": ["Chocolatey GUI"],
        "reason": "Package manager GUI. CLI sufficient. Rarely needed running."
    },
    "WinGet UI": {
        "type": "Redundant Utility",
        "detection": ["WinGet UI", "Winget-UI"],
        "reason": "Windows Package Manager GUI. CMD line sufficient. Unnecessary wrapper."
    },
    "Scoop": {
        "type": "Utility",
        "detection": ["Scoop"],
        "reason": "Package manager. Can accumulate unused packages. Manual management better."
    },
    "Revo Uninstaller Free": {
        "type": "Trialware/Nagware",
        "detection": ["Revo Uninstaller Free"],
        "reason": "Uninstaller with upgrade nags. Pro features locked. Built-in uninstaller sufficient."
    },
    "Geek Uninstaller": {
        "type": "Bloatware",
        "detection": ["Geek Uninstaller"],
        "reason": "Third-party uninstaller. Not needed after use. Windows uninstaller works."
    },
    "Absolute Uninstaller": {
        "type": "Bloatware",
        "detection": ["Absolute Uninstaller"],
        "reason": "Uninstaller tool. Minimal benefits over Windows built-in."
    },
    "Your Uninstaller": {
        "type": "Trialware",
        "detection": ["Your Uninstaller"],
        "reason": "Paid uninstaller. Trial nags. Unnecessary expense."
    },
    "Bulk Crap Uninstaller": {
        "type": "Utility Bloatware",
        "detection": ["BCUninstaller", "Bulk Crap Uninstaller"],
        "reason": "Uninstaller. Good tool but can be removed after cleanup. Not needed running."
    },
    "Steam (Pre-installed)": {
        "type": "Bloatware",
        "detection": ["Steam OEM"],
        "reason": "Gaming platform preinstalled. Should be user choice. Resource usage."
    },
    "Origin (Pre-installed)": {
        "type": "Bloatware",
        "detection": ["Origin OEM", "EA Origin"],
        "reason": "EA gaming platform. Should be installed by user when needed."
    },
    "Epic Games Launcher OEM": {
        "type": "Bloatware",
        "detection": ["Epic Games Launcher OEM"],
        "reason": "Game launcher preinstalled. User should install when needed."
    },
    "Battle.net OEM": {
        "type": "Bloatware",
        "detection": ["Battle.net OEM", "Blizzard Battle.net OEM"],
        "reason": "Blizzard games platform. Preinstallation unnecessary. User choice."
    },
    "GOG Galaxy OEM": {
        "type": "Bloatware",
        "detection": ["GOG Galaxy OEM"],
        "reason": "Game platform preinstalled. Should be user-installed."
    },
    "Ubisoft Connect OEM": {
        "type": "Bloatware",
        "detection": ["Ubisoft Connect OEM", "Uplay OEM"],
        "reason": "Ubisoft gaming platform. Preinstalled bloatware."
    },
    "Rockstar Games Launcher OEM": {
        "type": "Bloatware",
        "detection": ["Rockstar Games Launcher OEM"],
        "reason": "Game launcher. Should be user-installed when needed."
    },
    "Twitch OEM": {
        "type": "Bloatware",
        "detection": ["Twitch OEM", "Twitch Desktop App OEM"],
        "reason": "Streaming app preinstalled. Browser version better. User choice."
    },
    "TeamViewer OEM": {
        "type": "Bloatware/Security Risk",
        "detection": ["TeamViewer OEM"],
        "reason": "Remote access tool. Security risk if preinstalled. Should be user choice."
    },
    "AnyDesk OEM": {
        "type": "Bloatware/Security Risk",
        "detection": ["AnyDesk OEM"],
        "reason": "Remote desktop tool. Security concern preinstalled. User should install."
    },
    "LogMeIn": {
        "type": "Bloatware/Trial",
        "detection": ["LogMeIn", "LogMeIn Hamachi OEM"],
        "reason": "Remote access tool. Often trial. Security concern. User installation better."
    },
    "Chrome Remote Desktop OEM": {
        "type": "Bloatware",
        "detection": ["Chrome Remote Desktop OEM"],
        "reason": "Remote access preinstalled. Security risk. User should install when needed."
    },
    "VNC Viewer OEM": {
        "type": "Bloatware",
        "detection": ["VNC Viewer OEM", "RealVNC OEM"],
        "reason": "Remote desktop viewer. Not needed preinstalled. Security concern."
    },
    "Splashtop": {
        "type": "Bloatware/Trial",
        "detection": ["Splashtop", "Splashtop Streamer"],
        "reason": "Remote desktop trial. Security concern. Should be user choice."
    },
    "PCMover": {
        "type": "Bloatware/One-Time Use",
        "detection": ["PCMover", "Laplink PCMover"],
        "reason": "Migration tool. Only needed once. Takes space permanently."
    },
    "EaseUS Todo Backup": {
        "type": "Trialware",
        "detection": ["EaseUS Todo Backup", "EaseUS OEM"],
        "reason": "Backup software trial. Nagware. Windows Backup sufficient."
    },
    "Acronis True Image OEM": {
        "type": "Trialware",
        "detection": ["Acronis True Image OEM"],
        "reason": "Backup trial. Limited features. Expensive. Alternative solutions better."
    },
    "Macrium Reflect Free OEM": {
        "type": "Bloatware",
        "detection": ["Macrium Reflect OEM"],
        "reason": "Backup tool preinstalled. Should be user choice."
    },
    "Paragon Backup": {
        "type": "Trialware",
        "detection": ["Paragon Backup & Recovery"],
        "reason": "Backup trial. Nagware. Not needed preinstalled."
    },
    "AOMEI Backupper": {
        "type": "Bloatware/Nagware",
        "detection": ["AOMEI Backupper"],
        "reason": "Backup tool. Free version limited. Upgrade nags."
    },
    "NovaBACKUP": {
        "type": "Trialware",
        "detection": ["NovaBACKUP"],
        "reason": "Backup trial. Expensive. Better free alternatives."
    },
    "Cobian Backup": {
        "type": "Bloatware",
        "detection": ["Cobian Backup", "Cobian Reflector"],
        "reason": "Backup utility. Not needed running constantly."
    },
    "SyncBackFree": {
        "type": "Bloatware/Nagware",
        "detection": ["SyncBackFree", "2BrightSparks"],
        "reason": "Backup sync tool. Nagware for pro version."
    },
    "GoodSync": {
        "type": "Trialware",
        "detection": ["GoodSync"],
        "reason": "Sync tool trial. Expensive. Simpler alternatives exist."
    },
    "FreeFileSync": {
        "type": "Bundleware Risk",
        "detection": ["FreeFileSync"],
        "reason": "Sync tool that sometimes bundles offers. Donation nags."
    },
    "MiniTool Partition Wizard": {
        "type": "Trialware/Nagware",
        "detection": ["MiniTool Partition Wizard"],
        "reason": "Partition tool. Free version limited. Upgrade prompts. Disk Management sufficient."
    },
    "AOMEI Partition Assistant": {
        "type": "Bloatware/Nagware",
        "detection": ["AOMEI Partition Assistant"],
        "reason": "Partition manager. Free limited. Constant upgrade nags."
    },
    "EaseUS Partition Master": {
        "type": "Trialware",
        "detection": ["EaseUS Partition Master"],
        "reason": "Partition tool trial. Nagware. Windows tools sufficient."
    },
    "Paragon Partition Manager": {
        "type": "Trialware",
        "detection": ["Paragon Partition Manager"],
        "reason": "Partition manager trial. Expensive. Not needed for most users."
    },
    "Acronis Disk Director": {
        "type": "Trialware",
        "detection": ["Acronis Disk Director"],
        "reason": "Partition tool. Enterprise focused. Expensive. Overkill for home."
    },
    "Active@ Partition Manager": {
        "type": "Bloatware/Trial",
        "detection": ["Active@ Partition Manager"],
        "reason": "Partition tool. Trial limitations. Not needed preinstalled."
    },
    "Stellar Data Recovery": {
        "type": "Scareware/Trial",
        "detection": ["Stellar Data Recovery", "Stellar Phoenix"],
        "reason": "Data recovery trial. Can only scan in trial. Expensive to actually recover."
    },
    "Recuva Professional": {
        "type": "Trialware",
        "detection": ["Recuva Professional"],
        "reason": "Data recovery. Free version sufficient. Pro upgrade nags."
    },
    "EaseUS Data Recovery": {
        "type": "Trialware/Limited",
        "detection": ["EaseUS Data Recovery Wizard"],
        "reason": "Data recovery with severe trial limits. Can only recover 2GB free."
    },
    "Disk Drill": {
        "type": "Trialware/Limited",
        "detection": ["Disk Drill"],
        "reason": "Data recovery. Free version very limited. Expensive upgrade."
    },
    "Wondershare Recoverit": {
        "type": "Trialware/Scareware",
        "detection": ["Wondershare Recoverit", "Recoverit"],
        "reason": "Data recovery. Shows files but requires payment. Expensive."
    },
    "R-Studio": {
        "type": "Expensive Trial",
        "detection": ["R-Studio"],
        "reason": "Professional data recovery. Very expensive. Overkill for home users."
    },
    "GetDataBack": {
        "type": "Expensive Trial",
        "detection": ["GetDataBack"],
        "reason": "Data recovery tool. Expensive. Trial very limited."
    },
    "Hetman Recovery": {
        "type": "Trialware/Scareware",
        "detection": ["Hetman", "Hetman Partition Recovery"],
        "reason": "Recovery suite. Shows recoverable files but requires payment."
    },
    "Puran File Recovery": {
        "type": "Bloatware",
        "detection": ["Puran File Recovery"],
        "reason": "Recovery tool. Free alternatives better. Rarely needed."
    },
    "Glary Undelete": {
        "type": "Bloatware",
        "detection": ["Glary Undelete"],
        "reason": "Part of Glary suite. Individual tool not needed."
    },
    "Toolwiz File Recovery": {
        "type": "Bloatware",
        "detection": ["Toolwiz"],
        "reason": "Recovery tool. Limited functionality. Better alternatives."
    },
    "PhotoRec": {
        "type": "Utility Bloatware",
        "detection": ["PhotoRec"],
        "reason": "Recovery utility. Command-line better. GUI wrapper unnecessary."
    },
    "TestDisk": {
        "type": "Utility Bloatware",
        "detection": ["TestDisk"],
        "reason": "Partition recovery. Advanced tool. GUI wrappers often bloat."
    }
}
