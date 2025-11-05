# -*- coding: utf-8 -*-
"""
Bloatware Database Module
Contains comprehensive definitions of unwanted, potentially harmful, or unnecessary software
with detailed descriptions of why each is not recommended.
"""

# Comprehensive database of target software with expanded entries
TARGET_SOFTWARE = {
    # Windows Bloatware - Apps that come preinstalled with Windows
    "3D Viewer": {
        "type": "Bloatware",
        "detection": ["Microsoft.Microsoft3DViewer"],
        "reason": "Rarely used 3D model viewer. Most users never need this app. Can be replaced with free alternatives if needed."
    },
    "Paint 3D": {
        "type": "Bloatware",
        "detection": ["Microsoft.MSPaint"],
        "reason": "Unnecessary 3D painting app that most users don't use. Traditional Paint or better alternatives exist."
    },
    "Print 3D": {
        "type": "Bloatware",
        "detection": ["Microsoft.Print3D"],
        "reason": "3D printing utility rarely needed. Only useful if you own a 3D printer."
    },
    "Mixed Reality Portal": {
        "type": "Bloatware",
        "detection": ["Microsoft.MixedReality.Portal"],
        "reason": "VR/AR portal only needed for Windows Mixed Reality headsets. Wastes resources for non-VR users."
    },
    "Clipchamp": {
        "type": "Bloatware",
        "detection": ["Clipchamp", "Microsoft.Clipchamp"],
        "reason": "Video editor with limited free features. Better free alternatives available."
    },
    "Adobe Express": {
        "type": "Bloatware",
        "detection": ["Adobe Express", "AdobeSystemsIncorporated.AdobeExpress"],
        "reason": "Limited trial version of Adobe product. Often preinstalled as bloatware with full features locked behind paywall."
    },
    
    # Adware and Unwanted Games
    "Candy Crush Saga": {
        "type": "Adware/Juego",
        "detection": ["king.com.CandyCrushSaga", "Candy Crush Saga"],
        "reason": "Mobile game with aggressive monetization and ads. Preinstalled bloatware that wastes disk space and may track user behavior."
    },
    "Candy Crush Soda Saga": {
        "type": "Adware/Juego",
        "detection": ["king.com.CandyCrushSodaSaga", "Candy Crush Soda Saga"],
        "reason": "Another King game with in-app purchases and ads. Unnecessary preinstalled bloatware."
    },
    "Candy Crush Friends Saga": {
        "type": "Adware/Juego",
        "detection": ["king.com.CandyCrushFriendsSaga", "Candy Crush Friends Saga"],
        "reason": "Yet another Candy Crush variant. Preinstalled adware that serves no productivity purpose."
    },
    "FarmVille 2: Country Escape": {
        "type": "Adware/Juego",
        "detection": ["ZyngaInc.FarmVille2CountryEscape", "FarmVille 2"],
        "reason": "Zynga game with aggressive monetization. Known for data collection and battery drain."
    },
    "Hidden City: Hidden Object": {
        "type": "Adware/Juego",
        "detection": ["G5EntertainmentAB.HiddenCityHiddenObjectAdventure", "Hidden City"],
        "reason": "Casual game with in-app purchases. Preinstalled bloatware with no productivity value."
    },
    "Bubble Witch 3 Saga": {
        "type": "Adware/Juego",
        "detection": ["king.com.BubbleWitch3Saga", "Bubble Witch 3 Saga"],
        "reason": "King game with ads and microtransactions. Bloatware that shouldn't be preinstalled on PCs."
    },
    "Asphalt 8: Airborne": {
        "type": "Adware/Juego",
        "detection": ["GAMELOFTSA.Asphalt8Airborne", "Asphalt 8"],
        "reason": "Mobile racing game with heavy ads and in-app purchases. Not suitable for preinstallation."
    },
    "Age of Empires: Castle Siege": {
        "type": "Bloatware",
        "detection": ["Microsoft.AgeofEmpiresCastleSiege", "Age of Empires: Castle Siege"],
        "reason": "Freemium mobile game. Not the classic Age of Empires, but a monetized variant."
    },
    "Minecraft": {
        "type": "Bloatware",
        "detection": ["Microsoft.MinecraftUWP", "Minecraft for Windows"],
        "reason": "While popular, preinstalling without user consent is bloatware. Users should choose to install games."
    },
    "Microsoft Solitaire Collection": {
        "type": "Adware/Juego",
        "detection": ["Microsoft.MicrosoftSolitaireCollection"],
        "reason": "Contains ads unless premium version purchased. Classic Solitaire had no ads."
    },
    "Roblox": {
        "type": "Adware/Juego",
        "detection": ["ROBLOXCORPORATION.ROBLOX", "Roblox"],
        "reason": "Gaming platform with microtransactions. Should be user-installed, not preloaded."
    },
    "Farm Heroes Saga": {
        "type": "Adware/Juego",
        "detection": ["king.com.FarmHeroesSaga", "Farm Heroes Saga"],
        "reason": "King game with typical freemium model and ads. Unwanted preinstalled bloatware."
    },
    "World of Tanks Blitz": {
        "type": "Bloatware",
        "detection": ["WargamingGroupLimited.WorldofTanksBlitz", "World of Tanks Blitz"],
        "reason": "Free-to-play game with microtransactions. Bloatware when preinstalled without consent."
    },
    "Disney Magic Kingdoms": {
        "type": "Adware/Juego",
        "detection": ["GAMELOFTSA.DisneyMagicKingdoms", "Disney Magic Kingdoms"],
        "reason": "Gameloft freemium game with aggressive monetization. Bloatware on professional systems."
    },
    
    # Social Media and Streaming Apps
    "TikTok": {
        "type": "Bloatware/Privacy Risk",
        "detection": ["ByteDancePte.Ltd.TikTok", "TikTok"],
        "reason": "Privacy concerns with data collection. Known for excessive permissions and tracking. Should be user choice to install."
    },
    "Instagram": {
        "type": "Bloatware",
        "detection": ["Facebook.InstagramBeta", "Instagram"],
        "reason": "Social media app better accessed via browser. Preinstalled app may track more data than necessary."
    },
    "Facebook": {
        "type": "Bloatware/Privacy Risk",
        "detection": ["Facebook.Facebook", "Facebook"],
        "reason": "Known for extensive data collection. Desktop app has more permissions than web version. User should decide to install."
    },
    "Twitter": {
        "type": "Bloatware",
        "detection": ["9E2F88E3.Twitter", "Twitter"],
        "reason": "Social media better accessed via browser. Preinstalled app unnecessary for most users."
    },
    "Netflix": {
        "type": "Bloatware",
        "detection": ["Netflix.Netflix", "Netflix"],
        "reason": "Streaming app that works fine in browser. App version uses more resources and disk space."
    },
    "Prime Video": {
        "type": "Bloatware",
        "detection": ["AmazonVideo.PrimeVideo", "Prime Video"],
        "reason": "Amazon streaming app. Browser version works equally well without taking disk space."
    },
    "Spotify": {
        "type": "Bloatware",
        "detection": ["SpotifyAB.SpotifyMusic", "Spotify"],
        "reason": "Music streaming app. While popular, should be user-installed, not preloaded bloatware."
    },
    "Duolingo": {
        "type": "Bloatware",
        "detection": ["Duolingo.Duolingo-LearnLanguagesforFree", "Duolingo"],
        "reason": "Language learning app. Works better on mobile or web. Shouldn't be preinstalled on PCs."
    },
    
    # Microsoft Bloatware
    "Microsoft News": {
        "type": "Bloatware",
        "detection": ["Microsoft.BingNews", "Noticias"],
        "reason": "News aggregator app. Web browsers provide better news access without dedicated app."
    },
    "Tiempo": {
        "type": "Bloatware",
        "detection": ["Microsoft.BingWeather"],
        "reason": "Weather app that duplicates web functionality. Uses resources for minimal benefit."
    },
    "Cortana": {
        "type": "Spyware/Bloatware",
        "detection": ["Microsoft.549981C3F5F10"],
        "reason": "Voice assistant with privacy concerns. Collects voice data and search history. Most users prefer to disable."
    },
    "OneDrive": {
        "type": "Bloatware",
        "detection": ["OneDrive", "Microsoft OneDrive"],
        "reason": "Cloud storage forced on users. Should be optional. Uses resources and may auto-upload files without clear consent."
    },
    "Microsoft Teams": {
        "type": "Bloatware",
        "detection": ["Microsoft Teams", "Teams Machine-Wide Installer"],
        "reason": "Business communication tool. Shouldn't be preinstalled on consumer PCs. Auto-starts and uses resources."
    },
    "OneNote": {
        "type": "Bloatware",
        "detection": ["Microsoft.Office.OneNote"],
        "reason": "Note-taking app part of Office suite. Should be user-installed, not forced bloatware."
    },
    "Xbox Game Bar": {
        "type": "Bloatware",
        "detection": ["Microsoft.XboxGamingOverlay"],
        "reason": "Gaming overlay. Uses resources even when not gaming. Not needed by non-gamers."
    },
    "Xbox Console Companion": {
        "type": "Bloatware",
        "detection": ["Microsoft.XboxApp"],
        "reason": "Xbox integration app. Only needed by Xbox users. Runs background processes unnecessarily."
    },
    "Your Phone": {
        "type": "Bloatware",
        "detection": ["Microsoft.YourPhone", "Enlace Móvil", "Phone Link"],
        "reason": "Phone integration app. Privacy concerns with data sync. Should be optional, not preinstalled."
    },
    "Consejos": {
        "type": "Bloatware",
        "detection": ["Microsoft.Getstarted", "Microsoft Tips"],
        "reason": "Tips app that's redundant after Windows setup. Takes space for minimal value."
    },
    "Feedback Hub": {
        "type": "Bloatware",
        "detection": ["Microsoft.WindowsFeedbackHub", "Centro de opiniones"],
        "reason": "Feedback collection tool. Most users never use it. Potential telemetry concerns."
    },
    "Microsoft Photos": {
        "type": "Bloatware",
        "detection": ["Microsoft.Windows.Photos", "Microsoft Photos"],
        "reason": "Photo viewer with cloud integration. Better lightweight alternatives exist. May upload photos to cloud."
    },
    "Mail and Calendar": {
        "type": "Bloatware",
        "detection": ["microsoft.windowscommunicationsapps", "Mail and Calendar", "Correo y Calendario"],
        "reason": "Basic mail client. Better alternatives available. Limited functionality compared to dedicated email apps."
    },
    
    # Trial Antivirus (often more harmful than helpful)
    "McAfee": {
        "type": "Trial AV/PUP",
        "detection": ["McAfee", "McAfee Security Scan Plus"],
        "reason": "Trial antivirus known for aggressive popups and difficult uninstallation. Resource-heavy. Often considered bloatware even by security experts."
    },
    "Norton": {
        "type": "Trial AV/PUP",
        "detection": ["Norton", "Symantec"],
        "reason": "Trial security software with aggressive renewal tactics. Heavy system resource usage. Windows Defender often sufficient."
    },
    "Segurazo": {
        "type": "Rogue AV/Malware",
        "detection": ["Segurazo", "SAntivirus"],
        "reason": "FAKE antivirus that installs without proper consent. Shows false positives to scare users. Very difficult to remove. Classified as PUP/malware."
    },
    "SpyHunter": {
        "type": "PUP/Rogue Security",
        "detection": ["SpyHunter"],
        "reason": "Questionable anti-malware that detects false positives to sell full version. Installs via bundleware. Hard to uninstall."
    },
    "TotalAV": {
        "type": "PUP/Aggressive AV",
        "detection": ["TotalAV", "PC Protect"],
        "reason": "Aggressive marketing and scare tactics. Often bundled with other software. Questionable detection methods."
    },
    
    # System Optimizers (Snake Oil Software)
    "Advanced SystemCare": {
        "type": "PUP/Optimizador",
        "detection": ["Advanced SystemCare"],
        "reason": "System optimizer that exaggerates problems to sell premium version. Creates more issues than it solves. Considered PUP."
    },
    "CCleaner": {
        "type": "Formerly Trusted/Now Risky",
        "detection": ["CCleaner", "Piriform", "ccsetup"],
        "reason": "Once trusted, now owned by Avast. Had malware incidents. Registry cleaning can break Windows. Modern Windows doesn't need registry cleaners."
    },
    "PC Accelerate Pro": {
        "type": "PUP/Scareware",
        "detection": ["PC Accelerate Pro"],
        "reason": "Fake optimizer showing false problems. Scareware tactics to sell useless software."
    },
    "PC Speed Up": {
        "type": "PUP/Scareware",
        "detection": ["PC Speed Up", "PC Optimizer Pro"],
        "reason": "Scareware showing fake system issues. Does nothing useful, may harm system."
    },
    "OneSafe PC Cleaner": {
        "type": "PUP/Scareware",
        "detection": ["OneSafe PC Cleaner"],
        "reason": "Aggressive optimizer with false detection. Difficult to remove. Classified as PUP."
    },
    "Advanced System Protector": {
        "type": "PUP/Fake Security",
        "detection": ["Advanced System Protector"],
        "reason": "Fake security tool showing false threats. Bundled with malware. Classified as potentially unwanted program."
    },
    "RegClean Pro": {
        "type": "PUP/Registry Cleaner",
        "detection": ["RegClean Pro"],
        "reason": "Registry cleaner that can damage Windows. Fake scan results. Windows doesn't need registry cleaning."
    },
    "Reimage Repair": {
        "type": "PUP/Scareware",
        "detection": ["Reimage Repair"],
        "reason": "Scareware showing fake critical errors. Aggressive tactics to sell expensive software."
    },
    "Restoro": {
        "type": "PUP/Scareware",
        "detection": ["Restoro"],
        "reason": "System repair tool with questionable methods. Shows exaggerated problems. Often bundled malware."
    },
    "Outbyte PC Repair": {
        "type": "PUP/Scareware",
        "detection": ["Outbyte PC Repair"],
        "reason": "Fake PC repair tool. Shows false problems to scare users into purchase."
    },
    
    # Driver Updaters (Dangerous Snake Oil)
    "Driver Booster": {
        "type": "PUP/Driver Updater",
        "detection": ["Driver Booster"],
        "reason": "May install wrong or outdated drivers. Windows Update handles drivers safely. Can cause hardware issues."
    },
    "DriverPack Solution": {
        "type": "Adware/Bundle Malware",
        "detection": ["DriverPack Solution", "DriverPack Notifier"],
        "reason": "Known for bundling malware and adware. Installs unwanted software. Very aggressive and hard to remove."
    },
    "Driver Easy": {
        "type": "PUP/Driver Updater",
        "detection": ["Driver Easy"],
        "reason": "Driver updater with questionable practices. May install incompatible drivers. Windows Update safer."
    },
    "SlimDrivers": {
        "type": "PUP/Driver Updater",
        "detection": ["SlimDrivers"],
        "reason": "Driver updater that can cause system instability. Often bundled with PUPs."
    },
    "Slimware Utilities": {
        "type": "PUP/Optimizer",
        "detection": ["Slimware Utilities", "DriverUpdate"],
        "reason": "Suite of questionable utilities. Shows false problems. Installs bundled software."
    },
    "WinZip Driver Updater": {
        "type": "PUP/Driver Updater",
        "detection": ["WinZip Driver Updater"],
        "reason": "Unrelated to real WinZip. Shows fake driver issues. Potentially causes hardware problems."
    },
    "Driver Support": {
        "type": "PUP/Driver Updater",
        "detection": ["Driver Support", "Asurvio"],
        "reason": "Aggressive driver updater with scare tactics. Can install wrong drivers causing system issues."
    },
    
    # Toolbars and Browser Hijackers
    "Ask Toolbar": {
        "type": "Adware/Browser Hijacker",
        "detection": ["Ask Toolbar", "Updater by Ask", "Ask.com"],
        "reason": "Browser hijacker changing search engine and homepage. Tracks browsing. Very hard to remove completely."
    },
    "MyWay": {
        "type": "Browser Hijacker/Malware",
        "detection": ["MyWay", "MindSpark"],
        "reason": "Aggressive browser hijacker. Changes settings, tracks browsing, shows ads. Difficult to remove."
    },
    "Conduit": {
        "type": "Adware/Browser Hijacker",
        "detection": ["Conduit", "Search Protect"],
        "reason": "Browser hijacker modifying search and homepages. Tracks user data. Spreads via bundleware."
    },
    "SweetIM": {
        "type": "Adware/Spyware",
        "detection": ["SweetIM"],
        "reason": "Adware and spyware bundle. Changes browser settings. Tracks browsing behavior for ads."
    },
    "RelevantKnowledge": {
        "type": "Spyware",
        "detection": ["RelevantKnowledge"],
        "reason": "Market research spyware tracking all browsing. Installed secretly via bundles. Privacy violation."
    },
    "DealPly": {
        "type": "Adware",
        "detection": ["DealPly"],
        "reason": "Adware showing unwanted shopping ads. Tracks browsing. Changes browser settings."
    },
    "Snap.do": {
        "type": "Browser Hijacker",
        "detection": ["Snap.do"],
        "reason": "Browser hijacker changing search engine. Tracks searches. Difficult to remove."
    },
    "Funmoods": {
        "type": "Adware/Browser Hijacker",
        "detection": ["Funmoods"],
        "reason": "Browser hijacker with emoticon toolbar. Changes homepage and search. Tracks data."
    },
    "Yontoo": {
        "type": "Adware",
        "detection": ["Yontoo"],
        "reason": "Adware injecting shopping ads into websites. Tracks browsing. Browser extension malware."
    },
    "Crossrider": {
        "type": "Adware Platform",
        "detection": ["Crossrider"],
        "reason": "Adware platform used by many malicious extensions. Injects ads into web pages."
    },
    "Babylon": {
        "type": "Adware/Browser Hijacker",
        "detection": ["Babylon"],
        "reason": "Toolbar and search hijacker. Changes browser settings. Hard to remove completely."
    },
    "Delta Search": {
        "type": "Browser Hijacker",
        "detection": ["Delta Search"],
        "reason": "Search hijacker replacing default search engine. Tracks searches. Distributed via bundleware."
    },
    "Spigot": {
        "type": "Adware",
        "detection": ["Spigot"],
        "reason": "Adware platform installing browser extensions and toolbars. Difficult to remove."
    },
    
    # Office and Compression Tools (Trial/Bloatware)
    "Microsoft Office": {
        "type": "Trialware",
        "detection": ["Microsoft Office 365", "Microsoft 365"],
        "reason": "Trial version with constant upgrade prompts. Should be user-installed if needed. Free alternatives exist."
    },
    "WinZip": {
        "type": "Bloatware/Nagware",
        "detection": ["WinZip"],
        "reason": "Paid compression tool when Windows has built-in support. Constant nag screens. Free alternatives better."
    },
    "WPS Office": {
        "type": "Bloatware/Adware",
        "detection": ["WPS Office"],
        "reason": "Office suite with ads. Privacy concerns with data collection. Better free alternatives exist."
    },
    "Dropbox": {
        "type": "Bloatware",
        "detection": ["Dropbox OEM"],
        "reason": "Cloud storage preinstalled by OEMs. Should be user choice. Uses resources for background sync."
    },
    "Evernote": {
        "type": "Bloatware",
        "detection": ["Evernote OEM"],
        "reason": "Note-taking app. Often preinstalled as bloatware. Limited free tier. User should choose."
    },
    
    # Gaming and Multimedia Bloatware
    "WildTangent Games": {
        "type": "Bloatware/Adware",
        "detection": ["WildTangent"],
        "reason": "Game portal preinstalled by OEMs. Trial games with purchase prompts. Takes significant disk space."
    },
    "CyberLink": {
        "type": "Bloatware",
        "detection": ["CyberLink"],
        "reason": "Media software suite. Trial versions with limited features. Better free alternatives available."
    },
    "Roxio": {
        "type": "Bloatware",
        "detection": ["Roxio"],
        "reason": "CD/DVD burning software. Mostly obsolete technology. Windows has built-in burning capability."
    },
    "Nero": {
        "type": "Bloatware",
        "detection": ["Nero"],
        "reason": "Burning and media suite. Bloated, expensive. Mostly unnecessary with modern Windows."
    },
    
    # OEM Bloatware - Manufacturer Software
    "HP Support Assistant": {
        "type": "Bloatware/Resource Hog",
        "detection": ["HP Support Assistant"],
        "reason": "HP utility that uses excessive resources. Constant background updates. Most features accessible via Windows."
    },
    "HP JumpStart": {
        "type": "Bloatware",
        "detection": ["HP JumpStart"],
        "reason": "HP setup wizard. Only needed once. Takes space and resources after initial setup."
    },
    "HP Audio Switch": {
        "type": "Bloatware",
        "detection": ["HP Audio Switch"],
        "reason": "HP audio utility. Windows audio settings sufficient. Unnecessary extra layer."
    },
    "HP Connection Optimizer": {
        "type": "Bloatware",
        "detection": ["HP Connection Optimizer"],
        "reason": "HP network utility. Dubious benefit. May interfere with network settings."
    },
    "HP Command Center": {
        "type": "Bloatware",
        "detection": ["HP Command Center", "OMEN Command Center"],
        "reason": "HP system control utility. Uses resources. Most features accessible through Windows."
    },
    "HP Touchpoint Analytics": {
        "type": "Spyware/Telemetry",
        "detection": ["HP Touchpoint Analytics Client"],
        "reason": "HP telemetry collecting usage data. Privacy concern. Sends data to HP servers without clear benefit to user."
    },
    "Dell SupportAssist": {
        "type": "Bloatware/Security Risk",
        "detection": ["Dell SupportAssist"],
        "reason": "Dell utility with history of security vulnerabilities. Uses resources. Most features redundant with Windows."
    },
    "Dell Update": {
        "type": "Bloatware",
        "detection": ["Dell Update", "Dell Digital Delivery"],
        "reason": "Dell update utility. Windows Update handles most drivers. Redundant software."
    },
    "Dell Customer Connect": {
        "type": "Bloatware/Telemetry",
        "detection": ["Dell Customer Connect"],
        "reason": "Dell feedback and telemetry tool. Collects usage data. No benefit to user."
    },
    "Dell Mobile Connect": {
        "type": "Bloatware",
        "detection": ["Dell Mobile Connect"],
        "reason": "Phone integration app. Works on specific Dell models only. Limited usefulness."
    },
    "Lenovo Vantage": {
        "type": "Utility/Bloatware",
        "detection": ["Lenovo Vantage"],
        "reason": "Lenovo system utility. Some features useful but uses significant resources. Ads and notifications."
    },
    "Lenovo Solution Center": {
        "type": "Bloatware",
        "detection": ["Lenovo Solution Center"],
        "reason": "Older Lenovo utility. Redundant with Windows tools. Uses resources unnecessarily."
    },
    "Lenovo Accelerator": {
        "type": "Bloatware/Vulnerability",
        "detection": ["Lenovo Accelerator Application"],
        "reason": "Lenovo app with past security vulnerabilities. Minimal benefit. Resource usage."
    },
    "Lenovo App Explorer": {
        "type": "Bloatware/Adware",
        "detection": ["Lenovo App Explorer"],
        "reason": "Lenovo app store promoting software installs. Bloatware that suggests more bloatware."
    },
    "ASUS GiftBox": {
        "type": "Bloatware/Adware",
        "detection": ["ASUS GiftBox", "ASUS AppDeals"],
        "reason": "ASUS promotion tool suggesting software. Bloatware promoting more bloatware. Ads and unwanted suggestions."
    },
    "ASUS Live Update": {
        "type": "Bloatware/Security Risk",
        "detection": ["ASUS Live Update"],
        "reason": "ASUS update utility with past security issues. Windows Update more secure. Potential vulnerability."
    },
    "MyASUS": {
        "type": "Bloatware",
        "detection": ["MyASUS", "ASUS System Control Interface"],
        "reason": "ASUS system utility. Most features redundant. Uses background resources."
    },
    "Acer Care Center": {
        "type": "Bloatware",
        "detection": ["Acer Care Center"],
        "reason": "Acer system utility. Redundant diagnostic tools. Uses resources."
    },
    "Acer Product Registration": {
        "type": "Bloatware",
        "detection": ["Acer Product Registration"],
        "reason": "One-time registration tool. No need to keep installed. Pure bloatware after registration."
    },
    "Acer Portal": {
        "type": "Bloatware",
        "detection": ["Acer BYOC Apps", "abDocs", "abFiles"],
        "reason": "Acer cloud apps. Redundant with Windows and cloud services. Privacy concerns."
    },
    "MSI Dragon Center": {
        "type": "Bloatware/Resource Hog",
        "detection": ["MSI Dragon Center"],
        "reason": "MSI gaming utility. Heavy resource usage. Many features accessible through Windows."
    },
    "MSI App Player": {
        "type": "Bloatware",
        "detection": ["MSI App Player"],
        "reason": "Android emulator by MSI. Large disk space usage. User should install if needed."
    },
    "Samsung Settings": {
        "type": "Bloatware",
        "detection": ["Samsung Settings", "Samsung Update"],
        "reason": "Samsung utilities. Redundant with Windows settings. Update tool less reliable than Windows Update."
    },
    "VAIO Care": {
        "type": "Bloatware",
        "detection": ["VAIO Care", "VAIO Control Center"],
        "reason": "VAIO system utilities. Mostly obsolete. Redundant with modern Windows."
    },
    "Armoury Crate": {
        "type": "Bloatware/Persistent",
        "detection": ["Armoury Crate", "ArmouryCrateInstaller"],
        "reason": "ASUS RGB and system control. Very difficult to remove completely. Uses excessive resources. Known for reinstalling itself."
    },
    
    # Dangerous Software
    "KMSPico": {
        "type": "HackTool/Trojan",
        "detection": ["KMSPico", "KMSpico Portable"],
        "reason": "ILLEGAL Windows/Office activation tool. Often contains trojans and malware. Steals system access. Violates Microsoft license."
    },
    "Hola VPN": {
        "type": "Malicious VPN",
        "detection": ["Hola VPN"],
        "reason": "VPN that sells your bandwidth to others. Turns your PC into exit node for strangers. Major security and privacy risk."
    },
}


def get_software_info(software_name):
    """
    Get detailed information about a specific software
    
    Args:
        software_name (str): Name of the software
    
    Returns:
        dict: Software information including type, detection patterns, and reason
    """
    return TARGET_SOFTWARE.get(software_name, None)


def get_all_detection_patterns():
    """
    Get all detection patterns from the database
    
    Returns:
        list: List of all detection patterns
    """
    patterns = []
    for software_data in TARGET_SOFTWARE.values():
        patterns.extend(software_data["detection"])
    return patterns


def get_software_by_type(software_type):
    """
    Get all software of a specific type
    
    Args:
        software_type (str): Type of software (e.g., "Bloatware", "Adware", etc.)
    
    Returns:
        dict: Dictionary of software matching the type
    """
    return {
        name: data for name, data in TARGET_SOFTWARE.items()
        if software_type.lower() in data["type"].lower()
    }


def get_software_count():
    """
    Get total count of software in database
    
    Returns:
        int: Total number of software entries
    """
    return len(TARGET_SOFTWARE)
