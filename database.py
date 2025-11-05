# -*- coding: utf-8 -*-
"""
TANKEKIT - Database Module
Comprehensive database of unwanted, potentially harmful, or unnecessary software
with professional justifications based on security, performance, and privacy concerns.
"""

# Comprehensive database of target software
# Each entry contains:
# - type: Category of the software (Bloatware, Adware, Spyware, PUP, etc.)
# - detection: List of strings used to detect the software
# - reason: Professional justification for removal
TARGET_SOFTWARE = {
    # Windows Bloatware - Rarely Used Features
    "3D Viewer": {
        "type": "Bloatware",
        "detection": ['Microsoft.Microsoft3DViewer'],
        "reason": "3D model viewer with limited functionality. Consumes ~50MB disk space. Unnecessary for 95% of users who don't work with 3D files. Can be reinstalled from Microsoft Store if needed.",
    },
    "Paint 3D": {
        "type": "Bloatware",
        "detection": ['Microsoft.MSPaint'],
        "reason": "3D painting application consuming ~200MB+ with limited professional capabilities. Most users prefer traditional Paint or professional alternatives like GIMP. Runs background processes affecting startup time.",
    },
    "Print 3D": {
        "type": "Bloatware",
        "detection": ['Microsoft.Print3D'],
        "reason": "3D printing utility consuming ~30MB. Only relevant for users with 3D printers (estimated <5% of PC users). Better alternatives exist from printer manufacturers.",
    },
    "Mixed Reality Portal": {
        "type": "Bloatware",
        "detection": ['Microsoft.MixedReality.Portal'],
        "reason": "VR/AR application consuming ~300MB+ and loading drivers unnecessary for non-VR users. Increases system overhead. Only needed for Windows Mixed Reality headsets (discontinued product line).",
    },
    "Clipchamp": {
        "type": "Bloatware",
        "detection": ['Clipchamp', 'Microsoft.Clipchamp'],
        "reason": "Video editor with limited free features (watermarks, resolution limits). Consumes ~100MB+. Better free alternatives include DaVinci Resolve, Shotcut. Microsoft acquisition resulted in forced installation.",
    },
    "Adobe Express": {
        "type": "Bloatware",
        "detection": ['Adobe Express', 'AdobeSystemsIncorporated.AdobeExpress'],
        "reason": "Limited trial version preinstalled without consent. Full features locked behind subscription. Runs telemetry services consuming resources. Can be installed from official Adobe site if needed.",
    },
    
    # Games and Adware - Entertainment Bloatware
    "Candy Crush Saga": {
        "type": "Adware/Game",
        "detection": ['king.com.CandyCrushSaga', 'Candy Crush Saga'],
        "reason": "Mobile game with aggressive monetization, ads, and user tracking. Consumes ~200MB+ and network bandwidth for ads. Privacy concerns: collects user behavior data. Microsoft receives payment for preinstallation.",
    },
    "Candy Crush Soda Saga": {
        "type": "Adware/Game",
        "detection": ['king.com.CandyCrushSodaSaga', 'Candy Crush Soda Saga'],
        "reason": "King game with in-app purchases and advertisement tracking. Consumes resources and bandwidth. Known to cache advertising data consuming additional storage.",
    },
    "Candy Crush Friends Saga": {
        "type": "Adware/Game",
        "detection": ['king.com.CandyCrushFriendsSaga', 'Candy Crush Friends Saga'],
        "reason": "Third Candy Crush variant with same monetization concerns. Preinstalled bloatware consuming disk space (~150MB) without user consent. No productivity value.",
    },
    "FarmVille 2: Country Escape": {
        "type": "Adware/Game",
        "detection": ['ZyngaInc.FarmVille2CountryEscape', 'FarmVille 2'],
        "reason": "Zynga game known for aggressive data collection and battery drain. Connects to multiple tracking services. Previous security concerns with Zynga's privacy policies.",
    },
    "Hidden City: Hidden Object": {
        "type": "Adware/Game",
        "detection": ['G5EntertainmentAB.HiddenCityHiddenObjectAdventure', 'Hidden City'],
        "reason": "Casual game with in-app purchases. Preinstalled bloatware with no productivity value. Consumes ~300MB+ with game data.",
    },
    "Bubble Witch 3 Saga": {
        "type": "Adware/Game",
        "detection": ['king.com.BubbleWitch3Saga', 'Bubble Witch 3 Saga'],
        "reason": "King game with microtransactions and ads. Part of bloatware package deal with Microsoft. Should be user choice, not preinstalled.",
    },
    "Asphalt 8: Airborne": {
        "type": "Adware/Game",
        "detection": ['GAMELOFTSA.Asphalt8Airborne', 'Asphalt 8'],
        "reason": "Mobile racing game consuming ~2GB+ with updates. Heavy ads and in-app purchases. Not suitable for work PCs. Impacts startup performance.",
    },
    "Age of Empires: Castle Siege": {
        "type": "Bloatware",
        "detection": ['Microsoft.AgeofEmpiresCastleSiege', 'Age of Empires: Castle Siege'],
        "reason": "Freemium mobile game variant, not the classic Age of Empires. Contains monetization mechanics. Discontinued but still appears on some systems.",
    },
    "Minecraft": {
        "type": "Bloatware",
        "detection": ['Microsoft.MinecraftUWP', 'Minecraft for Windows'],
        "reason": "While popular, preinstalling without consent is bloatware. Consumes ~500MB+. Users should choose to purchase and install games, not have them forced.",
    },
    "Microsoft Solitaire Collection": {
        "type": "Adware/Game",
        "detection": ['Microsoft.MicrosoftSolitaireCollection'],
        "reason": "Contains video ads unless premium subscription purchased. Classic Solitaire was ad-free. Privacy concerns with ad tracking. Consumes ~150MB with cached ads.",
    },
    "Roblox": {
        "type": "Adware/Game",
        "detection": ['ROBLOXCORPORATION.ROBLOX', 'Roblox'],
        "reason": "Gaming platform with microtransactions. Security concerns with user-generated content. Should be parental choice, not preinstalled. Consumes significant resources when running.",
    },
    "Farm Heroes Saga": {
        "type": "Adware/Game",
        "detection": ['king.com.FarmHeroesSaga', 'Farm Heroes Saga'],
        "reason": "King game with freemium model and ads. Part of Microsoft's revenue-sharing bloatware deals. Unnecessary preinstallation.",
    },
    "World of Tanks Blitz": {
        "type": "Adware/Game",
        "detection": ['WarGamingNet.WorldofTanksBlitz', 'World of Tanks Blitz'],
        "reason": "Online game with microtransactions consuming ~2GB+. Runs background services. Not appropriate for preinstallation on business or personal PCs.",
    },
    "March of Empires": {
        "type": "Adware/Game",
        "detection": ['GAMELOFTSA.MarchofEmpires', 'March of Empires'],
        "reason": "Gameloft strategy game with aggressive monetization. Large install size. Bloatware deal with OEMs.",
    },
    "Disney Magic Kingdoms": {
        "type": "Adware/Game",
        "detection": ['GAMELOFTSA.DisneyMagicKingdoms', 'Disney Magic Kingdoms'],
        "reason": "Disney-themed game with heavy in-app purchases. Targets children. Parental control concerns. Consumes ~1GB+ storage.",
    },
    
    # Social Media Bloatware
    "TikTok": {
        "type": "Bloatware/Privacy Risk",
        "detection": ['TikTok', 'BytedancePte.Ltd.TikTok'],
        "reason": "Social media app with significant privacy and security concerns. Data collection practices questioned by multiple governments. Should be user choice. Web version available.",
    },
    "Facebook": {
        "type": "Bloatware/Privacy Risk",
        "detection": ['Facebook', 'Meta.Facebook'],
        "reason": "Social media app with extensive tracking capabilities. Meta's privacy policies controversial. Consumes resources with background updates. Web version fully functional.",
    },
    "Instagram": {
        "type": "Bloatware/Privacy Risk",
        "detection": ['Instagram', 'Meta.Instagram'],
        "reason": "Meta-owned app with data collection concerns. Preinstalled without consent. Web and mobile versions sufficient. Desktop app runs telemetry.",
    },
    "Twitter": {
        "type": "Bloatware",
        "detection": ['Twitter', 'X'],
        "reason": "Social media app unnecessary on desktop. Web version provides full functionality. Preinstallation serves no purpose for most users.",
    },
    "LinkedIn": {
        "type": "Bloatware",
        "detection": ['LinkedIn', 'Microsoft.LinkedIn'],
        "reason": "Professional network better accessed via browser. Desktop app consumes resources. Microsoft integration resulted in preinstallation on some systems.",
    },
    
    # Streaming Services Bloatware
    "Netflix": {
        "type": "Bloatware",
        "detection": ['Netflix', '4DF9E0F8.Netflix'],
        "reason": "Streaming service app preinstalled without subscription. Consumes ~50MB. Web version offers better features and performance. Unnecessary preinstallation.",
    },
    "Spotify": {
        "type": "Bloatware",
        "detection": ['Spotify', 'SpotifyAB.SpotifyMusic'],
        "reason": "Music streaming app should be user choice. Desktop version available from official site. Preinstalled version may lack features. Consumes resources.",
    },
    "Disney+": {
        "type": "Bloatware",
        "detection": ['Disney+', 'DisneyPlus'],
        "reason": "Streaming service requiring subscription. Preinstalled bloatware. Web version fully functional. No reason for forced installation.",
    },
    "Hulu": {
        "type": "Bloatware",
        "detection": ['Hulu'],
        "reason": "US streaming service preinstalled. Requires subscription. Regional restrictions make it useless for many users. Web version available.",
    },
    "Amazon Prime Video": {
        "type": "Bloatware",
        "detection": ['Prime Video', 'AmazonVideo.PrimeVideo'],
        "reason": "Amazon streaming app preinstalled without Prime subscription. Web version works better. Unnecessary bloatware.",
    },
    
    # Aggressive/Problematic Antivirus
    "McAfee": {
        "type": "PUP/Aggressive Antivirus",
        "detection": ['McAfee', 'McAfee Security', 'McAfee LiveSafe', 'McAfee Total Protection'],
        "reason": "Aggressive trial antivirus notorious for difficult removal and constant upgrade nags. High resource consumption (400MB+ RAM). Multiple background processes. Windows Defender provides adequate free protection. Known to slow system performance significantly.",
    },
    "Norton": {
        "type": "PUP/Aggressive Antivirus",
        "detection": ['Norton', 'Norton Security', 'Norton 360', 'Norton AntiVirus', 'Norton Internet Security', 'NortonLifeLock'],
        "reason": "Resource-intensive antivirus (500MB+ RAM) with aggressive renewal tactics. Multiple background services impact performance. Windows Defender free alternative. Difficult to fully uninstall. Known for popup notifications.",
    },
    "Avast": {
        "type": "PUP/Privacy Concern",
        "detection": ['Avast', 'Avast Free Antivirus', 'Avast Internet Security'],
        "reason": "Free antivirus caught selling user browsing data in 2020 scandal. Aggressive upselling. Installs browser extensions without clear consent. Windows Defender sufficient. Privacy policy concerns remain.",
    },
    "AVG": {
        "type": "PUP/Privacy Concern",
        "detection": ['AVG', 'AVG AntiVirus', 'AVG Internet Security', 'AVG Technologies'],
        "reason": "Owned by Avast (same data selling scandal). Aggressive advertising for premium features. Installs unwanted toolbars. High resource usage. Windows Defender better privacy alternative.",
    },
    "Avira": {
        "type": "PUP/Bundleware",
        "detection": ['Avira', 'Avira Free Security', 'Avira Antivirus'],
        "reason": "Free antivirus with constant premium upgrade prompts. Partners with bundleware distributors. Installs browser extensions. Resource consumption impacts performance.",
    },
    "Bitdefender": {
        "type": "Trialware",
        "detection": ['Bitdefender', 'Bitdefender Antivirus'],
        "reason": "Trial antivirus preinstalled on OEM systems. Limited trial period followed by aggressive purchase prompts. Resource intensive. Free alternatives available.",
    },
    
    # Fake/Rogue Antivirus
    "Segurazo": {
        "type": "Scareware/Fake AV",
        "detection": ['Segurazo', 'Santivirus Realtime Protection', 'SAntivirus'],
        "reason": "ROGUE ANTIVIRUS: Classified as potentially unwanted program (PUP) by legitimate security vendors. Uses scare tactics showing fake threats. Extremely difficult to uninstall. Hijacks browser settings. No legitimate antivirus certification.",
    },
    "SpyHunter": {
        "type": "Scareware/Questionable AV",
        "detection": ['SpyHunter', 'Enigma Software'],
        "reason": "Controversial security software using aggressive scare tactics. Shows fake threats to force purchases. Complained about by Better Business Bureau. Very difficult removal. Not recommended by security professionals.",
    },
    "Windows Malware Defender": {
        "type": "Scareware/Fake AV",
        "detection": ['Windows Malware Defender', 'WinMalwareDefender'],
        "reason": "FAKE ANTIVIRUS: Malware disguised as security software. Not affiliated with Microsoft despite name. Uses scare tactics. Extremely difficult to remove. May install additional malware.",
    },
    "Antimalware Doctor": {
        "type": "Scareware/Fake AV",
        "detection": ['Antimalware Doctor'],
        "reason": "ROGUE ANTIVIRUS: Known scareware showing fabricated threats. Demands payment for fake removal. Classified as malware by legitimate security vendors.",
    },
    "Windows Security Suite": {
        "type": "Scareware/Fake AV",
        "detection": ['Windows Security Suite'],
        "reason": "FAKE ANTIVIRUS: Malware masquerading as Microsoft security software. Not legitimate Microsoft product. Uses fake scans showing false threats.",
    },
    "Windows Protection Suite": {
        "type": "Scareware/Fake AV",
        "detection": ['Windows Protection Suite'],
        "reason": "ROGUE SECURITY SOFTWARE: Fake antivirus using Microsoft branding without authorization. Shows false positives to scare users into purchasing.",
    },
    "System Doctor": {
        "type": "Scareware/Fake AV",
        "detection": ['System Doctor', 'System Doctor 2014'],
        "reason": "SCAREWARE: Fake optimization tool showing fabricated system problems. Aggressive purchase prompts. May bundle additional unwanted software.",
    },
    "Smart Fortress": {
        "type": "Scareware/Fake AV",
        "detection": ['Smart Fortress'],
        "reason": "ROGUE ANTIVIRUS: Known scareware with fake threat detection. Not recognized by legitimate security organizations. Difficult to remove.",
    },
    
    # OEM Bloatware - HP
    "HP Support Assistant": {
        "type": "Bloatware",
        "detection": ['HP Support Assistant', 'HPSupportAssistant'],
        "reason": "HP diagnostic tool running constant background checks consuming 100-200MB RAM. Most users never need it. Windows has built-in diagnostic tools. Startup impact. Can cause conflicts with updates.",
    },
    "HP JumpStart": {
        "type": "Bloatware",
        "detection": ['HP JumpStart', 'HPJumpStart'],
        "reason": "HP tutorial app useful only for first-time setup. Continues running background services after initial use. Consumes resources. Unnecessary after first day.",
    },
    "HP Documentation": {
        "type": "Bloatware",
        "detection": ['HP Documentation'],
        "reason": "Static help files consuming disk space. Better and updated information available online. Outdated after system updates. Unnecessary local storage.",
    },
    "HP ePrint": {
        "type": "Bloatware",
        "detection": ['HP ePrint'],
        "reason": "Cloud printing service requiring HP account. Privacy concerns with document uploads. Most users prefer direct printing. Runs background services.",
    },
    "HP Games": {
        "type": "Bloatware",
        "detection": ['HP Games'],
        "reason": "Game launcher for casual games. Bloatware on professional systems. Contains links to paid games. No productivity value.",
    },
    "HP Sure Click": {
        "type": "Bloatware/Trialware",
        "detection": ['HP Sure Click'],
        "reason": "Security isolation software requiring subscription after trial. Most features redundant with Windows security. Enterprise-focused, overkill for home users.",
    },
    
    # OEM Bloatware - Dell
    "Dell SupportAssist": {
        "type": "Bloatware/Security Risk",
        "detection": ['Dell SupportAssist', 'SupportAssist'],
        "reason": "Dell diagnostic tool with history of security vulnerabilities (CVE-2019-12280, CVE-2019-3718). High resource usage. Telemetry concerns. Windows diagnostic tools sufficient. Previous vulnerabilities allowed privilege escalation.",
    },
    "Dell Data Vault": {
        "type": "Bloatware",
        "detection": ['Dell Data Vault'],
        "reason": "Backup software consuming significant resources. Better free alternatives available (Windows Backup, cloud services). Limited functionality in free version.",
    },
    "Dell Power Manager": {
        "type": "Bloatware",
        "detection": ['Dell Power Manager'],
        "reason": "Power management utility mostly redundant with Windows power options. Adds complexity without significant benefit. Background service impacts performance.",
    },
    "Dell Foundation Services": {
        "type": "Bloatware",
        "detection": ['Dell Foundation Services'],
        "reason": "Backend service for Dell apps. Runs even if Dell apps uninstalled. Consumes resources. Privacy concerns with telemetry data sent to Dell.",
    },
    
    # OEM Bloatware - Lenovo
    "Lenovo Vantage": {
        "type": "Bloatware",
        "detection": ['Lenovo Vantage', 'LenovoVantage'],
        "reason": "Lenovo utility suite consuming 200MB+ RAM. Most features redundant with Windows settings. Telemetry and advertising. Previous security concerns with Lenovo software (Superfish scandal legacy).",
    },
    "Lenovo REACHit": {
        "type": "Bloatware/Privacy Risk",
        "detection": ['Lenovo REACHit'],
        "reason": "Cloud storage and file sharing service. Privacy concerns with file indexing. Consumes resources. Better alternatives available (OneDrive, Google Drive).",
    },
    "Lenovo QuickCast": {
        "type": "Bloatware",
        "detection": ['Lenovo QuickCast'],
        "reason": "Screen sharing utility. Windows has built-in screen sharing. Runs background services. Limited usefulness for most users.",
    },
    "Lenovo Photo Master": {
        "type": "Bloatware",
        "detection": ['Lenovo Photo Master'],
        "reason": "Photo management app. Windows Photos app more integrated. Consumes resources. No significant advantages over built-in alternatives.",
    },
    
    # OEM Bloatware - ASUS
    "ASUS WebStorage": {
        "type": "Bloatware",
        "detection": ['ASUS WebStorage'],
        "reason": "Cloud storage with limited free space. Constant upgrade prompts. Better alternatives available. Background sync consumes bandwidth.",
    },
    "ASUS Splendid": {
        "type": "Bloatware",
        "detection": ['ASUS Splendid'],
        "reason": "Display color adjustment utility. Windows has built-in display settings. Runs background service. Most users don't need specialized color management.",
    },
    "ASUS Gaming Center": {
        "type": "Bloatware",
        "detection": ['ASUS Gaming Center', 'ROG Gaming Center'],
        "reason": "Gaming optimization tool with limited benefit. Most settings accessible through Windows. Runs background processes impacting performance paradoxically.",
    },
    "ASUS AI Suite": {
        "type": "Bloatware",
        "detection": ['ASUS AI Suite'],
        "reason": "System monitoring and tweaking tool. Can cause system instability. Advanced users prefer specialized tools. Runs multiple background services.",
    },
    
    # OEM Bloatware - Acer
    "Acer Quick Access": {
        "type": "Bloatware",
        "detection": ['Acer Quick Access'],
        "reason": "Utility for Acer hotkeys. Limited functionality. Windows has native hotkey support. Background service uses resources.",
    },
    "abPhoto": {
        "type": "Bloatware",
        "detection": ['abPhoto', 'Acer abPhoto'],
        "reason": "Acer photo viewer. Windows Photos app superior and integrated. Unnecessary duplicate functionality.",
    },
    "abFiles": {
        "type": "Bloatware",
        "detection": ['abFiles', 'Acer abFiles'],
        "reason": "File manager redundant with Windows Explorer. No significant features over built-in file manager. Bloatware.",
    },
    
    # Toolbars and Adware
    "Ask Toolbar": {
        "type": "Adware/Toolbar/PUP",
        "detection": ['Ask Toolbar', 'Ask.com Toolbar'],
        "reason": "KNOWN PUP: Browser hijacker changing search engine and homepage without consent. Tracks browsing behavior. Difficult to remove. Classified as potentially unwanted program by most security vendors.",
    },
    "Babylon Toolbar": {
        "type": "Adware/Toolbar/PUP",
        "detection": ['Babylon Toolbar', 'Babylon'],
        "reason": "BROWSER HIJACKER: Changes search settings without permission. Known for bundling with free software. Tracks user activity. Very difficult removal process.",
    },
    "Conduit": {
        "type": "Adware/Toolbar/PUP",
        "detection": ['Conduit', 'Conduit Toolbar'],
        "reason": "KNOWN ADWARE: Browser hijacker with extensive tracking. Changes search engine and new tab page. Bundled with free software. Classified as PUP by security vendors.",
    },
    "MyWebSearch": {
        "type": "Adware/Toolbar/PUP",
        "detection": ['MyWebSearch', 'MyWay'],
        "reason": "ADWARE: Browser hijacker with aggressive behavior. Changes browser settings forcefully. Shows excessive ads. Difficult to remove completely.",
    },
    "Delta Search": {
        "type": "Adware/Browser Hijacker",
        "detection": ['Delta Search', 'Delta Toolbar'],
        "reason": "BROWSER HIJACKER: Changes default search engine. Redirects searches to monetized results. Tracks browsing data. Classified as malicious by security researchers.",
    },
    
    # System Optimizers (Often Questionable)
    "CCleaner": {
        "type": "Questionable Utility",
        "detection": ['CCleaner', 'Piriform CCleaner'],
        "reason": "System cleaner with diminishing benefits on modern Windows. 2017 security breach compromised millions of users. Aggressive advertising for paid version. Manual Windows cleanup safer. Registry cleaning can cause instability.",
    },
    "Advanced SystemCare": {
        "type": "PUP/Optimizer",
        "detection": ['Advanced SystemCare', 'IObit Advanced SystemCare'],
        "reason": "System optimizer using scare tactics showing fake problems. Aggressive upselling. IObit has reputation for questionable practices. Windows built-in tools sufficient.",
    },
    "Driver Booster": {
        "type": "PUP/Questionable",
        "detection": ['Driver Booster', 'IObit Driver Booster'],
        "reason": "Driver updater from IObit with questionable driver sources. Can install incompatible drivers causing system instability. Windows Update handles driver updates safely.",
    },
    "PC Speedup": {
        "type": "Scareware/PUP",
        "detection": ['PC Speedup', 'Systweak PC Speedup'],
        "reason": "SCAREWARE: Shows fabricated performance problems. Aggressive purchase prompts. No real optimization benefits. Classified as PUP by security vendors.",
    },
    "Registry Cleaner": {
        "type": "Scareware/PUP",
        "detection": ['Registry Cleaner', 'Registry Optimizer'],
        "reason": "QUESTIONABLE UTILITY: Registry cleaning rarely needed on modern Windows and can cause system instability. Often shows fake problems. Microsoft discourages registry cleaners.",
    },
    
    # Others - Miscellaneous Bloatware
    "WildTangent Games": {
        "type": "Bloatware/Trialware",
        "detection": ['WildTangent', 'WildTangent Games'],
        "reason": "Game platform preinstalled on OEM PCs. Trial games with purchase prompts. Consumes ~500MB+. Runs background services. No productivity value.",
    },
    "Bonjour": {
        "type": "Bloatware",
        "detection": ['Bonjour', 'Apple Bonjour'],
        "reason": "Apple networking service often installed with iTunes/Adobe products. Unnecessary for most users unless using specific Apple devices. Background service consumes resources.",
    },
    "Java": {
        "type": "Security Risk (if outdated)",
        "detection": ['Java', 'Oracle Java', 'Java Runtime Environment'],
        "reason": "Runtime environment frequently targeted by exploits when outdated. Many modern applications don't require Java. Browser plugin disabled in most browsers due to security concerns. Only keep if specifically needed.",
    },
    "Internet Explorer": {
        "type": "Deprecated/Security Risk",
        "detection": ['Internet Explorer'],
        "reason": "DEPRECATED BROWSER: Microsoft officially ended support June 2022. Known security vulnerabilities no longer patched. Modern websites incompatible. Microsoft recommends Edge. Continued use exposes system to attacks.",
    },
    "WeChat": {
        "type": "Bloatware/Privacy Risk",
        "detection": ['WeChat', 'Tencent WeChat'],
        "reason": "Chinese messaging app with significant privacy concerns. Data sharing with Chinese government documented. Heavy resource usage. Web version available. Security researchers warn against desktop installation.",
    },
    "Cortana": {
        "type": "Bloatware/Privacy Concern",
        "detection": ['Cortana'],
        "reason": "Voice assistant with limited Windows integration since updates. Privacy concerns with voice data collection. High resource usage. Most functionality available through Windows search without Cortana.",
    },
    "Prime Video": {
        "type": "Bloatware",
        "detection": ['AmazonVideo.PrimeVideo', 'Prime Video'],
        "reason": "Amazon streaming app. Browser version works equally well without taking disk space.",
    },
    "Duolingo": {
        "type": "Bloatware",
        "detection": ['Duolingo.Duolingo-LearnLanguagesforFree', 'Duolingo'],
        "reason": "Language learning app. Works better on mobile or web. Shouldn't be preinstalled on PCs.",
    },
    "Microsoft News": {
        "type": "Bloatware",
        "detection": ['Microsoft.BingNews', 'Noticias'],
        "reason": "News aggregator app. Web browsers provide better news access without dedicated app.",
    },
    "Tiempo": {
        "type": "Bloatware",
        "detection": ['Microsoft.BingWeather'],
        "reason": "Weather app that duplicates web functionality. Uses resources for minimal benefit.",
    },
    "OneDrive": {
        "type": "Bloatware",
        "detection": ['OneDrive', 'Microsoft OneDrive'],
        "reason": "Cloud storage forced on users. Should be optional. Uses resources and may auto-upload files without clear consent.",
    },
    "Microsoft Teams": {
        "type": "Bloatware",
        "detection": ['Microsoft Teams', 'Teams Machine-Wide Installer'],
        "reason": "Business communication tool. Shouldn't be preinstalled on consumer PCs. Auto-starts and uses resources.",
    },
    "OneNote": {
        "type": "Bloatware",
        "detection": ['Microsoft.Office.OneNote'],
        "reason": "Note-taking app part of Office suite. Should be user-installed, not forced bloatware.",
    },
    "Xbox Game Bar": {
        "type": "Bloatware",
        "detection": ['Microsoft.XboxGamingOverlay'],
        "reason": "Gaming overlay. Uses resources even when not gaming. Not needed by non-gamers.",
    },
    "Xbox Console Companion": {
        "type": "Bloatware",
        "detection": ['Microsoft.XboxApp'],
        "reason": "Xbox integration app. Only needed by Xbox users. Runs background processes unnecessarily.",
    },
    "Your Phone": {
        "type": "Bloatware",
        "detection": ['Microsoft.YourPhone', 'Enlace Móvil', 'Phone Link'],
        "reason": "Phone integration app. Privacy concerns with data sync. Should be optional, not preinstalled.",
    },
    "Consejos": {
        "type": "Bloatware",
        "detection": ['Microsoft.Getstarted', 'Microsoft Tips'],
        "reason": "Tips app that's redundant after Windows setup. Takes space for minimal value.",
    },
    "Feedback Hub": {
        "type": "Bloatware",
        "detection": ['Microsoft.WindowsFeedbackHub', 'Centro de opiniones'],
        "reason": "Feedback collection tool. Most users never use it. Potential telemetry concerns.",
    },
    "Microsoft Photos": {
        "type": "Bloatware",
        "detection": ['Microsoft.Windows.Photos', 'Microsoft Photos'],
        "reason": "Photo viewer with cloud integration. Better lightweight alternatives exist. May upload photos to cloud.",
    },
    "Mail and Calendar": {
        "type": "Bloatware",
        "detection": ['microsoft.windowscommunicationsapps', 'Mail and Calendar', 'Correo y Calendario'],
        "reason": "Basic mail client. Better alternatives available. Limited functionality compared to dedicated email apps.",
    },
    "TotalAV": {
        "type": "PUP/Aggressive AV",
        "detection": ['TotalAV', 'PC Protect'],
        "reason": "Aggressive marketing and scare tactics. Often bundled with other software. Questionable detection methods.",
    },
    "PC Accelerate Pro": {
        "type": "PUP/Scareware",
        "detection": ['PC Accelerate Pro'],
        "reason": "Fake optimizer showing false problems. Scareware tactics to sell useless software.",
    },
    "PC Speed Up": {
        "type": "PUP/Scareware",
        "detection": ['PC Speed Up', 'PC Optimizer Pro'],
        "reason": "Scareware showing fake system issues. Does nothing useful, may harm system.",
    },
    "OneSafe PC Cleaner": {
        "type": "PUP/Scareware",
        "detection": ['OneSafe PC Cleaner'],
        "reason": "Aggressive optimizer with false detection. Difficult to remove. Classified as PUP.",
    },
    "Advanced System Protector": {
        "type": "PUP/Fake Security",
        "detection": ['Advanced System Protector'],
        "reason": "Fake security tool showing false threats. Bundled with malware. Classified as potentially unwanted program.",
    },
    "RegClean Pro": {
        "type": "PUP/Registry Cleaner",
        "detection": ['RegClean Pro'],
        "reason": "Registry cleaner that can damage Windows. Fake scan results. Windows doesn't need registry cleaning.",
    },
    "Reimage Repair": {
        "type": "PUP/Scareware",
        "detection": ['Reimage Repair'],
        "reason": "Scareware showing fake critical errors. Aggressive tactics to sell expensive software.",
    },
    "Restoro": {
        "type": "PUP/Scareware",
        "detection": ['Restoro'],
        "reason": "System repair tool with questionable methods. Shows exaggerated problems. Often bundled malware.",
    },
    "Outbyte PC Repair": {
        "type": "PUP/Scareware",
        "detection": ['Outbyte PC Repair'],
        "reason": "Fake PC repair tool. Shows false problems to scare users into purchase.",
    },
    "DriverPack Solution": {
        "type": "Adware/Bundle Malware",
        "detection": ['DriverPack Solution', 'DriverPack Notifier'],
        "reason": "Known for bundling malware and adware. Installs unwanted software. Very aggressive and hard to remove.",
    },
    "Driver Easy": {
        "type": "PUP/Driver Updater",
        "detection": ['Driver Easy'],
        "reason": "Driver updater with questionable practices. May install incompatible drivers. Windows Update safer.",
    },
    "SlimDrivers": {
        "type": "PUP/Driver Updater",
        "detection": ['SlimDrivers'],
        "reason": "Driver updater that can cause system instability. Often bundled with PUPs.",
    },
    "Slimware Utilities": {
        "type": "PUP/Optimizer",
        "detection": ['Slimware Utilities', 'DriverUpdate'],
        "reason": "Suite of questionable utilities. Shows false problems. Installs bundled software.",
    },
    "WinZip Driver Updater": {
        "type": "PUP/Scareware",
        "detection": ['WinZip Driver Updater', 'winzipdu'],
        "reason": "Misleading driver updater showing false problems. Pushes unnecessary driver updates and paid version.",
    },
    "Driver Support": {
        "type": "PUP/Driver Updater",
        "detection": ['Driver Support', 'Asurvio'],
        "reason": "Aggressive driver updater with scare tactics. Can install wrong drivers causing system issues.",
    },
    "MyWay": {
        "type": "Browser Hijacker/Malware",
        "detection": ['MyWay', 'MindSpark'],
        "reason": "Aggressive browser hijacker. Changes settings, tracks browsing, shows ads. Difficult to remove.",
    },
    "SweetIM": {
        "type": "Adware/Spyware",
        "detection": ['SweetIM'],
        "reason": "Adware and spyware bundle. Changes browser settings. Tracks browsing behavior for ads.",
    },
    "RelevantKnowledge": {
        "type": "Spyware",
        "detection": ['RelevantKnowledge'],
        "reason": "Market research spyware tracking all browsing. Installed secretly via bundles. Privacy violation.",
    },
    "DealPly": {
        "type": "Adware",
        "detection": ['DealPly'],
        "reason": "Adware showing unwanted shopping ads. Tracks browsing. Changes browser settings.",
    },
    "Snap.do": {
        "type": "Browser Hijacker",
        "detection": ['Snap.do', 'snapdo', 'smartbar'],
        "reason": "Browser toolbar and hijacker. Changes search settings, injects ads, tracks browsing activity.",
    },
    "Funmoods": {
        "type": "Adware/Browser Hijacker",
        "detection": ['Funmoods'],
        "reason": "Browser hijacker with emoticon toolbar. Changes homepage and search. Tracks data.",
    },
    "Yontoo": {
        "type": "Adware",
        "detection": ['Yontoo'],
        "reason": "Adware injecting shopping ads into websites. Tracks browsing. Browser extension malware.",
    },
    "Crossrider": {
        "type": "Adware Platform",
        "detection": ['Crossrider'],
        "reason": "Adware platform used by many malicious extensions. Injects ads into web pages.",
    },
    "Babylon": {
        "type": "Adware/Browser Hijacker",
        "detection": ['Babylon'],
        "reason": "Toolbar and search hijacker. Changes browser settings. Hard to remove completely.",
    },
    "Spigot": {
        "type": "Adware",
        "detection": ['Spigot'],
        "reason": "Adware platform installing browser extensions and toolbars. Difficult to remove.",
    },
    "Microsoft Office": {
        "type": "Trialware",
        "detection": ['Microsoft Office 365', 'Microsoft 365'],
        "reason": "Trial version with constant upgrade prompts. Should be user-installed if needed. Free alternatives exist.",
    },
    "WinZip": {
        "type": "Bloatware/Nagware",
        "detection": ['WinZip'],
        "reason": "Paid compression tool when Windows has built-in support. Constant nag screens. Free alternatives better.",
    },
    "WPS Office": {
        "type": "Bloatware/Adware",
        "detection": ['WPS Office', 'Kingsoft Office'],
        "reason": "ADWARE - Office suite with ads in free version. Often preinstalled. Microsoft Office or LibreOffice better. Privacy concerns with Chinese company.",
    },
    "Dropbox": {
        "type": "Bloatware",
        "detection": ['Dropbox OEM'],
        "reason": "Cloud storage preinstalled by OEMs. Should be user choice. Uses resources for background sync.",
    },
    "Evernote": {
        "type": "Bloatware",
        "detection": ['Evernote OEM'],
        "reason": "Note-taking app. Often preinstalled as bloatware. Limited free tier. User should choose.",
    },
    "CyberLink": {
        "type": "Bloatware",
        "detection": ['CyberLink'],
        "reason": "Media software suite. Trial versions with limited features. Better free alternatives available.",
    },
    "Roxio": {
        "type": "Bloatware",
        "detection": ['Roxio'],
        "reason": "CD/DVD burning software. Mostly obsolete technology. Windows has built-in burning capability.",
    },
    "Nero": {
        "type": "Bloatware",
        "detection": ['Nero'],
        "reason": "Burning and media suite. Bloated, expensive. Mostly unnecessary with modern Windows.",
    },
    "HP Audio Switch": {
        "type": "Bloatware",
        "detection": ['HP Audio Switch'],
        "reason": "HP audio utility. Windows audio settings sufficient. Unnecessary extra layer.",
    },
    "HP Connection Optimizer": {
        "type": "Bloatware",
        "detection": ['HP Connection Optimizer'],
        "reason": "HP network utility. Dubious benefit. May interfere with network settings.",
    },
    "HP Command Center": {
        "type": "Bloatware",
        "detection": ['HP Command Center', 'OMEN Command Center'],
        "reason": "HP system control utility. Uses resources. Most features accessible through Windows.",
    },
    "HP Touchpoint Analytics": {
        "type": "Spyware/Telemetry",
        "detection": ['HP Touchpoint Analytics Client'],
        "reason": "HP telemetry collecting usage data. Privacy concern. Sends data to HP servers without clear benefit to user.",
    },
    "Dell Update": {
        "type": "Bloatware",
        "detection": ['Dell Update', 'Dell Digital Delivery'],
        "reason": "Dell update utility. Windows Update handles most drivers. Redundant software.",
    },
    "Dell Customer Connect": {
        "type": "Bloatware/Telemetry",
        "detection": ['Dell Customer Connect'],
        "reason": "Dell feedback and telemetry tool. Collects usage data. No benefit to user.",
    },
    "Dell Mobile Connect": {
        "type": "Bloatware",
        "detection": ['Dell Mobile Connect'],
        "reason": "Phone integration app. Works on specific Dell models only. Limited usefulness.",
    },
    "Lenovo Solution Center": {
        "type": "Bloatware",
        "detection": ['Lenovo Solution Center'],
        "reason": "Older Lenovo utility. Redundant with Windows tools. Uses resources unnecessarily.",
    },
    "Lenovo Accelerator": {
        "type": "Bloatware/Vulnerability",
        "detection": ['Lenovo Accelerator Application'],
        "reason": "Lenovo app with past security vulnerabilities. Minimal benefit. Resource usage.",
    },
    "Lenovo App Explorer": {
        "type": "Bloatware/Adware",
        "detection": ['Lenovo App Explorer'],
        "reason": "Lenovo app store promoting software installs. Bloatware that suggests more bloatware.",
    },
    "ASUS GiftBox": {
        "type": "Bloatware/Adware",
        "detection": ['ASUS GiftBox', 'ASUS AppDeals'],
        "reason": "ASUS promotion tool suggesting software. Bloatware promoting more bloatware. Ads and unwanted suggestions.",
    },
    "ASUS Live Update": {
        "type": "Bloatware/Security Risk",
        "detection": ['ASUS Live Update'],
        "reason": "ASUS update utility with past security issues. Windows Update more secure. Potential vulnerability.",
    },
    "MyASUS": {
        "type": "Bloatware",
        "detection": ['MyASUS', 'ASUS System Control Interface'],
        "reason": "ASUS system utility. Most features redundant. Uses background resources.",
    },
    "Acer Care Center": {
        "type": "Bloatware",
        "detection": ['Acer Care Center'],
        "reason": "Acer system utility. Redundant diagnostic tools. Uses resources.",
    },
    "Acer Product Registration": {
        "type": "Bloatware",
        "detection": ['Acer Product Registration'],
        "reason": "One-time registration tool. No need to keep installed. Pure bloatware after registration.",
    },
    "Acer Portal": {
        "type": "Bloatware",
        "detection": ['Acer BYOC Apps', 'abDocs', 'abFiles'],
        "reason": "Acer cloud apps. Redundant with Windows and cloud services. Privacy concerns.",
    },
    "MSI Dragon Center": {
        "type": "Bloatware/Resource Hog",
        "detection": ['MSI Dragon Center'],
        "reason": "MSI gaming utility. Heavy resource usage. Many features accessible through Windows.",
    },
    "MSI App Player": {
        "type": "Bloatware",
        "detection": ['MSI App Player'],
        "reason": "Android emulator by MSI. Large disk space usage. User should install if needed.",
    },
    "Samsung Settings": {
        "type": "Bloatware",
        "detection": ['Samsung Settings', 'Samsung Update'],
        "reason": "Samsung utilities. Redundant with Windows settings. Update tool less reliable than Windows Update.",
    },
    "VAIO Care": {
        "type": "Bloatware",
        "detection": ['VAIO Care', 'VAIO Control Center'],
        "reason": "VAIO system utilities. Mostly obsolete. Redundant with modern Windows.",
    },
    "Armoury Crate": {
        "type": "Bloatware/Persistent",
        "detection": ['Armoury Crate', 'ArmouryCrateInstaller'],
        "reason": "ASUS RGB and system control. Very difficult to remove completely. Uses excessive resources. Known for reinstalling itself.",
    },
    "KMSPico": {
        "type": "HackTool/Trojan",
        "detection": ['KMSPico', 'KMSpico Portable'],
        "reason": "ILLEGAL Windows/Office activation tool. Often contains trojans and malware. Steals system access. Violates Microsoft license.",
    },
    "Hola VPN": {
        "type": "Malicious VPN",
        "detection": ['Hola VPN'],
        "reason": "VPN that sells your bandwidth to others. Turns your PC into exit node for strangers. Major security and privacy risk.",
    },
    "Avast Free Antivirus": {
        "type": "Bloatware/Aggressive AV",
        "detection": ['Avast', 'Avast Free Antivirus'],
        "reason": "Free antivirus with very aggressive advertising and data collection. Caught selling user browsing data. Installs browser extensions without clear consent. Resource heavy.",
    },
    "AVG Free": {
        "type": "Bloatware/Aggressive AV",
        "detection": ['AVG', 'AVG Free', 'AVG AntiVirus Free'],
        "reason": "Sister product of Avast with same privacy issues. Aggressive upselling. Collects and shares user data. Better free alternatives exist.",
    },
    "Opera Browser": {
        "type": "Bloatware/Privacy Risk",
        "detection": ['Opera', 'Opera Browser', 'Opera Stable'],
        "reason": "Browser owned by Chinese consortium. Privacy concerns with data collection. Often preinstalled as bloatware. Built-in VPN logs data.",
    },
    "Brave Browser Trial": {
        "type": "Bloatware",
        "detection": ['Brave Trial', 'Brave Browser OEM'],
        "reason": "While Brave itself is fine, OEM trial versions are bloatware. Should be user choice to install. Preinstalled versions may have promotional deals.",
    },
    "Avira Free Security": {
        "type": "PUP/Aggressive AV",
        "detection": ['Avira', 'Avira Free Security', 'Avira Antivirus'],
        "reason": "Aggressive popups and upselling. Installs browser extensions and search modifications. Resource intensive. Privacy concerns with data sharing.",
    },
    "Bitdefender Free": {
        "type": "Trialware/Nagware",
        "detection": ['Bitdefender Free', 'Bitdefender Antivirus Free'],
        "reason": "Free version with constant upgrade prompts. Limited functionality to push paid version. Better alternatives available.",
    },
    "Malwarebytes Trial": {
        "type": "Trialware",
        "detection": ['Malwarebytes Trial', 'Malwarebytes OEM'],
        "reason": "Trial version preinstalled by OEMs. Constant upgrade nags. Should be user-installed if needed. Free version sufficient for most users.",
    },
    "Search Baron": {
        "type": "Browser Hijacker/Malware",
        "detection": ['Search Baron', 'SearchBaron'],
        "reason": "Malicious browser hijacker. Changes search engine and homepage. Extremely difficult to remove. Tracks browsing behavior.",
    },
    "Chromium Malware Variants": {
        "type": "Malware/Fake Browser",
        "detection": ['Chromium Browser Malware', 'Fake Chrome Update', 'Chromium Virus'],
        "reason": "Fake Chromium browsers bundled with malware. Not the legitimate Chromium. Changes browser settings, shows ads, tracks data. NOTE: This targets only malicious variants found in suspicious locations, not legitimate Chromium installations.",
    },
    "PC Optimizer Pro": {
        "type": "PUP/Scareware",
        "detection": ['PC Optimizer Pro', 'PCOptimizerPro'],
        "reason": "Fake optimizer showing false system problems. Scareware tactics. No real optimization performed. Difficult to uninstall.",
    },
    "MyCleanPC": {
        "type": "PUP/Scareware",
        "detection": ['MyCleanPC', 'My Clean PC'],
        "reason": "Aggressive optimizer with false positives. Heavy advertising. Expensive subscription for minimal benefit. Windows built-in tools better.",
    },
    "iolo System Mechanic": {
        "type": "PUP/Aggressive Optimizer",
        "detection": ['iolo', 'System Mechanic'],
        "reason": "Aggressive system optimizer with questionable benefits. Expensive. Constant upgrade prompts. May cause more problems than it solves.",
    },
    "Ashampoo WinOptimizer": {
        "type": "Bloatware/Trialware",
        "detection": ['Ashampoo WinOptimizer', 'Ashampoo'],
        "reason": "Trial optimizer preinstalled by OEMs. Limited trial features. Constant nags. Modern Windows doesn't need such tools.",
    },
    "Norton Utilities": {
        "type": "PUP/Expensive Optimizer",
        "detection": ['Norton Utilities', 'Norton 360 Utilities'],
        "reason": "Expensive optimizer by Norton. Aggressive renewal tactics. Questionable performance improvements. Windows tools sufficient.",
    },
    "Glary Utilities": {
        "type": "Redundant Utility/PUP",
        "detection": ['Glary Utilities', 'GlaryUtilities'],
        "reason": "System utility suite with questionable benefits. Many features duplicate Windows built-in tools. Often bundled with other software.",
    },
    "Auslogics BoostSpeed": {
        "type": "PUP/Aggressive Optimizer",
        "detection": ['Auslogics BoostSpeed', 'Auslogics'],
        "reason": "Aggressive system optimizer. Installs browser extensions. False positives to scare users. Expensive license for questionable benefits.",
    },
    "WinThruster": {
        "type": "PUP/Registry Cleaner",
        "detection": ['WinThruster', 'Solvusoft'],
        "reason": "Registry cleaner that can damage Windows. Shows false errors. Expensive. Windows doesn't benefit from registry cleaning.",
    },
    "Wise Registry Cleaner": {
        "type": "Risky Utility",
        "detection": ['Wise Registry Cleaner', 'WiseRegCleaner'],
        "reason": "Registry cleaner that can cause system instability. Modern Windows self-maintains registry. Risk of breaking system outweighs benefits.",
    },
    "IObit Uninstaller": {
        "type": "Bloatware/Bundleware",
        "detection": ['IObit Uninstaller', 'IObit'],
        "reason": "Uninstaller tool that often comes bundled. Installs other IObit products. Aggressive advertising. Windows uninstaller sufficient.",
    },
    "Smart Defrag": {
        "type": "Bloatware/Unnecessary",
        "detection": ['Smart Defrag', 'IObit Smart Defrag'],
        "reason": "Defragmentation tool unnecessary for modern systems with SSDs. Can damage SSDs if used. Windows has built-in defrag.",
    },
    "360 Total Security": {
        "type": "PUP/Chinese Software",
        "detection": ['360 Total Security', '360 Security'],
        "reason": "Chinese security software with privacy concerns. Data collection unclear. Better alternatives available. Often bundled without consent.",
    },
    "Baidu Antivirus": {
        "type": "PUP/Privacy Risk",
        "detection": ['Baidu Antivirus', 'Baidu'],
        "reason": "Chinese antivirus with serious privacy concerns. Sends data to Chinese servers. Often installed without consent. Difficult to remove.",
    },
    "Tencent PC Manager": {
        "type": "Bloatware/Privacy Risk",
        "detection": ['Tencent PC Manager', 'QQPCMgr'],
        "reason": "Chinese system utility. Privacy concerns with data collection. Installs without clear consent. Sends telemetry to Chinese servers.",
    },
    "Weather Bug": {
        "type": "Adware",
        "detection": ['WeatherBug', 'Weather Bug'],
        "reason": "Weather app that shows ads. Tracks user behavior. Preinstalled bloatware. Web weather sites work better without tracking.",
    },
    "PC Health Kit": {
        "type": "PUP/Scareware",
        "detection": ['PC Health Kit', 'PCHealthKit'],
        "reason": "Fake system health tool showing false warnings. Scareware tactics to sell product. No real system improvements.",
    },
    "System Healer": {
        "type": "PUP/Scareware",
        "detection": ['System Healer', 'SystemHealer'],
        "reason": "Rogue system optimizer. False scan results. Aggressive popups. Expensive and ineffective. Classified as PUP by many AV vendors.",
    },
    "Advanced PC Care": {
        "type": "PUP/Scareware",
        "detection": ['Advanced PC Care', 'AdvancedPCCare'],
        "reason": "Fake PC optimization tool. Shows false errors to scare users. Expensive license. No real system improvements.",
    },
    "SpeedMaxPc": {
        "type": "PUP/Scareware",
        "detection": ['SpeedMaxPc', 'Speed Max PC'],
        "reason": "Rogue optimizer with false positives. Aggressive advertising. Difficult to uninstall. No performance benefits.",
    },
    "WinZip System Utilities": {
        "type": "PUP/Optimizer",
        "detection": ['WinZip System Utilities Suite', 'WinZip Utilities'],
        "reason": "Unrelated to real WinZip. Shows false system issues. Expensive subscription. No real optimization.",
    },
    "MacKeeper": {
        "type": "Scareware/PUP",
        "detection": ['MacKeeper', 'mackeeper'],
        "reason": "Controversial Mac cleaner with aggressive marketing. Shows exaggerated issues to push sales. Often considered scareware.",
    },
    "PC Cleaner Pro": {
        "type": "PUP/Scareware",
        "detection": ['PC Cleaner Pro', 'PCCleanerPro'],
        "reason": "Fake cleaner showing false system problems. No real cleaning performed. Expensive. Classified as PUP.",
    },
    "Uniblue": {
        "type": "PUP/Scareware",
        "detection": ['Uniblue', 'DriverScanner', 'PowerSuite'],
        "reason": "Suite of questionable utilities. False scan results. Expensive licenses. Can cause system issues. Better alternatives exist.",
    },
    "PC Fix Speed": {
        "type": "PUP/Scareware",
        "detection": ['PC Fix Speed', 'PCFixSpeed'],
        "reason": "Rogue PC repair tool. Shows fake errors. No real fixes. Scareware tactics. Expensive.",
    },
    "Windows Security Alert": {
        "type": "Fake Antivirus",
        "detection": ['Windows Security Alert', 'WinSecurityAlert'],
        "reason": "Fake antivirus masquerading as Windows Security. Shows false threats to scare users into paying. Actually malware.",
    },
    "System Progressive Protection": {
        "type": "Rogue AV/Malware",
        "detection": ['System Progressive Protection'],
        "reason": "Notorious rogue antivirus. Prevents legitimate program execution. Shows fake threats. Demands payment. Very malicious.",
    },
    "Antivirus Live": {
        "type": "Rogue AV/Malware",
        "detection": ['Antivirus Live', 'AV Live'],
        "reason": "Fake antivirus showing false threats. Blocks legitimate software. Demands payment. Classified as malware.",
    },
    "Privacy Protection": {
        "type": "Rogue Security/Malware",
        "detection": ['Privacy Protection', 'PrivacyProtection'],
        "reason": "Rogue privacy tool showing fake privacy issues. Scareware. Demands payment. No real protection.",
    },
    "Search Protect by Conduit": {
        "type": "Browser Hijacker/Adware",
        "detection": ['Search Protect', 'SearchProtect'],
        "reason": "Browser hijacker preventing search engine changes. Tracks browsing. Very difficult to remove. Changes browser settings persistently.",
    },
    "Browser Modifier": {
        "type": "Browser Hijacker",
        "detection": ['Browser Modifier', 'BrowserModifier'],
        "reason": "Generic browser hijacker. Changes homepage and search engine. Shows ads. Tracks browsing behavior.",
    },
    "Websearch": {
        "type": "Browser Hijacker",
        "detection": ['Websearch', 'WebSearch Toolbar'],
        "reason": "Search hijacker redirecting searches. Injects ads into search results. Tracks user queries. Difficult to remove.",
    },
    "StartPage Toolbar": {
        "type": "Browser Hijacker/Adware",
        "detection": ['StartPage', 'StartPage Toolbar'],
        "reason": "Toolbar changing homepage and new tab page. Not the legitimate startpage.com. Shows ads and tracks browsing.",
    },
    "Trovi Search": {
        "type": "Browser Hijacker",
        "detection": ['Trovi', 'Trovi Search'],
        "reason": "Browser hijacker by Conduit. Changes search engine to trovi.com. Tracks searches. Injects ads.",
    },
    "iLivid": {
        "type": "Adware/PUP",
        "detection": ['iLivid', 'iLivid Download Manager'],
        "reason": "Download manager bundling adware. Changes browser settings. Installs toolbars. Tracks user behavior.",
    },
    "Wajam": {
        "type": "Adware",
        "detection": ['Wajam', 'WajIntEnhance'],
        "reason": "Adware that injects sponsored links into search results and webpages. Tracks browsing habits for advertising.",
    },
    "Iminent": {
        "type": "Adware/Browser Hijacker",
        "detection": ['Iminent', 'Iminent Toolbar'],
        "reason": "Toolbar and emoticon adware. Changes browser settings. Shows unwanted ads. Tracks browsing behavior.",
    },
    "Optimizer Pro": {
        "type": "PUP/Scareware",
        "detection": ['Optimizer Pro', 'OptimizerPro'],
        "reason": "Rogue optimizer by Iminent. False scan results. Bundles with other PUPs. No real optimization.",
    },
    "SaveSense": {
        "type": "Adware",
        "detection": ['SaveSense', 'Save Sense'],
        "reason": "Shopping adware injecting coupons and ads. Tracks shopping behavior. Slows browser. Privacy concerns.",
    },
    "PriceMeter": {
        "type": "Adware",
        "detection": ['PriceMeter'],
        "reason": "Shopping comparison adware. Injects ads and popups. Tracks browsing and shopping. Slows system.",
    },
    "Shopper Pro": {
        "type": "Adware",
        "detection": ['Shopper Pro', 'ShopperPro'],
        "reason": "Advertising program showing coupons and deals. Tracks browsing behavior and displays intrusive pop-ups.",
    },
    "Price Chopper": {
        "type": "Adware",
        "detection": ['Price Chopper', 'PriceChopper'],
        "reason": "Adware injecting shopping ads. Tracks browsing. Modifies web pages to show coupons.",
    },
    "CouponBar": {
        "type": "Adware/Toolbar",
        "detection": ['CouponBar', 'Coupon Bar'],
        "reason": "Toolbar showing coupon ads. Tracks shopping behavior. Changes browser settings.",
    },
    "Cinema Plus": {
        "type": "Adware",
        "detection": ['Cinema Plus', 'CinemaPlus'],
        "reason": "Video adware showing popups. Injects ads into video streaming sites. Tracks viewing habits.",
    },
    "Media Player Classic Codec Pack Malware": {
        "type": "Adware/Bundleware",
        "detection": ['MPC Codec Pack', 'Codec Pack'],
        "reason": "Fake codec packs bundling adware. Not the legitimate codec pack. Installs toolbars and malware.",
    },
    "Video Converter Bundleware": {
        "type": "Adware/PUP",
        "detection": ['Free Video Converter', 'VideoConverter'],
        "reason": "Free video converters often bundle adware. Install toolbars and change browser settings. Better alternatives exist.",
    },
    "DVDVideoSoft": {
        "type": "Bloatware/Bundleware",
        "detection": ['DVDVideoSoft', 'Free Studio'],
        "reason": "Free media tools bundling browser extensions and toolbars. Aggressive installer. Changes browser settings.",
    },
    "OpenCandy": {
        "type": "Adware Platform",
        "detection": ['OpenCandy'],
        "reason": "Bundleware platform used by many free software installers. Downloads and installs additional offers during installation.",
    },
    "Installcore": {
        "type": "Adware Platform/PUP",
        "detection": ['Installcore', 'InstallCore'],
        "reason": "Bundleware installer installing unwanted software. Used by many free software distributors. Difficult to opt out.",
    },
    "Amonetize": {
        "type": "Adware Platform",
        "detection": ['Amonetize'],
        "reason": "Pay-per-install adware platform. Bundles PUPs with legitimate software. Installs multiple unwanted programs.",
    },
    "Vittalia": {
        "type": "Adware Platform",
        "detection": ['Vittalia'],
        "reason": "Adware installer bundling unwanted software. Used by sketchy free software sites.",
    },
    "Download Manager by 2squared": {
        "type": "Adware/PUP",
        "detection": ['2squared', 'Download Manager'],
        "reason": "Fake download manager bundling adware. Not needed for downloads. Installs unwanted software.",
    },
    "GoPhoto.it": {
        "type": "Photo Viewer Bloatware",
        "detection": ['GoPhoto.it', 'GoPhoto'],
        "reason": "Unnecessary photo viewer preinstalled. Basic features. Windows Photos app sufficient.",
    },
    "Fresh Paint": {
        "type": "Bloatware",
        "detection": ['Microsoft.FreshPaint', 'Fresh Paint'],
        "reason": "Basic painting app preinstalled. Most users never use it. Better alternatives available.",
    },
    "Drawboard PDF": {
        "type": "Trial Bloatware",
        "detection": ['Drawboard PDF', 'Drawboard'],
        "reason": "PDF viewer trial preinstalled. Limited free features. Adobe Reader or browser PDF viewer better.",
    },
    "Music Maker Jam": {
        "type": "Bloatware/Trialware",
        "detection": ['MAGIX.MusicMakerJam', 'Music Maker Jam'],
        "reason": "Trial music making app. Limited free features. Preinstalled bloatware. Better DAWs available.",
    },
    "Minecraft: Windows 10 Edition Trial": {
        "type": "Trialware",
        "detection": ['Microsoft.MinecraftEducationEdition'],
        "reason": "Trial version of Minecraft. Should be user choice. Takes space without consent.",
    },
    "Mixed Reality Viewer": {
        "type": "Bloatware",
        "detection": ['Microsoft.Mixed Reality Viewer'],
        "reason": "VR viewer for those without VR headsets. Useless for most users. Wastes disk space.",
    },
    "Office Lens": {
        "type": "Bloatware",
        "detection": ['Microsoft.OfficeLens', 'Office Lens'],
        "reason": "Document scanner app. More useful on mobile. Desktop has better alternatives.",
    },
    "OneNote for Windows 10": {
        "type": "Bloatware",
        "detection": ['Microsoft.Office.OneNote', 'OneNote'],
        "reason": "UWP version of OneNote. Desktop version better. Preinstalled without consent.",
    },
    "Paid Wi-Fi & Cellular": {
        "type": "Bloatware",
        "detection": ['Microsoft.OneConnect'],
        "reason": "App for paid mobile data plans. Useless for most users. Preinstalled bloatware.",
    },
    "Print3D": {
        "type": "Bloatware",
        "detection": ['Microsoft.Print3D'],
        "reason": "3D printing app. Only needed if you have 3D printer. Bloatware for most.",
    },
    "Skype UWP": {
        "type": "Bloatware",
        "detection": ['Microsoft.SkypeApp', 'Skype'],
        "reason": "Preinstalled Skype. Most prefer desktop version or other chat apps. Runs in background.",
    },
    "Sticky Notes": {
        "type": "Bloatware",
        "detection": ['Microsoft.MicrosoftStickyNotes'],
        "reason": "Simple notes app. Many better alternatives. Bloatware if you don't use it.",
    },
    "Wallet": {
        "type": "Bloatware",
        "detection": ['Microsoft.Wallet'],
        "reason": "Digital wallet app. Limited merchant support. Most users prefer other payment methods.",
    },
    "Whiteboard": {
        "type": "Bloatware",
        "detection": ['Microsoft.Whiteboard', 'Whiteboard'],
        "reason": "Digital whiteboard app. Niche use case. Better collaboration tools exist.",
    },
    "Zune Music": {
        "type": "Obsolete Bloatware",
        "detection": ['Microsoft.ZuneMusic', 'Zune Music'],
        "reason": "Obsolete music player. Zune service dead. Groove Music replacement also discontinued.",
    },
    "Zune Video": {
        "type": "Obsolete Bloatware",
        "detection": ['Microsoft.ZuneVideo', 'Zune Video'],
        "reason": "Obsolete video player. No longer supported. Better alternatives available.",
    },
    "Alarms & Clock": {
        "type": "Bloatware",
        "detection": ['Microsoft.WindowsAlarms', 'Alarms & Clock'],
        "reason": "Basic alarm app. Phone does this better. Takes space most users don't need.",
    },
    "Calculator": {
        "type": "Core Utility (Optional)",
        "detection": ['Microsoft.WindowsCalculator'],
        "reason": "Windows Calculator. CORE UTILITY - Only remove if you have a preferred alternative. Most users should keep this. Only included for advanced users who want complete control.",
    },
    "Camera": {
        "type": "Bloatware",
        "detection": ['Microsoft.WindowsCamera', 'Camera'],
        "reason": "Basic camera app. Most PCs don't have cameras or use better webcam software.",
    },
    "Groove Music": {
        "type": "Abandoned Bloatware",
        "detection": ['Microsoft.ZuneMusic', 'Groove Music'],
        "reason": "Discontinued music service app. Microsoft killed Groove Music. No longer useful.",
    },
    "Microsoft Messaging": {
        "type": "Obsolete Bloatware",
        "detection": ['Microsoft.Messaging'],
        "reason": "Obsolete messaging app. Replaced by Your Phone. No longer maintained.",
    },
    "Maps": {
        "type": "Bloatware",
        "detection": ['Microsoft.WindowsMaps', 'Maps'],
        "reason": "Windows Maps app. Google Maps in browser works better. Desktop maps rarely needed.",
    },
    "People": {
        "type": "Bloatware",
        "detection": ['Microsoft.People', 'People'],
        "reason": "Contact management app. Most use phone for contacts. Limited integration.",
    },
    "Sound Recorder": {
        "type": "Bloatware",
        "detection": ['Microsoft.WindowsSoundRecorder', 'Voice Recorder'],
        "reason": "Basic voice recorder. Better audio recording software available. Minimal features.",
    },
    "Toshiba Service Station": {
        "type": "OEM Bloatware",
        "detection": ['TOSHIBA Service Station', 'Toshiba Service'],
        "reason": "Toshiba update utility. Often redundant with Windows Update. Uses background resources.",
    },
    "Toshiba Book Place": {
        "type": "OEM Bloatware",
        "detection": ['TOSHIBA Book Place'],
        "reason": "Toshiba e-book reader. Rarely used. Better e-reader apps available.",
    },
    "Sony PlayMemories": {
        "type": "OEM Bloatware",
        "detection": ['PlayMemories Home', 'Sony PlayMemories'],
        "reason": "Sony photo/video management. Resource intensive. Better alternatives exist.",
    },
    "Sony VAIO Update": {
        "type": "OEM Bloatware",
        "detection": ['VAIO Update', 'Sony VAIO Update'],
        "reason": "Sony update utility. Often causes issues. Windows Update more reliable.",
    },
    "Fujitsu DeskUpdate": {
        "type": "Bloatware/Redundant",
        "detection": ['Fujitsu DeskUpdate'],
        "reason": "REDUNDANT - Fujitsu update utility. Windows Update handles most drivers. Unnecessary background service.",
    },
    "Panasonic PC Settings Utility": {
        "type": "OEM Bloatware",
        "detection": ['PC Settings Utility', 'Panasonic PC Settings'],
        "reason": "Panasonic system utility. Most features accessible via Windows. Unnecessary.",
    },
    "Gateway Registration": {
        "type": "OEM Bloatware",
        "detection": ['Gateway Registration', 'Gateway MyBackup'],
        "reason": "Gateway registration tool. Only needed once. Takes space after registration.",
    },
    "eMachines Registration": {
        "type": "OEM Bloatware",
        "detection": ['eMachines Registration', 'eMachines Recovery Management'],
        "reason": "eMachines bloatware. One-time use tools taking permanent space.",
    },
    "Packard Bell InfoCentre": {
        "type": "OEM Bloatware",
        "detection": ['InfoCentre', 'Packard Bell InfoCentre'],
        "reason": "Packard Bell system info tool. Redundant features. Resource usage.",
    },
    "Razer Synapse (OEM)": {
        "type": "OEM Bloatware",
        "detection": ['Razer Synapse OEM', 'Razer Central'],
        "reason": "Razer device software preinstalled on non-Razer devices. User should install only if they have Razer peripherals.",
    },
    "Logitech Gaming Software (OEM)": {
        "type": "OEM Bloatware",
        "detection": ['Logitech Gaming Software OEM'],
        "reason": "Logitech software preinstalled without Logitech devices. Should be user-installed when needed.",
    },
    "Intel Rapid Storage Technology": {
        "type": "Debatable OEM",
        "detection": ['Intel Rapid Storage Technology', 'Intel RST'],
        "reason": "Intel storage driver GUI. Driver needed, GUI optional. Takes resources for rarely-used interface.",
    },
    "Intel Optane Memory": {
        "type": "Conditional Bloatware",
        "detection": ['Intel Optane Memory', 'Intel Optane'],
        "reason": "Only useful if system has Optane hardware. Bloatware on systems without it.",
    },
    "AMD Ryzen Master (OEM)": {
        "type": "Conditional Bloatware",
        "detection": ['AMD Ryzen Master OEM'],
        "reason": "Overclocking utility. Only for enthusiasts. Preinstalled version bloatware for average users.",
    },
    "NVIDIA GeForce Experience (Bloat Components)": {
        "type": "Partial Bloatware",
        "detection": ['NVIDIA GeForce Experience', 'NvContainer'],
        "reason": "Useful for drivers, but includes telemetry, mandatory login, and game recording most don't use. Privacy concerns.",
    },
    "Apple Application Support": {
        "type": "Apple Bloatware",
        "detection": ['Apple Application Support'],
        "reason": "Support library for iTunes. Takes space even if iTunes uninstalled. Leftover bloatware.",
    },
    "Apple Software Update": {
        "type": "Apple Bloatware",
        "detection": ['Apple Software Update'],
        "reason": "Update utility for Apple software. Runs in background. Not needed if no Apple software installed.",
    },
    "Java Auto Updater": {
        "type": "Bloatware/Security Risk",
        "detection": ['Java Auto Updater', 'Java Update Scheduler'],
        "reason": "Java updater running constantly. Security risk if outdated. Most users don't need Java. Disable if Java required.",
    },
    "Adobe Acrobat Update Service": {
        "type": "Background Bloatware",
        "detection": ['AdobeARMservice', 'Adobe Acrobat Update Service'],
        "reason": "Adobe Reader updater running 24/7. Resource usage. Manual updates sufficient.",
    },
    "Adobe Creative Cloud (Trial)": {
        "type": "Trial Bloatware",
        "detection": ['Adobe Creative Cloud Trial', 'Creative Cloud'],
        "reason": "Expensive Creative Cloud trial. Constant upgrade nags. Takes significant resources. Should be user-installed.",
    },
    "Google Update Service": {
        "type": "Bloatware/Resource Hog",
        "detection": ['Google Update', 'GoogleUpdate'],
        "reason": "Background service constantly checking for updates. Modern Chrome has built-in update mechanism. Redundant process consuming resources.",
    },
    "Skype Click to Call": {
        "type": "Browser Extension Bloatware",
        "detection": ['Skype Click to Call'],
        "reason": "Browser extension for Skype. Tracks phone numbers on web pages. Privacy concern. Not needed.",
    },
    "RealNetworks Update": {
        "type": "Obsolete Bloatware",
        "detection": ['RealNetworks Scheduler', 'RealPlayer Update'],
        "reason": "RealPlayer and RealDownloader updates. Obsolete software. Security risks. Better alternatives exist.",
    },
    "Corel Direct Disc Labeler": {
        "type": "OEM Bloatware",
        "detection": ['Corel Direct Disc Labeler'],
        "reason": "CD/DVD labeling software. Obsolete technology. Rarely used. Takes space.",
    },
    "Zoom Bloatware": {
        "type": "Bloatware/Privacy",
        "detection": ['Zoom OEM', 'Zoom Preinstalled'],
        "reason": "Video conferencing preinstalled without consent. Privacy concerns with data collection. Should be user choice.",
    },
    "Discord OEM": {
        "type": "Bloatware",
        "detection": ['Discord OEM', 'Discord Preinstalled'],
        "reason": "Gaming chat app preinstalled. Should be user installed when needed.",
    },
    "Microsoft Sticky Notes": {
        "type": "Bloatware",
        "detection": ['Microsoft.MicrosoftStickyNotes'],
        "reason": "Basic notes app. Many better alternatives. Optional for most users.",
    },
    "Weather": {
        "type": "Bloatware",
        "detection": ['Microsoft.BingWeather', 'MSN Weather'],
        "reason": "Weather widget. Redundant with web browsers. Uses resources.",
    },
    "Yahoo Powered": {
        "type": "Adware/Toolbar",
        "detection": ['Yahoo Powered', 'Yahoo Toolbar'],
        "reason": "Yahoo toolbar changing search settings. Tracking and ads. Difficult to remove.",
    },
    "Bing Bar": {
        "type": "Bloatware/Toolbar",
        "detection": ['Bing Bar', 'Microsoft Bing Bar'],
        "reason": "Microsoft search toolbar. Redundant. Changes browser settings.",
    },
    "PC Matic": {
        "type": "PUP/Aggressive AV",
        "detection": ['PC Matic'],
        "reason": "Aggressive antivirus with questionable detection. Fear tactics. Expensive.",
    },
    "Panda Free Antivirus": {
        "type": "Bloatware/AV",
        "detection": ['Panda Free', 'Panda Security'],
        "reason": "Free antivirus with aggressive upselling. Resource intensive. Privacy concerns.",
    },
    "Kaspersky Trial": {
        "type": "Trialware/Privacy Risk",
        "detection": ['Kaspersky Security Trial', 'Kaspersky OEM'],
        "reason": "PRIVACY RISK TRIALWARE - Russian antivirus with government concerns. Banned by several governments. Windows Defender safer.",
    },
    "ESET NOD32 Trial": {
        "type": "Trialware",
        "detection": ['ESET NOD32 Trial', 'ESET OEM'],
        "reason": "Trial security software. Nag screens. Should be user installed.",
    },
    "Trend Micro Trial": {
        "type": "Trialware/Redundant",
        "detection": ['Trend Micro Security Trial', 'Trend Micro OEM'],
        "reason": "REDUNDANT TRIALWARE - Trial antivirus. Windows Defender sufficient. Trial expires with nag screens.",
    },
    "Webroot SecureAnywhere Trial": {
        "type": "Trialware",
        "detection": ['Webroot SecureAnywhere', 'Webroot OEM'],
        "reason": "Cloud-based AV trial. Limited trial period. Constant reminders.",
    },
    "Sophos Home": {
        "type": "Bloatware/AV",
        "detection": ['Sophos Home'],
        "reason": "Enterprise AV for home. Overkill for consumers. Resource intensive.",
    },
    "Quick Heal": {
        "type": "PUP/AV",
        "detection": ['Quick Heal'],
        "reason": "Lesser-known AV with questionable practices. Often bundled. Aggressive.",
    },
    "K7 Antivirus": {
        "type": "Bloatware/AV",
        "detection": ['K7 Total Security', 'K7 Antivirus'],
        "reason": "Regional AV with limited support. Better alternatives available.",
    },
    "Comodo Antivirus": {
        "type": "PUP/Aggressive",
        "detection": ['Comodo', 'Comodo Internet Security'],
        "reason": "Aggressive antivirus. Installs own DNS. Changes settings without clear consent.",
    },
    "ZoneAlarm": {
        "type": "Bloatware/Firewall",
        "detection": ['ZoneAlarm', 'Check Point ZoneAlarm'],
        "reason": "Firewall software. Windows Firewall sufficient. Nagware. Resource heavy.",
    },
    "F-Secure Trial": {
        "type": "Trialware",
        "detection": ['F-Secure Trial', 'F-Secure OEM'],
        "reason": "Trial security suite. Limited features. Upgrade prompts.",
    },
    "G DATA": {
        "type": "Trialware/AV",
        "detection": ['G DATA', 'G DATA Antivirus'],
        "reason": "Lesser-known AV trial. Nagware. Resource usage.",
    },
    "BullGuard": {
        "type": "Trialware",
        "detection": ['BullGuard', 'BullGuard Antivirus'],
        "reason": "Trial antivirus. Aggressive marketing. Limited trial period.",
    },
    "Vipre": {
        "type": "PUP/AV",
        "detection": ['VIPRE', 'ThreatTrack Security'],
        "reason": "Enterprise AV marketed to consumers. Questionable practices. Expensive.",
    },
    "ByteFence": {
        "type": "PUP/Rogue",
        "detection": ['ByteFence'],
        "reason": "Rogue anti-malware. False positives. Bundled with other PUPs. Difficult to remove.",
    },
    "Emsisoft": {
        "type": "Trialware",
        "detection": ['Emsisoft Anti-Malware'],
        "reason": "Trial anti-malware. Constant upgrade prompts. Expensive subscription.",
    },
    "SUPERAntiSpyware": {
        "type": "PUP/Questionable",
        "detection": ['SUPERAntiSpyware'],
        "reason": "Questionable anti-spyware. False positives. Aggressive upselling.",
    },
    "Malwarebytes AdwCleaner OEM": {
        "type": "Bloatware",
        "detection": ['AdwCleaner OEM'],
        "reason": "Cleanup tool preinstalled. One-time use. Shouldn't stay installed.",
    },
    "PC Decrapifier": {
        "type": "Ironic Bloatware",
        "detection": ['PC Decrapifier'],
        "reason": "Bloatware remover that itself becomes bloatware if left installed.",
    },
    "Should I Remove It": {
        "type": "Nagware",
        "detection": ['Should I Remove It', 'Reason Company'],
        "reason": "Software advisor with constant prompts. Questionable recommendations.",
    },
    "Unchecky": {
        "type": "Bloatware Post-Purpose",
        "detection": ['Unchecky'],
        "reason": "Toolbar blocker. Useful but becomes bloatware if forgotten. Can interfere with legitimate installers.",
    },
    "Ninite": {
        "type": "Utility Bloatware",
        "detection": ['Ninite'],
        "reason": "Installer utility. No need to keep installed after initial setup.",
    },
    "FileHippo App Manager": {
        "type": "Update Nagware",
        "detection": ['FileHippo App Manager'],
        "reason": "Software updater. Constant notifications. Manual updates better.",
    },
    "Patch My PC": {
        "type": "Update Bloatware",
        "detection": ['Patch My PC'],
        "reason": "Update tool. Redundant with built-in updaters. Can cause conflicts.",
    },
    "SUMo": {
        "type": "Update Nagware",
        "detection": ['SUMo', 'Software Update Monitor'],
        "reason": "Software updater with nagware. Free version very limited. Constant upgrade prompts.",
    },
    "Chocolatey GUI": {
        "type": "Utility Bloatware",
        "detection": ['Chocolatey GUI'],
        "reason": "Package manager GUI. CLI sufficient. Rarely needed running.",
    },
    "WinGet UI": {
        "type": "Redundant Utility",
        "detection": ['WinGet UI', 'Winget-UI'],
        "reason": "Windows Package Manager GUI. CMD line sufficient. Unnecessary wrapper.",
    },
    "Scoop": {
        "type": "Utility",
        "detection": ['Scoop'],
        "reason": "Package manager. Can accumulate unused packages. Manual management better.",
    },
    "Revo Uninstaller Free": {
        "type": "Trialware/Nagware",
        "detection": ['Revo Uninstaller Free'],
        "reason": "Uninstaller with upgrade nags. Pro features locked. Built-in uninstaller sufficient.",
    },
    "Geek Uninstaller": {
        "type": "Bloatware",
        "detection": ['Geek Uninstaller'],
        "reason": "Third-party uninstaller. Not needed after use. Windows uninstaller works.",
    },
    "Absolute Uninstaller": {
        "type": "Bloatware",
        "detection": ['Absolute Uninstaller'],
        "reason": "Uninstaller tool. Minimal benefits over Windows built-in.",
    },
    "Your Uninstaller": {
        "type": "Trialware",
        "detection": ['Your Uninstaller'],
        "reason": "Paid uninstaller. Trial nags. Unnecessary expense.",
    },
    "Bulk Crap Uninstaller": {
        "type": "Utility Bloatware",
        "detection": ['BCUninstaller', 'Bulk Crap Uninstaller'],
        "reason": "Uninstaller. Good tool but can be removed after cleanup. Not needed running.",
    },
    "Steam (Pre-installed)": {
        "type": "Bloatware",
        "detection": ['Steam OEM'],
        "reason": "Gaming platform preinstalled. Should be user choice. Resource usage.",
    },
    "Origin (Pre-installed)": {
        "type": "Bloatware",
        "detection": ['Origin OEM', 'EA Origin'],
        "reason": "EA gaming platform. Should be installed by user when needed.",
    },
    "Epic Games Launcher OEM": {
        "type": "Bloatware",
        "detection": ['Epic Games Launcher OEM'],
        "reason": "Game launcher preinstalled. User should install when needed.",
    },
    "Battle.net OEM": {
        "type": "Bloatware",
        "detection": ['Battle.net OEM', 'Blizzard Battle.net OEM'],
        "reason": "Blizzard games platform. Preinstallation unnecessary. User choice.",
    },
    "GOG Galaxy OEM": {
        "type": "Bloatware",
        "detection": ['GOG Galaxy OEM'],
        "reason": "Game platform preinstalled. Should be user-installed.",
    },
    "Ubisoft Connect OEM": {
        "type": "Bloatware",
        "detection": ['Ubisoft Connect OEM', 'Uplay OEM'],
        "reason": "Ubisoft gaming platform. Preinstalled bloatware.",
    },
    "Rockstar Games Launcher OEM": {
        "type": "Bloatware",
        "detection": ['Rockstar Games Launcher OEM'],
        "reason": "Game launcher. Should be user-installed when needed.",
    },
    "Twitch OEM": {
        "type": "Bloatware",
        "detection": ['Twitch OEM', 'Twitch Desktop App OEM'],
        "reason": "Streaming app preinstalled. Browser version better. User choice.",
    },
    "TeamViewer OEM": {
        "type": "Bloatware/Security Risk",
        "detection": ['TeamViewer OEM'],
        "reason": "Remote access tool. Security risk if preinstalled. Should be user choice.",
    },
    "AnyDesk OEM": {
        "type": "Bloatware/Security Risk",
        "detection": ['AnyDesk OEM'],
        "reason": "Remote desktop tool. Security concern preinstalled. User should install.",
    },
    "LogMeIn": {
        "type": "Bloatware/Trial",
        "detection": ['LogMeIn', 'LogMeIn Hamachi OEM'],
        "reason": "Remote access tool. Often trial. Security concern. User installation better.",
    },
    "Chrome Remote Desktop OEM": {
        "type": "Bloatware",
        "detection": ['Chrome Remote Desktop OEM'],
        "reason": "Remote access preinstalled. Security risk. User should install when needed.",
    },
    "VNC Viewer OEM": {
        "type": "Bloatware",
        "detection": ['VNC Viewer OEM', 'RealVNC OEM'],
        "reason": "Remote desktop viewer. Not needed preinstalled. Security concern.",
    },
    "Splashtop": {
        "type": "Bloatware/Trial",
        "detection": ['Splashtop', 'Splashtop Streamer'],
        "reason": "Remote desktop trial. Security concern. Should be user choice.",
    },
    "PCMover": {
        "type": "Bloatware/One-Time Use",
        "detection": ['PCMover', 'Laplink PCMover'],
        "reason": "Migration tool. Only needed once. Takes space permanently.",
    },
    "EaseUS Todo Backup": {
        "type": "Trialware",
        "detection": ['EaseUS Todo Backup', 'EaseUS OEM'],
        "reason": "Backup software trial. Nagware. Windows Backup sufficient.",
    },
    "Acronis True Image OEM": {
        "type": "Trialware",
        "detection": ['Acronis True Image OEM'],
        "reason": "Backup trial. Limited features. Expensive. Alternative solutions better.",
    },
    "Macrium Reflect Free OEM": {
        "type": "Bloatware",
        "detection": ['Macrium Reflect OEM'],
        "reason": "Backup tool preinstalled. Should be user choice.",
    },
    "Paragon Backup": {
        "type": "Trialware",
        "detection": ['Paragon Backup & Recovery'],
        "reason": "Backup trial. Nagware. Not needed preinstalled.",
    },
    "AOMEI Backupper": {
        "type": "Bloatware/Nagware",
        "detection": ['AOMEI Backupper'],
        "reason": "Backup tool. Free version limited. Upgrade nags.",
    },
    "NovaBACKUP": {
        "type": "Trialware",
        "detection": ['NovaBACKUP'],
        "reason": "Backup trial. Expensive. Better free alternatives.",
    },
    "Cobian Backup": {
        "type": "Bloatware",
        "detection": ['Cobian Backup', 'Cobian Reflector'],
        "reason": "Backup utility. Not needed running constantly.",
    },
    "SyncBackFree": {
        "type": "Bloatware/Nagware",
        "detection": ['SyncBackFree', '2BrightSparks'],
        "reason": "Backup sync tool. Nagware for pro version.",
    },
    "GoodSync": {
        "type": "Trialware",
        "detection": ['GoodSync'],
        "reason": "Sync tool trial. Expensive. Simpler alternatives exist.",
    },
    "FreeFileSync": {
        "type": "Bundleware Risk",
        "detection": ['FreeFileSync'],
        "reason": "Sync tool that sometimes bundles offers. Donation nags.",
    },
    "MiniTool Partition Wizard": {
        "type": "Trialware/Nagware",
        "detection": ['MiniTool Partition Wizard'],
        "reason": "Partition tool. Free version limited. Upgrade prompts. Disk Management sufficient.",
    },
    "AOMEI Partition Assistant": {
        "type": "Bloatware/Nagware",
        "detection": ['AOMEI Partition Assistant'],
        "reason": "Partition manager. Free limited. Constant upgrade nags.",
    },
    "EaseUS Partition Master": {
        "type": "Trialware",
        "detection": ['EaseUS Partition Master'],
        "reason": "Partition tool trial. Nagware. Windows tools sufficient.",
    },
    "Paragon Partition Manager": {
        "type": "Trialware",
        "detection": ['Paragon Partition Manager'],
        "reason": "Partition manager trial. Expensive. Not needed for most users.",
    },
    "Acronis Disk Director": {
        "type": "Trialware",
        "detection": ['Acronis Disk Director'],
        "reason": "Partition tool. Enterprise focused. Expensive. Overkill for home.",
    },
    "Active@ Partition Manager": {
        "type": "Bloatware/Trial",
        "detection": ['Active@ Partition Manager'],
        "reason": "Partition tool. Trial limitations. Not needed preinstalled.",
    },
    "Stellar Data Recovery": {
        "type": "Scareware/Trial",
        "detection": ['Stellar Data Recovery', 'Stellar Phoenix'],
        "reason": "Data recovery trial. Can only scan in trial. Expensive to actually recover.",
    },
    "Recuva Professional": {
        "type": "Trialware",
        "detection": ['Recuva Professional'],
        "reason": "Data recovery. Free version sufficient. Pro upgrade nags.",
    },
    "EaseUS Data Recovery": {
        "type": "Trialware/Limited",
        "detection": ['EaseUS Data Recovery Wizard'],
        "reason": "Data recovery with severe trial limits. Can only recover 2GB free.",
    },
    "Disk Drill": {
        "type": "Trialware/Limited",
        "detection": ['Disk Drill'],
        "reason": "Data recovery. Free version very limited. Expensive upgrade.",
    },
    "Wondershare Recoverit": {
        "type": "Trialware/Scareware",
        "detection": ['Wondershare Recoverit', 'Recoverit'],
        "reason": "Data recovery. Shows files but requires payment. Expensive.",
    },
    "R-Studio": {
        "type": "Expensive Trial",
        "detection": ['R-Studio'],
        "reason": "Professional data recovery. Very expensive. Overkill for home users.",
    },
    "GetDataBack": {
        "type": "Expensive Trial",
        "detection": ['GetDataBack'],
        "reason": "Data recovery tool. Expensive. Trial very limited.",
    },
    "Hetman Recovery": {
        "type": "Trialware/Scareware",
        "detection": ['Hetman', 'Hetman Partition Recovery'],
        "reason": "Recovery suite. Shows recoverable files but requires payment.",
    },
    "Puran File Recovery": {
        "type": "Bloatware",
        "detection": ['Puran File Recovery'],
        "reason": "Recovery tool. Free alternatives better. Rarely needed.",
    },
    "Glary Undelete": {
        "type": "Bloatware",
        "detection": ['Glary Undelete'],
        "reason": "Part of Glary suite. Individual tool not needed.",
    },
    "Toolwiz File Recovery": {
        "type": "Bloatware",
        "detection": ['Toolwiz'],
        "reason": "Recovery tool. Limited functionality. Better alternatives.",
    },
    "PhotoRec": {
        "type": "Utility Bloatware",
        "detection": ['PhotoRec'],
        "reason": "Recovery utility. Command-line better. GUI wrapper unnecessary.",
    },
    "TestDisk": {
        "type": "Utility Bloatware",
        "detection": ['TestDisk'],
        "reason": "Partition recovery. Advanced tool. GUI wrappers often bloat.",
    },
    "XMRig": {
        "type": "Malware/Cryptominer",
        "detection": ['XMRig', 'xmrig', 'monero'],
        "reason": "Cryptocurrency mining software often installed without consent. Consumes CPU/GPU resources, increases electricity bills, and reduces system performance. High risk of being bundled malware.",
    },
    "NiceHash Miner": {
        "type": "PUP/Cryptominer",
        "detection": ['NiceHash', 'nicehash miner'],
        "reason": "Crypto mining software. While legitimate, often bundled without clear consent. Drains system resources and electricity.",
    },
    "Coinhive": {
        "type": "Malware/Cryptominer",
        "detection": ['Coinhive', 'coin-hive'],
        "reason": "Browser-based cryptocurrency miner. Known for being embedded in websites and software without user consent. Performance killer.",
    },
    "CryptoTab": {
        "type": "PUP/Browser Hijacker",
        "detection": ['CryptoTab', 'cryptotab browser'],
        "reason": "Browser that mines cryptocurrency using your CPU. Disguised as legitimate browser. Major resource drain.",
    },
    "DarkComet": {
        "type": "Malware/RAT",
        "detection": ['DarkComet', 'Dark Comet'],
        "reason": "Remote Access Trojan. Allows complete remote control of infected systems. Used for data theft, surveillance, and system compromise.",
    },
    "NanoCore": {
        "type": "Malware/RAT",
        "detection": ['NanoCore', 'Nano Core'],
        "reason": "Remote administration tool frequently used as malware. Enables keylogging, webcam access, and file theft.",
    },
    "njRAT": {
        "type": "Malware/RAT",
        "detection": ['njRAT', 'njrat', 'Bladabindi'],
        "reason": "Notorious remote access trojan. Steals passwords, logs keystrokes, and provides full remote control to attackers.",
    },
    "Actual Keylogger": {
        "type": "Spyware/Keylogger",
        "detection": ['Actual Keylogger', 'actualkeylogger'],
        "reason": "Keylogging software marketed as monitoring tool. Records all keystrokes including passwords and sensitive data. Major privacy violation.",
    },
    "Refog Keylogger": {
        "type": "Spyware/Keylogger",
        "detection": ['Refog', 'refog keylogger'],
        "reason": "Commercial keylogger. Captures keystrokes, screenshots, clipboard content. Often installed without proper disclosure.",
    },
    "KidLogger": {
        "type": "Spyware/Keylogger",
        "detection": ['KidLogger', 'kidlogger'],
        "reason": "Monitoring software with keylogging capabilities. Privacy invasion tool that records all user activity.",
    },
    "WebWatcher": {
        "type": "Spyware",
        "detection": ['WebWatcher', 'web watcher'],
        "reason": "Computer monitoring software. Tracks browsing history, keystrokes, and screenshots. Significant privacy concern.",
    },
    "Search Protect": {
        "type": "Browser Hijacker",
        "detection": ['Search Protect', 'Conduit Search Protect'],
        "reason": "Browser hijacker that modifies search settings and homepage. Redirects searches to generate ad revenue. Difficult to remove.",
    },
    "Sweet Page": {
        "type": "Browser Hijacker/Malicious",
        "detection": ['Sweet Page', 'sweet-page.com'],
        "reason": "MALICIOUS - Browser hijacker redirecting searches. Shows intrusive ads. Privacy violation through tracking.",
    },
    "Qvo6": {
        "type": "Browser Hijacker",
        "detection": ['Qvo6', 'qvo6.com'],
        "reason": "Aggressive browser hijacker. Modifies browser settings, redirects searches, displays unwanted ads.",
    },
    "iStart123": {
        "type": "Browser Hijacker",
        "detection": ['iStart123', 'istart123'],
        "reason": "Browser hijacker that takes over homepage and search engine. Displays ads and collects browsing data.",
    },
    "Mystart": {
        "type": "Browser Hijacker",
        "detection": ['Mystart', 'mystart.incredibar'],
        "reason": "Part of Incredibar. Changes browser homepage and search provider. Tracks user behavior for advertising.",
    },
    "PC Mechanic": {
        "type": "Scareware/PUP",
        "detection": ['PC Mechanic', 'PCMechanic'],
        "reason": "Fake optimizer showing false errors to scare users into purchasing. No real optimization benefits. Classic scareware.",
    },
    "PC Health Advisor": {
        "type": "Scareware/PUP",
        "detection": ['PC Health Advisor', 'PcHealthAdvisor'],
        "reason": "Fake system optimizer displaying fabricated issues. Designed to scare users into paying for unnecessary fixes.",
    },
    "Smart PC Care": {
        "type": "Scareware/PUP",
        "detection": ['Smart PC Care', 'smartpccare'],
        "reason": "Fake optimization tool showing false registry errors and system issues. Demands payment for 'fixes'.",
    },
    "Wise Disk Cleaner": {
        "type": "Redundant Utility",
        "detection": ['Wise Disk Cleaner', 'WiseCleaner'],
        "reason": "Disk cleaner redundant with Windows built-in tools. Minimal benefit over native Disk Cleanup.",
    },
    "Auslogics Disk Defrag": {
        "type": "Redundant Utility",
        "detection": ['Auslogics Disk Defrag', 'auslogics defrag'],
        "reason": "Defragmentation tool obsolete for modern SSDs and Windows has built-in defrag scheduler. Can harm SSDs if misused.",
    },
    "IObit Smart Defrag": {
        "type": "Redundant Utility/PUP",
        "detection": ['IObit Smart Defrag', 'SmartDefrag'],
        "reason": "Another defragmentation tool redundant with Windows features. Potentially harmful for SSDs. IObit software often bundles additional unwanted programs.",
    },
    "Superfish": {
        "type": "Adware/Security Risk",
        "detection": ['Superfish', 'VisualDiscovery'],
        "reason": "Notorious adware that breaks HTTPS security by installing root certificates. Injects ads into webpages. Major security vulnerability discovered in 2015.",
    },
    "Genieo": {
        "type": "Adware/Mac",
        "detection": ['Genieo', 'InstallMac'],
        "reason": "Mac adware that hijacks browsers. Changes homepage and search settings. Displays intrusive advertisements.",
    },
    "BitTorrent (with ads)": {
        "type": "PUP/Bundleware",
        "detection": ['BitTorrent Inc', 'bittorrent.exe'],
        "reason": "While BitTorrent itself is legitimate, official versions now include ads, cryptocurrency mining offers, and bundled software. Better alternatives exist (qBittorrent).",
    },
    "uTorrent (modern versions)": {
        "type": "PUP/Bundleware",
        "detection": ['uTorrent', 'utorrent', 'BitTorrent Inc'],
        "reason": "Modern versions include ads, bundled offers, and controversially tested cryptocurrency mining. Privacy concerns. Older versions or alternatives recommended.",
    },
    "Download Accelerator Plus": {
        "type": "PUP/Bundleware",
        "detection": ['Download Accelerator Plus', 'DAP', 'SpeedBit'],
        "reason": "Download manager known for bundling toolbars and adware. Aggressive upselling. Modern browsers make it unnecessary.",
    },
    "Internet Download Manager (cracked)": {
        "type": "Piracy/Malware Risk",
        "detection": ['IDM Crack', 'Internet Download Manager Crack'],
        "reason": "Cracked software containing high malware risk. Legitimate IDM is paid software; cracked versions often contain trojans, keyloggers, or ransomware.",
    },
    "Windows Defence Unit": {
        "type": "Fake Antivirus",
        "detection": ['Windows Defence Unit', 'WinDefenceUnit'],
        "reason": "Rogue security software showing fake virus alerts. Demands payment to remove non-existent threats. It IS the malware.",
    },
    "Live Security Platinum": {
        "type": "Fake Antivirus",
        "detection": ['Live Security Platinum', 'LSPlatinum'],
        "reason": "Notorious fake antivirus. Displays fake scan results and blocks legitimate programs. Scareware demanding payment.",
    },
    "Adobe Flash Player": {
        "type": "Deprecated/Security Risk",
        "detection": ['Adobe Flash Player', 'Flash Player', 'flashplayer'],
        "reason": "DEPRECATED since December 2020. Major security vulnerability. All major browsers removed support. Must be uninstalled immediately for security.",
    },
    "Java (old versions)": {
        "type": "Security Risk",
        "detection": ['Java 6', 'Java 7', 'Java 1.6', 'Java 1.7', 'jre1.6', 'jre1.7', 'jdk1.6', 'jdk1.7', 'jre-6', 'jre-7'],
        "reason": "Outdated Java versions with known critical security vulnerabilities. If Java is needed, update to latest version immediately.",
    },
    "Chrome Remote Desktop (unused)": {
        "type": "Redundant Utility",
        "detection": ['Chrome Remote Desktop', 'remoting_host'],
        "reason": "Remote desktop service running in background. If not actively used, wastes system resources. Consider Windows built-in Remote Desktop.",
    },
    "Adobe Genuine Service": {
        "type": "Bloatware",
        "detection": ['Adobe Genuine Service', 'AdobeGenuineService', 'AGSService'],
        "reason": "Adobe validation service checking for pirated software. Runs in background even if you have legitimate licenses. Resource waste and privacy concern.",
    },
    "HP Registration": {
        "type": "Bloatware/Useless",
        "detection": ['HP Registration', 'HP Product Registration'],
        "reason": "USELESS - One-time registration tool. No need to keep installed after registration. Pure bloatware consuming disk space.",
    },
    "HP Sure Sense": {
        "type": "Bloatware/Redundant",
        "detection": ['HP Sure Sense', 'HP Sure Sense Advanced'],
        "reason": "REDUNDANT - HP AI-based antivirus. Duplicates Windows Defender functionality. Resource hog with minimal added value.",
    },
    "HP Velocity": {
        "type": "Bloatware/Inefficient",
        "detection": ['HP Velocity'],
        "reason": "INEFFICIENT - HP network optimization tool. Questionable performance improvements. May interfere with normal network operations.",
    },
    "HP Hotkey Support": {
        "type": "Bloatware/Redundant",
        "detection": ['HP Hotkey Support', 'HP Quick Launch'],
        "reason": "REDUNDANT - HP keyboard shortcut manager. Windows handles most hotkeys natively. Unnecessary background process.",
    },
    "HP System Event Utility": {
        "type": "Bloatware/Resource-Consuming",
        "detection": ['HP System Event Utility'],
        "reason": "RESOURCE-CONSUMING - HP event monitoring tool. Runs constantly in background. Minimal user benefit. Duplicates Windows functionality.",
    },
    "HP Wireless Button Driver": {
        "type": "Bloatware/Obsolete",
        "detection": ['HP Wireless Button Driver'],
        "reason": "OBSOLETE - Driver for physical wireless toggle buttons. Modern laptops use function keys. Unnecessary on most systems.",
    },
    "Dell CinemaColor": {
        "type": "Bloatware/Useless",
        "detection": ['Dell CinemaColor', 'Dell Cinema'],
        "reason": "USELESS - Dell display color management. Minimal visible improvements. Can be adjusted via Windows display settings.",
    },
    "My Dell": {
        "type": "Bloatware/Redundant",
        "detection": ['My Dell', 'Dell Help & Support'],
        "reason": "REDUNDANT - Dell support portal app. All information available on Dell website. Unnecessary bloatware with notifications.",
    },
    "Dell ControlVault": {
        "type": "Bloatware/Niche",
        "detection": ['Dell ControlVault', 'Dell Data Protection'],
        "reason": "NICHE - Enterprise security feature. Unnecessary for home users. Adds complexity without consumer benefit.",
    },
    "WavesMaxxAudio": {
        "type": "Bloatware/Redundant",
        "detection": ['WavesMaxxAudio', 'Waves MaxxAudio Pro', 'MaxxAudioPro'],
        "reason": "REDUNDANT - Audio enhancement suite preinstalled on Dell/HP/Lenovo. Windows audio drivers sufficient. Resource usage for marginal benefit.",
    },
    "Lenovo Customer Feedback": {
        "type": "Bloatware/Privacy Risk",
        "detection": ['Lenovo Customer Feedback', 'Lenovo Experience Improvement'],
        "reason": "PRIVACY RISK - Telemetry collection tool. Sends usage data to Lenovo servers. No benefit to user. Privacy concern.",
    },
    "Lenovo Settings": {
        "type": "Bloatware/Redundant",
        "detection": ['Lenovo Settings', 'Lenovo Companion'],
        "reason": "REDUNDANT - Lenovo system settings manager. Windows Settings handles most functions. Duplicate control panel.",
    },
    "Lenovo System Update": {
        "type": "Bloatware/Security Risk",
        "detection": ['Lenovo System Update', 'Lenovo Update'],
        "reason": "SECURITY RISK - Lenovo update utility with past security vulnerabilities. Windows Update more secure and reliable. Potential exploit vector.",
    },
    "Lenovo Welcome": {
        "type": "Bloatware/Useless",
        "detection": ['Lenovo Welcome', 'Lenovo Transition'],
        "reason": "USELESS - One-time setup wizard. No purpose after initial setup. Waste of disk space.",
    },
    "Lenovo PowerDVD": {
        "type": "Bloatware/Trialware",
        "detection": ['Lenovo PowerDVD', 'CyberLink PowerDVD Lenovo'],
        "reason": "TRIALWARE - Trial DVD player by CyberLink. Limited trial period. VLC Media Player free and superior.",
    },
    "ASUS FancyStart": {
        "type": "Bloatware/Useless",
        "detection": ['ASUS FancyStart'],
        "reason": "USELESS - Decorative start menu customizer. Purely cosmetic. No functional value. Waste of resources.",
    },
    "ASUS FaceLogon": {
        "type": "Bloatware/Security Risk",
        "detection": ['ASUS FaceLogon'],
        "reason": "SECURITY RISK - Facial recognition login. Unreliable and insecure compared to password/PIN. Privacy concerns with face data storage.",
    },
    "ASUS Vibe": {
        "type": "Bloatware/Obsolete",
        "detection": ['ASUS Vibe', 'ASUS@Vibe'],
        "reason": "OBSOLETE - ASUS social sharing platform. Service discontinued. Completely useless. Should be removed immediately.",
    },
    "ASUS Device Activation": {
        "type": "Bloatware/Useless",
        "detection": ['ASUS Device Activation'],
        "reason": "USELESS - One-time device registration tool. No purpose after activation. Pure bloatware.",
    },
    "ASUS InstantOn": {
        "type": "Bloatware/Redundant",
        "detection": ['ASUS InstantOn'],
        "reason": "REDUNDANT - Fast boot utility. Windows Fast Startup provides same functionality. Duplicate feature.",
    },
    "ASUS Virtual Camera": {
        "type": "Bloatware/Niche",
        "detection": ['ASUS Virtual Camera'],
        "reason": "NICHE - Virtual camera effects utility. Limited usefulness. Most video apps have built-in effects.",
    },
    "Acer abPhoto": {
        "type": "Bloatware/Redundant",
        "detection": ['Acer abPhoto', 'abPhoto'],
        "reason": "REDUNDANT - Acer cloud photo service. Windows Photos and OneDrive superior. Unnecessary cloud service.",
    },
    "Acer abFiles": {
        "type": "Bloatware/Redundant",
        "detection": ['Acer abFiles', 'abFiles'],
        "reason": "REDUNDANT - Acer cloud file service. OneDrive and Google Drive more reliable. Unnecessary duplication.",
    },
    "Acer abDocs": {
        "type": "Bloatware/Redundant",
        "detection": ['Acer abDocs', 'abDocs'],
        "reason": "REDUNDANT - Acer cloud document service. Office 365 and Google Docs better. Pointless cloud service.",
    },
    "Acer BYOC Apps": {
        "type": "Bloatware/Privacy Risk",
        "detection": ['Acer BYOC'],
        "reason": "PRIVACY RISK - Acer 'Bring Your Own Cloud' apps. Requires sharing credentials with Acer. Security and privacy concerns.",
    },
    "Acer User Experience Improvement": {
        "type": "Bloatware/Privacy Risk",
        "detection": ['Acer User Experience Improvement', 'ACERUEI'],
        "reason": "PRIVACY RISK - Telemetry collection program. Sends usage data to Acer without clear user benefit. Privacy concern.",
    },
    "TOSHIBA Service Station": {
        "type": "Bloatware/Redundant",
        "detection": ['TOSHIBA Service Station'],
        "reason": "REDUNDANT - Toshiba update checker. Windows Update handles most updates. Unnecessary background service.",
    },
    "TOSHIBA Bulletin Board": {
        "type": "Bloatware/Useless",
        "detection": ['TOSHIBA Bulletin Board'],
        "reason": "USELESS - Desktop note/reminder app. Windows Sticky Notes better. Pointless bloatware.",
    },
    "TOSHIBA Face Recognition": {
        "type": "Bloatware/Security Risk",
        "detection": ['TOSHIBA Face Recognition'],
        "reason": "SECURITY RISK - Outdated facial recognition. Unreliable and insecure. Windows Hello better alternative.",
    },
    "TOSHIBA ConfigFree": {
        "type": "Bloatware/Obsolete",
        "detection": ['TOSHIBA ConfigFree'],
        "reason": "OBSOLETE - Old network management utility. Windows native networking superior. Ancient bloatware.",
    },
    "TOSHIBA eco Utility": {
        "type": "Bloatware/Redundant",
        "detection": ['TOSHIBA eco Utility'],
        "reason": "REDUNDANT - Power saving utility. Windows power management better. Duplicate functionality.",
    },
    "TOSHIBA App Place": {
        "type": "Bloatware/Adware",
        "detection": ['TOSHIBA App Place', 'TOSHIBA AppPlace'],
        "reason": "ADWARE - Toshiba app store promoting software. Bloatware suggesting more bloatware. Advertisements.",
    },
    "TOSHIBA Media Controller": {
        "type": "Bloatware/Redundant",
        "detection": ['TOSHIBA Media Controller'],
        "reason": "REDUNDANT - Media streaming utility. Windows Media Player and modern streaming apps better. Obsolete.",
    },
    "TOSHIBA Password Utility": {
        "type": "Bloatware/Security Risk",
        "detection": ['TOSHIBA Password Utility'],
        "reason": "SECURITY RISK - Proprietary password manager. Third-party password managers like Bitwarden more secure. Outdated.",
    },
    "MSI Center": {
        "type": "Bloatware/Resource-Consuming",
        "detection": ['MSI Center', 'MSI Dragon Center 2'],
        "reason": "RESOURCE-CONSUMING - MSI system control suite. Heavy RAM and CPU usage. Most features accessible via Windows.",
    },
    "MSI True Color": {
        "type": "Bloatware/Redundant",
        "detection": ['MSI True Color'],
        "reason": "REDUNDANT - Display color calibration. Windows color management sufficient. Minimal benefit.",
    },
    "MSI BurnRecovery": {
        "type": "Bloatware/Obsolete",
        "detection": ['MSI BurnRecovery'],
        "reason": "OBSOLETE - Optical disc burning utility. USB recovery better. CD/DVD burning rarely needed.",
    },
    "Nahimic Audio": {
        "type": "Bloatware/Resource-Consuming",
        "detection": ['Nahimic', 'Nahimic Audio', 'Nahimic Service'],
        "reason": "RESOURCE-CONSUMING - Audio enhancement suite. Known for bugs and high CPU usage. Windows audio sufficient.",
    },
    "MSI Fast Boot": {
        "type": "Bloatware/Redundant",
        "detection": ['MSI Fast Boot'],
        "reason": "REDUNDANT - Fast boot utility. Windows Fast Startup provides same feature. Unnecessary duplication.",
    },
    "VAIO Control Center": {
        "type": "Bloatware/Obsolete",
        "detection": ['VAIO Control Center'],
        "reason": "OBSOLETE - Sony system settings manager. Brand discontinued. All features in Windows Settings.",
    },
    "VAIO Media Plus": {
        "type": "Bloatware/Redundant",
        "detection": ['VAIO Media Plus', 'VAIO Media Gallery'],
        "reason": "REDUNDANT - Sony media manager. Windows Photos and Groove Music better. Obsolete software.",
    },
    "PlayMemories Home": {
        "type": "Bloatware/Redundant",
        "detection": ['PlayMemories Home', 'PMHome'],
        "reason": "REDUNDANT - Sony photo/video manager. Windows Photos sufficient. Bloated with unnecessary features.",
    },
    "VAIO Messenger": {
        "type": "Bloatware/Obsolete",
        "detection": ['VAIO Messenger'],
        "reason": "OBSOLETE - Sony communication tool. Service discontinued. Completely useless.",
    },
    "ArcSoft WebCam Companion": {
        "type": "Bloatware/Redundant",
        "detection": ['ArcSoft WebCam Companion', 'Magic-i Visual Effects'],
        "reason": "REDUNDANT - Webcam effects software. Most video apps have built-in effects. Unnecessary bloatware.",
    },
    "Fujitsu Display Manager": {
        "type": "Bloatware/Redundant",
        "detection": ['Fujitsu Display Manager'],
        "reason": "REDUNDANT - Display management utility. Windows display settings sufficient. Pointless overlay.",
    },
    "Fujitsu Application Panel": {
        "type": "Bloatware/Useless",
        "detection": ['Fujitsu Application Panel'],
        "reason": "USELESS - App launcher utility. Windows Start Menu better. Unnecessary bloatware.",
    },
    "Razer Cortex": {
        "type": "Bloatware/Resource-Consuming",
        "detection": ['Razer Cortex', 'Razer Game Booster'],
        "reason": "RESOURCE-CONSUMING - Game optimization tool. Questionable performance benefits. Uses resources while claiming to free them.",
    },
    "Razer Surround": {
        "type": "Bloatware/Niche",
        "detection": ['Razer Surround'],
        "reason": "NICHE - Virtual surround sound software. Limited benefit without specific headphones. Unnecessary for most users.",
    },
    "Snap.do Toolbar": {
        "type": "Browser Hijacker/Malicious",
        "detection": ['Snap.do', 'SnapDo', 'Search.snapdo.com'],
        "reason": "MALICIOUS - Browser hijacker changing homepage and search engine. Tracks browsing data. Difficult to remove.",
    },
    "Delta Toolbar": {
        "type": "Browser Hijacker/Adware",
        "detection": ['Delta Toolbar', 'Delta Search', 'delta-search.com'],
        "reason": "ADWARE - Bundled toolbar hijacker. Changes default search to Delta Search. Displays unwanted advertisements.",
    },
    "iMesh Toolbar": {
        "type": "Browser Hijacker/Adware",
        "detection": ['iMesh Toolbar', 'iMeshBar'],
        "reason": "ADWARE - Bundled with iMesh P2P software. Browser hijacker with ads. Tracks browsing behavior.",
    },
    "Shopping Helper Smartbar": {
        "type": "Adware/Malicious",
        "detection": ['Shopping Helper Smartbar', 'Smartbar'],
        "reason": "MALICIOUS - Aggressive adware showing shopping deals. Browser hijacker. Extremely difficult to remove completely.",
    },
    "MyWebSearch Toolbar": {
        "type": "Browser Hijacker/Spyware",
        "detection": ['MyWebSearch', 'MyWebSearch Toolbar', 'MyWay'],
        "reason": "SPYWARE - Known browser hijacker and spyware. Tracks all browsing activity. Changes search provider and homepage.",
    },
    "GoSave Toolbar": {
        "type": "Adware/Malicious",
        "detection": ['GoSave', 'GoSave Toolbar'],
        "reason": "MALICIOUS - Shopping adware injecting ads into websites. Browser hijacker. Privacy invasion through tracking.",
    },
    "Coupon Server": {
        "type": "Adware/Malicious",
        "detection": ['Coupon Server', 'CouponServer'],
        "reason": "MALICIOUS - Adware injecting unwanted coupons and ads. Slows browsing. Tracks shopping behavior.",
    },
    "RocketTab": {
        "type": "Browser Hijacker/Malicious",
        "detection": ['RocketTab', 'Rocket Tab'],
        "reason": "MALICIOUS - Browser hijacker changing new tab page. Shows ads and sponsored content. Tracks browsing data.",
    },
    "Marquis": {
        "type": "Browser Hijacker/Adware",
        "detection": ['Marquis', 'SearchMarquis'],
        "reason": "ADWARE - Mac and Windows browser hijacker. Redirects searches through affiliate links. Privacy invasion.",
    },
    "VSearch": {
        "type": "Browser Hijacker/Malicious",
        "detection": ['VSearch', 'Vsearch.com'],
        "reason": "MALICIOUS - Browser hijacker changing search provider. Displays misleading ads. Tracks user searches.",
    },
    "CoolWebSearch": {
        "type": "Browser Hijacker/Malware",
        "detection": ['CoolWebSearch', 'CWS'],
        "reason": "MALWARE - Notorious browser hijacker family. Extremely difficult to remove. Changes homepage and search repeatedly.",
    },
    "OneWebSearch": {
        "type": "Browser Hijacker/Adware",
        "detection": ['OneWebSearch'],
        "reason": "ADWARE - Browser hijacker redirecting searches. Shows sponsored results. Privacy concern with data collection.",
    },
    "SourceForge Installer": {
        "type": "Bundleware/Adware",
        "detection": ['SourceForge Installer', 'SF Installer'],
        "reason": "BUNDLEWARE - SourceForge installer bundling unwanted software. Often installs toolbars and adware. Use direct downloads only.",
    },
    "WinZip Trial": {
        "type": "Trialware/Redundant",
        "detection": ['WinZip Trial', 'WinZip Evaluation'],
        "reason": "REDUNDANT TRIALWARE - Trial compression utility. Windows has built-in ZIP support. 7-Zip free and superior. Expensive license for basic features.",
    },
    "WinRAR Trial": {
        "type": "Trialware",
        "detection": ['WinRAR Trial', 'WinRAR Evaluation'],
        "reason": "TRIALWARE - Trial archive manager. Free trial never expires but shows nag screens. 7-Zip completely free alternative.",
    },
    "CyberLink PowerDVD Trial": {
        "type": "Trialware/Obsolete",
        "detection": ['CyberLink PowerDVD Trial', 'PowerDVD OEM'],
        "reason": "OBSOLETE TRIALWARE - Trial DVD/Blu-ray player. Optical media declining. VLC Media Player free and plays everything.",
    },
    "CyberLink Power2Go": {
        "type": "Trialware/Obsolete",
        "detection": ['CyberLink Power2Go', 'Power2Go OEM'],
        "reason": "OBSOLETE TRIALWARE - Trial disc burning software. Optical media rarely used. Windows has built-in burning. Free alternatives better.",
    },
    "CyberLink PhotoDirector": {
        "type": "Trialware/Redundant",
        "detection": ['CyberLink PhotoDirector', 'PhotoDirector OEM'],
        "reason": "REDUNDANT TRIALWARE - Trial photo editor. Limited features in trial. Windows Photos or GIMP better alternatives.",
    },
    "CyberLink YouCam": {
        "type": "Trialware/Redundant",
        "detection": ['CyberLink YouCam'],
        "reason": "REDUNDANT TRIALWARE - Trial webcam effects software. Modern video apps have built-in effects. Unnecessary bloatware.",
    },
    "Nero Burning ROM Trial": {
        "type": "Trialware/Obsolete",
        "detection": ['Nero Burning ROM Trial', 'Nero Trial', 'Nero Essentials'],
        "reason": "OBSOLETE TRIALWARE - Trial disc burning suite. Optical media declining. Heavy software for rarely-needed feature.",
    },
    "Roxio Creator Trial": {
        "type": "Trialware/Obsolete",
        "detection": ['Roxio Creator Trial', 'Roxio OEM'],
        "reason": "OBSOLETE TRIALWARE - Trial multimedia suite. CD/DVD burning obsolete. Bloated software with limited trial.",
    },
    "Corel PaintShop Pro Trial": {
        "type": "Trialware",
        "detection": ['Corel PaintShop Pro Trial', 'PaintShop Pro OEM'],
        "reason": "TRIALWARE - Trial photo editor. Limited trial period. GIMP or Paint.NET free alternatives. Expensive full version.",
    },
    "Corel VideoStudio Trial": {
        "type": "Trialware",
        "detection": ['Corel VideoStudio Trial', 'VideoStudio OEM'],
        "reason": "TRIALWARE - Trial video editor. Limited features and time. DaVinci Resolve free and more powerful.",
    },
    "Evernote OEM": {
        "type": "Bloatware/Trialware",
        "detection": ['Evernote OEM', 'Evernote Preinstalled'],
        "reason": "TRIALWARE - Note-taking app preinstalled by OEMs. Limited free version. OneNote free and better integrated with Windows.",
    },
    "Dropbox Promotional": {
        "type": "Bloatware",
        "detection": ['Dropbox 25 GB', 'Dropbox Promotion'],
        "reason": "BLOATWARE - Promotional Dropbox installer. OEM deals for limited storage. Should be user choice to install.",
    },
    "McAfee WebAdvisor": {
        "type": "Bloatware/PUP",
        "detection": ['McAfee WebAdvisor', 'McAfee SiteAdvisor'],
        "reason": "PUP BLOATWARE - Browser extension often bundled. Slows browsing. Shows unnecessary warnings. McAfee branded but separate from AV.",
    },
    "Norton Safe Web": {
        "type": "Bloatware/Redundant",
        "detection": ['Norton Safe Web', 'Norton SafeWeb'],
        "reason": "REDUNDANT BLOATWARE - Browser extension for site ratings. Slows browsing. Windows Defender SmartScreen sufficient.",
    },
    "Adobe Acrobat Reader DC Trial": {
        "type": "Bloatware/Redundant",
        "detection": ['Adobe Acrobat Reader DC Trial', 'Adobe Reader Trial'],
        "reason": "REDUNDANT TRIALWARE - PDF reader with trial pro features. Edge browser reads PDFs. Sumatra PDF lightweight free alternative.",
    },
    "Office 365 Trial": {
        "type": "Trialware",
        "detection": ['Microsoft Office 365 Trial', 'Office Trial', 'Office 365 OEM'],
        "reason": "TRIALWARE - Time-limited Office trial. Should be user choice. LibreOffice free alternative. Expensive subscription.",
    },

}
