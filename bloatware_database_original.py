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
        "reason": "VPN that sells your bandwidth to others. Turns your PC into exit node for strangers. Major security and privacy risk.",
        "files": ["C:\\Program Files\\Hola", "C:\\Program Files (x86)\\Hola"],
        "registry": ["HKLM\\SOFTWARE\\Hola", "HKCU\\SOFTWARE\\Hola"],
        "services": ["HolaVPNService"]
    },
    
    # Additional Bloatware - Expanding Database
    "Avast Free Antivirus": {
        "type": "Bloatware/Aggressive AV",
        "detection": ["Avast", "Avast Free Antivirus"],
        "reason": "Free antivirus with very aggressive advertising and data collection. Caught selling user browsing data. Installs browser extensions without clear consent. Resource heavy.",
        "files": ["C:\\Program Files\\Avast Software", "C:\\ProgramData\\Avast Software"],
        "registry": ["HKLM\\SOFTWARE\\Avast Software", "HKLM\\SOFTWARE\\AVAST Software"],
        "services": ["avast! Antivirus", "AvastSvc"]
    },
    "AVG Free": {
        "type": "Bloatware/Aggressive AV",
        "detection": ["AVG", "AVG Free", "AVG AntiVirus Free"],
        "reason": "Sister product of Avast with same privacy issues. Aggressive upselling. Collects and shares user data. Better free alternatives exist.",
        "files": ["C:\\Program Files\\AVG", "C:\\ProgramData\\AVG"],
        "registry": ["HKLM\\SOFTWARE\\AVG", "HKLM\\SOFTWARE\\AVG Technologies"],
        "services": ["AVG Antivirus", "avgfws"]
    },
    "Opera Browser": {
        "type": "Bloatware/Privacy Risk",
        "detection": ["Opera", "Opera Browser", "Opera Stable"],
        "reason": "Browser owned by Chinese consortium. Privacy concerns with data collection. Often preinstalled as bloatware. Built-in VPN logs data.",
        "files": ["C:\\Program Files\\Opera", "C:\\Users\\*\\AppData\\Local\\Programs\\Opera"],
        "registry": ["HKLM\\SOFTWARE\\Opera Software", "HKCU\\SOFTWARE\\Opera Software"],
        "services": ["OperaUpdate"]
    },
    "Brave Browser Trial": {
        "type": "Bloatware",
        "detection": ["Brave Trial", "Brave Browser OEM"],
        "reason": "While Brave itself is fine, OEM trial versions are bloatware. Should be user choice to install. Preinstalled versions may have promotional deals.",
        "files": ["C:\\Program Files\\BraveSoftware\\Brave-Browser-Trial"],
        "registry": ["HKLM\\SOFTWARE\\BraveSoftware\\Trial"],
        "services": []
    },
    "Avira Free Security": {
        "type": "PUP/Aggressive AV",
        "detection": ["Avira", "Avira Free Security", "Avira Antivirus"],
        "reason": "Aggressive popups and upselling. Installs browser extensions and search modifications. Resource intensive. Privacy concerns with data sharing.",
        "files": ["C:\\Program Files (x86)\\Avira", "C:\\ProgramData\\Avira"],
        "registry": ["HKLM\\SOFTWARE\\Avira", "HKLM\\SOFTWARE\\WOW6432Node\\Avira"],
        "services": ["Avira.ServiceHost", "AntiVirService"]
    },
    "Bitdefender Free": {
        "type": "Trialware/Nagware",
        "detection": ["Bitdefender Free", "Bitdefender Antivirus Free"],
        "reason": "Free version with constant upgrade prompts. Limited functionality to push paid version. Better alternatives available.",
        "files": ["C:\\Program Files\\Bitdefender", "C:\\ProgramData\\Bitdefender"],
        "registry": ["HKLM\\SOFTWARE\\Bitdefender"],
        "services": ["VSSERV", "BdDesktopParental"]
    },
    "Malwarebytes Trial": {
        "type": "Trialware",
        "detection": ["Malwarebytes Trial", "Malwarebytes OEM"],
        "reason": "Trial version preinstalled by OEMs. Constant upgrade nags. Should be user-installed if needed. Free version sufficient for most users.",
        "files": ["C:\\Program Files\\Malwarebytes OEM"],
        "registry": ["HKLM\\SOFTWARE\\Malwarebytes\\OEM"],
        "services": ["MBAMService"]
    },
    "Search Baron": {
        "type": "Browser Hijacker/Malware",
        "detection": ["Search Baron", "SearchBaron"],
        "reason": "Malicious browser hijacker. Changes search engine and homepage. Extremely difficult to remove. Tracks browsing behavior.",
        "files": ["C:\\Users\\*\\AppData\\Local\\SearchBaron", "C:\\ProgramData\\SearchBaron"],
        "registry": ["HKCU\\SOFTWARE\\SearchBaron", "HKLM\\SOFTWARE\\SearchBaron"],
        "services": []
    },
    "Chromium Malware Variants": {
        "type": "Malware/Fake Browser",
        "detection": ["Chromium Browser Malware", "Fake Chrome Update", "Chromium Virus"],
        "reason": "Fake Chromium browsers bundled with malware. Not the legitimate Chromium. Changes browser settings, shows ads, tracks data. NOTE: This targets only malicious variants found in suspicious locations, not legitimate Chromium installations.",
        "files": ["C:\\Users\\*\\AppData\\Local\\Chromium\\Application\\chrome.exe"],
        "registry": ["HKCU\\SOFTWARE\\Chromium"],
        "services": []
    },
    "PC Optimizer Pro": {
        "type": "PUP/Scareware",
        "detection": ["PC Optimizer Pro", "PCOptimizerPro"],
        "reason": "Fake optimizer showing false system problems. Scareware tactics. No real optimization performed. Difficult to uninstall.",
        "files": ["C:\\Program Files\\PC Optimizer Pro", "C:\\Program Files (x86)\\PC Optimizer Pro"],
        "registry": ["HKLM\\SOFTWARE\\PC Optimizer Pro"],
        "services": ["PCOptimizerProService"]
    },
    "MyCleanPC": {
        "type": "PUP/Scareware",
        "detection": ["MyCleanPC", "My Clean PC"],
        "reason": "Aggressive optimizer with false positives. Heavy advertising. Expensive subscription for minimal benefit. Windows built-in tools better.",
        "files": ["C:\\Program Files\\MyCleanPC"],
        "registry": ["HKLM\\SOFTWARE\\MyCleanPC"],
        "services": ["MyCleanPCService"]
    },
    "iolo System Mechanic": {
        "type": "PUP/Aggressive Optimizer",
        "detection": ["iolo", "System Mechanic"],
        "reason": "Aggressive system optimizer with questionable benefits. Expensive. Constant upgrade prompts. May cause more problems than it solves.",
        "files": ["C:\\Program Files\\iolo", "C:\\ProgramData\\iolo"],
        "registry": ["HKLM\\SOFTWARE\\iolo"],
        "services": ["ioloSystemService"]
    },
    "Ashampoo WinOptimizer": {
        "type": "Bloatware/Trialware",
        "detection": ["Ashampoo WinOptimizer", "Ashampoo"],
        "reason": "Trial optimizer preinstalled by OEMs. Limited trial features. Constant nags. Modern Windows doesn't need such tools.",
        "files": ["C:\\Program Files\\Ashampoo", "C:\\Program Files (x86)\\Ashampoo"],
        "registry": ["HKLM\\SOFTWARE\\Ashampoo"],
        "services": []
    },
    "Norton Utilities": {
        "type": "PUP/Expensive Optimizer",
        "detection": ["Norton Utilities", "Norton 360 Utilities"],
        "reason": "Expensive optimizer by Norton. Aggressive renewal tactics. Questionable performance improvements. Windows tools sufficient.",
        "files": ["C:\\Program Files\\Norton Utilities"],
        "registry": ["HKLM\\SOFTWARE\\Norton\\Utilities"],
        "services": ["NortonUtilities"]
    },
    "Glary Utilities": {
        "type": "Bloatware/Optimizer",
        "detection": ["Glary Utilities", "Glarysoft"],
        "reason": "System utility suite often bundled. Some features useful but many unnecessary. Can cause registry issues. Free version has ads.",
        "files": ["C:\\Program Files\\Glary Utilities", "C:\\Program Files (x86)\\Glary Utilities 5"],
        "registry": ["HKLM\\SOFTWARE\\Glarysoft"],
        "services": ["GUBootService"]
    },
    "Auslogics BoostSpeed": {
        "type": "PUP/Aggressive Optimizer",
        "detection": ["Auslogics BoostSpeed", "Auslogics"],
        "reason": "Aggressive system optimizer. Installs browser extensions. False positives to scare users. Expensive license for questionable benefits.",
        "files": ["C:\\Program Files\\Auslogics", "C:\\ProgramData\\Auslogics"],
        "registry": ["HKLM\\SOFTWARE\\Auslogics"],
        "services": ["AuslogicsBoostSpeedService"]
    },
    "WinThruster": {
        "type": "PUP/Registry Cleaner",
        "detection": ["WinThruster", "Solvusoft"],
        "reason": "Registry cleaner that can damage Windows. Shows false errors. Expensive. Windows doesn't benefit from registry cleaning.",
        "files": ["C:\\Program Files\\Solvusoft\\WinThruster"],
        "registry": ["HKLM\\SOFTWARE\\Solvusoft\\WinThruster"],
        "services": []
    },
    "Wise Registry Cleaner": {
        "type": "Risky Utility",
        "detection": ["Wise Registry Cleaner", "WiseRegCleaner"],
        "reason": "Registry cleaner that can cause system instability. Modern Windows self-maintains registry. Risk of breaking system outweighs benefits.",
        "files": ["C:\\Program Files\\Wise", "C:\\Program Files (x86)\\Wise"],
        "registry": ["HKLM\\SOFTWARE\\WiseCleaner"],
        "services": []
    },
    "IObit Uninstaller": {
        "type": "Bloatware/Bundleware",
        "detection": ["IObit Uninstaller", "IObit"],
        "reason": "Uninstaller tool that often comes bundled. Installs other IObit products. Aggressive advertising. Windows uninstaller sufficient.",
        "files": ["C:\\Program Files\\IObit", "C:\\ProgramData\\IObit"],
        "registry": ["HKLM\\SOFTWARE\\IObit"],
        "services": ["IObitUnSvc", "LiveUpdate"]
    },
    "Smart Defrag": {
        "type": "Bloatware/Unnecessary",
        "detection": ["Smart Defrag", "IObit Smart Defrag"],
        "reason": "Defragmentation tool unnecessary for modern systems with SSDs. Can damage SSDs if used. Windows has built-in defrag.",
        "files": ["C:\\Program Files\\IObit\\Smart Defrag"],
        "registry": ["HKLM\\SOFTWARE\\IObit\\Smart Defrag"],
        "services": ["SmartDefragService"]
    },
    "360 Total Security": {
        "type": "PUP/Chinese Software",
        "detection": ["360 Total Security", "360 Security"],
        "reason": "Chinese security software with privacy concerns. Data collection unclear. Better alternatives available. Often bundled without consent.",
        "files": ["C:\\Program Files\\360", "C:\\Program Files (x86)\\360"],
        "registry": ["HKLM\\SOFTWARE\\360Safe", "HKLM\\SOFTWARE\\Qihoo"],
        "services": ["360rps", "360fsflt"]
    },
    "Baidu Antivirus": {
        "type": "PUP/Privacy Risk",
        "detection": ["Baidu Antivirus", "Baidu"],
        "reason": "Chinese antivirus with serious privacy concerns. Sends data to Chinese servers. Often installed without consent. Difficult to remove.",
        "files": ["C:\\Program Files\\Baidu Security", "C:\\Program Files (x86)\\Baidu"],
        "registry": ["HKLM\\SOFTWARE\\Baidu"],
        "services": ["BaiduProtect", "BaiduAn"]
    },
    "Tencent PC Manager": {
        "type": "Bloatware/Privacy Risk",
        "detection": ["Tencent PC Manager", "QQPCMgr"],
        "reason": "Chinese system utility. Privacy concerns with data collection. Installs without clear consent. Sends telemetry to Chinese servers.",
        "files": ["C:\\Program Files\\Tencent", "C:\\Program Files (x86)\\Tencent"],
        "registry": ["HKLM\\SOFTWARE\\Tencent"],
        "services": ["QQPCRTP"]
    },
    "Weather Bug": {
        "type": "Adware",
        "detection": ["WeatherBug", "Weather Bug"],
        "reason": "Weather app that shows ads. Tracks user behavior. Preinstalled bloatware. Web weather sites work better without tracking.",
        "files": ["C:\\Program Files\\WeatherBug", "C:\\Program Files (x86)\\AWS"],
        "registry": ["HKLM\\SOFTWARE\\WeatherBug"],
        "services": ["WeatherBugService"]
    },
    "PC Health Kit": {
        "type": "PUP/Scareware",
        "detection": ["PC Health Kit", "PCHealthKit"],
        "reason": "Fake system health tool showing false warnings. Scareware tactics to sell product. No real system improvements.",
        "files": ["C:\\Program Files\\PC Health Kit"],
        "registry": ["HKLM\\SOFTWARE\\PC Health Kit"],
        "services": []
    },
    "System Healer": {
        "type": "PUP/Scareware",
        "detection": ["System Healer", "SystemHealer"],
        "reason": "Rogue system optimizer. False scan results. Aggressive popups. Expensive and ineffective. Classified as PUP by many AV vendors.",
        "files": ["C:\\Program Files\\SystemHealer"],
        "registry": ["HKLM\\SOFTWARE\\SystemHealer"],
        "services": []
    },
    "Advanced PC Care": {
        "type": "PUP/Scareware",
        "detection": ["Advanced PC Care", "AdvancedPCCare"],
        "reason": "Fake PC optimization tool. Shows false errors to scare users. Expensive license. No real system improvements.",
        "files": ["C:\\Program Files\\Advanced PC Care"],
        "registry": ["HKLM\\SOFTWARE\\Advanced PC Care"],
        "services": []
    },
    "SpeedMaxPc": {
        "type": "PUP/Scareware",
        "detection": ["SpeedMaxPc", "Speed Max PC"],
        "reason": "Rogue optimizer with false positives. Aggressive advertising. Difficult to uninstall. No performance benefits.",
        "files": ["C:\\Program Files\\SpeedMaxPc"],
        "registry": ["HKLM\\SOFTWARE\\SpeedMaxPc"],
        "services": []
    },
    "WinZip System Utilities": {
        "type": "PUP/Optimizer",
        "detection": ["WinZip System Utilities Suite", "WinZip Utilities"],
        "reason": "Unrelated to real WinZip. Shows false system issues. Expensive subscription. No real optimization.",
        "files": ["C:\\Program Files\\WinZip System Utilities Suite"],
        "registry": ["HKLM\\SOFTWARE\\WinZip Computing\\WinZip System Utilities Suite"],
        "services": []
    },
    "MacKeeper": {
        "type": "PUP/Mac Scareware",
        "detection": ["MacKeeper", "Kromtech"],
        "reason": "Notorious Mac scareware (if found on Windows, it's a sign of infection). Aggressive marketing. False positives. Difficult to remove.",
        "files": [],
        "registry": [],
        "services": []
    },
    "PC Cleaner Pro": {
        "type": "PUP/Scareware",
        "detection": ["PC Cleaner Pro", "PCCleanerPro"],
        "reason": "Fake cleaner showing false system problems. No real cleaning performed. Expensive. Classified as PUP.",
        "files": ["C:\\Program Files\\PC Cleaner Pro"],
        "registry": ["HKLM\\SOFTWARE\\PC Cleaner Pro"],
        "services": []
    },
    "Uniblue": {
        "type": "PUP/Scareware",
        "detection": ["Uniblue", "DriverScanner", "PowerSuite"],
        "reason": "Suite of questionable utilities. False scan results. Expensive licenses. Can cause system issues. Better alternatives exist.",
        "files": ["C:\\Program Files\\Uniblue", "C:\\Program Files (x86)\\Uniblue"],
        "registry": ["HKLM\\SOFTWARE\\Uniblue"],
        "services": ["UbDriver"]
    },
    "PC Fix Speed": {
        "type": "PUP/Scareware",
        "detection": ["PC Fix Speed", "PCFixSpeed"],
        "reason": "Rogue PC repair tool. Shows fake errors. No real fixes. Scareware tactics. Expensive.",
        "files": ["C:\\Program Files\\PC Fix Speed"],
        "registry": ["HKLM\\SOFTWARE\\PC Fix Speed"],
        "services": []
    },
    "Windows Malware Defender": {
        "type": "Rogue AV/Malware",
        "detection": ["Windows Malware Defender", "Win Malware Defender"],
        "reason": "FAKE antivirus mimicking Windows Defender. Shows false threats. Attempts to steal payment info. Pure malware.",
        "files": ["C:\\Program Files\\Windows Malware Defender"],
        "registry": ["HKLM\\SOFTWARE\\Windows Malware Defender"],
        "services": []
    },
    "Windows Security Alert": {
        "type": "Scareware/Malware",
        "detection": ["Windows Security Alert", "Windows Defender Alert"],
        "reason": "FAKE security warning malware. Not related to real Windows Security. Shows false threats. Attempts payment theft.",
        "files": [],
        "registry": ["HKCU\\SOFTWARE\\Windows Security Alert"],
        "services": []
    },
    "System Progressive Protection": {
        "type": "Rogue AV/Malware",
        "detection": ["System Progressive Protection"],
        "reason": "Notorious rogue antivirus. Prevents legitimate program execution. Shows fake threats. Demands payment. Very malicious.",
        "files": ["C:\\Program Files\\System Progressive Protection"],
        "registry": ["HKLM\\SOFTWARE\\System Progressive Protection"],
        "services": []
    },
    "Antivirus Live": {
        "type": "Rogue AV/Malware",
        "detection": ["Antivirus Live", "AV Live"],
        "reason": "Fake antivirus showing false threats. Blocks legitimate software. Demands payment. Classified as malware.",
        "files": [],
        "registry": ["HKCU\\SOFTWARE\\Antivirus Live"],
        "services": []
    },
    "Smart Fortress": {
        "type": "Rogue AV/Malware",
        "detection": ["Smart Fortress", "SmartFortress"],
        "reason": "Rogue security software. False threat warnings. Prevents program execution. Payment scam.",
        "files": [],
        "registry": ["HKLM\\SOFTWARE\\Smart Fortress"],
        "services": []
    },
    "Antimalware Doctor": {
        "type": "Rogue AV/Malware",
        "detection": ["Antimalware Doctor"],
        "reason": "Famous rogue antivirus. Shows fake infections. Blocks system access. Steals payment information.",
        "files": [],
        "registry": ["HKCU\\SOFTWARE\\Antimalware Doctor"],
        "services": []
    },
    "Privacy Protection": {
        "type": "Rogue Security/Malware",
        "detection": ["Privacy Protection", "PrivacyProtection"],
        "reason": "Rogue privacy tool showing fake privacy issues. Scareware. Demands payment. No real protection.",
        "files": [],
        "registry": ["HKLM\\SOFTWARE\\Privacy Protection"],
        "services": []
    },
    "Windows Protection Suite": {
        "type": "Rogue AV/Malware",
        "detection": ["Windows Protection Suite"],
        "reason": "Fake Windows security tool. Shows false threats. Not from Microsoft. Payment scam malware.",
        "files": [],
        "registry": ["HKLM\\SOFTWARE\\Windows Protection Suite"],
        "services": []
    },
    "Search Protect by Conduit": {
        "type": "Browser Hijacker/Adware",
        "detection": ["Search Protect", "SearchProtect"],
        "reason": "Browser hijacker preventing search engine changes. Tracks browsing. Very difficult to remove. Changes browser settings persistently.",
        "files": ["C:\\Program Files\\SearchProtect", "C:\\Program Files (x86)\\SearchProtect"],
        "registry": ["HKLM\\SOFTWARE\\SearchProtect"],
        "services": ["CltMngSvc"]
    },
    "Browser Modifier": {
        "type": "Browser Hijacker",
        "detection": ["Browser Modifier", "BrowserModifier"],
        "reason": "Generic browser hijacker. Changes homepage and search engine. Shows ads. Tracks browsing behavior.",
        "files": ["C:\\Program Files\\BrowserModifier"],
        "registry": ["HKLM\\SOFTWARE\\BrowserModifier"],
        "services": []
    },
    "Websearch": {
        "type": "Browser Hijacker",
        "detection": ["Websearch", "WebSearch Toolbar"],
        "reason": "Search hijacker redirecting searches. Injects ads into search results. Tracks user queries. Difficult to remove.",
        "files": ["C:\\Program Files\\Websearch"],
        "registry": ["HKLM\\SOFTWARE\\Websearch"],
        "services": []
    },
    "StartPage Toolbar": {
        "type": "Browser Hijacker/Adware",
        "detection": ["StartPage", "StartPage Toolbar"],
        "reason": "Toolbar changing homepage and new tab page. Not the legitimate startpage.com. Shows ads and tracks browsing.",
        "files": ["C:\\Program Files\\StartPage"],
        "registry": ["HKLM\\SOFTWARE\\StartPage"],
        "services": []
    },
    "Trovi Search": {
        "type": "Browser Hijacker",
        "detection": ["Trovi", "Trovi Search"],
        "reason": "Browser hijacker by Conduit. Changes search engine to trovi.com. Tracks searches. Injects ads.",
        "files": ["C:\\Program Files\\Trovi"],
        "registry": ["HKLM\\SOFTWARE\\Trovi"],
        "services": []
    },
    "iLivid": {
        "type": "Adware/PUP",
        "detection": ["iLivid", "iLivid Download Manager"],
        "reason": "Download manager bundling adware. Changes browser settings. Installs toolbars. Tracks user behavior.",
        "files": ["C:\\Program Files\\iLivid"],
        "registry": ["HKLM\\SOFTWARE\\iLivid"],
        "services": []
    },
    "Wajam": {
        "type": "Adware/Browser Hijacker",
        "detection": ["Wajam"],
        "reason": "Social recommendation adware. Injects ads into web pages. Tracks browsing. Changes search results.",
        "files": ["C:\\Program Files\\Wajam", "C:\\Program Files (x86)\\Wajam"],
        "registry": ["HKLM\\SOFTWARE\\Wajam"],
        "services": ["WajamUpdater"]
    },
    "Iminent": {
        "type": "Adware/Browser Hijacker",
        "detection": ["Iminent", "Iminent Toolbar"],
        "reason": "Toolbar and emoticon adware. Changes browser settings. Shows unwanted ads. Tracks browsing behavior.",
        "files": ["C:\\Program Files\\Iminent"],
        "registry": ["HKLM\\SOFTWARE\\Iminent"],
        "services": ["SProtection"]
    },
    "Optimizer Pro": {
        "type": "PUP/Scareware",
        "detection": ["Optimizer Pro", "OptimizerPro"],
        "reason": "Rogue optimizer by Iminent. False scan results. Bundles with other PUPs. No real optimization.",
        "files": ["C:\\Program Files\\Optimizer Pro"],
        "registry": ["HKLM\\SOFTWARE\\Optimizer Pro"],
        "services": []
    },
    "SaveSense": {
        "type": "Adware",
        "detection": ["SaveSense", "Save Sense"],
        "reason": "Shopping adware injecting coupons and ads. Tracks shopping behavior. Slows browser. Privacy concerns.",
        "files": ["C:\\Program Files\\SaveSense"],
        "registry": ["HKLM\\SOFTWARE\\SaveSense"],
        "services": []
    },
    "PriceMeter": {
        "type": "Adware",
        "detection": ["PriceMeter"],
        "reason": "Shopping comparison adware. Injects ads and popups. Tracks browsing and shopping. Slows system.",
        "files": ["C:\\Program Files\\PriceMeterLiveUpdate"],
        "registry": ["HKLM\\SOFTWARE\\PriceMeterLiveUpdate"],
        "services": []
    },
    "Shopper Pro": {
        "type": "Adware",
        "detection": ["Shopper Pro", "ShopperPro"],
        "reason": "Shopping adware showing unwanted deals. Tracks purchases. Injects ads into shopping sites.",
        "files": ["C:\\Program Files\\Shopper-Pro"],
        "registry": ["HKLM\\SOFTWARE\\Shopper-Pro"],
        "services": []
    },
    "Price Chopper": {
        "type": "Adware",
        "detection": ["Price Chopper", "PriceChopper"],
        "reason": "Adware injecting shopping ads. Tracks browsing. Modifies web pages to show coupons.",
        "files": [],
        "registry": ["HKCU\\SOFTWARE\\PriceChopper"],
        "services": []
    },
    "CouponBar": {
        "type": "Adware/Toolbar",
        "detection": ["CouponBar", "Coupon Bar"],
        "reason": "Toolbar showing coupon ads. Tracks shopping behavior. Changes browser settings.",
        "files": ["C:\\Program Files\\CouponBar"],
        "registry": ["HKLM\\SOFTWARE\\CouponBar"],
        "services": []
    },
    "Cinema Plus": {
        "type": "Adware",
        "detection": ["Cinema Plus", "CinemaPlus"],
        "reason": "Video adware showing popups. Injects ads into video streaming sites. Tracks viewing habits.",
        "files": [],
        "registry": ["HKCU\\SOFTWARE\\CinemaPlus"],
        "services": []
    },
    "Media Player Classic Codec Pack Malware": {
        "type": "Adware/Bundleware",
        "detection": ["MPC Codec Pack", "Codec Pack"],
        "reason": "Fake codec packs bundling adware. Not the legitimate codec pack. Installs toolbars and malware.",
        "files": ["C:\\Program Files\\Codec Pack"],
        "registry": ["HKLM\\SOFTWARE\\Codec Pack"],
        "services": []
    },
    "Video Converter Bundleware": {
        "type": "Adware/PUP",
        "detection": ["Free Video Converter", "VideoConverter"],
        "reason": "Free video converters often bundle adware. Install toolbars and change browser settings. Better alternatives exist.",
        "files": ["C:\\Program Files\\Free Video Converter"],
        "registry": ["HKLM\\SOFTWARE\\FreeVideoConverter"],
        "services": []
    },
    "DVDVideoSoft": {
        "type": "Bloatware/Bundleware",
        "detection": ["DVDVideoSoft", "Free Studio"],
        "reason": "Free media tools bundling browser extensions and toolbars. Aggressive installer. Changes browser settings.",
        "files": ["C:\\Program Files\\DVDVideoSoft", "C:\\Program Files (x86)\\DVDVideoSoft"],
        "registry": ["HKLM\\SOFTWARE\\DVDVideoSoft"],
        "services": []
    },
    "OpenCandy": {
        "type": "Adware Platform",
        "detection": ["OpenCandy"],
        "reason": "Bundleware platform used by many free software installers. Downloads and installs additional offers during installation.",
        "files": ["C:\\Users\\*\\AppData\\Roaming\\OpenCandy"],
        "registry": ["HKCU\\SOFTWARE\\OpenCandy"],
        "services": []
    },
    "Installcore": {
        "type": "Adware Platform/PUP",
        "detection": ["Installcore", "InstallCore"],
        "reason": "Bundleware installer installing unwanted software. Used by many free software distributors. Difficult to opt out.",
        "files": ["C:\\Program Files\\Installcore"],
        "registry": ["HKLM\\SOFTWARE\\Installcore"],
        "services": []
    },
    "Amonetize": {
        "type": "Adware Platform",
        "detection": ["Amonetize"],
        "reason": "Pay-per-install adware platform. Bundles PUPs with legitimate software. Installs multiple unwanted programs.",
        "files": [],
        "registry": ["HKCU\\SOFTWARE\\Amonetize"],
        "services": []
    },
    "Vittalia": {
        "type": "Adware Platform",
        "detection": ["Vittalia"],
        "reason": "Adware installer bundling unwanted software. Used by sketchy free software sites.",
        "files": [],
        "registry": ["HKCU\\SOFTWARE\\Vittalia"],
        "services": []
    },
    "Download Manager by 2squared": {
        "type": "Adware/PUP",
        "detection": ["2squared", "Download Manager"],
        "reason": "Fake download manager bundling adware. Not needed for downloads. Installs unwanted software.",
        "files": ["C:\\Program Files\\2Squared"],
        "registry": ["HKLM\\SOFTWARE\\2Squared"],
        "services": []
    },
    "GoPhoto.it": {
        "type": "Photo Viewer Bloatware",
        "detection": ["GoPhoto.it", "GoPhoto"],
        "reason": "Unnecessary photo viewer preinstalled. Basic features. Windows Photos app sufficient.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Fresh Paint": {
        "type": "Bloatware",
        "detection": ["Microsoft.FreshPaint", "Fresh Paint"],
        "reason": "Basic painting app preinstalled. Most users never use it. Better alternatives available.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Drawboard PDF": {
        "type": "Trial Bloatware",
        "detection": ["Drawboard PDF", "Drawboard"],
        "reason": "PDF viewer trial preinstalled. Limited free features. Adobe Reader or browser PDF viewer better.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Music Maker Jam": {
        "type": "Bloatware/Trialware",
        "detection": ["MAGIX.MusicMakerJam", "Music Maker Jam"],
        "reason": "Trial music making app. Limited free features. Preinstalled bloatware. Better DAWs available.",
        "files": [],
        "registry": [],
        "services": []
    },
    "March of Empires": {
        "type": "Adware/Juego",
        "detection": ["GAMELOFTSA.MarchofEmpires", "March of Empires"],
        "reason": "Mobile game with in-app purchases preinstalled. No place on a PC. Ads and microtransactions.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Minecraft: Windows 10 Edition Trial": {
        "type": "Trialware",
        "detection": ["Microsoft.MinecraftEducationEdition"],
        "reason": "Trial version of Minecraft. Should be user choice. Takes space without consent.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Mixed Reality Viewer": {
        "type": "Bloatware",
        "detection": ["Microsoft.Mixed Reality Viewer"],
        "reason": "VR viewer for those without VR headsets. Useless for most users. Wastes disk space.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Office Lens": {
        "type": "Bloatware",
        "detection": ["Microsoft.OfficeLens", "Office Lens"],
        "reason": "Document scanner app. More useful on mobile. Desktop has better alternatives.",
        "files": [],
        "registry": [],
        "services": []
    },
    "OneNote for Windows 10": {
        "type": "Bloatware",
        "detection": ["Microsoft.Office.OneNote", "OneNote"],
        "reason": "UWP version of OneNote. Desktop version better. Preinstalled without consent.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Paid Wi-Fi & Cellular": {
        "type": "Bloatware",
        "detection": ["Microsoft.OneConnect"],
        "reason": "App for paid mobile data plans. Useless for most users. Preinstalled bloatware.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Print3D": {
        "type": "Bloatware",
        "detection": ["Microsoft.Print3D"],
        "reason": "3D printing app. Only needed if you have 3D printer. Bloatware for most.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Skype UWP": {
        "type": "Bloatware",
        "detection": ["Microsoft.SkypeApp", "Skype"],
        "reason": "Preinstalled Skype. Most prefer desktop version or other chat apps. Runs in background.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Sticky Notes": {
        "type": "Bloatware",
        "detection": ["Microsoft.MicrosoftStickyNotes"],
        "reason": "Simple notes app. Many better alternatives. Bloatware if you don't use it.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Wallet": {
        "type": "Bloatware",
        "detection": ["Microsoft.Wallet"],
        "reason": "Digital wallet app. Limited merchant support. Most users prefer other payment methods.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Whiteboard": {
        "type": "Bloatware",
        "detection": ["Microsoft.Whiteboard", "Whiteboard"],
        "reason": "Digital whiteboard app. Niche use case. Better collaboration tools exist.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Zune Music": {
        "type": "Obsolete Bloatware",
        "detection": ["Microsoft.ZuneMusic", "Zune Music"],
        "reason": "Obsolete music player. Zune service dead. Groove Music replacement also discontinued.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Zune Video": {
        "type": "Obsolete Bloatware",
        "detection": ["Microsoft.ZuneVideo", "Zune Video"],
        "reason": "Obsolete video player. No longer supported. Better alternatives available.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Alarms & Clock": {
        "type": "Bloatware",
        "detection": ["Microsoft.WindowsAlarms", "Alarms & Clock"],
        "reason": "Basic alarm app. Phone does this better. Takes space most users don't need.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Calculator": {
        "type": "Core Utility (Optional)",
        "detection": ["Microsoft.WindowsCalculator"],
        "reason": "Windows Calculator. CORE UTILITY - Only remove if you have a preferred alternative. Most users should keep this. Only included for advanced users who want complete control.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Camera": {
        "type": "Bloatware",
        "detection": ["Microsoft.WindowsCamera", "Camera"],
        "reason": "Basic camera app. Most PCs don't have cameras or use better webcam software.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Groove Music": {
        "type": "Abandoned Bloatware",
        "detection": ["Microsoft.ZuneMusic", "Groove Music"],
        "reason": "Discontinued music service app. Microsoft killed Groove Music. No longer useful.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Microsoft Messaging": {
        "type": "Obsolete Bloatware",
        "detection": ["Microsoft.Messaging"],
        "reason": "Obsolete messaging app. Replaced by Your Phone. No longer maintained.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Maps": {
        "type": "Bloatware",
        "detection": ["Microsoft.WindowsMaps", "Maps"],
        "reason": "Windows Maps app. Google Maps in browser works better. Desktop maps rarely needed.",
        "files": [],
        "registry": [],
        "services": []
    },
    "People": {
        "type": "Bloatware",
        "detection": ["Microsoft.People", "People"],
        "reason": "Contact management app. Most use phone for contacts. Limited integration.",
        "files": [],
        "registry": [],
        "services": []
    },
    "Sound Recorder": {
        "type": "Bloatware",
        "detection": ["Microsoft.WindowsSoundRecorder", "Voice Recorder"],
        "reason": "Basic voice recorder. Better audio recording software available. Minimal features.",
        "files": [],
        "registry": [],
        "services": []
    },
    
    # Additional OEM and Regional Bloatware
    "Toshiba Service Station": {
        "type": "OEM Bloatware",
        "detection": ["TOSHIBA Service Station", "Toshiba Service"],
        "reason": "Toshiba update utility. Often redundant with Windows Update. Uses background resources.",
        "files": ["C:\\Program Files\\TOSHIBA"],
        "registry": ["HKLM\\SOFTWARE\\TOSHIBA"],
        "services": ["TMachInfo", "ToshibaServiceStation"]
    },
    "Toshiba Book Place": {
        "type": "OEM Bloatware",
        "detection": ["TOSHIBA Book Place"],
        "reason": "Toshiba e-book reader. Rarely used. Better e-reader apps available.",
        "files": ["C:\\Program Files\\TOSHIBA\\TOSHIBA Book Place"],
        "registry": [],
        "services": []
    },
    "Sony PlayMemories": {
        "type": "OEM Bloatware",
        "detection": ["PlayMemories Home", "Sony PlayMemories"],
        "reason": "Sony photo/video management. Resource intensive. Better alternatives exist.",
        "files": ["C:\\Program Files\\Sony\\PlayMemories Home"],
        "registry": ["HKLM\\SOFTWARE\\Sony\\PlayMemories Home"],
        "services": []
    },
    "Sony VAIO Update": {
        "type": "OEM Bloatware",
        "detection": ["VAIO Update", "Sony VAIO Update"],
        "reason": "Sony update utility. Often causes issues. Windows Update more reliable.",
        "files": ["C:\\Program Files\\Sony\\VAIO Update"],
        "registry": ["HKLM\\SOFTWARE\\Sony\\VAIO Update"],
        "services": ["VUAgent"]
    },
    "Fujitsu DeskUpdate": {
        "type": "OEM Bloatware",
        "detection": ["DeskUpdate", "Fujitsu DeskUpdate"],
        "reason": "Fujitsu update tool. Redundant with Windows Update. Resource usage.",
        "files": ["C:\\Program Files\\Fujitsu\\DeskUpdate"],
        "registry": ["HKLM\\SOFTWARE\\Fujitsu\\DeskUpdate"],
        "services": ["DeskUpdateService"]
    },
    "Panasonic PC Settings Utility": {
        "type": "OEM Bloatware",
        "detection": ["PC Settings Utility", "Panasonic PC Settings"],
        "reason": "Panasonic system utility. Most features accessible via Windows. Unnecessary.",
        "files": ["C:\\Program Files\\Panasonic"],
        "registry": ["HKLM\\SOFTWARE\\Panasonic"],
        "services": []
    },
    "Gateway Registration": {
        "type": "OEM Bloatware",
        "detection": ["Gateway Registration", "Gateway MyBackup"],
        "reason": "Gateway registration tool. Only needed once. Takes space after registration.",
        "files": ["C:\\Program Files\\Gateway"],
        "registry": ["HKLM\\SOFTWARE\\Gateway"],
        "services": []
    },
    "eMachines Registration": {
        "type": "OEM Bloatware",
        "detection": ["eMachines Registration", "eMachines Recovery Management"],
        "reason": "eMachines bloatware. One-time use tools taking permanent space.",
        "files": ["C:\\Program Files\\eMachines"],
        "registry": ["HKLM\\SOFTWARE\\eMachines"],
        "services": []
    },
    "Packard Bell InfoCentre": {
        "type": "OEM Bloatware",
        "detection": ["InfoCentre", "Packard Bell InfoCentre"],
        "reason": "Packard Bell system info tool. Redundant features. Resource usage.",
        "files": ["C:\\Program Files\\Packard Bell"],
        "registry": ["HKLM\\SOFTWARE\\Packard Bell"],
        "services": []
    },
    "Razer Synapse (OEM)": {
        "type": "OEM Bloatware",
        "detection": ["Razer Synapse OEM", "Razer Central"],
        "reason": "Razer device software preinstalled on non-Razer devices. User should install only if they have Razer peripherals.",
        "files": ["C:\\Program Files (x86)\\Razer"],
        "registry": ["HKLM\\SOFTWARE\\Razer"],
        "services": ["Razer Game Scanner Service", "Razer Central Service"]
    },
    "Logitech Gaming Software (OEM)": {
        "type": "OEM Bloatware",
        "detection": ["Logitech Gaming Software OEM"],
        "reason": "Logitech software preinstalled without Logitech devices. Should be user-installed when needed.",
        "files": ["C:\\Program Files\\Logitech Gaming Software"],
        "registry": ["HKLM\\SOFTWARE\\Logitech\\Logitech Gaming Software"],
        "services": []
    },
    "Intel Rapid Storage Technology": {
        "type": "Debatable OEM",
        "detection": ["Intel Rapid Storage Technology", "Intel RST"],
        "reason": "Intel storage driver GUI. Driver needed, GUI optional. Takes resources for rarely-used interface.",
        "files": ["C:\\Program Files\\Intel\\Intel(R) Rapid Storage Technology"],
        "registry": ["HKLM\\SOFTWARE\\Intel\\IntelIAStorUtilUI"],
        "services": ["IAStorDataMgrSvc"]
    },
    "Intel Optane Memory": {
        "type": "Conditional Bloatware",
        "detection": ["Intel Optane Memory", "Intel Optane"],
        "reason": "Only useful if system has Optane hardware. Bloatware on systems without it.",
        "files": ["C:\\Program Files\\Intel\\OptaneMemoryUI"],
        "registry": ["HKLM\\SOFTWARE\\Intel\\OptaneMemory"],
        "services": ["OptaneService"]
    },
    "AMD Ryzen Master (OEM)": {
        "type": "Conditional Bloatware",
        "detection": ["AMD Ryzen Master OEM"],
        "reason": "Overclocking utility. Only for enthusiasts. Preinstalled version bloatware for average users.",
        "files": ["C:\\Program Files\\AMD\\RyzenMaster"],
        "registry": ["HKLM\\SOFTWARE\\AMD\\RyzenMaster"],
        "services": ["AMDRyzenMasterDriver"]
    },
    "NVIDIA GeForce Experience (Bloat Components)": {
        "type": "Partial Bloatware",
        "detection": ["NVIDIA GeForce Experience", "NvContainer"],
        "reason": "Useful for drivers, but includes telemetry, mandatory login, and game recording most don't use. Privacy concerns.",
        "files": ["C:\\Program Files\\NVIDIA Corporation\\GeForce Experience"],
        "registry": ["HKLM\\SOFTWARE\\NVIDIA Corporation\\GeForce Experience"],
        "services": ["NvContainerLocalSystem", "NvTelemetryContainer"]
    },
    "Bonjour": {
        "type": "Apple Bloatware",
        "detection": ["Bonjour", "mDNSResponder"],
        "reason": "Apple networking service installed by iTunes/iCloud. Not needed if you don't use Apple services. Security vulnerabilities.",
        "files": ["C:\\Program Files\\Bonjour", "C:\\Program Files (x86)\\Bonjour"],
        "registry": ["HKLM\\SOFTWARE\\Apple Inc.\\Bonjour"],
        "services": ["Bonjour Service"]
    },
    "Apple Application Support": {
        "type": "Apple Bloatware",
        "detection": ["Apple Application Support"],
        "reason": "Support library for iTunes. Takes space even if iTunes uninstalled. Leftover bloatware.",
        "files": ["C:\\Program Files\\Common Files\\Apple\\Apple Application Support"],
        "registry": ["HKLM\\SOFTWARE\\Apple Inc."],
        "services": []
    },
    "Apple Software Update": {
        "type": "Apple Bloatware",
        "detection": ["Apple Software Update"],
        "reason": "Update utility for Apple software. Runs in background. Not needed if no Apple software installed.",
        "files": ["C:\\Program Files\\Apple Software Update", "C:\\Program Files (x86)\\Apple Software Update"],
        "registry": ["HKLM\\SOFTWARE\\Apple Inc.\\Apple Software Update"],
        "services": []
    },
    "Java Auto Updater": {
        "type": "Bloatware/Security Risk",
        "detection": ["Java Auto Updater", "Java Update Scheduler"],
        "reason": "Java updater running constantly. Security risk if outdated. Most users don't need Java. Disable if Java required.",
        "files": [],
        "registry": ["HKLM\\SOFTWARE\\JavaSoft"],
        "services": ["JavaQuickStarterService"]
    },
    "Adobe Acrobat Update Service": {
        "type": "Background Bloatware",
        "detection": ["AdobeARMservice", "Adobe Acrobat Update Service"],
        "reason": "Adobe Reader updater running 24/7. Resource usage. Manual updates sufficient.",
        "files": ["C:\\Program Files (x86)\\Common Files\\Adobe\\ARM"],
        "registry": ["HKLM\\SOFTWARE\\Adobe\\Adobe ARM"],
        "services": ["AdobeARMservice"]
    },
    "Adobe Creative Cloud (Trial)": {
        "type": "Trial Bloatware",
        "detection": ["Adobe Creative Cloud Trial", "Creative Cloud"],
        "reason": "Expensive Creative Cloud trial. Constant upgrade nags. Takes significant resources. Should be user-installed.",
        "files": ["C:\\Program Files\\Adobe\\Adobe Creative Cloud"],
        "registry": ["HKLM\\SOFTWARE\\Adobe\\Adobe Creative Cloud"],
        "services": ["AdobeUpdateService", "AGSService"]
    },
    "Google Update Service": {
        "type": "Background Service",
        "detection": ["Google Update", "GoogleUpdate"],
        "reason": "Google's update service for Chrome and other Google apps. Runs constantly. Manual updates alternative.",
        "files": ["C:\\Program Files (x86)\\Google\\Update"],
        "registry": ["HKLM\\SOFTWARE\\Google\\Update"],
        "services": ["gupdate", "gupdatem"]
    },
    "Skype Click to Call": {
        "type": "Browser Extension Bloatware",
        "detection": ["Skype Click to Call"],
        "reason": "Browser extension for Skype. Tracks phone numbers on web pages. Privacy concern. Not needed.",
        "files": ["C:\\Program Files (x86)\\Skype\\Toolbars"],
        "registry": ["HKLM\\SOFTWARE\\Skype\\Toolbars"],
        "services": []
    },
    "RealNetworks Update": {
        "type": "Obsolete Bloatware",
        "detection": ["RealNetworks Scheduler", "RealPlayer Update"],
        "reason": "RealPlayer and RealDownloader updates. Obsolete software. Security risks. Better alternatives exist.",
        "files": ["C:\\Program Files (x86)\\Real"],
        "registry": ["HKLM\\SOFTWARE\\RealNetworks"],
        "services": ["RealNetworks Downloader Resolver Service"]
    },
    "Corel Direct Disc Labeler": {
        "type": "OEM Bloatware",
        "detection": ["Corel Direct Disc Labeler"],
        "reason": "CD/DVD labeling software. Obsolete technology. Rarely used. Takes space.",
        "files": ["C:\\Program Files\\Corel"],
        "registry": ["HKLM\\SOFTWARE\\Corel"],
        "services": []
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
