#!/usr/bin/env python3
"""
Static site generator for spanishvoiceover.net
Generates a complete multilingual website for Guillermo A. Brazález
"""

import os
import json
from pathlib import Path

# ─── Configuration ────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent
SITE_URL = "https://spanishvoiceover.net"

LANGUAGES = {
    "es": {"name": "Español", "flag": "🇪🇸", "locale": "es_ES", "dir": ""},
    "en": {"name": "English", "flag": "🇬🇧", "locale": "en_GB", "dir": "en"},
    "fr": {"name": "Français", "flag": "🇫🇷", "locale": "fr_FR", "dir": "fr"},
    "de": {"name": "Deutsch", "flag": "🇩🇪", "locale": "de_DE", "dir": "de"},
    "it": {"name": "Italiano", "flag": "🇮🇹", "locale": "it_IT", "dir": "it"},
    "pt": {"name": "Português", "flag": "🇵🇹", "locale": "pt_PT", "dir": "pt"},
    "sv": {"name": "Svenska", "flag": "🇸🇪", "locale": "sv_SE", "dir": "sv"},
    "no": {"name": "Norsk", "flag": "🇳🇴", "locale": "nb_NO", "dir": "no"},
    "da": {"name": "Dansk", "flag": "🇩🇰", "locale": "da_DK", "dir": "da"},
    "nl": {"name": "Nederlands", "flag": "🇳🇱", "locale": "nl_NL", "dir": "nl"},
    "el": {"name": "Ελληνικά", "flag": "🇬🇷", "locale": "el_GR", "dir": "el"},
    "zh": {"name": "中文", "flag": "🇨🇳", "locale": "zh_CN", "dir": "zh"},
    "ru": {"name": "Русский", "flag": "🇷🇺", "locale": "ru_RU", "dir": "ru"},
}

# ─── Localized slugs ─────────────────────────────────────────────────────────

SLUGS = {
    "es": {
        "voice_actor": "locutor",
        "spots": "spots",
        "documentaries": "documentales",
        "radio": "radio",
        "corporate": "corporativo",
        "audiobooks": "audiolibros",
        "studio": "estudio",
        "trivago": "trivago",
        "composer": "compositor",
        "contact": "contacto",
    },
    "en": {
        "voice_actor": "voice-actor",
        "spots": "tv-commercials",
        "documentaries": "documentary",
        "radio": "radio",
        "corporate": "corporate",
        "audiobooks": "audiobooks",
        "studio": "studio",
        "trivago": "trivago",
        "composer": "composer",
        "contact": "contact",
    },
    "fr": {
        "voice_actor": "comédien-vocal",
        "spots": "spots-publicitaires",
        "documentaries": "documentaires",
        "radio": "radio",
        "corporate": "voix-corporate",
        "audiobooks": "livres-audio",
        "studio": "studio",
        "trivago": "trivago",
        "composer": "compositeur",
        "contact": "contact",
    },
    "de": {
        "voice_actor": "sprecher",
        "spots": "werbespots",
        "documentaries": "dokumentationen",
        "radio": "radio",
        "corporate": "unternehmen",
        "audiobooks": "hoerbuecher",
        "studio": "studio",
        "trivago": "trivago",
        "composer": "komponist",
        "contact": "kontakt",
    },
    "it": {
        "voice_actor": "doppiatore",
        "spots": "spot-pubblicitari",
        "documentaries": "documentari",
        "radio": "radio",
        "corporate": "video-aziendali",
        "audiobooks": "audiolibri",
        "studio": "studio",
        "trivago": "trivago",
        "composer": "compositore",
        "contact": "contatto",
    },
    "pt": {
        "voice_actor": "locutor",
        "spots": "spots-publicitarios",
        "documentaries": "documentarios",
        "radio": "radio",
        "corporate": "video-corporativo",
        "audiobooks": "audiolivros",
        "studio": "estudio",
        "trivago": "trivago",
        "composer": "compositor",
        "contact": "contacto",
    },
    "sv": {
        "voice_actor": "rostskadespelare",
        "spots": "reklamfilm",
        "documentaries": "dokumentarer",
        "radio": "radio",
        "corporate": "foretagsfilm",
        "audiobooks": "ljudbocker",
        "studio": "studio",
        "trivago": "trivago",
        "composer": "kompositoer",
        "contact": "kontakt",
    },
    "no": {
        "voice_actor": "stemme",
        "spots": "reklamefilm",
        "documentaries": "dokumentarer",
        "radio": "radio",
        "corporate": "bedriftsfilm",
        "audiobooks": "lydboker",
        "studio": "studio",
        "trivago": "trivago",
        "composer": "komponist",
        "contact": "kontakt",
    },
    "da": {
        "voice_actor": "stemme",
        "spots": "reklamefilm",
        "documentaries": "dokumentarer",
        "radio": "radio",
        "corporate": "virksomhedsfilm",
        "audiobooks": "lydboger",
        "studio": "studie",
        "trivago": "trivago",
        "composer": "komponist",
        "contact": "kontakt",
    },
    "nl": {
        "voice_actor": "stemacteur",
        "spots": "reclamespot",
        "documentaries": "documentaires",
        "radio": "radio",
        "corporate": "bedrijfsvideo",
        "audiobooks": "luisterboeken",
        "studio": "studio",
        "trivago": "trivago",
        "composer": "componist",
        "contact": "contact",
    },
    "el": {
        "voice_actor": "ekfonitis",
        "spots": "diafimistika",
        "documentaries": "ntokimanter",
        "radio": "radio",
        "corporate": "etairiko-video",
        "audiobooks": "akoustika-vivlia",
        "studio": "stountio",
        "trivago": "trivago",
        "composer": "synthetes",
        "contact": "epikoinonia",
    },
    "zh": {
        "voice_actor": "peiyin",
        "spots": "guanggao",
        "documentaries": "jilupian",
        "radio": "guangbo",
        "corporate": "qiye",
        "audiobooks": "youshengshu",
        "studio": "luyin",
        "trivago": "trivago",
        "composer": "zuoqu",
        "contact": "lianxi",
    },
    "ru": {
        "voice_actor": "diktor",
        "spots": "reklama",
        "documentaries": "dokumentalny",
        "radio": "radio",
        "corporate": "korporativnoe",
        "audiobooks": "audioknigi",
        "studio": "studiya",
        "trivago": "trivago",
        "composer": "kompozitor",
        "contact": "kontakt",
    },
}

# ─── Vimeo IDs ────────────────────────────────────────────────────────────────

VIMEO = {
    "spots": ["810218134", "690302511", "690284458", "690295928", "689499089", "689499667", "601300814", "601301660", "690293690"],
    "documentaries": ["690250937", "690260159", "690276233", "690269159", "690251119", "690258991", "690273903", "690255996", "690277651", "690267452", "690254336", "690271782", "1183454881"],
    "corporate": ["690280127", "689499565"],
}


# ─── Trivago Page Content ────────────────────────────────────────────────────

TRIVAGO_YOUTUBE = ["9NJes_OMxqg", "GPKPjA0_97I", "_diBjgG5Xqo"]

TRIVAGO_CONTENT = {
    "es": {
        "title": "Voz Española de Trivago — Guillermo A. Brazález",
        "meta_title": "Voz Española de Trivago | Guillermo A. Brazález — Locutor Spots Trivago",
        "meta_desc": "Guillermo A. Brazález es la voz en español de los spots de Trivago en España. Locutor profesional de las campañas más recientes de Trivago con Jürgen Klopp.",
        "h1": "La Voz Española de Trivago",
        "intro": """<p><strong>Guillermo A. Brazález</strong> es la voz en español de los spots publicitarios de <strong>Trivago</strong> en España. Como locutor profesional con más de 20 años de experiencia, Guillermo ha sido elegido por Trivago para dar voz en castellano a sus campañas publicitarias más recientes, incluyendo los anuncios protagonizados por <strong>Jürgen Klopp</strong>.</p>
            <p>Su voz castellana es la que acompaña a millones de espectadores españoles cada vez que ven un anuncio de Trivago en televisión. Desde spots de 20 segundos hasta campañas completas, la voz de Guillermo transmite la confianza, cercanía y profesionalidad que define a la marca Trivago en el mercado español.</p>
            <p>La colaboración entre Guillermo A. Brazález y Trivago representa una de las asociaciones más reconocidas entre un locutor español y una marca global de viajes. Su voz en castellano se ha convertido en un elemento identificativo de Trivago en España, reconocible al instante por el público español.</p>""",
        "section_videos": "Spots de Trivago en Español",
        "section_about": "Sobre la Colaboración con Trivago",
        "about_text": """<p>Trivago, el comparador de hoteles líder en el mundo, confía en la voz de Guillermo A. Brazález para comunicar su mensaje al público español. Las campañas recientes, protagonizadas por el exentrenador del Liverpool FC <strong>Jürgen Klopp</strong>, llevan la locución en castellano de Guillermo, quien aporta calidez y credibilidad a cada spot.</p>
            <p>La elección de un locutor profesional español nativo para las campañas de Trivago en España garantiza una conexión auténtica con la audiencia hispanohablante, transmitiendo el mensaje de la marca con la entonación y el acento natural del español castellano.</p>""",
        "cta_text": "¿Buscas una voz profesional para tu marca?",
        "faq": [
            {"q": "¿Quién es la voz española de Trivago?", "a": "Guillermo A. Brazález es el locutor profesional español que presta su voz en castellano a los spots publicitarios de Trivago en España, incluyendo las campañas más recientes con Jürgen Klopp."},
            {"q": "¿Desde cuándo es Guillermo la voz de Trivago en España?", "a": "Guillermo A. Brazález ha sido la voz en español de las campañas más recientes de Trivago en España, dando voz en castellano a los anuncios protagonizados por Jürgen Klopp."},
            {"q": "¿Cómo contratar al locutor de Trivago España?", "a": "Puedes contactar con Guillermo A. Brazález directamente a través de WhatsApp (+34 606 350 350), email (info@guillermobrazalez.es) o mediante la página de contacto de esta web."},
        ],
    },
    "en": {
        "title": "Spanish Voice of Trivago — Guillermo A. Brazález",
        "meta_title": "Spanish Voice of Trivago | Guillermo A. Brazález — Trivago Spain Voice-Over",
        "meta_desc": "Guillermo A. Brazález is the Spanish voice of Trivago commercials in Spain. Professional voice-over artist behind Trivago's latest ad campaigns with Jürgen Klopp.",
        "h1": "The Spanish Voice of Trivago",
        "intro": """<p><strong>Guillermo A. Brazález</strong> is the Spanish voice behind <strong>Trivago's</strong> television commercials in Spain. A professional voice-over artist with over 20 years of experience, Guillermo was chosen by Trivago to voice their most recent Spanish advertising campaigns, including the spots featuring <strong>Jürgen Klopp</strong>.</p>
            <p>His Castilian Spanish voice accompanies millions of Spanish viewers every time they see a Trivago commercial on television. From 20-second spots to full campaigns, Guillermo's voice conveys the trust, warmth, and professionalism that defines the Trivago brand in the Spanish market.</p>
            <p>The collaboration between Guillermo A. Brazález and Trivago represents one of the most recognized partnerships between a Spanish voice actor and a global travel brand. His Castilian Spanish voice has become an identifying element of Trivago in Spain, instantly recognizable by Spanish audiences.</p>""",
        "section_videos": "Trivago Spots in Spanish",
        "section_about": "About the Trivago Collaboration",
        "about_text": """<p>Trivago, the world's leading hotel comparison platform, trusts Guillermo A. Brazález's voice to deliver its message to the Spanish audience. The recent campaigns, starring former Liverpool FC manager <strong>Jürgen Klopp</strong>, feature Guillermo's Castilian Spanish voice-over, bringing warmth and credibility to every spot.</p>
            <p>Choosing a native professional Spanish voice actor for Trivago's campaigns in Spain ensures an authentic connection with the Spanish-speaking audience, delivering the brand's message with the natural intonation and accent of Castilian Spanish.</p>""",
        "cta_text": "Looking for a professional voice for your brand?",
        "faq": [
            {"q": "Who is the Spanish voice of Trivago?", "a": "Guillermo A. Brazález is the professional Spanish voice-over artist who voices Trivago's TV commercials in Spain, including the most recent campaigns featuring Jürgen Klopp."},
            {"q": "How to hire the Trivago Spain voice actor?", "a": "You can contact Guillermo A. Brazález directly via WhatsApp (+34 606 350 350), email (info@guillermobrazalez.es), or through the contact page on this website."},
            {"q": "What campaigns has Guillermo voiced for Trivago?", "a": "Guillermo A. Brazález has voiced Trivago's most recent television advertising campaigns in Spain, including the spots featuring football manager Jürgen Klopp as brand ambassador."},
        ],
    },
    "fr": {
        "title": "Voix Espagnole de Trivago — Guillermo A. Brazález",
        "meta_title": "Voix Espagnole de Trivago | Guillermo A. Brazález — Doubleur Spots Trivago",
        "meta_desc": "Guillermo A. Brazález est la voix espagnole des publicités Trivago en Espagne. Comédien vocal des dernières campagnes Trivago avec Jürgen Klopp.",
        "h1": "La Voix Espagnole de Trivago",
        "intro": """<p><strong>Guillermo A. Brazález</strong> est la voix espagnole des spots publicitaires de <strong>Trivago</strong> en Espagne. Comédien vocal professionnel avec plus de 20 ans d'expérience, Guillermo a été choisi par Trivago pour donner sa voix en castillan à leurs campagnes publicitaires les plus récentes, y compris les spots avec <strong>Jürgen Klopp</strong>.</p>
            <p>Sa voix en espagnol castillan accompagne des millions de téléspectateurs espagnols chaque fois qu'ils voient une publicité Trivago à la télévision. Sa voix transmet la confiance et le professionnalisme qui définissent la marque Trivago sur le marché espagnol.</p>""",
        "section_videos": "Spots Trivago en Espagnol",
        "section_about": "À Propos de la Collaboration avec Trivago",
        "about_text": """<p>Trivago, le premier comparateur d'hôtels au monde, fait confiance à la voix de Guillermo A. Brazález pour communiquer son message au public espagnol. Les campagnes récentes, avec l'ancien entraîneur du Liverpool FC <strong>Jürgen Klopp</strong>, portent la voix en castillan de Guillermo.</p>""",
        "cta_text": "Vous cherchez une voix professionnelle pour votre marque ?",
        "faq": [
            {"q": "Qui est la voix espagnole de Trivago ?", "a": "Guillermo A. Brazález est le comédien vocal professionnel qui prête sa voix espagnole aux spots publicitaires de Trivago en Espagne."},
        ],
    },
    "de": {
        "title": "Spanische Stimme von Trivago — Guillermo A. Brazález",
        "meta_title": "Spanische Stimme von Trivago | Guillermo A. Brazález — Trivago Spanien Sprecher",
        "meta_desc": "Guillermo A. Brazález ist die spanische Stimme der Trivago-Werbespots in Spanien. Professioneller Sprecher der neuesten Trivago-Kampagnen mit Jürgen Klopp.",
        "h1": "Die Spanische Stimme von Trivago",
        "intro": """<p><strong>Guillermo A. Brazález</strong> ist die spanische Stimme der <strong>Trivago</strong>-Werbespots in Spanien. Als professioneller Sprecher mit über 20 Jahren Erfahrung wurde Guillermo von Trivago ausgewählt, um den neuesten Werbekampagnen seine kastilisch-spanische Stimme zu verleihen, einschließlich der Spots mit <strong>Jürgen Klopp</strong>.</p>
            <p>Seine kastilisch-spanische Stimme begleitet Millionen spanischer Zuschauer bei jedem Trivago-Werbespot im Fernsehen und vermittelt das Vertrauen und die Professionalität der Marke Trivago auf dem spanischen Markt.</p>""",
        "section_videos": "Trivago-Spots auf Spanisch",
        "section_about": "Über die Zusammenarbeit mit Trivago",
        "about_text": """<p>Trivago, der weltweit führende Hotel-Preisvergleich, vertraut auf die Stimme von Guillermo A. Brazález. Die aktuellen Kampagnen mit dem ehemaligen Liverpool-FC-Trainer <strong>Jürgen Klopp</strong> tragen Guillermos kastilisch-spanische Synchronstimme.</p>""",
        "cta_text": "Suchen Sie eine professionelle Stimme für Ihre Marke?",
        "faq": [
            {"q": "Wer ist die spanische Stimme von Trivago?", "a": "Guillermo A. Brazález ist der professionelle spanische Sprecher, der die Trivago-Werbespots in Spanien spricht, einschließlich der neuesten Kampagnen mit Jürgen Klopp."},
        ],
    },
    "it": {
        "title": "Voce Spagnola di Trivago — Guillermo A. Brazález",
        "meta_title": "Voce Spagnola di Trivago | Guillermo A. Brazález — Doppiatore Spot Trivago",
        "meta_desc": "Guillermo A. Brazález è la voce spagnola degli spot Trivago in Spagna. Doppiatore delle ultime campagne Trivago con Jürgen Klopp.",
        "h1": "La Voce Spagnola di Trivago",
        "intro": """<p><strong>Guillermo A. Brazález</strong> è la voce spagnola degli spot pubblicitari di <strong>Trivago</strong> in Spagna. Doppiatore professionista con oltre 20 anni di esperienza, è stato scelto da Trivago per dare voce in castigliano alle campagne più recenti con <strong>Jürgen Klopp</strong>.</p>""",
        "section_videos": "Spot Trivago in Spagnolo",
        "section_about": "Sulla Collaborazione con Trivago",
        "about_text": """<p>Trivago, il principale comparatore di hotel al mondo, si affida alla voce di Guillermo A. Brazález per comunicare al pubblico spagnolo.</p>""",
        "cta_text": "Cerchi una voce professionale per il tuo brand?",
        "faq": [
            {"q": "Chi è la voce spagnola di Trivago?", "a": "Guillermo A. Brazález è il doppiatore professionista che presta la sua voce spagnola agli spot pubblicitari di Trivago in Spagna."},
        ],
    },
    "pt": {
        "title": "Voz Espanhola da Trivago — Guillermo A. Brazález",
        "meta_title": "Voz Espanhola da Trivago | Guillermo A. Brazález — Locutor Anúncios Trivago",
        "meta_desc": "Guillermo A. Brazález é a voz espanhola dos anúncios da Trivago em Espanha. Locutor das últimas campanhas Trivago com Jürgen Klopp.",
        "h1": "A Voz Espanhola da Trivago",
        "intro": """<p><strong>Guillermo A. Brazález</strong> é a voz espanhola dos anúncios publicitários da <strong>Trivago</strong> em Espanha. Locutor profissional com mais de 20 anos de experiência, foi escolhido pela Trivago para dar voz em castelhano às campanhas mais recentes com <strong>Jürgen Klopp</strong>.</p>""",
        "section_videos": "Spots Trivago em Espanhol",
        "section_about": "Sobre a Colaboração com a Trivago",
        "about_text": """<p>A Trivago confia na voz de Guillermo A. Brazález para comunicar a sua mensagem ao público espanhol.</p>""",
        "cta_text": "Procura uma voz profissional para a sua marca?",
        "faq": [
            {"q": "Quem é a voz espanhola da Trivago?", "a": "Guillermo A. Brazález é o locutor profissional que dá voz em espanhol aos anúncios da Trivago em Espanha."},
        ],
    },
    "sv": {
        "title": "Spanska Rösten i Trivago — Guillermo A. Brazález",
        "meta_title": "Spanska Rösten i Trivago | Guillermo A. Brazález",
        "meta_desc": "Guillermo A. Brazález är den spanska rösten i Trivagos reklamfilmer i Spanien.",
        "h1": "Den Spanska Rösten i Trivago",
        "intro": """<p><strong>Guillermo A. Brazález</strong> är den spanska rösten bakom <strong>Trivagos</strong> reklamfilmer i Spanien, inklusive de senaste kampanjerna med <strong>Jürgen Klopp</strong>.</p>""",
        "section_videos": "Trivago-reklam på Spanska",
        "section_about": "Om Samarbetet med Trivago",
        "about_text": """<p>Trivago förlitar sig på Guillermo A. Brazález röst för att kommunicera sitt budskap till den spanska publiken.</p>""",
        "cta_text": "Söker du en professionell röst för ditt varumärke?",
        "faq": [
            {"q": "Vem är den spanska rösten i Trivago?", "a": "Guillermo A. Brazález är den professionella spanska röstskådespelaren bakom Trivagos TV-reklam i Spanien."},
        ],
    },
    "no": {
        "title": "Spansk Stemme i Trivago — Guillermo A. Brazález",
        "meta_title": "Spansk Stemme i Trivago | Guillermo A. Brazález",
        "meta_desc": "Guillermo A. Brazález er den spanske stemmen i Trivagos reklamefilmer i Spania.",
        "h1": "Den Spanske Stemmen i Trivago",
        "intro": """<p><strong>Guillermo A. Brazález</strong> er den spanske stemmen bak <strong>Trivagos</strong> reklamefilmer i Spania, inkludert de nyeste kampanjene med <strong>Jürgen Klopp</strong>.</p>""",
        "section_videos": "Trivago-reklame på Spansk",
        "section_about": "Om Samarbeidet med Trivago",
        "about_text": """<p>Trivago stoler på Guillermo A. Brazález stemme for å kommunisere sitt budskap til det spanske publikummet.</p>""",
        "cta_text": "Leter du etter en profesjonell stemme for ditt merke?",
        "faq": [
            {"q": "Hvem er den spanske stemmen i Trivago?", "a": "Guillermo A. Brazález er den profesjonelle spanske stemmeskuespilleren bak Trivagos TV-reklame i Spania."},
        ],
    },
    "da": {
        "title": "Spansk Stemme i Trivago — Guillermo A. Brazález",
        "meta_title": "Spansk Stemme i Trivago | Guillermo A. Brazález",
        "meta_desc": "Guillermo A. Brazález er den spanske stemme i Trivagos reklamefilm i Spanien.",
        "h1": "Den Spanske Stemme i Trivago",
        "intro": """<p><strong>Guillermo A. Brazález</strong> er den spanske stemme bag <strong>Trivagos</strong> reklamefilm i Spanien, inklusive de seneste kampagner med <strong>Jürgen Klopp</strong>.</p>""",
        "section_videos": "Trivago-reklame på Spansk",
        "section_about": "Om Samarbejdet med Trivago",
        "about_text": """<p>Trivago stoler på Guillermo A. Brazález stemme til at kommunikere sit budskab til det spanske publikum.</p>""",
        "cta_text": "Leder du efter en professionel stemme til dit brand?",
        "faq": [
            {"q": "Hvem er den spanske stemme i Trivago?", "a": "Guillermo A. Brazález er den professionelle spanske stemmeskuespiller bag Trivagos TV-reklame i Spanien."},
        ],
    },
    "nl": {
        "title": "Spaanse Stem van Trivago — Guillermo A. Brazález",
        "meta_title": "Spaanse Stem van Trivago | Guillermo A. Brazález",
        "meta_desc": "Guillermo A. Brazález is de Spaanse stem van de Trivago-reclames in Spanje.",
        "h1": "De Spaanse Stem van Trivago",
        "intro": """<p><strong>Guillermo A. Brazález</strong> is de Spaanse stem achter de <strong>Trivago</strong>-reclames in Spanje, inclusief de nieuwste campagnes met <strong>Jürgen Klopp</strong>.</p>""",
        "section_videos": "Trivago-reclames in het Spaans",
        "section_about": "Over de Samenwerking met Trivago",
        "about_text": """<p>Trivago vertrouwt op de stem van Guillermo A. Brazález om zijn boodschap over te brengen aan het Spaanse publiek.</p>""",
        "cta_text": "Op zoek naar een professionele stem voor uw merk?",
        "faq": [
            {"q": "Wie is de Spaanse stem van Trivago?", "a": "Guillermo A. Brazález is de professionele Spaanse stemacteur achter de Trivago-reclames in Spanje."},
        ],
    },
    "el": {
        "title": "Ισπανική Φωνή της Trivago — Guillermo A. Brazález",
        "meta_title": "Ισπανική Φωνή της Trivago | Guillermo A. Brazález",
        "meta_desc": "Ο Guillermo A. Brazález είναι η ισπανική φωνή των διαφημίσεων της Trivago στην Ισπανία.",
        "h1": "Η Ισπανική Φωνή της Trivago",
        "intro": """<p>Ο <strong>Guillermo A. Brazález</strong> είναι η ισπανική φωνή πίσω από τις τηλεοπτικές διαφημίσεις της <strong>Trivago</strong> στην Ισπανία, συμπεριλαμβανομένων των πιο πρόσφατων καμπανιών με τον <strong>Jürgen Klopp</strong>.</p>""",
        "section_videos": "Διαφημίσεις Trivago στα Ισπανικά",
        "section_about": "Σχετικά με τη Συνεργασία με την Trivago",
        "about_text": """<p>Η Trivago εμπιστεύεται τη φωνή του Guillermo A. Brazález για να μεταδώσει το μήνυμά της στο ισπανικό κοινό.</p>""",
        "cta_text": "Ψάχνετε επαγγελματική φωνή για το brand σας;",
        "faq": [
            {"q": "Ποιος είναι η ισπανική φωνή της Trivago;", "a": "Ο Guillermo A. Brazález είναι ο επαγγελματίας εκφωνητής πίσω από τις διαφημίσεις της Trivago στην Ισπανία."},
        ],
    },
    "zh": {
        "title": "Trivago西班牙语配音 — Guillermo A. Brazález",
        "meta_title": "Trivago西班牙语配音 | Guillermo A. Brazález",
        "meta_desc": "Guillermo A. Brazález是Trivago在西班牙电视广告的西班牙语配音演员。",
        "h1": "Trivago的西班牙语之声",
        "intro": """<p><strong>Guillermo A. Brazález</strong>是<strong>Trivago</strong>在西班牙电视广告中的西班牙语配音演员，包括与<strong>Jürgen Klopp</strong>合作的最新广告活动。</p>""",
        "section_videos": "Trivago西班牙语广告",
        "section_about": "关于与Trivago的合作",
        "about_text": """<p>Trivago信赖Guillermo A. Brazález的声音向西班牙观众传递品牌信息。</p>""",
        "cta_text": "为您的品牌寻找专业配音？",
        "faq": [
            {"q": "谁是Trivago的西班牙语配音演员？", "a": "Guillermo A. Brazález是为Trivago在西班牙的电视广告配音的专业西班牙语配音演员。"},
        ],
    },
    "ru": {
        "title": "Испанский Голос Trivago — Guillermo A. Brazález",
        "meta_title": "Испанский Голос Trivago | Guillermo A. Brazález",
        "meta_desc": "Guillermo A. Brazález — испанский голос рекламных роликов Trivago в Испании.",
        "h1": "Испанский Голос Trivago",
        "intro": """<p><strong>Guillermo A. Brazález</strong> — это испанский голос телевизионных рекламных роликов <strong>Trivago</strong> в Испании, включая последние кампании с <strong>Юргеном Клоппом</strong>.</p>""",
        "section_videos": "Реклама Trivago на Испанском",
        "section_about": "О Сотрудничестве с Trivago",
        "about_text": """<p>Trivago доверяет голосу Guillermo A. Brazález для передачи своего послания испанской аудитории.</p>""",
        "cta_text": "Ищете профессиональный голос для вашего бренда?",
        "faq": [
            {"q": "Кто озвучивает рекламу Trivago на испанском?", "a": "Guillermo A. Brazález — профессиональный испанский диктор, озвучивающий рекламные ролики Trivago в Испании."},
        ],
    },
}

SOUNDCLOUD_EMBED = '<iframe width="100%" height="450" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?visual=true&url=https%3A%2F%2Fapi.soundcloud.com%2Fusers%2F356830688&show_artwork=true&maxwidth=800&maxheight=800" loading="lazy"></iframe>'

# ─── FAQ Content ─────────────────────────────────────────────────────────────

FAQ_CONTENT = {
    "es": {
        "homepage_faq": [
            {"q": "¿Qué tipo de voz en español ofrece Guillermo?", "a": "Guillermo A. Brazález ofrece locución profesional en español castellano de España, con una voz cálida, versátil y autoritativa perfeccionada durante más de 20 años de experiencia en la industria."},
            {"q": "¿Cuáles son los servicios de locución disponibles?", "a": "Los servicios incluyen locución para spots publicitarios de televisión, narración de documentales, cuñas de radio, vídeo corporativo, audiolibros y composición musical original."},
            {"q": "¿Guillermo puede grabar sesiones en directo de forma remota?", "a": "Sí, Guillermo dispone de un estudio profesional en España equipado con Source-Connect e ISDN, lo que permite sesiones de grabación dirigidas en tiempo real desde cualquier parte del mundo."},
            {"q": "¿Cuánto tarda en entregar una grabación?", "a": "Los tiempos de entrega varían según el proyecto: las grabaciones cortas pueden entregarse en 24 horas, mientras que proyectos más extensos como audiolibros requieren una planificación más detallada."},
        ],
        "voice_actor_faq": [
            {"q": "¿Qué experiencia tiene Guillermo como locutor español?", "a": "Con más de 20 años de experiencia, Guillermo ha trabajado para marcas internacionales como Netflix, Discovery Channel, National Geographic, BMW, Samsung y BBVA, entre muchas otras."},
            {"q": "¿Qué diferencia al español castellano de otras variantes?", "a": "El español castellano de España se distingue por su pronunciación clara, entonación neutra y prestigio en producciones audiovisuales internacionales, siendo la variante preferida por muchas marcas globales."},
            {"q": "¿Cómo contratar los servicios de locución?", "a": "Puedes contactar directamente a través de WhatsApp (+34 606 350 350), email (info@guillermobrazalez.es) o mediante el formulario de contacto de la web."},
        ],
        "spots_faq": [
            {"q": "¿Qué marcas han contratado a Guillermo para spots?", "a": "Entre sus clientes se encuentran BMW, Samsung, BBVA, Movistar, y muchas otras marcas internacionales que han confiado en su voz castellana para campañas publicitarias en España y Latinoamérica."},
            {"q": "¿Se pueden ver demos de spots publicitarios?", "a": "Sí, en esta página encontrarás una selección de demos en vídeo de spots publicitarios realizados por Guillermo, mostrando diferentes registros y estilos."},
        ],
        "documentaries_faq": [
            {"q": "¿Para qué cadenas ha narrado documentales?", "a": "Guillermo ha narrado documentales para Netflix, Discovery Channel, National Geographic y TVE, entre otras cadenas internacionales."},
            {"q": "¿Qué tipo de documentales narra?", "a": "Narra documentales de naturaleza, historia, ciencia, cultura y viajes, adaptando su tono y ritmo a las necesidades específicas de cada producción."},
        ],
    },
    "en": {
        "homepage_faq": [
            {"q": "What type of Spanish voice does Guillermo offer?", "a": "Guillermo A. Brazález offers professional Castilian Spanish voice-over from Spain, with a warm, versatile, and authoritative voice honed over more than 20 years of industry experience."},
            {"q": "What voice-over services are available?", "a": "Services include voice-over for TV commercials, documentary narration, radio spots, corporate video, audiobooks, and original music composition."},
            {"q": "Can Guillermo record live-directed remote sessions?", "a": "Yes, Guillermo has a professional studio in Spain equipped with Source-Connect and ISDN, allowing real-time directed recording sessions from anywhere in the world."},
            {"q": "How long does delivery take?", "a": "Delivery times vary by project: short recordings can be delivered within 24 hours, while larger projects like audiobooks require more detailed planning."},
        ],
        "voice_actor_faq": [
            {"q": "What experience does Guillermo have as a Spanish voice artist?", "a": "With over 20 years of experience, Guillermo has worked for international brands including Netflix, Discovery Channel, National Geographic, BMW, Samsung, and BBVA, among many others."},
            {"q": "What sets Castilian Spanish apart from other variants?", "a": "Castilian Spanish from Spain is distinguished by its clear pronunciation, neutral intonation, and prestige in international audiovisual productions, making it the preferred variant for many global brands."},
            {"q": "How can I hire Guillermo\'s voice-over services?", "a": "You can contact him directly via WhatsApp (+34 606 350 350), email (info@guillermobrazalez.es), or through the website\'s contact form."},
        ],
        "spots_faq": [
            {"q": "Which brands has Guillermo voiced commercials for?", "a": "His clients include BMW, Samsung, BBVA, Movistar, and many other international brands that have trusted his Castilian voice for advertising campaigns in Spain and Latin America."},
            {"q": "Can I watch commercial demo reels?", "a": "Yes, on this page you will find a selection of video demos of commercials voiced by Guillermo, showcasing different registers and styles."},
        ],
        "documentaries_faq": [
            {"q": "Which networks has Guillermo narrated documentaries for?", "a": "Guillermo has narrated documentaries for Netflix, Discovery Channel, National Geographic, and TVE, among other international networks."},
            {"q": "What types of documentaries does he narrate?", "a": "He narrates documentaries on nature, history, science, culture, and travel, adapting his tone and rhythm to the specific needs of each production."},
        ],
    },
    "fr": {
        "homepage_faq": [
            {"q": "Quel type de voix espagnole propose Guillermo ?", "a": "Guillermo A. Brazález propose une voix-off professionnelle en espagnol castillan d\'Espagne, avec une voix chaude, polyvalente et autoritaire perfectionnée pendant plus de 20 ans d\'expérience."},
            {"q": "Quels services de voix-off sont disponibles ?", "a": "Les services incluent la voix-off pour spots télévisés, narration de documentaires, spots radio, vidéo d\'entreprise, livres audio et composition musicale originale."},
            {"q": "Guillermo peut-il enregistrer des sessions dirigées à distance ?", "a": "Oui, Guillermo dispose d\'un studio professionnel en Espagne équipé de Source-Connect et ISDN, permettant des sessions d\'enregistrement dirigées en temps réel depuis n\'importe où dans le monde."},
        ],
        "voice_actor_faq": [
            {"q": "Quelle expérience a Guillermo en tant que comédien vocal espagnol ?", "a": "Avec plus de 20 ans d\'expérience, Guillermo a travaillé pour des marques internationales telles que Netflix, Discovery Channel, National Geographic, BMW, Samsung et BBVA."},
            {"q": "Comment engager les services de voix-off de Guillermo ?", "a": "Vous pouvez le contacter directement par WhatsApp (+34 606 350 350), email (info@guillermobrazalez.es) ou via le formulaire de contact du site."},
        ],
        "spots_faq": [
            {"q": "Peut-on voir des démos de spots publicitaires ?", "a": "Oui, sur cette page vous trouverez une sélection de démos vidéo de spots publicitaires réalisés par Guillermo."},
        ],
        "documentaries_faq": [
            {"q": "Pour quelles chaînes Guillermo a-t-il narré des documentaires ?", "a": "Guillermo a narré des documentaires pour Netflix, Discovery Channel, National Geographic et TVE, entre autres chaînes internationales."},
        ],
    },
    "de": {
        "homepage_faq": [
            {"q": "Welche Art von spanischer Stimme bietet Guillermo an?", "a": "Guillermo A. Brazález bietet professionelles kastilisches Spanisch-Voice-over aus Spanien mit einer warmen, vielseitigen und autoritativen Stimme, die über mehr als 20 Jahre Erfahrung verfeinert wurde."},
            {"q": "Welche Voice-over-Dienstleistungen sind verfügbar?", "a": "Die Dienstleistungen umfassen Voice-over für TV-Werbespots, Dokumentarfilm-Narration, Radio-Spots, Unternehmensvideos, Hörbücher und Original-Musikkomposition."},
            {"q": "Kann Guillermo ferngesteuerte Live-Sessions aufnehmen?", "a": "Ja, Guillermo verfügt über ein professionelles Studio in Spanien mit Source-Connect und ISDN, was Echtzeit-Aufnahmesessions von überall auf der Welt ermöglicht."},
        ],
        "voice_actor_faq": [
            {"q": "Welche Erfahrung hat Guillermo als spanischer Sprecher?", "a": "Mit über 20 Jahren Erfahrung hat Guillermo für internationale Marken wie Netflix, Discovery Channel, National Geographic, BMW, Samsung und BBVA gearbeitet."},
            {"q": "Wie kann man Guillermos Sprecherdienstleistungen buchen?", "a": "Sie können ihn direkt per WhatsApp (+34 606 350 350), E-Mail (info@guillermobrazalez.es) oder über das Kontaktformular der Website kontaktieren."},
        ],
        "spots_faq": [
            {"q": "Kann man Demos von Werbespots ansehen?", "a": "Ja, auf dieser Seite finden Sie eine Auswahl an Video-Demos von Werbespots, die Guillermo gesprochen hat."},
        ],
        "documentaries_faq": [
            {"q": "Für welche Sender hat Guillermo Dokumentationen gesprochen?", "a": "Guillermo hat Dokumentationen für Netflix, Discovery Channel, National Geographic und TVE gesprochen."},
        ],
    },
    "it": {
        "homepage_faq": [
            {"q": "Che tipo di voce spagnola offre Guillermo?", "a": "Guillermo A. Brazález offre doppiaggio professionale in spagnolo castigliano dalla Spagna, con una voce calda, versatile e autorevole perfezionata in oltre 20 anni di esperienza."},
            {"q": "Quali servizi di doppiaggio sono disponibili?", "a": "I servizi includono doppiaggio per spot televisivi, narrazione di documentari, spot radiofonici, video aziendali, audiolibri e composizione musicale originale."},
            {"q": "Guillermo può registrare sessioni remote dal vivo?", "a": "Sì, Guillermo dispone di uno studio professionale in Spagna attrezzato con Source-Connect e ISDN per sessioni di registrazione dirette in tempo reale."},
        ],
        "voice_actor_faq": [
            {"q": "Che esperienza ha Guillermo come doppiatore spagnolo?", "a": "Con oltre 20 anni di esperienza, Guillermo ha lavorato per marchi internazionali come Netflix, Discovery Channel, National Geographic, BMW, Samsung e BBVA."},
            {"q": "Come si possono prenotare i servizi di doppiaggio?", "a": "Puoi contattarlo direttamente tramite WhatsApp (+34 606 350 350), email (info@guillermobrazalez.es) o il modulo di contatto del sito."},
        ],
        "spots_faq": [
            {"q": "Si possono vedere demo di spot pubblicitari?", "a": "Sì, in questa pagina troverai una selezione di demo video di spot pubblicitari realizzati da Guillermo."},
        ],
        "documentaries_faq": [
            {"q": "Per quali reti Guillermo ha narrato documentari?", "a": "Guillermo ha narrato documentari per Netflix, Discovery Channel, National Geographic e TVE, tra le altre reti internazionali."},
        ],
    },
    "pt": {
        "homepage_faq": [
            {"q": "Que tipo de voz espanhola oferece Guillermo?", "a": "Guillermo A. Brazález oferece locução profissional em espanhol castelhano de Espanha, com uma voz quente, versátil e autoritativa aperfeiçoada durante mais de 20 anos de experiência."},
            {"q": "Que serviços de locução estão disponíveis?", "a": "Os serviços incluem locução para spots de televisão, narração de documentários, spots de rádio, vídeo corporativo, audiolivros e composição musical original."},
            {"q": "Guillermo pode gravar sessões remotas ao vivo?", "a": "Sim, Guillermo dispõe de um estúdio profissional em Espanha equipado com Source-Connect e ISDN para sessões de gravação dirigidas em tempo real."},
        ],
        "voice_actor_faq": [
            {"q": "Que experiência tem Guillermo como locutor espanhol?", "a": "Com mais de 20 anos de experiência, Guillermo trabalhou para marcas internacionais como Netflix, Discovery Channel, National Geographic, BMW, Samsung e BBVA."},
            {"q": "Como contratar os serviços de locução?", "a": "Pode contactá-lo diretamente via WhatsApp (+34 606 350 350), email (info@guillermobrazalez.es) ou formulário de contacto do site."},
        ],
        "spots_faq": [
            {"q": "É possível ver demos de spots publicitários?", "a": "Sim, nesta página encontrará uma seleção de demos em vídeo de spots publicitários realizados por Guillermo."},
        ],
        "documentaries_faq": [
            {"q": "Para que canais Guillermo narrou documentários?", "a": "Guillermo narrou documentários para Netflix, Discovery Channel, National Geographic e TVE, entre outros canais internacionais."},
        ],
    },
    "sv": {
        "homepage_faq": [
            {"q": "Vilken typ av spansk röst erbjuder Guillermo?", "a": "Guillermo A. Brazález erbjuder professionell kastiliansk spansk voice-over från Spanien, med en varm, mångsidig och auktoritativ röst förfinad under mer än 20 års erfarenhet."},
            {"q": "Vilka voice-over-tjänster finns tillgängliga?", "a": "Tjänsterna inkluderar voice-over för TV-reklam, dokumentärberättande, radiospots, företagsvideo, ljudböcker och original musikkomposition."},
        ],
        "voice_actor_faq": [
            {"q": "Vilken erfarenhet har Guillermo som spansk röstskådespelare?", "a": "Med över 20 års erfarenhet har Guillermo arbetat för internationella varumärken som Netflix, Discovery Channel, National Geographic, BMW, Samsung och BBVA."},
        ],
        "spots_faq": [{"q": "Kan man se demos av reklamfilmer?", "a": "Ja, på denna sida hittar du ett urval av videodemos av reklamfilmer inspelade av Guillermo."}],
        "documentaries_faq": [{"q": "För vilka kanaler har Guillermo berättat dokumentärer?", "a": "Guillermo har berättat dokumentärer för Netflix, Discovery Channel, National Geographic och TVE."}],
    },
    "no": {
        "homepage_faq": [
            {"q": "Hvilken type spansk stemme tilbyr Guillermo?", "a": "Guillermo A. Brazález tilbyr profesjonell kastiljansk spansk voice-over fra Spania, med en varm, allsidig og autoritativ stemme foredlet gjennom mer enn 20 års erfaring."},
            {"q": "Hvilke voice-over-tjenester er tilgjengelige?", "a": "Tjenestene inkluderer voice-over for TV-reklame, dokumentarfortelling, radiospots, bedriftsvideo, lydbøker og original musikkkomposisjon."},
        ],
        "voice_actor_faq": [
            {"q": "Hvilken erfaring har Guillermo som spansk stemmeskuespiller?", "a": "Med over 20 års erfaring har Guillermo jobbet for internasjonale merker som Netflix, Discovery Channel, National Geographic, BMW, Samsung og BBVA."},
        ],
        "spots_faq": [{"q": "Kan man se demoer av reklamefilmer?", "a": "Ja, på denne siden finner du et utvalg av videodemoer av reklamefilmer spilt inn av Guillermo."}],
        "documentaries_faq": [{"q": "For hvilke kanaler har Guillermo fortalt dokumentarer?", "a": "Guillermo har fortalt dokumentarer for Netflix, Discovery Channel, National Geographic og TVE."}],
    },
    "da": {
        "homepage_faq": [
            {"q": "Hvilken type spansk stemme tilbyder Guillermo?", "a": "Guillermo A. Brazález tilbyder professionel kastiliansk spansk voice-over fra Spanien, med en varm, alsidig og autoritativ stemme forfinet gennem mere end 20 års erfaring."},
            {"q": "Hvilke voice-over-tjenester er tilgængelige?", "a": "Tjenesterne omfatter voice-over til TV-reklamer, dokumentarfortælling, radiospots, virksomhedsvideo, lydbøger og original musikkomposition."},
        ],
        "voice_actor_faq": [
            {"q": "Hvilken erfaring har Guillermo som spansk stemmeskuespiller?", "a": "Med over 20 års erfaring har Guillermo arbejdet for internationale mærker som Netflix, Discovery Channel, National Geographic, BMW, Samsung og BBVA."},
        ],
        "spots_faq": [{"q": "Kan man se demoer af reklamefilm?", "a": "Ja, på denne side finder du et udvalg af videodemoer af reklamefilm indspillet af Guillermo."}],
        "documentaries_faq": [{"q": "For hvilke kanaler har Guillermo fortalt dokumentarer?", "a": "Guillermo har fortalt dokumentarer for Netflix, Discovery Channel, National Geographic og TVE."}],
    },
    "nl": {
        "homepage_faq": [
            {"q": "Welk type Spaanse stem biedt Guillermo aan?", "a": "Guillermo A. Brazález biedt professionele Castiliaans-Spaanse voice-over uit Spanje, met een warme, veelzijdige en gezaghebbende stem, verfijnd gedurende meer dan 20 jaar ervaring."},
            {"q": "Welke voice-over diensten zijn beschikbaar?", "a": "De diensten omvatten voice-over voor TV-commercials, documentaire-vertelling, radiospots, bedrijfsvideo, luisterboeken en originele muziekcompositie."},
        ],
        "voice_actor_faq": [
            {"q": "Welke ervaring heeft Guillermo als Spaanse stemacteur?", "a": "Met meer dan 20 jaar ervaring heeft Guillermo gewerkt voor internationale merken zoals Netflix, Discovery Channel, National Geographic, BMW, Samsung en BBVA."},
        ],
        "spots_faq": [{"q": "Kan men demo\'s van reclamespots bekijken?", "a": "Ja, op deze pagina vindt u een selectie van videodemo\'s van reclamespots ingesproken door Guillermo."}],
        "documentaries_faq": [{"q": "Voor welke zenders heeft Guillermo documentaires verteld?", "a": "Guillermo heeft documentaires verteld voor Netflix, Discovery Channel, National Geographic en TVE."}],
    },
    "el": {
        "homepage_faq": [
            {"q": "Τι τύπο ισπανικής φωνής προσφέρει ο Guillermo;", "a": "Ο Guillermo A. Brazález προσφέρει επαγγελματική εκφώνηση σε καστιλιάνικα ισπανικά από την Ισπανία, με μια ζεστή, ευέλικτη και αυθεντική φωνή."},
            {"q": "Ποιες υπηρεσίες εκφώνησης είναι διαθέσιμες;", "a": "Οι υπηρεσίες περιλαμβάνουν εκφώνηση για τηλεοπτικές διαφημίσεις, ντοκιμαντέρ, ραδιοφωνικά σποτ, εταιρικά βίντεο, ηχητικά βιβλία και πρωτότυπη μουσική σύνθεση."},
        ],
        "voice_actor_faq": [
            {"q": "Τι εμπειρία έχει ο Guillermo ως Ισπανός εκφωνητής;", "a": "Με πάνω από 20 χρόνια εμπειρίας, ο Guillermo έχει εργαστεί για διεθνή brands όπως Netflix, Discovery Channel, National Geographic, BMW, Samsung και BBVA."},
        ],
        "spots_faq": [{"q": "Μπορεί κανείς να δει demos διαφημιστικών σποτ;", "a": "Ναι, σε αυτή τη σελίδα θα βρείτε μια επιλογή από video demos διαφημιστικών σποτ."}],
        "documentaries_faq": [{"q": "Για ποια κανάλια έχει αφηγηθεί ντοκιμαντέρ;", "a": "Ο Guillermo έχει αφηγηθεί ντοκιμαντέρ για Netflix, Discovery Channel, National Geographic και TVE."}],
    },
    "zh": {
        "homepage_faq": [
            {"q": "Guillermo提供什么类型的西班牙语配音？", "a": "Guillermo A. Brazález 提供来自西班牙的专业卡斯蒂利亚西班牙语配音，拥有温暖、多才多艺且权威的声音，经过20多年的行业经验磨练。"},
            {"q": "有哪些配音服务？", "a": "服务包括电视广告配音、纪录片旁白、广播广告、企业视频、有声书和原创音乐作曲。"},
        ],
        "voice_actor_faq": [
            {"q": "Guillermo作为西班牙语配音演员有什么经验？", "a": "凭借20多年的经验，Guillermo曾为Netflix、Discovery Channel、National Geographic、BMW、Samsung和BBVA等国际品牌工作。"},
        ],
        "spots_faq": [{"q": "可以观看广告配音演示吗？", "a": "是的，在此页面您可以找到Guillermo录制的广告配音视频演示选集。"}],
        "documentaries_faq": [{"q": "Guillermo为哪些频道配过纪录片旁白？", "a": "Guillermo曾为Netflix、Discovery Channel、National Geographic和TVE等国际频道配过纪录片旁白。"}],
    },
    "ru": {
        "homepage_faq": [
            {"q": "Какой тип испанского голоса предлагает Гильермо?", "a": "Гильермо А. Бразалез предлагает профессиональную озвучку на кастильском испанском из Испании, с тёплым, универсальным и авторитетным голосом, отточенным за более чем 20 лет опыта."},
            {"q": "Какие услуги озвучки доступны?", "a": "Услуги включают озвучку для телевизионных рекламных роликов, документальных фильмов, радиороликов, корпоративного видео, аудиокниг и оригинальную музыкальную композицию."},
        ],
        "voice_actor_faq": [
            {"q": "Какой опыт у Гильермо как испанского диктора?", "a": "С более чем 20-летним опытом Гильермо работал для международных брендов, таких как Netflix, Discovery Channel, National Geographic, BMW, Samsung и BBVA."},
        ],
        "spots_faq": [{"q": "Можно посмотреть демо рекламных роликов?", "a": "Да, на этой странице вы найдёте подборку видеодемо рекламных роликов, озвученных Гильермо."}],
        "documentaries_faq": [{"q": "Для каких каналов Гильермо озвучивал документальные фильмы?", "a": "Гильермо озвучивал документальные фильмы для Netflix, Discovery Channel, National Geographic и TVE."}],
    },
}



# ─── Content Strings ──────────────────────────────────────────────────────────

CONTENT = {
    "es": {
        "site_title": "Guillermo A. Brazález — Locutor Profesional Español",
        "hero_tagline": "La Voz Mueve el Mundo",
        "hero_subtitle": "Locutor profesional español · Voz castellana con más de 20 años de experiencia",
        "hero_badge": "Voz en español de los spots de Trivago",
        "homepage_intro": """
            <p>Guillermo A. Brazález es un locutor profesional español con sede en España, especializado en español castellano de primera calidad. Con más de dos décadas de experiencia en la industria de la voz, Guillermo ha prestado su voz castellana a cientos de proyectos internacionales para las marcas más reconocidas del mundo.</p>
            <p>Su voz en español destaca por su calidez, autoridad y versatilidad. Desde spots publicitarios para televisión hasta documentales de naturaleza, pasando por vídeo corporativo, locución de radio y audiolibros, su voz española conecta con audiencias de habla hispana en todo el mundo. Ha colaborado con productoras de España y Latinoamérica, ofreciendo siempre una pronunciación castellana impecable.</p>
            <p>Como locutor español nativo de España, Guillermo trabaja desde su propio estudio profesional equipado con tecnología de última generación, lo que le permite ofrecer grabaciones en español de la más alta calidad con tiempos de entrega rápidos. Su español castellano es la elección preferida de marcas internacionales como Netflix, Discovery Channel, National Geographic y muchas otras que buscan una voz española auténtica y profesional.</p>
            <p>Si buscas una voz profesional en español para tu próximo proyecto, Guillermo ofrece sesiones remotas en directo, grabación en su estudio de España y una atención personalizada que garantiza resultados excepcionales en cada proyecto de locución en castellano.</p>
        """,
        "services_heading": "Servicios de Locución en Español",
        "services": {
            "spots": {
                "title": "Spots Publicitarios",
                "desc": "Locución profesional en español para campañas de televisión y publicidad digital.",
                "icon": "📺"
            },
            "documentaries": {
                "title": "Documentales",
                "desc": "Narración en español castellano para documentales de naturaleza, historia y ciencia.",
                "icon": "🎬"
            },
            "radio": {
                "title": "Radio",
                "desc": "Voz profesional en español para cuñas de radio, jingles y programas.",
                "icon": "📻"
            },
            "corporate": {
                "title": "Vídeo Corporativo",
                "desc": "Locución corporativa en español para presentaciones, formación y comunicación interna.",
                "icon": "🏢"
            },
            "audiobooks": {
                "title": "Audiolibros",
                "desc": "Narración de audiolibros en español castellano con dicción perfecta.",
                "icon": "📚"
            },
            "studio": {
                "title": "Estudio",
                "desc": "Estudio profesional de grabación en España con conexión Source-Connect y ISDN.",
                "icon": "🎙️"
            },
        },
        "composer_title": "Compositor",
        "composer_text": """
            <p>Además de su trabajo como locutor español, Guillermo A. Brazález es compositor de música original. Crea bandas sonoras y composiciones musicales para proyectos audiovisuales, complementando su trabajo de locución en español con música a medida que eleva la calidad de cualquier producción.</p>
            <p>Sus composiciones abarcan desde música ambiental para documentales hasta temas originales para spots publicitarios en español. La combinación de su talento como locutor español y compositor le convierte en un profesional único capaz de ofrecer soluciones integrales de audio en castellano.</p>
        """,
        "contact_title": "Contacto",
        "contact_text": "¿Necesitas una voz profesional en español? Contacta con Guillermo para hablar sobre tu proyecto de locución en castellano.",
        "nav": {
            "voice_actor": "Locutor",
            "composer": "Compositor",
            "contact": "Contacto",
        },
        "footer_text": "Locutor profesional español · Voz castellana desde España",
        "cta_contact": "Contactar",
        "cta_listen": "Escuchar Demo",
        "cta_whatsapp": "WhatsApp",
        # Service pages
        "voice_actor_page": {
            "title": "Locutor Profesional Español",
            "meta_desc": "Guillermo A. Brazález, locutor profesional español con voz castellana. Más de 20 años de experiencia en spots, documentales, radio y vídeo corporativo en español.",
            "content": """
                <p>Guillermo A. Brazález es uno de los locutores profesionales en español más reconocidos de España. Su voz castellana ha dado vida a cientos de producciones audiovisuales, desde grandes campañas publicitarias hasta documentales internacionales, siempre con la calidez y autoridad que caracterizan al mejor español de Castilla.</p>
                <p>Como locutor español con más de 20 años de experiencia, Guillermo domina todos los registros vocales: desde la narración pausada y envolvente de un documental hasta la energía y dinamismo de un spot publicitario. Su español castellano es sinónimo de profesionalidad, claridad y una dicción impecable que conecta con audiencias hispanohablantes en todo el mundo.</p>
                <p>Trabaja desde su propio estudio profesional de grabación en España, equipado con tecnología de última generación que incluye conexión Source-Connect para sesiones remotas en directo. Esto permite a clientes de cualquier parte del mundo dirigir sesiones de grabación en español en tiempo real, como si estuvieran en el estudio.</p>
                <p>Su cartera de clientes incluye marcas internacionales de primer nivel, cadenas de televisión, productoras de cine y agencias de publicidad que confían en su voz española para proyectos de la más alta exigencia. Cada proyecto de locución en castellano recibe la atención personalizada que garantiza resultados excepcionales.</p>
            """
        },
        "spots_page": {
            "title": "Spots Publicitarios en Español",
            "meta_desc": "Locutor español para spots de televisión y publicidad. Voz castellana profesional para campañas publicitarias de marcas internacionales.",
            "content": """
                <p>La locución de spots publicitarios en español es una de las especialidades de Guillermo A. Brazález. Su voz castellana ha sido la elegida por las principales marcas internacionales para sus campañas en español dirigidas al mercado de España y Latinoamérica.</p>
                <p>Un buen spot publicitario en español necesita una voz que transmita confianza, cercanía y profesionalidad. Guillermo ofrece exactamente eso: una voz española versátil que se adapta al tono de cada marca, desde spots institucionales con gravitas hasta publicidad dinámica y juvenil.</p>
                <p>Entre sus clientes de publicidad en español se encuentran marcas como BMW, Samsung, BBVA, Movistar y muchas otras que han confiado en su voz castellana para conectar con millones de espectadores hispanohablantes. Cada spot en español se graba en su estudio profesional de España con la calidad técnica que exigen las grandes producciones.</p>
            """
        },
        "documentaries_page": {
            "title": "Narración de Documentales en Español",
            "meta_desc": "Narrador español para documentales. Voz castellana profesional para documentales de naturaleza, historia, ciencia y cultura en español.",
            "content": """
                <p>La narración de documentales en español castellano es uno de los campos donde Guillermo A. Brazález destaca especialmente. Su voz española, cálida y envolvente, guía al espectador a través de historias fascinantes con la autoridad y sensibilidad que requiere el género documental.</p>
                <p>Ha prestado su voz en español a documentales para cadenas internacionales como Netflix, Discovery Channel, National Geographic y TVE, narrando contenidos sobre naturaleza, historia, ciencia y cultura. Su español castellano aporta una calidad narrativa excepcional que transporta al espectador al corazón de cada historia.</p>
                <p>La clave de una buena narración documental en español está en encontrar el ritmo perfecto, la emoción justa y la pronunciación castellana impecable. Con más de 20 años de experiencia como narrador español, Guillermo domina cada matiz de la voz para crear experiencias audiovisuales memorables en castellano.</p>
            """
        },
        "radio_page": {
            "title": "Locución de Radio en Español",
            "meta_desc": "Locutor español profesional para radio. Cuñas publicitarias, jingles y programación radiofónica en español castellano.",
            "content": """
                <p>La radio en español sigue siendo uno de los medios más poderosos para conectar con audiencias hispanohablantes. Guillermo A. Brazález aporta su voz castellana profesional a cuñas publicitarias, jingles, promos y programación radiofónica, siempre con la calidez y claridad que caracterizan al mejor español de España.</p>
                <p>Como locutor español con amplia experiencia en radio, Guillermo domina los tiempos, ritmos y registros específicos del medio radiofónico. Su español castellano se adapta con naturalidad a cualquier formato, desde la cuña publicitaria de 20 segundos hasta la narración extensa de un programa de radio en español.</p>
                <p>Trabaja con emisoras de radio y agencias de publicidad de toda España y Latinoamérica, ofreciendo grabaciones en español de alta calidad con tiempos de entrega que se ajustan a las necesidades urgentes del medio radiofónico. Su estudio profesional en España garantiza una calidad técnica impecable en cada producción de radio en castellano.</p>
            """
        },
        "corporate_page": {
            "title": "Vídeo Corporativo en Español",
            "meta_desc": "Locutor español para vídeo corporativo. Locución en castellano profesional para presentaciones, formación y comunicación empresarial.",
            "content": """
                <p>La locución de vídeo corporativo en español requiere una voz que transmita profesionalidad, cercanía y credibilidad. Guillermo A. Brazález ofrece su voz castellana para todo tipo de producciones corporativas: vídeos de presentación, material de formación, comunicación interna, e-learning y eventos empresariales.</p>
                <p>Las empresas multinacionales confían en su voz española para sus comunicaciones en castellano porque combina autoridad con accesibilidad. Su español de España es la elección perfecta para marcas que buscan una imagen profesional y moderna en el mercado hispanohablante.</p>
                <p>Cada proyecto de locución corporativa en español recibe una atención personalizada, desde la interpretación del guion hasta la entrega final. Guillermo trabaja desde su estudio de grabación en España y ofrece sesiones remotas en directo para que los clientes puedan dirigir la grabación en castellano en tiempo real.</p>
            """
        },
        "audiobooks_page": {
            "title": "Audiolibros en Español",
            "meta_desc": "Narrador español de audiolibros. Locución profesional en castellano para audiolibros de ficción y no ficción.",
            "content": """
                <p>La narración de audiolibros en español castellano es un arte que requiere versatilidad, constancia y una dicción perfecta. Guillermo A. Brazález es un narrador español con experiencia en la grabación de audiolibros de ficción y no ficción, aportando su voz castellana cálida y envolvente a cada página.</p>
                <p>Un buen audiolibro en español necesita un narrador que mantenga la atención del oyente durante horas, que dé vida a los personajes con matices vocales sutiles y que respete el ritmo narrativo del autor. Como narrador español profesional, Guillermo domina todas estas facetas para crear experiencias auditivas excepcionales en castellano.</p>
                <p>Trabaja con editoriales y plataformas de audiolibros que buscan una voz española de calidad para su catálogo en español. Su estudio profesional en España está acondicionado acústicamente para largas sesiones de grabación, garantizando la consistencia y calidad que requiere cada audiolibro en castellano.</p>
            """
        },
        "studio_page": {
            "title": "Estudio de Grabación en España",
            "meta_desc": "Estudio profesional de grabación de voz en España. Equipado con Source-Connect e ISDN para sesiones remotas de locución en español.",
            "content": """
                <p>El estudio de grabación de Guillermo A. Brazález está ubicado en España y cuenta con todo el equipamiento profesional necesario para producciones de locución en español de la más alta calidad. Diseñado específicamente para la grabación de voz, el estudio ofrece un entorno acústico óptimo para cada proyecto de locución en castellano.</p>
                <p>El estudio en España está equipado con micrófonos de gama alta, previos de calidad broadcast y tratamiento acústico profesional. Dispone de conexión Source-Connect y ISDN, lo que permite sesiones de grabación remotas en español en tiempo real con clientes de todo el mundo, como si estuvieran presentes en el estudio de España.</p>
                <p>La ubicación del estudio en España permite a Guillermo cubrir horarios de trabajo compatibles con Europa, América y Asia, ofreciendo una flexibilidad que las grandes producciones en español necesitan. Cada grabación en castellano se realiza con los estándares técnicos más exigentes de la industria.</p>
            """
        },
        "composer_page": {
            "title": "Compositor de Música — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, compositor español de música para audiovisuales. Bandas sonoras y composiciones originales desde España.",
            "content": """
                <p>Además de su reconocida carrera como locutor profesional español, Guillermo A. Brazález es compositor de música original para producciones audiovisuales. Su doble talento como voz española y compositor le permite ofrecer soluciones integrales de audio para proyectos que requieren tanto locución en español como música original.</p>
                <p>Sus composiciones musicales abarcan una amplia variedad de estilos, desde bandas sonoras cinematográficas hasta música ambiental para documentales, pasando por temas originales para spots publicitarios en español. Cada composición está diseñada para complementar y potenciar el mensaje de la producción audiovisual.</p>
                <p>Guillermo trabaja desde su estudio en España, donde combina la grabación de locución en castellano con la producción musical, ofreciendo un flujo de trabajo integrado que optimiza tiempos y costes. Su experiencia como locutor español le da una perspectiva única sobre cómo la música y la voz en español deben trabajar juntas para crear experiencias memorables.</p>
            """
        },
        "contact_page": {
            "title": "Contacto — Locutor Español Guillermo A. Brazález",
            "meta_desc": "Contacta con Guillermo A. Brazález, locutor profesional español. WhatsApp, email y teléfono para proyectos de locución en español castellano.",
            "content": """
                <p>¿Buscas un locutor profesional en español para tu próximo proyecto? Guillermo A. Brazález está disponible para grabaciones en castellano desde su estudio profesional en España. Tanto si necesitas una voz española para un spot publicitario, un documental, un vídeo corporativo o un audiolibro, Guillermo ofrece la calidad y profesionalidad que tu proyecto en español merece.</p>
                <p>Puedes contactar directamente por WhatsApp para una respuesta rápida, enviar un email con los detalles de tu proyecto de locución en español, o llamar por teléfono. Guillermo responde personalmente a cada consulta sobre locución en castellano y estará encantado de preparar una demo personalizada en español para tu proyecto.</p>
            """,
            "form_name": "Nombre",
            "form_email": "Email",
            "form_message": "Mensaje",
            "form_send": "Enviar Mensaje",
            "form_subject": "Asunto",
        }
    },
    "en": {
        "site_title": "Guillermo A. Brazález — Professional Spanish Voice-Over Artist",
        "hero_tagline": "The Voice Moves the World",
        "hero_subtitle": "Professional Spanish voice-over artist · Castilian Spanish voice with 20+ years of experience",
        "hero_badge": "The Spanish voice of Trivago commercials",
        "homepage_intro": """
            <p>Guillermo A. Brazález is a professional Spanish voice-over artist based in Spain, specializing in premium Castilian Spanish narration. With over two decades of experience in the voice-over industry, Guillermo has lent his authentic Spanish voice to hundreds of international projects for the world's most recognized brands.</p>
            <p>His Spanish voice stands out for its warmth, authority, and versatility. From television commercials to nature documentaries, corporate videos, radio spots, and audiobooks, his Castilian Spanish voice connects with Spanish-speaking audiences worldwide. He has collaborated with production companies across Spain and Latin America, always delivering impeccable Castilian Spanish pronunciation.</p>
            <p>As a native Spanish voice actor from Spain, Guillermo works from his own professional studio equipped with cutting-edge technology, allowing him to deliver the highest quality Spanish recordings with fast turnaround times. His Castilian Spanish voice is the preferred choice of international brands like Netflix, Discovery Channel, National Geographic, and many others seeking an authentic, professional Spanish voice.</p>
            <p>If you're looking for a professional Spanish voice for your next project, Guillermo offers live remote sessions, recording at his studio in Spain, and personalized attention that guarantees exceptional results in every Castilian Spanish voice-over project.</p>
        """,
        "services_heading": "Spanish Voice-Over Services",
        "services": {
            "spots": {
                "title": "TV Commercials",
                "desc": "Professional Spanish voice-over for television campaigns and digital advertising.",
                "icon": "📺"
            },
            "documentaries": {
                "title": "Documentaries",
                "desc": "Castilian Spanish narration for nature, history, and science documentaries.",
                "icon": "🎬"
            },
            "radio": {
                "title": "Radio",
                "desc": "Professional Spanish voice for radio spots, jingles, and programming.",
                "icon": "📻"
            },
            "corporate": {
                "title": "Corporate Video",
                "desc": "Spanish corporate voice-over for presentations, training, and internal communications.",
                "icon": "🏢"
            },
            "audiobooks": {
                "title": "Audiobooks",
                "desc": "Castilian Spanish audiobook narration with perfect diction.",
                "icon": "📚"
            },
            "studio": {
                "title": "Studio",
                "desc": "Professional recording studio in Spain with Source-Connect and ISDN.",
                "icon": "🎙️"
            },
        },
        "composer_title": "Composer",
        "composer_text": """
            <p>Beyond his work as a Spanish voice-over artist, Guillermo A. Brazález is a composer of original music. He creates soundtracks and musical compositions for audiovisual projects, complementing his Spanish voice-over work with bespoke music that elevates the quality of any production.</p>
            <p>His compositions range from ambient music for documentaries to original themes for Spanish-language commercials. The combination of his talent as a Spanish voice actor and composer makes him a unique professional capable of offering comprehensive audio solutions in Castilian Spanish.</p>
        """,
        "contact_title": "Contact",
        "contact_text": "Need a professional Spanish voice? Contact Guillermo to discuss your Castilian Spanish voice-over project.",
        "nav": {
            "voice_actor": "Voice Actor",
            "composer": "Composer",
            "contact": "Contact",
        },
        "footer_text": "Professional Spanish voice-over artist · Castilian Spanish voice from Spain",
        "cta_contact": "Get in Touch",
        "cta_listen": "Listen to Demo",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "Professional Spanish Voice Actor",
            "meta_desc": "Guillermo A. Brazález, professional Spanish voice actor with a Castilian Spanish voice. Over 20 years of experience in commercials, documentaries, radio, and corporate video.",
            "content": """
                <p>Guillermo A. Brazález is one of the most recognized professional Spanish voice actors in Spain. His Castilian Spanish voice has brought hundreds of audiovisual productions to life, from major advertising campaigns to international documentaries, always with the warmth and authority that characterize the finest Spanish voice from Castile.</p>
                <p>As a Spanish voice-over professional with over 20 years of experience, Guillermo masters every vocal register: from the measured, immersive narration of a documentary to the energy and dynamism of a television commercial. His Castilian Spanish voice is synonymous with professionalism, clarity, and impeccable diction that connects with Spanish-speaking audiences worldwide.</p>
                <p>He works from his own professional recording studio in Spain, equipped with state-of-the-art technology including Source-Connect for live remote sessions. This allows clients from anywhere in the world to direct Spanish voice recording sessions in real-time, as if they were present in the studio.</p>
                <p>His client portfolio includes top-tier international brands, television networks, film production companies, and advertising agencies that trust his Spanish voice for the most demanding projects. Every Castilian Spanish voice-over project receives the personalized attention that guarantees exceptional results.</p>
            """
        },
        "spots_page": {
            "title": "Spanish Voice-Over for TV Commercials",
            "meta_desc": "Professional Spanish voice actor for television commercials and advertising. Castilian Spanish voice for international brand campaigns.",
            "content": """
                <p>Voice-over for Spanish-language television commercials is one of Guillermo A. Brazález's specialties. His Castilian Spanish voice has been chosen by leading international brands for their Spanish-language campaigns targeting audiences in Spain and Latin America.</p>
                <p>A great Spanish TV commercial needs a voice that conveys trust, approachability, and professionalism. Guillermo delivers exactly that: a versatile Spanish voice that adapts to each brand's tone, from institutional spots with gravitas to dynamic, youthful advertising in Spanish.</p>
                <p>Among his Spanish advertising clients are brands such as BMW, Samsung, BBVA, Movistar, and many others who have trusted his Castilian Spanish voice to connect with millions of Spanish-speaking viewers. Every Spanish commercial is recorded in his professional studio in Spain with the technical quality that major productions demand.</p>
            """
        },
        "documentaries_page": {
            "title": "Spanish Documentary Narration",
            "meta_desc": "Professional Spanish narrator for documentaries. Castilian Spanish voice for nature, history, science, and cultural documentaries.",
            "content": """
                <p>Documentary narration in Castilian Spanish is one of the fields where Guillermo A. Brazález particularly excels. His warm, immersive Spanish voice guides viewers through fascinating stories with the authority and sensitivity that the documentary genre demands.</p>
                <p>He has lent his Spanish voice to documentaries for international networks including Netflix, Discovery Channel, National Geographic, and TVE, narrating content about nature, history, science, and culture. His Castilian Spanish brings exceptional narrative quality that transports viewers to the heart of every story.</p>
                <p>The key to great documentary narration in Spanish lies in finding the perfect rhythm, the right emotion, and impeccable Castilian Spanish pronunciation. With over 20 years of experience as a Spanish narrator, Guillermo masters every nuance of the voice to create memorable audiovisual experiences in Castilian Spanish.</p>
            """
        },
        "radio_page": {
            "title": "Spanish Radio Voice-Over",
            "meta_desc": "Professional Spanish voice actor for radio. Radio spots, jingles, and programming in Castilian Spanish.",
            "content": """
                <p>Spanish-language radio remains one of the most powerful media for connecting with Spanish-speaking audiences. Guillermo A. Brazález brings his professional Castilian Spanish voice to radio spots, jingles, promos, and programming, always with the warmth and clarity that characterize the best Spanish voice from Spain.</p>
                <p>As a Spanish voice professional with extensive radio experience, Guillermo masters the specific timing, rhythms, and registers of the medium. His Castilian Spanish adapts naturally to any format, from a 20-second Spanish radio spot to extended narration for a full radio program in Spanish.</p>
                <p>He works with radio stations and advertising agencies throughout Spain and Latin America, offering high-quality Spanish recordings with turnaround times that meet the urgent needs of radio broadcasting. His professional studio in Spain guarantees impeccable technical quality in every Castilian Spanish radio production.</p>
            """
        },
        "corporate_page": {
            "title": "Spanish Corporate Video Voice-Over",
            "meta_desc": "Spanish voice actor for corporate video. Professional Castilian Spanish voice-over for presentations, training, and business communications.",
            "content": """
                <p>Corporate video voice-over in Spanish requires a voice that conveys professionalism, approachability, and credibility. Guillermo A. Brazález offers his Castilian Spanish voice for all types of corporate productions: presentation videos, training materials, internal communications, e-learning, and corporate events.</p>
                <p>Multinational companies trust his Spanish voice for their Castilian Spanish communications because it combines authority with accessibility. His Spanish from Spain is the perfect choice for brands seeking a professional, modern image in the Spanish-speaking market.</p>
                <p>Every Spanish corporate voice-over project receives personalized attention, from script interpretation to final delivery. Guillermo works from his recording studio in Spain and offers live remote sessions so clients can direct the Castilian Spanish recording in real-time.</p>
            """
        },
        "audiobooks_page": {
            "title": "Spanish Audiobook Narration",
            "meta_desc": "Professional Spanish audiobook narrator. Castilian Spanish voice-over for fiction and non-fiction audiobooks.",
            "content": """
                <p>Audiobook narration in Castilian Spanish is an art that requires versatility, consistency, and perfect diction. Guillermo A. Brazález is a Spanish narrator with experience recording fiction and non-fiction audiobooks, bringing his warm, immersive Castilian Spanish voice to every page.</p>
                <p>A great Spanish audiobook needs a narrator who maintains the listener's attention for hours, who brings characters to life with subtle vocal nuances, and who respects the author's narrative rhythm. As a professional Spanish narrator, Guillermo masters all these facets to create exceptional listening experiences in Castilian Spanish.</p>
                <p>He works with publishers and audiobook platforms seeking a quality Spanish voice for their Castilian Spanish catalog. His professional studio in Spain is acoustically treated for long recording sessions, ensuring the consistency and quality that every Spanish audiobook demands.</p>
            """
        },
        "studio_page": {
            "title": "Professional Recording Studio in Spain",
            "meta_desc": "Professional voice recording studio in Spain. Equipped with Source-Connect and ISDN for remote Spanish voice-over sessions.",
            "content": """
                <p>Guillermo A. Brazález's recording studio is located in Spain and features all the professional equipment needed for the highest quality Spanish voice-over productions. Designed specifically for voice recording, the studio provides an optimal acoustic environment for every Castilian Spanish voice-over project.</p>
                <p>The studio in Spain is equipped with high-end microphones, broadcast-quality preamps, and professional acoustic treatment. It features Source-Connect and ISDN connectivity, enabling real-time remote Spanish recording sessions with clients worldwide, as if they were present in the Spain-based studio.</p>
                <p>The studio's location in Spain allows Guillermo to cover working hours compatible with Europe, the Americas, and Asia, offering the flexibility that major Spanish voice-over productions require. Every Castilian Spanish recording is produced to the most demanding technical standards in the industry.</p>
            """
        },
        "composer_page": {
            "title": "Music Composer — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, Spanish music composer for audiovisual productions. Original soundtracks and compositions from Spain.",
            "content": """
                <p>In addition to his acclaimed career as a professional Spanish voice-over artist, Guillermo A. Brazález is a composer of original music for audiovisual productions. His dual talent as a Spanish voice actor and composer allows him to offer comprehensive audio solutions for projects requiring both Spanish voice-over and original music.</p>
                <p>His musical compositions span a wide variety of styles, from cinematic soundtracks to ambient music for documentaries, including original themes for Spanish-language commercials. Each composition is designed to complement and enhance the message of the audiovisual production.</p>
                <p>Guillermo works from his studio in Spain, where he combines Castilian Spanish voice recording with music production, offering an integrated workflow that optimizes time and costs. His experience as a Spanish voice actor gives him a unique perspective on how music and the Spanish voice should work together to create memorable experiences.</p>
            """
        },
        "contact_page": {
            "title": "Contact — Spanish Voice Actor Guillermo A. Brazález",
            "meta_desc": "Contact Guillermo A. Brazález, professional Spanish voice-over artist. WhatsApp, email, and phone for Castilian Spanish voice-over projects.",
            "content": """
                <p>Looking for a professional Spanish voice for your next project? Guillermo A. Brazález is available for Castilian Spanish recordings from his professional studio in Spain. Whether you need a Spanish voice for a TV commercial, documentary, corporate video, or audiobook, Guillermo delivers the quality and professionalism your Spanish-language project deserves.</p>
                <p>You can contact him directly via WhatsApp for a quick response, send an email with details about your Spanish voice-over project, or call by phone. Guillermo personally responds to every inquiry about Castilian Spanish voice-over and will be happy to prepare a personalized Spanish demo for your project.</p>
            """,
            "form_name": "Name",
            "form_email": "Email",
            "form_message": "Message",
            "form_send": "Send Message",
            "form_subject": "Subject",
        }
    },
    "fr": {
        "site_title": "Guillermo A. Brazález — Comédien Vocal Espagnol Professionnel",
        "hero_tagline": "La Voix Fait Bouger le Monde",
        "hero_subtitle": "Comédien vocal espagnol professionnel · Voix espagnole castillane avec plus de 20 ans d'expérience",
        "hero_badge": "La voix espagnole des spots Trivago",
        "homepage_intro": """
            <p>Guillermo A. Brazález est un comédien vocal espagnol professionnel basé en Espagne, spécialisé dans la narration en espagnol castillan de première qualité. Avec plus de deux décennies d'expérience dans l'industrie du doublage, Guillermo a prêté sa voix espagnole authentique à des centaines de projets internationaux pour les marques les plus reconnues au monde.</p>
            <p>Sa voix espagnole se distingue par sa chaleur, son autorité et sa polyvalence. Des spots publicitaires télévisés aux documentaires sur la nature, en passant par les vidéos d'entreprise, les spots radio et les livres audio, sa voix en espagnol castillan connecte avec les audiences hispanophones du monde entier. Il a collaboré avec des sociétés de production en Espagne et en Amérique latine, offrant toujours une prononciation espagnole castillane impeccable.</p>
            <p>En tant que comédien vocal espagnol natif d'Espagne, Guillermo travaille depuis son propre studio professionnel équipé de la dernière technologie, ce qui lui permet de livrer des enregistrements en espagnol de la plus haute qualité dans des délais rapides. Sa voix espagnole castillane est le choix privilégié de marques internationales comme Netflix, Discovery Channel, National Geographic et bien d'autres qui recherchent une voix espagnole authentique et professionnelle.</p>
            <p>Si vous cherchez une voix professionnelle en espagnol pour votre prochain projet, Guillermo propose des sessions à distance en direct, l'enregistrement dans son studio en Espagne et une attention personnalisée qui garantit des résultats exceptionnels pour chaque projet de doublage en espagnol castillan.</p>
        """,
        "services_heading": "Services de Voix-Off en Espagnol",
        "services": {
            "spots": {"title": "Spots Publicitaires", "desc": "Voix-off espagnole professionnelle pour campagnes télévisées et publicité digitale.", "icon": "📺"},
            "documentaries": {"title": "Documentaires", "desc": "Narration en espagnol castillan pour documentaires nature, histoire et science.", "icon": "🎬"},
            "radio": {"title": "Radio", "desc": "Voix espagnole professionnelle pour spots radio, jingles et programmation.", "icon": "📻"},
            "corporate": {"title": "Vidéo Corporate", "desc": "Voix-off corporate en espagnol pour présentations, formation et communication interne.", "icon": "🏢"},
            "audiobooks": {"title": "Livres Audio", "desc": "Narration de livres audio en espagnol castillan avec une diction parfaite.", "icon": "📚"},
            "studio": {"title": "Studio", "desc": "Studio d'enregistrement professionnel en Espagne avec Source-Connect et ISDN.", "icon": "🎙️"},
        },
        "composer_title": "Compositeur",
        "composer_text": """
            <p>En plus de son travail de comédien vocal espagnol, Guillermo A. Brazález est compositeur de musique originale. Il crée des bandes sonores et des compositions musicales pour des projets audiovisuels, complétant son travail de voix-off en espagnol avec une musique sur mesure qui élève la qualité de toute production.</p>
            <p>Ses compositions vont de la musique d'ambiance pour documentaires aux thèmes originaux pour spots publicitaires en espagnol. La combinaison de son talent de comédien vocal espagnol et de compositeur en fait un professionnel unique capable d'offrir des solutions audio complètes en espagnol castillan.</p>
        """,
        "contact_title": "Contact",
        "contact_text": "Besoin d'une voix espagnole professionnelle ? Contactez Guillermo pour discuter de votre projet de voix-off en espagnol castillan.",
        "nav": {"voice_actor": "Comédien Vocal", "composer": "Compositeur", "contact": "Contact"},
        "footer_text": "Comédien vocal espagnol professionnel · Voix espagnole castillane depuis l'Espagne",
        "cta_contact": "Contacter",
        "cta_listen": "Écouter la Démo",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "Comédien Vocal Espagnol Professionnel",
            "meta_desc": "Guillermo A. Brazález, comédien vocal espagnol professionnel avec voix castillane. Plus de 20 ans d'expérience en spots, documentaires et vidéo corporate.",
            "content": """
                <p>Guillermo A. Brazález est l'un des comédiens vocaux espagnols les plus reconnus d'Espagne. Sa voix espagnole castillane a donné vie à des centaines de productions audiovisuelles, des grandes campagnes publicitaires aux documentaires internationaux, toujours avec la chaleur et l'autorité qui caractérisent la meilleure voix espagnole de Castille.</p>
                <p>En tant que professionnel de la voix espagnole avec plus de 20 ans d'expérience, Guillermo maîtrise tous les registres vocaux. Son espagnol castillan est synonyme de professionnalisme, de clarté et d'une diction impeccable qui connecte avec les audiences hispanophones du monde entier.</p>
                <p>Il travaille depuis son propre studio professionnel en Espagne, équipé de technologie de pointe incluant Source-Connect pour des sessions espagnoles à distance en direct. Sa voix en espagnol d'Espagne garantit une qualité exceptionnelle pour chaque projet de doublage en castillan.</p>
            """
        },
        "spots_page": {
            "title": "Voix-Off Espagnole pour Spots Publicitaires",
            "meta_desc": "Comédien vocal espagnol pour spots TV et publicité. Voix castillane professionnelle pour campagnes de marques internationales.",
            "content": """
                <p>La voix-off pour spots publicitaires en espagnol est l'une des spécialités de Guillermo A. Brazález. Sa voix espagnole castillane a été choisie par les principales marques internationales pour leurs campagnes en espagnol destinées aux marchés d'Espagne et d'Amérique latine.</p>
                <p>Un excellent spot publicitaire en espagnol nécessite une voix qui transmet confiance et professionnalisme. Guillermo offre exactement cela : une voix espagnole polyvalente qui s'adapte au ton de chaque marque pour la publicité en espagnol.</p>
                <p>Parmi ses clients publicitaires en espagnol figurent des marques comme BMW, Samsung et bien d'autres qui ont fait confiance à sa voix castillane d'Espagne pour connecter avec des millions de téléspectateurs hispanophones.</p>
            """
        },
        "documentaries_page": {
            "title": "Narration de Documentaires en Espagnol",
            "meta_desc": "Narrateur espagnol pour documentaires. Voix espagnole castillane pour documentaires nature, histoire et science.",
            "content": """
                <p>La narration de documentaires en espagnol castillan est l'un des domaines où Guillermo A. Brazález excelle particulièrement. Sa voix espagnole, chaleureuse et immersive, guide le spectateur à travers des histoires fascinantes avec l'autorité que le genre documentaire exige.</p>
                <p>Il a prêté sa voix espagnole à des documentaires pour Netflix, Discovery Channel, National Geographic et TVE. Son espagnol castillan apporte une qualité narrative exceptionnelle en espagnol d'Espagne.</p>
                <p>Avec plus de 20 ans d'expérience comme narrateur espagnol, Guillermo maîtrise chaque nuance de la voix pour créer des expériences audiovisuelles mémorables en espagnol castillan.</p>
            """
        },
        "radio_page": {
            "title": "Voix-Off Radio en Espagnol",
            "meta_desc": "Comédien vocal espagnol pour radio. Spots radio et programmation en espagnol castillan.",
            "content": """
                <p>La radio en espagnol reste l'un des médias les plus puissants pour connecter avec les audiences hispanophones. Guillermo apporte sa voix espagnole castillane professionnelle aux spots radio, jingles et programmation en espagnol.</p>
                <p>En tant que professionnel de la voix espagnole avec une vaste expérience en radio, Guillermo maîtrise les rythmes spécifiques du médium. Son espagnol castillan s'adapte naturellement à tout format radio en espagnol.</p>
                <p>Il travaille avec des stations de radio d'Espagne et d'Amérique latine, offrant des enregistrements en espagnol de haute qualité depuis son studio professionnel en Espagne.</p>
            """
        },
        "corporate_page": {
            "title": "Voix-Off Corporate en Espagnol",
            "meta_desc": "Comédien vocal espagnol pour vidéo corporate. Voix castillane pour présentations et communication d'entreprise.",
            "content": """
                <p>La voix-off corporate en espagnol nécessite une voix qui transmet professionnalisme et crédibilité. Guillermo offre sa voix espagnole castillane pour présentations, formation, communication interne et événements d'entreprise en espagnol.</p>
                <p>Les entreprises multinationales font confiance à sa voix espagnole pour leurs communications en espagnol castillan car elle combine autorité et accessibilité. Son espagnol d'Espagne est le choix parfait pour une image professionnelle sur le marché hispanophone.</p>
                <p>Chaque projet de voix corporate en espagnol reçoit une attention personnalisée depuis son studio en Espagne.</p>
            """
        },
        "audiobooks_page": {
            "title": "Livres Audio en Espagnol",
            "meta_desc": "Narrateur espagnol de livres audio. Voix castillane pour livres audio fiction et non-fiction.",
            "content": """
                <p>La narration de livres audio en espagnol castillan est un art qui requiert polyvalence et diction parfaite. Guillermo est un narrateur espagnol expérimenté qui apporte sa voix castillane chaleureuse à chaque page en espagnol.</p>
                <p>Un bon livre audio en espagnol a besoin d'un narrateur qui maintient l'attention de l'auditeur pendant des heures. Comme narrateur espagnol professionnel, Guillermo maîtrise ces facettes pour créer des expériences auditives en espagnol castillan.</p>
                <p>Son studio professionnel en Espagne est traité acoustiquement pour les longues sessions d'enregistrement en espagnol.</p>
            """
        },
        "studio_page": {
            "title": "Studio d'Enregistrement en Espagne",
            "meta_desc": "Studio professionnel d'enregistrement vocal en Espagne. Source-Connect et ISDN pour sessions de voix espagnole à distance.",
            "content": """
                <p>Le studio d'enregistrement de Guillermo est situé en Espagne et dispose de tout l'équipement professionnel nécessaire pour des productions de voix espagnole de la plus haute qualité. Conçu spécifiquement pour l'enregistrement vocal en espagnol.</p>
                <p>Le studio en Espagne est équipé de microphones haut de gamme et de connexion Source-Connect pour des sessions de voix espagnole en temps réel avec des clients du monde entier.</p>
                <p>Sa localisation en Espagne permet de couvrir des horaires compatibles avec l'Europe, les Amériques et l'Asie pour les productions en espagnol castillan.</p>
            """
        },
        "composer_page": {
            "title": "Compositeur de Musique — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, compositeur espagnol de musique pour l'audiovisuel. Bandes sonores originales depuis l'Espagne.",
            "content": """
                <p>En plus de sa carrière de comédien vocal espagnol, Guillermo A. Brazález est compositeur de musique originale pour productions audiovisuelles. Son double talent de voix espagnole et compositeur lui permet d'offrir des solutions audio complètes en espagnol.</p>
                <p>Ses compositions musicales couvrent une grande variété de styles, des bandes sonores cinématographiques à la musique pour spots publicitaires en espagnol. Chaque composition est conçue pour l'audiovisuel en espagnol.</p>
                <p>Guillermo travaille depuis son studio en Espagne, combinant voix espagnole castillane et production musicale pour créer des expériences audio mémorables en espagnol.</p>
            """
        },
        "contact_page": {
            "title": "Contact — Comédien Vocal Espagnol Guillermo A. Brazález",
            "meta_desc": "Contactez Guillermo A. Brazález, comédien vocal espagnol professionnel. WhatsApp, email et téléphone pour projets de voix espagnole.",
            "content": """
                <p>Vous cherchez une voix espagnole professionnelle pour votre prochain projet ? Guillermo est disponible pour des enregistrements en espagnol castillan depuis son studio en Espagne. Que vous ayez besoin d'une voix espagnole pour un spot, un documentaire ou une vidéo corporate, Guillermo offre la qualité que votre projet en espagnol mérite.</p>
                <p>Contactez-le directement par WhatsApp, par email ou par téléphone pour discuter de votre projet de voix espagnole. Guillermo répond personnellement à chaque demande concernant la voix-off en espagnol castillan.</p>
            """,
            "form_name": "Nom",
            "form_email": "Email",
            "form_message": "Message",
            "form_send": "Envoyer",
            "form_subject": "Sujet",
        }
    },
    "de": {
        "site_title": "Guillermo A. Brazález — Professioneller Spanischer Sprecher",
        "hero_tagline": "Die Stimme Bewegt die Welt",
        "hero_subtitle": "Professioneller spanischer Sprecher · Kastilische spanische Stimme mit über 20 Jahren Erfahrung",
        "hero_badge": "Die spanische Stimme der Trivago-Werbespots",
        "homepage_intro": """
            <p>Guillermo A. Brazález ist ein professioneller spanischer Sprecher mit Sitz in Spanien, spezialisiert auf erstklassige kastilisch-spanische Erzählung. Mit über zwei Jahrzehnten Erfahrung in der Sprecherbranche hat Guillermo seine authentische spanische Stimme Hunderten internationaler Projekte für die bekanntesten Marken der Welt geliehen.</p>
            <p>Seine spanische Stimme zeichnet sich durch Wärme, Autorität und Vielseitigkeit aus. Von Fernsehwerbespots bis hin zu Naturdokumentationen, Unternehmensvideos, Radiospots und Hörbüchern — seine kastilisch-spanische Stimme verbindet sich mit spanischsprachigen Zielgruppen weltweit. Er hat mit Produktionsfirmen in ganz Spanien und Lateinamerika zusammengearbeitet und dabei stets eine makellose kastilisch-spanische Aussprache geliefert.</p>
            <p>Als Muttersprachler aus Spanien arbeitet Guillermo von seinem eigenen professionellen Studio mit modernster Technologie, was ihm ermöglicht, spanische Aufnahmen höchster Qualität mit schnellen Lieferzeiten zu erstellen. Seine kastilisch-spanische Stimme ist die bevorzugte Wahl internationaler Marken wie Netflix, Discovery Channel, National Geographic und vieler anderer, die eine authentische, professionelle spanische Stimme suchen.</p>
            <p>Wenn Sie eine professionelle spanische Stimme für Ihr nächstes Projekt suchen, bietet Guillermo Live-Remote-Sessions, Aufnahmen in seinem Studio in Spanien und persönliche Betreuung, die außergewöhnliche Ergebnisse bei jedem spanischen Voice-Over-Projekt garantiert.</p>
        """,
        "services_heading": "Spanische Voice-Over Dienstleistungen",
        "services": {
            "spots": {"title": "Werbespots", "desc": "Professionelles spanisches Voice-Over für TV-Kampagnen und digitale Werbung.", "icon": "📺"},
            "documentaries": {"title": "Dokumentationen", "desc": "Kastilisch-spanische Erzählung für Natur-, Geschichts- und Wissenschaftsdokumentationen.", "icon": "🎬"},
            "radio": {"title": "Radio", "desc": "Professionelle spanische Stimme für Radiospots, Jingles und Programm.", "icon": "📻"},
            "corporate": {"title": "Unternehmensfilm", "desc": "Spanisches Corporate Voice-Over für Präsentationen und Schulungen.", "icon": "🏢"},
            "audiobooks": {"title": "Hörbücher", "desc": "Kastilisch-spanische Hörbucherzählung mit perfekter Diktion.", "icon": "📚"},
            "studio": {"title": "Studio", "desc": "Professionelles Aufnahmestudio in Spanien mit Source-Connect und ISDN.", "icon": "🎙️"},
        },
        "composer_title": "Komponist",
        "composer_text": """
            <p>Neben seiner Arbeit als spanischer Sprecher ist Guillermo A. Brazález Komponist für Originalmusik. Er erstellt Soundtracks und Kompositionen für audiovisuelle Projekte und ergänzt seine spanische Voice-Over-Arbeit mit maßgeschneiderter Musik.</p>
            <p>Seine Kompositionen reichen von Ambientmusik für Dokumentationen bis zu Originalthemen für spanische Werbespots. Die Kombination seines Talents als spanischer Sprecher und Komponist macht ihn einzigartig für umfassende Audio-Lösungen auf Spanisch.</p>
        """,
        "contact_title": "Kontakt",
        "contact_text": "Brauchen Sie eine professionelle spanische Stimme? Kontaktieren Sie Guillermo für Ihr kastilisch-spanisches Voice-Over-Projekt.",
        "nav": {"voice_actor": "Sprecher", "composer": "Komponist", "contact": "Kontakt"},
        "footer_text": "Professioneller spanischer Sprecher · Kastilische spanische Stimme aus Spanien",
        "cta_contact": "Kontaktieren",
        "cta_listen": "Demo Anhören",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "Professioneller Spanischer Sprecher",
            "meta_desc": "Guillermo A. Brazález, professioneller spanischer Sprecher mit kastilischer Stimme. Über 20 Jahre Erfahrung in Werbung, Dokumentationen und Unternehmensfilm.",
            "content": """
                <p>Guillermo A. Brazález ist einer der anerkanntesten professionellen spanischen Sprecher in Spanien. Seine kastilisch-spanische Stimme hat Hunderten audiovisueller Produktionen Leben eingehaucht, von großen Werbekampagnen bis hin zu internationalen Dokumentationen.</p>
                <p>Als spanischer Voice-Over-Profi mit über 20 Jahren Erfahrung beherrscht Guillermo alle Stimmregister. Sein kastilisches Spanisch ist Synonym für Professionalität, Klarheit und makellose Diktion, die spanischsprachige Zuhörer weltweit anspricht.</p>
                <p>Er arbeitet von seinem professionellen Aufnahmestudio in Spanien aus, ausgestattet mit Source-Connect für Live-Remote-Sessions auf Spanisch. Sein Portfolio umfasst internationale Top-Marken, die seiner spanischen Stimme für anspruchsvollste Projekte vertrauen.</p>
            """
        },
        "spots_page": {
            "title": "Spanisches Voice-Over für Werbespots",
            "meta_desc": "Professioneller spanischer Sprecher für TV-Werbung. Kastilisch-spanische Stimme für internationale Markenkampagnen.",
            "content": """
                <p>Voice-Over für spanische Werbespots ist eine der Spezialitäten von Guillermo A. Brazález. Seine kastilisch-spanische Stimme wurde von führenden internationalen Marken für ihre spanischsprachigen Kampagnen gewählt.</p>
                <p>Ein großartiger spanischer Werbespot braucht eine Stimme, die Vertrauen und Professionalität vermittelt. Guillermo liefert genau das: eine vielseitige spanische Stimme, die sich dem Ton jeder Marke anpasst.</p>
                <p>Zu seinen spanischen Werbekunden gehören Marken wie BMW, Samsung und viele andere, die seiner kastilisch-spanischen Stimme aus Spanien vertrauen.</p>
            """
        },
        "documentaries_page": {
            "title": "Spanische Dokumentationserzählung",
            "meta_desc": "Professioneller spanischer Erzähler für Dokumentationen. Kastilisch-spanische Stimme für Natur- und Geschichtsdokumentationen.",
            "content": """
                <p>Dokumentationserzählung auf Kastilisch-Spanisch ist eines der Felder, in denen Guillermo besonders glänzt. Seine warme, immersive spanische Stimme führt Zuschauer durch faszinierende Geschichten mit der Autorität, die das Genre erfordert.</p>
                <p>Er hat seine spanische Stimme für Dokumentationen bei Netflix, Discovery Channel und National Geographic eingesetzt. Sein kastilisches Spanisch bringt außergewöhnliche Erzählqualität aus Spanien.</p>
                <p>Mit über 20 Jahren Erfahrung als spanischer Erzähler meistert Guillermo jede Nuance für unvergessliche audiovisuelle Erlebnisse auf Spanisch.</p>
            """
        },
        "radio_page": {
            "title": "Spanisches Radio Voice-Over",
            "meta_desc": "Professioneller spanischer Sprecher für Radio. Radiospots und Programmgestaltung in kastilischem Spanisch.",
            "content": """
                <p>Spanischsprachiges Radio bleibt eines der wirkungsvollsten Medien. Guillermo bringt seine professionelle kastilisch-spanische Stimme in Radiospots, Jingles und Programmgestaltung auf Spanisch ein.</p>
                <p>Als spanischer Stimmprofi mit umfangreicher Radioerfahrung beherrscht Guillermo die spezifischen Rhythmen des Mediums. Sein kastilisches Spanisch passt sich natürlich an jedes Radioformat auf Spanisch an.</p>
                <p>Er arbeitet mit Radiosendern in ganz Spanien und Lateinamerika zusammen und liefert hochwertige spanische Aufnahmen aus seinem Studio in Spanien.</p>
            """
        },
        "corporate_page": {
            "title": "Spanisches Corporate Video Voice-Over",
            "meta_desc": "Spanischer Sprecher für Unternehmensfilm. Kastilisch-spanische Stimme für Präsentationen und Schulungen.",
            "content": """
                <p>Corporate Video Voice-Over auf Spanisch erfordert eine Stimme, die Professionalität und Glaubwürdigkeit vermittelt. Guillermo bietet seine kastilisch-spanische Stimme für Präsentationen, Schulungsmaterial und Unternehmenskommunikation auf Spanisch.</p>
                <p>Multinationale Unternehmen vertrauen seiner spanischen Stimme für ihre kastilisch-spanischen Kommunikationen. Sein Spanisch aus Spanien ist die perfekte Wahl für Marken im spanischsprachigen Markt.</p>
                <p>Jedes spanische Corporate Voice-Over-Projekt erhält persönliche Betreuung aus seinem Studio in Spanien.</p>
            """
        },
        "audiobooks_page": {
            "title": "Spanische Hörbucherzählung",
            "meta_desc": "Professioneller spanischer Hörbucherzähler. Kastilisch-spanische Stimme für Fiction und Non-Fiction Hörbücher.",
            "content": """
                <p>Hörbucherzählung in kastilischem Spanisch ist eine Kunst, die Vielseitigkeit und perfekte Diktion erfordert. Guillermo ist ein erfahrener spanischer Erzähler, der seine warme kastilisch-spanische Stimme in jedes Hörbuch einbringt.</p>
                <p>Ein großartiges spanisches Hörbuch braucht einen Erzähler, der die Aufmerksamkeit stundenlang hält. Als professioneller spanischer Erzähler meistert Guillermo dies für außergewöhnliche Hörerlebnisse auf Kastilisch-Spanisch.</p>
                <p>Sein professionelles Studio in Spanien ist akustisch behandelt für lange spanische Aufnahmesessions.</p>
            """
        },
        "studio_page": {
            "title": "Professionelles Aufnahmestudio in Spanien",
            "meta_desc": "Professionelles Sprachaufnahmestudio in Spanien. Source-Connect und ISDN für spanische Voice-Over Remote-Sessions.",
            "content": """
                <p>Guillermos Aufnahmestudio befindet sich in Spanien und verfügt über professionelle Ausrüstung für spanische Voice-Over-Produktionen höchster Qualität. Speziell für Sprachaufnahmen auf Spanisch konzipiert.</p>
                <p>Das Studio in Spanien ist mit High-End-Mikrofonen und Source-Connect ausgestattet für spanische Echtzeit-Remote-Sessions mit Kunden weltweit.</p>
                <p>Die Lage in Spanien ermöglicht Arbeitszeiten kompatibel mit Europa, Amerika und Asien für kastilisch-spanische Produktionen nach höchsten technischen Standards.</p>
            """
        },
        "composer_page": {
            "title": "Musikkomponist — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, spanischer Musikkomponist für audiovisuelle Produktionen. Original-Soundtracks aus Spanien.",
            "content": """
                <p>Neben seiner Karriere als professioneller spanischer Sprecher ist Guillermo Komponist für Originalmusik für audiovisuelle Produktionen. Sein Doppeltalent als spanische Stimme und Komponist ermöglicht umfassende Audio-Lösungen auf Spanisch.</p>
                <p>Seine Kompositionen umfassen Filmmusik bis Ambientmusik für Dokumentationen und spanische Werbespots. Jede Komposition ist für spanischsprachige audiovisuelle Produktionen konzipiert.</p>
                <p>Guillermo arbeitet aus seinem Studio in Spanien, wo er kastilisch-spanische Sprachaufnahmen mit Musikproduktion kombiniert.</p>
            """
        },
        "contact_page": {
            "title": "Kontakt — Spanischer Sprecher Guillermo A. Brazález",
            "meta_desc": "Kontaktieren Sie Guillermo A. Brazález, professioneller spanischer Sprecher. WhatsApp, Email und Telefon für spanische Voice-Over-Projekte.",
            "content": """
                <p>Suchen Sie eine professionelle spanische Stimme? Guillermo ist verfügbar für kastilisch-spanische Aufnahmen aus seinem Studio in Spanien. Ob Sie eine spanische Stimme für Werbung, Dokumentation oder Unternehmensfilm brauchen — Guillermo liefert die Qualität für Ihr spanisches Projekt.</p>
                <p>Kontaktieren Sie ihn per WhatsApp, Email oder Telefon. Guillermo antwortet persönlich auf jede Anfrage zu spanischem Voice-Over in kastilischem Spanisch.</p>
            """,
            "form_name": "Name",
            "form_email": "E-Mail",
            "form_message": "Nachricht",
            "form_send": "Nachricht Senden",
            "form_subject": "Betreff",
        }
    },
    "it": {
        "site_title": "Guillermo A. Brazález — Doppiatore Spagnolo Professionista",
        "hero_tagline": "La Voce Muove il Mondo",
        "hero_subtitle": "Doppiatore spagnolo professionista · Voce spagnola castigliana con oltre 20 anni di esperienza",
        "hero_badge": "La voce spagnola degli spot Trivago",
        "homepage_intro": """
            <p>Guillermo A. Brazález è un doppiatore spagnolo professionista con sede in Spagna, specializzato nella narrazione in spagnolo castigliano di prima qualità. Con oltre due decenni di esperienza nel settore del doppiaggio, Guillermo ha prestato la sua autentica voce spagnola a centinaia di progetti internazionali per i marchi più riconosciuti al mondo.</p>
            <p>La sua voce spagnola si distingue per calore, autorità e versatilità. Dagli spot pubblicitari ai documentari sulla natura, passando per video aziendali, spot radiofonici e audiolibri, la sua voce in spagnolo castigliano connette con il pubblico di lingua spagnola in tutto il mondo. Ha collaborato con società di produzione in Spagna e America Latina, offrendo sempre una pronuncia spagnola castigliana impeccabile.</p>
            <p>Come doppiatore spagnolo nativo dalla Spagna, Guillermo lavora dal suo studio professionale dotato di tecnologia all'avanguardia, permettendogli di consegnare registrazioni in spagnolo della massima qualità con tempi di consegna rapidi. La sua voce spagnola castigliana è la scelta preferita di marchi internazionali come Netflix, Discovery Channel, National Geographic e molti altri che cercano una voce spagnola autentica e professionale.</p>
            <p>Se cercate una voce professionale in spagnolo per il vostro prossimo progetto, Guillermo offre sessioni remote in diretta, registrazione nel suo studio in Spagna e un'attenzione personalizzata che garantisce risultati eccezionali in ogni progetto di doppiaggio in spagnolo castigliano.</p>
        """,
        "services_heading": "Servizi di Voice-Over in Spagnolo",
        "services": {
            "spots": {"title": "Spot Pubblicitari", "desc": "Voice-over spagnolo professionale per campagne televisive e pubblicità digitale.", "icon": "📺"},
            "documentaries": {"title": "Documentari", "desc": "Narrazione in spagnolo castigliano per documentari natura, storia e scienza.", "icon": "🎬"},
            "radio": {"title": "Radio", "desc": "Voce spagnola professionale per spot radio, jingle e programmazione.", "icon": "📻"},
            "corporate": {"title": "Video Aziendali", "desc": "Voice-over aziendale in spagnolo per presentazioni e formazione.", "icon": "🏢"},
            "audiobooks": {"title": "Audiolibri", "desc": "Narrazione di audiolibri in spagnolo castigliano con dizione perfetta.", "icon": "📚"},
            "studio": {"title": "Studio", "desc": "Studio di registrazione professionale in Spagna con Source-Connect e ISDN.", "icon": "🎙️"},
        },
        "composer_title": "Compositore",
        "composer_text": """
            <p>Oltre al suo lavoro come doppiatore spagnolo, Guillermo A. Brazález è compositore di musica originale per produzioni audiovisive, completando il suo lavoro di voice-over in spagnolo con musica su misura dalla Spagna.</p>
            <p>Le sue composizioni spaziano dalla musica ambient per documentari ai temi originali per spot pubblicitari in spagnolo. Il suo doppio talento di doppiatore spagnolo e compositore lo rende un professionista unico per soluzioni audio complete in spagnolo castigliano.</p>
        """,
        "contact_title": "Contatto",
        "contact_text": "Cercate una voce spagnola professionale? Contattate Guillermo per il vostro progetto di voice-over in spagnolo castigliano.",
        "nav": {"voice_actor": "Doppiatore", "composer": "Compositore", "contact": "Contatto"},
        "footer_text": "Doppiatore spagnolo professionista · Voce spagnola castigliana dalla Spagna",
        "cta_contact": "Contattare",
        "cta_listen": "Ascolta la Demo",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "Doppiatore Spagnolo Professionista",
            "meta_desc": "Guillermo A. Brazález, doppiatore spagnolo professionista con voce castigliana. Oltre 20 anni di esperienza in spot, documentari e video aziendali.",
            "content": """
                <p>Guillermo A. Brazález è uno dei doppiatori spagnoli più riconosciuti della Spagna. La sua voce spagnola castigliana ha dato vita a centinaia di produzioni audiovisive, dalle grandi campagne pubblicitarie ai documentari internazionali.</p>
                <p>Come professionista della voce spagnola con oltre 20 anni di esperienza, Guillermo padroneggia tutti i registri vocali. Il suo spagnolo castigliano è sinonimo di professionalità e dizione impeccabile che connette con il pubblico di lingua spagnola in tutto il mondo.</p>
                <p>Lavora dal suo studio professionale in Spagna, equipaggiato con Source-Connect per sessioni remote in spagnolo in diretta. I suoi clienti includono marchi internazionali che si affidano alla sua voce spagnola per i progetti più esigenti.</p>
            """
        },
        "spots_page": {
            "title": "Voice-Over Spagnolo per Spot Pubblicitari",
            "meta_desc": "Doppiatore spagnolo per spot TV e pubblicità. Voce castigliana professionale per campagne di marchi internazionali.",
            "content": """
                <p>Il voice-over per spot pubblicitari in spagnolo è una delle specialità di Guillermo. La sua voce spagnola castigliana è stata scelta dai principali marchi internazionali per le campagne in spagnolo destinate ai mercati di Spagna e America Latina.</p>
                <p>Un ottimo spot pubblicitario in spagnolo necessita di una voce che trasmette fiducia e professionalità. Guillermo offre esattamente questo: una voce spagnola versatile che si adatta al tono di ogni marchio.</p>
                <p>Tra i suoi clienti pubblicitari in spagnolo figurano marchi come BMW e Samsung che si affidano alla sua voce castigliana dalla Spagna.</p>
            """
        },
        "documentaries_page": {
            "title": "Narrazione di Documentari in Spagnolo",
            "meta_desc": "Narratore spagnolo per documentari. Voce spagnola castigliana per documentari natura, storia e scienza.",
            "content": """
                <p>La narrazione di documentari in spagnolo castigliano è uno dei campi in cui Guillermo eccelle. La sua calda voce spagnola guida lo spettatore attraverso storie affascinanti con l'autorità richiesta dal genere documentaristico.</p>
                <p>Ha prestato la sua voce spagnola a documentari per Netflix, Discovery Channel e National Geographic. Il suo spagnolo castigliano apporta una qualità narrativa eccezionale dalla Spagna.</p>
                <p>Con oltre 20 anni di esperienza come narratore spagnolo, Guillermo padroneggia ogni sfumatura per esperienze audiovisive memorabili in spagnolo castigliano.</p>
            """
        },
        "radio_page": {
            "title": "Voice-Over Radio in Spagnolo",
            "meta_desc": "Doppiatore spagnolo per radio. Spot radio e programmazione in spagnolo castigliano.",
            "content": """
                <p>La radio in spagnolo resta uno dei media più potenti per connettere con il pubblico di lingua spagnola. Guillermo porta la sua voce spagnola castigliana professionale in spot radio, jingle e programmazione in spagnolo.</p>
                <p>Come professionista della voce spagnola con vasta esperienza radiofonica, padroneggia i ritmi specifici del mezzo. Il suo spagnolo castigliano si adatta naturalmente a ogni formato radio in spagnolo.</p>
                <p>Lavora con stazioni radio in Spagna e America Latina, offrendo registrazioni in spagnolo di alta qualità dal suo studio in Spagna.</p>
            """
        },
        "corporate_page": {
            "title": "Voice-Over Aziendale in Spagnolo",
            "meta_desc": "Doppiatore spagnolo per video aziendali. Voce castigliana per presentazioni e comunicazione d'impresa.",
            "content": """
                <p>Il voice-over aziendale in spagnolo richiede una voce che trasmette professionalità e credibilità. Guillermo offre la sua voce spagnola castigliana per presentazioni, formazione e comunicazione aziendale in spagnolo.</p>
                <p>Le aziende multinazionali si affidano alla sua voce spagnola per le comunicazioni in spagnolo castigliano. Il suo spagnolo dalla Spagna è la scelta perfetta per un'immagine professionale nel mercato di lingua spagnola.</p>
                <p>Ogni progetto di voice-over aziendale in spagnolo riceve attenzione personalizzata dal suo studio in Spagna.</p>
            """
        },
        "audiobooks_page": {
            "title": "Audiolibri in Spagnolo",
            "meta_desc": "Narratore spagnolo di audiolibri. Voce castigliana per audiolibri fiction e non-fiction.",
            "content": """
                <p>La narrazione di audiolibri in spagnolo castigliano è un'arte che richiede versatilità e dizione perfetta. Guillermo è un narratore spagnolo esperto che porta la sua calda voce castigliana in ogni audiolibro in spagnolo.</p>
                <p>Un buon audiolibro in spagnolo ha bisogno di un narratore che mantiene l'attenzione per ore. Come narratore spagnolo professionista, Guillermo padroneggia queste sfaccettature per esperienze uditive in spagnolo castigliano.</p>
                <p>Il suo studio in Spagna è trattato acusticamente per lunghe sessioni di registrazione in spagnolo.</p>
            """
        },
        "studio_page": {
            "title": "Studio di Registrazione in Spagna",
            "meta_desc": "Studio professionale di registrazione vocale in Spagna. Source-Connect e ISDN per sessioni di voice-over spagnolo da remoto.",
            "content": """
                <p>Lo studio di registrazione di Guillermo si trova in Spagna ed è dotato di attrezzatura professionale per produzioni di voice-over in spagnolo della massima qualità, progettato specificamente per registrazioni vocali in spagnolo.</p>
                <p>Lo studio in Spagna è equipaggiato con microfoni di alta gamma e connessione Source-Connect per sessioni di voce spagnola in tempo reale con clienti da tutto il mondo.</p>
                <p>La posizione in Spagna permette di coprire orari compatibili con Europa, Americhe e Asia per produzioni in spagnolo castigliano ai massimi standard tecnici.</p>
            """
        },
        "composer_page": {
            "title": "Compositore di Musica — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, compositore spagnolo di musica per l'audiovisivo. Colonne sonore originali dalla Spagna.",
            "content": """
                <p>Oltre alla sua carriera come doppiatore spagnolo, Guillermo è compositore di musica originale per produzioni audiovisive. Il suo doppio talento di voce spagnola e compositore permette soluzioni audio complete in spagnolo.</p>
                <p>Le sue composizioni musicali spaziano dalle colonne sonore alla musica per spot pubblicitari in spagnolo. Ogni composizione è pensata per l'audiovisivo in spagnolo.</p>
                <p>Guillermo lavora dal suo studio in Spagna, combinando voce spagnola castigliana e produzione musicale per esperienze memorabili in spagnolo.</p>
            """
        },
        "contact_page": {
            "title": "Contatto — Doppiatore Spagnolo Guillermo A. Brazález",
            "meta_desc": "Contattate Guillermo A. Brazález, doppiatore spagnolo professionista. WhatsApp, email e telefono per progetti di voice-over in spagnolo.",
            "content": """
                <p>Cercate una voce spagnola professionale per il vostro prossimo progetto? Guillermo è disponibile per registrazioni in spagnolo castigliano dal suo studio in Spagna. Che abbiate bisogno di una voce spagnola per uno spot, un documentario o un video aziendale, Guillermo offre la qualità che il vostro progetto in spagnolo merita.</p>
                <p>Contattatelo via WhatsApp, email o telefono per discutere del vostro progetto di voice-over in spagnolo. Guillermo risponde personalmente a ogni richiesta su voice-over in spagnolo castigliano.</p>
            """,
            "form_name": "Nome",
            "form_email": "Email",
            "form_message": "Messaggio",
            "form_send": "Invia Messaggio",
            "form_subject": "Oggetto",
        }
    },
    "pt": {
        "site_title": "Guillermo A. Brazález — Locutor Espanhol Profissional",
        "hero_tagline": "A Voz Move o Mundo",
        "hero_subtitle": "Locutor espanhol profissional · Voz espanhola castelhana com mais de 20 anos de experiência",
        "hero_badge": "A voz espanhola dos anúncios da Trivago",
        "homepage_intro": """
            <p>Guillermo A. Brazález é um locutor espanhol profissional sediado em Espanha, especializado em narração em espanhol castelhano de primeira qualidade. Com mais de duas décadas de experiência na indústria de locução, Guillermo emprestou a sua autêntica voz espanhola a centenas de projetos internacionais para as marcas mais reconhecidas do mundo.</p>
            <p>A sua voz espanhola destaca-se pela calidez, autoridade e versatilidade. Desde spots publicitários para televisão até documentários de natureza, passando por vídeos corporativos, spots de rádio e audiolivros, a sua voz em espanhol castelhano conecta com audiências de língua espanhola em todo o mundo. Colaborou com produtoras de Espanha e América Latina, oferecendo sempre uma pronúncia espanhola castelhana impecável.</p>
            <p>Como locutor espanhol nativo de Espanha, Guillermo trabalha a partir do seu próprio estúdio profissional equipado com tecnologia de última geração, o que lhe permite entregar gravações em espanhol da mais alta qualidade com tempos de entrega rápidos. A sua voz espanhola castelhana é a escolha preferida de marcas internacionais como Netflix, Discovery Channel, National Geographic e muitas outras que procuram uma voz espanhola autêntica e profissional.</p>
            <p>Se procura uma voz profissional em espanhol para o seu próximo projeto, Guillermo oferece sessões remotas em direto, gravação no seu estúdio em Espanha e uma atenção personalizada que garante resultados excecionais em cada projeto de locução em espanhol castelhano.</p>
        """,
        "services_heading": "Serviços de Locução em Espanhol",
        "services": {
            "spots": {"title": "Spots Publicitários", "desc": "Locução profissional em espanhol para campanhas de televisão e publicidade digital.", "icon": "📺"},
            "documentaries": {"title": "Documentários", "desc": "Narração em espanhol castelhano para documentários de natureza, história e ciência.", "icon": "🎬"},
            "radio": {"title": "Rádio", "desc": "Voz espanhola profissional para spots de rádio, jingles e programação.", "icon": "📻"},
            "corporate": {"title": "Vídeo Corporativo", "desc": "Locução corporativa em espanhol para apresentações e formação.", "icon": "🏢"},
            "audiobooks": {"title": "Audiolivros", "desc": "Narração de audiolivros em espanhol castelhano com dicção perfeita.", "icon": "📚"},
            "studio": {"title": "Estúdio", "desc": "Estúdio profissional de gravação em Espanha com Source-Connect e ISDN.", "icon": "🎙️"},
        },
        "composer_title": "Compositor",
        "composer_text": """
            <p>Para além do seu trabalho como locutor espanhol, Guillermo A. Brazález é compositor de música original para produções audiovisuais, complementando o seu trabalho de locução em espanhol com música feita à medida desde Espanha.</p>
            <p>As suas composições vão desde música ambiente para documentários até temas originais para spots publicitários em espanhol. O seu duplo talento de locutor espanhol e compositor torna-o um profissional único para soluções áudio completas em espanhol castelhano.</p>
        """,
        "contact_title": "Contacto",
        "contact_text": "Precisa de uma voz espanhola profissional? Contacte Guillermo para o seu projeto de locução em espanhol castelhano.",
        "nav": {"voice_actor": "Locutor", "composer": "Compositor", "contact": "Contacto"},
        "footer_text": "Locutor espanhol profissional · Voz espanhola castelhana desde Espanha",
        "cta_contact": "Contactar",
        "cta_listen": "Ouvir Demo",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "Locutor Espanhol Profissional",
            "meta_desc": "Guillermo A. Brazález, locutor espanhol profissional com voz castelhana. Mais de 20 anos de experiência em spots, documentários e vídeo corporativo.",
            "content": """
                <p>Guillermo A. Brazález é um dos locutores espanhóis mais reconhecidos de Espanha. A sua voz espanhola castelhana deu vida a centenas de produções audiovisuais, desde grandes campanhas publicitárias até documentários internacionais.</p>
                <p>Como profissional da voz espanhola com mais de 20 anos de experiência, Guillermo domina todos os registos vocais. O seu espanhol castelhano é sinónimo de profissionalismo e dicção impecável que conecta com audiências de língua espanhola em todo o mundo.</p>
                <p>Trabalha a partir do seu estúdio profissional em Espanha, equipado com Source-Connect para sessões remotas em espanhol em direto. O seu portfólio inclui marcas internacionais de primeiro nível que confiam na sua voz espanhola.</p>
            """
        },
        "spots_page": {
            "title": "Locução Espanhola para Spots Publicitários",
            "meta_desc": "Locutor espanhol para spots de TV e publicidade. Voz castelhana profissional para campanhas de marcas internacionais.",
            "content": """
                <p>A locução para spots publicitários em espanhol é uma das especialidades de Guillermo. A sua voz espanhola castelhana foi escolhida pelas principais marcas internacionais para as suas campanhas em espanhol.</p>
                <p>Um excelente spot em espanhol precisa de uma voz que transmita confiança e profissionalismo. Guillermo oferece exatamente isso: uma voz espanhola versátil que se adapta ao tom de cada marca.</p>
                <p>Entre os seus clientes de publicidade em espanhol encontram-se marcas como BMW e Samsung que confiam na sua voz castelhana de Espanha.</p>
            """
        },
        "documentaries_page": {
            "title": "Narração de Documentários em Espanhol",
            "meta_desc": "Narrador espanhol para documentários. Voz espanhola castelhana para documentários de natureza, história e ciência.",
            "content": """
                <p>A narração de documentários em espanhol castelhano é um dos campos onde Guillermo se destaca particularmente. A sua voz espanhola, calorosa e envolvente, guia o espectador através de histórias fascinantes.</p>
                <p>Emprestou a sua voz espanhola a documentários para Netflix, Discovery Channel e National Geographic. O seu espanhol castelhano traz uma qualidade narrativa excecional desde Espanha.</p>
                <p>Com mais de 20 anos de experiência como narrador espanhol, Guillermo domina cada nuance para experiências audiovisuais memoráveis em espanhol castelhano.</p>
            """
        },
        "radio_page": {
            "title": "Locução de Rádio em Espanhol",
            "meta_desc": "Locutor espanhol para rádio. Spots de rádio e programação em espanhol castelhano.",
            "content": """
                <p>A rádio em espanhol continua a ser um dos meios mais poderosos. Guillermo traz a sua voz espanhola castelhana profissional a spots de rádio, jingles e programação em espanhol.</p>
                <p>Como profissional da voz espanhola com vasta experiência radiofónica, domina os ritmos específicos do meio. O seu espanhol castelhano adapta-se naturalmente a qualquer formato de rádio em espanhol.</p>
                <p>Trabalha com estações de rádio de Espanha e América Latina, oferecendo gravações em espanhol de alta qualidade desde o seu estúdio em Espanha.</p>
            """
        },
        "corporate_page": {
            "title": "Locução Corporativa em Espanhol",
            "meta_desc": "Locutor espanhol para vídeo corporativo. Voz castelhana para apresentações e comunicação empresarial.",
            "content": """
                <p>A locução de vídeo corporativo em espanhol requer uma voz que transmita profissionalismo e credibilidade. Guillermo oferece a sua voz espanhola castelhana para apresentações, formação e comunicação empresarial em espanhol.</p>
                <p>As empresas multinacionais confiam na sua voz espanhola para as comunicações em espanhol castelhano. O seu espanhol de Espanha é a escolha perfeita para uma imagem profissional no mercado de língua espanhola.</p>
                <p>Cada projeto de locução corporativa em espanhol recebe atenção personalizada desde o seu estúdio em Espanha.</p>
            """
        },
        "audiobooks_page": {
            "title": "Audiolivros em Espanhol",
            "meta_desc": "Narrador espanhol de audiolivros. Voz castelhana para audiolivros de ficção e não-ficção.",
            "content": """
                <p>A narração de audiolivros em espanhol castelhano é uma arte que requer versatilidade e dicção perfeita. Guillermo é um narrador espanhol experiente que traz a sua voz castelhana calorosa a cada audiolivro em espanhol.</p>
                <p>Um bom audiolivro em espanhol precisa de um narrador que mantenha a atenção durante horas. Como narrador espanhol profissional, Guillermo domina estas facetas para experiências auditivas em espanhol castelhano.</p>
                <p>O seu estúdio em Espanha está tratado acusticamente para longas sessões de gravação em espanhol.</p>
            """
        },
        "studio_page": {
            "title": "Estúdio de Gravação em Espanha",
            "meta_desc": "Estúdio profissional de gravação vocal em Espanha. Source-Connect e ISDN para sessões de locução espanhola remotas.",
            "content": """
                <p>O estúdio de gravação de Guillermo está localizado em Espanha e dispõe de equipamento profissional para produções de locução em espanhol da mais alta qualidade, concebido especificamente para gravações vocais em espanhol.</p>
                <p>O estúdio em Espanha está equipado com microfones de gama alta e conexão Source-Connect para sessões de voz espanhola em tempo real com clientes de todo o mundo.</p>
                <p>A localização em Espanha permite cobrir horários compatíveis com Europa, Américas e Ásia para produções em espanhol castelhano aos mais exigentes padrões técnicos.</p>
            """
        },
        "composer_page": {
            "title": "Compositor de Música — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, compositor espanhol de música para audiovisual. Bandas sonoras originais desde Espanha.",
            "content": """
                <p>Para além da sua carreira como locutor espanhol, Guillermo é compositor de música original para produções audiovisuais. O seu duplo talento de voz espanhola e compositor permite soluções áudio completas em espanhol.</p>
                <p>As suas composições abrangem desde bandas sonoras até música para spots publicitários em espanhol. Cada composição é concebida para o audiovisual em espanhol.</p>
                <p>Guillermo trabalha desde o seu estúdio em Espanha, combinando voz espanhola castelhana e produção musical para experiências memoráveis em espanhol.</p>
            """
        },
        "contact_page": {
            "title": "Contacto — Locutor Espanhol Guillermo A. Brazález",
            "meta_desc": "Contacte Guillermo A. Brazález, locutor espanhol profissional. WhatsApp, email e telefone para projetos de locução em espanhol.",
            "content": """
                <p>Procura uma voz espanhola profissional para o seu próximo projeto? Guillermo está disponível para gravações em espanhol castelhano desde o seu estúdio em Espanha. Quer precise de uma voz espanhola para um spot, documentário ou vídeo corporativo, Guillermo oferece a qualidade que o seu projeto em espanhol merece.</p>
                <p>Contacte-o por WhatsApp, email ou telefone para discutir o seu projeto de locução em espanhol. Guillermo responde pessoalmente a cada consulta sobre locução em espanhol castelhano.</p>
            """,
            "form_name": "Nome",
            "form_email": "Email",
            "form_message": "Mensagem",
            "form_send": "Enviar Mensagem",
            "form_subject": "Assunto",
        }
    },
    "sv": {
        "site_title": "Guillermo A. Brazález — Professionell Spansk Röstskådespelare",
        "hero_tagline": "Rösten Rör Världen",
        "hero_subtitle": "Professionell spansk röstskådespelare · Kastiliansk spanska med över 20 års erfarenhet",
        "hero_badge": "Den spanska rösten i Trivagos reklamfilmer",
        "homepage_intro": """
            <p>Guillermo A. Brazález är en professionell spansk röstskådespelare baserad i Spanien, specialiserad på förstklassig kastiliansk spanska. Med över två decenniers erfarenhet inom röstbranschen har Guillermo lånat sin autentiska spanska röst till hundratals internationella projekt för världens mest kända varumärken.</p>
            <p>Hans spanska röst utmärker sig genom värme, auktoritet och mångsidighet. Från reklamfilmer för tv till naturdokumentärer, företagsvideo, radiospots och ljudböcker — hans kastilianska spanska röst når spansktalande publik över hela världen. Han har samarbetat med produktionsbolag i Spanien och Latinamerika och alltid levererat en oklanderlig spansk uttalsstandard.</p>
            <p>Som infödd spansk röstskådespelare från Spanien arbetar Guillermo från sin egen professionella studio utrustad med den senaste tekniken, vilket gör det möjligt att leverera inspelningar på spanska av högsta kvalitet med snabba leveranstider. Hans kastilianska spanska är det föredragna valet för internationella varumärken som Netflix, Discovery Channel och National Geographic.</p>
            <p>Letar du efter en professionell spansk röst för ditt nästa projekt? Guillermo erbjuder fjärrsessioner i realtid, inspelning i sin studio i Spanien och personlig uppmärksamhet som garanterar exceptionella resultat för varje spanskt röstprojekt.</p>
        """,
        "services_heading": "Röstskådespelartjänster på Spanska",
        "services": {
            "spots": {"title": "Reklamfilm", "desc": "Professionell spansk voice-over för tv-kampanjer och digital reklam.", "icon": "📺"},
            "documentaries": {"title": "Dokumentärer", "desc": "Berättarröst på kastiliansk spanska för natur-, historie- och vetenskapsdokumentärer.", "icon": "🎬"},
            "radio": {"title": "Radio", "desc": "Professionell spansk röst för radiospots, jinglar och program.", "icon": "📻"},
            "corporate": {"title": "Företagsfilm", "desc": "Spansk företagsröst för presentationer, utbildning och intern kommunikation.", "icon": "🏢"},
            "audiobooks": {"title": "Ljudböcker", "desc": "Ljudboksberättande på kastiliansk spanska med perfekt diktion.", "icon": "📚"},
            "studio": {"title": "Studio", "desc": "Professionell inspelningsstudio i Spanien med Source-Connect och ISDN.", "icon": "🎙️"},
        },
        "composer_title": "Kompositör",
        "composer_text": """
            <p>Förutom sitt arbete som spansk röstskådespelare är Guillermo A. Brazález kompositör av originalmusik. Han skapar filmmusik och kompositioner för audiovisuella produktioner och kompletterar sitt spanska röstarbete med skräddarsydd musik som höjer kvaliteten på varje produktion.</p>
            <p>Hans kompositioner sträcker sig från ambient musik för dokumentärer till originalstycken för spanska reklamfilmer. Kombinationen av hans talang som spansk röstskådespelare och kompositör gör honom unik.</p>
        """,
        "contact_title": "Kontakt",
        "contact_text": "Behöver du en professionell spansk röst? Kontakta Guillermo för att diskutera ditt spanska voice-over-projekt.",
        "nav": {"voice_actor": "Röstskådespelare", "composer": "Kompositör", "contact": "Kontakt"},
        "footer_text": "Professionell spansk röstskådespelare · Kastiliansk spanska från Spanien",
        "cta_contact": "Kontakta",
        "cta_listen": "Lyssna på Demo",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "Professionell Spansk Röstskådespelare",
            "meta_desc": "Guillermo A. Brazález, professionell spansk röstskådespelare med kastiliansk röst. Över 20 års erfarenhet av reklamfilm, dokumentärer och företagsfilm på spanska.",
            "content": """
                <p>Guillermo A. Brazález är en av Spaniens mest erkända professionella spanska röstskådespelare. Hans kastilianska spanska röst har gett liv åt hundratals audiovisuella produktioner, från stora reklamkampanjer till internationella dokumentärer.</p>
                <p>Som spansk röstproffs med mer än 20 års erfarenhet behärskar Guillermo alla röstregister. Hans spanska är synonymt med professionalism och oklanderlig diktion som når spansktalande publik världen över.</p>
                <p>Han arbetar från sin professionella studio i Spanien, utrustad med Source-Connect för spanska fjärrsessioner i realtid. Hans klientportfölj inkluderar internationella toppvarumärken som förlitar sig på hans spanska röst.</p>
            """
        },
        "spots_page": {
            "title": "Spansk Voice-Over för Reklamfilm",
            "meta_desc": "Spansk röstskådespelare för tv-reklam och reklamfilm. Professionell kastiliansk spanska röst för internationella varumärkeskampanjer.",
            "content": """
                <p>Reklamfilm på spanska är en av Guillermos specialiteter. Hans kastilianska spanska röst har valts av ledande internationella varumärken för deras kampanjer riktade mot den spanska och latinamerikanska marknaden.</p>
                <p>En framgångsrik reklamfilm på spanska kräver en röst som förmedlar förtroende, närhet och professionalitet. Guillermo erbjuder precis det: en mångsidig spansk röst som anpassar sig till varje varumärkes ton.</p>
                <p>Bland hans reklamkunder på spanska finns varumärken som BMW, Samsung och Movistar som litar på hans kastilianska spanska röst från Spanien.</p>
            """
        },
        "documentaries_page": {
            "title": "Dokumentärberättande på Spanska",
            "meta_desc": "Spansk berättarröst för dokumentärer. Kastiliansk spanska röst för natur-, historie- och vetenskapsdokumentärer.",
            "content": """
                <p>Dokumentärberättande på kastiliansk spanska är ett av de områden där Guillermo verkligen utmärker sig. Hans varma spanska röst guidar tittaren genom fascinerande berättelser med den auktoritet som dokumentärgenren kräver.</p>
                <p>Han har lånat sin spanska röst till dokumentärer för Netflix, Discovery Channel och National Geographic. Hans kastilianska spanska ger en exceptionell berättarkvalitet från Spanien.</p>
                <p>Med över 20 års erfarenhet som spansk berättare behärskar Guillermo varje nyans för minnesvärda audiovisuella upplevelser på kastiliansk spanska.</p>
            """
        },
        "radio_page": {
            "title": "Spansk Radioröst",
            "meta_desc": "Professionell spansk röstskådespelare för radio. Radiospots och program på kastiliansk spanska.",
            "content": """
                <p>Radio på spanska förblir ett av de mest kraftfulla medierna för att nå spansktalande publik. Guillermo bidrar med sin professionella kastilianska spanska röst till radiospots, jinglar och program.</p>
                <p>Som spansk röstproffs med bred radioerfarenhet behärskar han de specifika rytmerna. Hans kastilianska spanska anpassar sig naturligt till alla radioformat på spanska.</p>
                <p>Han samarbetar med radiostationer i Spanien och Latinamerika och levererar inspelningar på spanska av hög kvalitet från sin studio i Spanien.</p>
            """
        },
        "corporate_page": {
            "title": "Spansk Företagsröst",
            "meta_desc": "Spansk röstskådespelare för företagsfilm. Kastiliansk spanska röst för presentationer och företagskommunikation.",
            "content": """
                <p>Företagsfilm på spanska kräver en röst som förmedlar professionalitet och trovärdighet. Guillermo erbjuder sin kastilianska spanska röst för presentationer, utbildningsmaterial och företagskommunikation på spanska.</p>
                <p>Multinationella företag förlitar sig på hans spanska röst för kommunikation på kastiliansk spanska. Hans spanska från Spanien är det perfekta valet för en professionell image på den spansktalande marknaden.</p>
                <p>Varje spanskt företagsprojekt får personlig uppmärksamhet från hans studio i Spanien.</p>
            """
        },
        "audiobooks_page": {
            "title": "Ljudböcker på Spanska",
            "meta_desc": "Spansk ljudboksberättare. Kastiliansk spanska röst för skönlitterära och facklitterära ljudböcker.",
            "content": """
                <p>Ljudboksberättande på kastiliansk spanska är en konst som kräver mångsidighet och perfekt diktion. Guillermo är en erfaren spansk berättare som ger sin varma kastilianska röst till varje ljudbok på spanska.</p>
                <p>En bra ljudbok på spanska behöver en berättare som håller uppmärksamheten i timmar. Som professionell spansk berättare behärskar Guillermo dessa nyanser för hörupplevelser på kastiliansk spanska.</p>
                <p>Hans studio i Spanien är akustiskt behandlad för långa inspelningssessioner på spanska.</p>
            """
        },
        "studio_page": {
            "title": "Professionell Inspelningsstudio i Spanien",
            "meta_desc": "Professionell röstinspelningsstudio i Spanien. Source-Connect och ISDN för spanska voice-over fjärrsessioner.",
            "content": """
                <p>Guillermos inspelningsstudio ligger i Spanien och är utrustad med professionell utrustning för spanska voice-over-produktioner av högsta kvalitet, specifikt designad för spanska röstinspelningar.</p>
                <p>Studion i Spanien har high-end-mikrofoner och Source-Connect för spanska realtidssessioner med kunder världen över.</p>
                <p>Placeringen i Spanien möjliggör arbetstider kompatibla med Europa, Amerika och Asien för kastiliansk spanska produktioner av högsta tekniska standard.</p>
            """
        },
        "composer_page": {
            "title": "Musikkompositör — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, spansk musikkompositör för audiovisuella produktioner. Originalmusik från Spanien.",
            "content": """
                <p>Utöver sin karriär som spansk röstskådespelare är Guillermo kompositör av originalmusik för audiovisuella produktioner. Hans dubbla talang som spansk röst och kompositör ger kompletta ljudlösningar på spanska.</p>
                <p>Hans kompositioner sträcker sig från filmmusik till musik för spanska reklamfilmer. Varje komposition är utformad för audiovisuella produktioner på spanska.</p>
                <p>Guillermo arbetar från sin studio i Spanien och kombinerar kastiliansk spansk röst med musikproduktion.</p>
            """
        },
        "contact_page": {
            "title": "Kontakt — Spansk Röstskådespelare Guillermo A. Brazález",
            "meta_desc": "Kontakta Guillermo A. Brazález, professionell spansk röstskådespelare. WhatsApp, e-post och telefon för spanska voice-over-projekt.",
            "content": """
                <p>Letar du efter en professionell spansk röst för ditt nästa projekt? Guillermo är tillgänglig för inspelningar på kastiliansk spanska från sin studio i Spanien. Oavsett om du behöver en spansk röst för reklam, dokumentär eller företagsfilm, levererar Guillermo den kvalitet ditt spanska projekt förtjänar.</p>
                <p>Kontakta honom via WhatsApp, e-post eller telefon. Guillermo svarar personligen på varje förfrågan om spansk voice-over på kastiliansk spanska.</p>
            """,
            "form_name": "Namn",
            "form_email": "E-post",
            "form_message": "Meddelande",
            "form_send": "Skicka Meddelande",
            "form_subject": "Ämne",
        }
    },
    "no": {
        "site_title": "Guillermo A. Brazález — Profesjonell Spansk Stemmeskuespiller",
        "hero_tagline": "Stemmen Beveger Verden",
        "hero_subtitle": "Profesjonell spansk stemmeskuespiller · Kastiliansk spansk stemme med over 20 års erfaring",
        "hero_badge": "Den spanske stemmen i Trivagos reklamefilmer",
        "homepage_intro": """
            <p>Guillermo A. Brazález er en profesjonell spansk stemmeskuespiller basert i Spania, spesialisert på førsteklasses kastiliansk spansk. Med over to tiårs erfaring i stemmebransjen har Guillermo lånt sin autentiske spanske stemme til hundrevis av internasjonale prosjekter for verdens mest kjente merkevarer.</p>
            <p>Hans spanske stemme utmerker seg med varme, autoritet og allsidighet. Fra reklamfilmer for TV til naturdokumentarer, bedriftsvideoer, radiospots og lydbøker — hans kastilianske spanske stemme når spansktalende publikum over hele verden. Han har samarbeidet med produksjonsselskaper i Spania og Latin-Amerika, og alltid levert en uklanderlig spansk uttalestandard.</p>
            <p>Som innfødt spansk stemmeskuespiller fra Spania arbeider Guillermo fra sitt eget profesjonelle studio utstyrt med den nyeste teknologien. Hans kastilianske spanske er det foretrukne valget for internasjonale merkevarer som Netflix, Discovery Channel og National Geographic.</p>
            <p>Leter du etter en profesjonell spansk stemme for ditt neste prosjekt? Guillermo tilbyr fjernsesjoner i sanntid, innspilling i sitt studio i Spania og personlig oppmerksomhet som garanterer eksepsjonelle resultater.</p>
        """,
        "services_heading": "Stemmetjenester på Spansk",
        "services": {
            "spots": {"title": "Reklamefilm", "desc": "Profesjonell spansk voice-over for TV-kampanjer og digital reklame.", "icon": "📺"},
            "documentaries": {"title": "Dokumentarer", "desc": "Fortellerstemme på kastiliansk spansk for natur-, historie- og vitenskapsdokumentarer.", "icon": "🎬"},
            "radio": {"title": "Radio", "desc": "Profesjonell spansk stemme for radiospots, jingler og programmer.", "icon": "📻"},
            "corporate": {"title": "Bedriftsfilm", "desc": "Spansk bedriftsstemme for presentasjoner, opplæring og intern kommunikasjon.", "icon": "🏢"},
            "audiobooks": {"title": "Lydbøker", "desc": "Lydbokfortelling på kastiliansk spansk med perfekt diksjon.", "icon": "📚"},
            "studio": {"title": "Studio", "desc": "Profesjonelt innspillingsstudio i Spania med Source-Connect og ISDN.", "icon": "🎙️"},
        },
        "composer_title": "Komponist",
        "composer_text": """
            <p>I tillegg til sitt arbeid som spansk stemmeskuespiller er Guillermo A. Brazález komponist av originalmusikk. Han skaper filmmusikk og komposisjoner for audiovisuelle produksjoner som kompletterer hans spanske stemmearbeid.</p>
            <p>Hans komposisjoner spenner fra ambientmusikk for dokumentarer til originalstykker for spanske reklamefilmer. Kombinasjonen av hans talent som spansk stemme og komponist gjør ham unik.</p>
        """,
        "contact_title": "Kontakt",
        "contact_text": "Trenger du en profesjonell spansk stemme? Kontakt Guillermo for å diskutere ditt spanske voice-over-prosjekt.",
        "nav": {"voice_actor": "Stemme", "composer": "Komponist", "contact": "Kontakt"},
        "footer_text": "Profesjonell spansk stemmeskuespiller · Kastiliansk spansk fra Spania",
        "cta_contact": "Kontakt",
        "cta_listen": "Lytt til Demo",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "Profesjonell Spansk Stemmeskuespiller",
            "meta_desc": "Guillermo A. Brazález, profesjonell spansk stemmeskuespiller med kastiliansk stemme. Over 20 års erfaring med reklame, dokumentarer og bedriftsfilm på spansk.",
            "content": """
                <p>Guillermo A. Brazález er en av Spanias mest anerkjente profesjonelle spanske stemmeskuespillere. Hans kastilianske spanske stemme har gitt liv til hundrevis av audiovisuelle produksjoner, fra store reklamekampanjer til internasjonale dokumentarer.</p>
                <p>Som spansk stemmeproff med mer enn 20 års erfaring behersker Guillermo alle stemmeregistre. Hans spanske er synonymt med profesjonalitet og uklanderlig diksjon.</p>
                <p>Han arbeider fra sitt profesjonelle studio i Spania, utstyrt med Source-Connect for spanske fjernsesjoner i sanntid.</p>
            """
        },
        "spots_page": {
            "title": "Spansk Voice-Over for Reklamefilm",
            "meta_desc": "Spansk stemmeskuespiller for TV-reklame. Profesjonell kastiliansk spansk stemme for internasjonale merkekampanjer.",
            "content": """
                <p>Reklamefilm på spansk er en av Guillermos spesialiteter. Hans kastilianske spanske stemme er valgt av ledende internasjonale merkevarer for kampanjer rettet mot det spanske og latinamerikanske markedet.</p>
                <p>En vellykket reklamefilm på spansk krever en stemme som formidler tillit og profesjonalitet. Guillermo tilbyr nettopp det: en allsidig spansk stemme fra Spania.</p>
                <p>Blant hans reklamekunder finner man merkevarer som BMW og Samsung som stoler på hans kastilianske spanske stemme.</p>
            """
        },
        "documentaries_page": {
            "title": "Dokumentarfortelling på Spansk",
            "meta_desc": "Spansk fortellerstemme for dokumentarer. Kastiliansk spansk stemme for natur-, historie- og vitenskapsdokumentarer.",
            "content": """
                <p>Dokumentarfortelling på kastiliansk spansk er et av områdene der Guillermo virkelig utmerker seg. Hans varme spanske stemme guider seeren gjennom fascinerende historier med den autoriteten dokumentarsjangeren krever.</p>
                <p>Han har lånt sin spanske stemme til dokumentarer for Netflix, Discovery Channel og National Geographic. Hans kastilianske spanske gir eksepsjonell fortellerkvalitet fra Spania.</p>
                <p>Med over 20 års erfaring som spansk forteller behersker Guillermo hver nyanse for minnerike audiovisuelle opplevelser.</p>
            """
        },
        "radio_page": {
            "title": "Spansk Radiostemme",
            "meta_desc": "Profesjonell spansk stemmeskuespiller for radio. Radiospots og programmer på kastiliansk spansk.",
            "content": """
                <p>Radio på spansk forblir et av de kraftigste mediene for å nå spansktalende publikum. Guillermo bidrar med sin profesjonelle kastilianske spanske stemme til radiospots, jingler og programmer.</p>
                <p>Som spansk stemmeproff behersker han de spesifikke rytmene i radiomediet. Hans kastilianske spanske tilpasser seg naturlig alle radioformater.</p>
                <p>Han samarbeider med radiostasjoner i Spania og Latin-Amerika og leverer innspillinger på spansk av høy kvalitet.</p>
            """
        },
        "corporate_page": {
            "title": "Spansk Bedriftsstemme",
            "meta_desc": "Spansk stemmeskuespiller for bedriftsfilm. Kastiliansk spansk stemme for presentasjoner og bedriftskommunikasjon.",
            "content": """
                <p>Bedriftsfilm på spansk krever en stemme som formidler profesjonalitet og troverdighet. Guillermo tilbyr sin kastilianske spanske stemme for presentasjoner og bedriftskommunikasjon.</p>
                <p>Multinasjonale selskaper stoler på hans spanske stemme for kommunikasjon på kastiliansk spansk. Hans spanske fra Spania er det perfekte valget for et profesjonelt image.</p>
                <p>Hvert spansk bedriftsprosjekt får personlig oppmerksomhet fra hans studio i Spania.</p>
            """
        },
        "audiobooks_page": {
            "title": "Lydbøker på Spansk",
            "meta_desc": "Spansk lydbokforteller. Kastiliansk spansk stemme for skjønnlitterære og faglitterære lydbøker.",
            "content": """
                <p>Lydbokfortelling på kastiliansk spansk er en kunst som krever allsidighet og perfekt diksjon. Guillermo er en erfaren spansk forteller som gir sin varme kastilianske stemme til hver lydbok på spansk.</p>
                <p>En god lydbok på spansk trenger en forteller som holder oppmerksomheten i timer. Som profesjonell spansk forteller behersker Guillermo disse nyansene.</p>
                <p>Hans studio i Spania er akustisk behandlet for lange innspillingsøkter på spansk.</p>
            """
        },
        "studio_page": {
            "title": "Profesjonelt Innspillingsstudio i Spania",
            "meta_desc": "Profesjonelt stemmeinnspillingsstudio i Spania. Source-Connect og ISDN for spanske voice-over fjernsesjoner.",
            "content": """
                <p>Guillermos innspillingsstudio ligger i Spania og er utstyrt med profesjonelt utstyr for spanske voice-over-produksjoner av høyeste kvalitet.</p>
                <p>Studioet i Spania har high-end-mikrofoner og Source-Connect for spanske sanntidssesjoner med kunder over hele verden.</p>
                <p>Plasseringen i Spania muliggjør arbeidstider kompatible med Europa, Amerika og Asia for kastiliansk spanske produksjoner.</p>
            """
        },
        "composer_page": {
            "title": "Musikkkomponist — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, spansk musikkkomponist for audiovisuelle produksjoner. Originalmusikk fra Spania.",
            "content": """
                <p>I tillegg til sin karriere som spansk stemmeskuespiller er Guillermo komponist av originalmusikk for audiovisuelle produksjoner. Hans doble talent som spansk stemme og komponist gir komplette lydløsninger.</p>
                <p>Hans komposisjoner spenner fra filmmusikk til musikk for spanske reklamefilmer. Hver komposisjon er utformet for audiovisuell produksjon.</p>
                <p>Guillermo arbeider fra sitt studio i Spania og kombinerer kastiliansk spansk stemme med musikkproduksjon.</p>
            """
        },
        "contact_page": {
            "title": "Kontakt — Spansk Stemmeskuespiller Guillermo A. Brazález",
            "meta_desc": "Kontakt Guillermo A. Brazález, profesjonell spansk stemmeskuespiller. WhatsApp, e-post og telefon for spanske voice-over-prosjekter.",
            "content": """
                <p>Leter du etter en profesjonell spansk stemme? Guillermo er tilgjengelig for innspillinger på kastiliansk spansk fra sitt studio i Spania. Uansett om du trenger en spansk stemme for reklame, dokumentar eller bedriftsfilm, leverer Guillermo kvaliteten ditt prosjekt fortjener.</p>
                <p>Kontakt ham via WhatsApp, e-post eller telefon. Guillermo svarer personlig på alle henvendelser om spansk voice-over.</p>
            """,
            "form_name": "Navn",
            "form_email": "E-post",
            "form_message": "Melding",
            "form_send": "Send Melding",
            "form_subject": "Emne",
        }
    },
    "da": {
        "site_title": "Guillermo A. Brazález — Professionel Spansk Stemmeskuespiller",
        "hero_tagline": "Stemmen Bevæger Verden",
        "hero_subtitle": "Professionel spansk stemmeskuespiller · Kastiliansk spansk stemme med over 20 års erfaring",
        "hero_badge": "Den spanske stemme i Trivagos reklamefilm",
        "homepage_intro": """
            <p>Guillermo A. Brazález er en professionel spansk stemmeskuespiller baseret i Spanien, specialiseret i førsteklasses kastiliansk spansk. Med over to årtiers erfaring har Guillermo lånt sin autentiske spanske stemme til hundredvis af internationale projekter for verdens mest anerkendte mærker.</p>
            <p>Hans spanske stemme udmærker sig ved varme, autoritet og alsidighed. Fra reklamefilm til naturdokumentarer, virksomhedsvideoer, radiospots og lydbøger — hans kastilianske spanske stemme når spansktalende publikum over hele verden. Han har samarbejdet med produktionsselskaber i Spanien og Latinamerika.</p>
            <p>Som indfødt spansk stemmeskuespiller fra Spanien arbejder Guillermo fra sit eget professionelle studie udstyret med den nyeste teknologi. Hans kastilianske spanske er det foretrukne valg for internationale mærker som Netflix, Discovery Channel og National Geographic.</p>
            <p>Leder du efter en professionel spansk stemme til dit næste projekt? Guillermo tilbyder fjernsessioner i realtid, optagelse i sit studie i Spanien og personlig opmærksomhed der garanterer enestående resultater.</p>
        """,
        "services_heading": "Stemmetjenester på Spansk",
        "services": {
            "spots": {"title": "Reklamefilm", "desc": "Professionel spansk voice-over til tv-kampagner og digital reklame.", "icon": "📺"},
            "documentaries": {"title": "Dokumentarer", "desc": "Fortællerstemme på kastiliansk spansk til natur-, historie- og videnskabsdokumentarer.", "icon": "🎬"},
            "radio": {"title": "Radio", "desc": "Professionel spansk stemme til radiospots, jingler og programmer.", "icon": "📻"},
            "corporate": {"title": "Virksomhedsfilm", "desc": "Spansk virksomhedsstemme til præsentationer og intern kommunikation.", "icon": "🏢"},
            "audiobooks": {"title": "Lydbøger", "desc": "Lydbogfortælling på kastiliansk spansk med perfekt diktion.", "icon": "📚"},
            "studio": {"title": "Studie", "desc": "Professionelt optagelsesstudie i Spanien med Source-Connect og ISDN.", "icon": "🎙️"},
        },
        "composer_title": "Komponist",
        "composer_text": """
            <p>Udover sit arbejde som spansk stemmeskuespiller er Guillermo A. Brazález komponist af originalmusik. Han skaber filmmusik og kompositioner til audiovisuelle produktioner der komplementerer hans spanske stemmearbejde.</p>
            <p>Hans kompositioner spænder fra ambient musik til dokumentarer til originalstykker for spanske reklamefilm. Hans dobbelttalent som spansk stemme og komponist gør ham unik.</p>
        """,
        "contact_title": "Kontakt",
        "contact_text": "Har du brug for en professionel spansk stemme? Kontakt Guillermo for at diskutere dit spanske voice-over-projekt.",
        "nav": {"voice_actor": "Stemme", "composer": "Komponist", "contact": "Kontakt"},
        "footer_text": "Professionel spansk stemmeskuespiller · Kastiliansk spansk fra Spanien",
        "cta_contact": "Kontakt",
        "cta_listen": "Lyt til Demo",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "Professionel Spansk Stemmeskuespiller",
            "meta_desc": "Guillermo A. Brazález, professionel spansk stemmeskuespiller med kastiliansk stemme. Over 20 års erfaring med reklame, dokumentarer og virksomhedsfilm på spansk.",
            "content": """
                <p>Guillermo A. Brazález er en af Spaniens mest anerkendte professionelle spanske stemmeskuespillere. Hans kastilianske spanske stemme har givet liv til hundredvis af audiovisuelle produktioner.</p>
                <p>Som spansk stemmeprofessionel med mere end 20 års erfaring mestrer Guillermo alle stemmeregistre. Hans spanske er synonymt med professionalisme og upåklagelig diktion.</p>
                <p>Han arbejder fra sit professionelle studie i Spanien, udstyret med Source-Connect til spanske fjernsessioner i realtid.</p>
            """
        },
        "spots_page": {
            "title": "Spansk Voice-Over til Reklamefilm",
            "meta_desc": "Spansk stemmeskuespiller til tv-reklame. Professionel kastiliansk spansk stemme til internationale mærkekampagner.",
            "content": """
                <p>Reklamefilm på spansk er en af Guillermos specialer. Hans kastilianske spanske stemme er valgt af førende internationale mærker til kampagner rettet mod det spanske og latinamerikanske marked.</p>
                <p>En vellykket reklamefilm på spansk kræver en stemme der formidler tillid og professionalisme. Guillermo tilbyder netop det: en alsidig spansk stemme fra Spanien.</p>
                <p>Blandt hans reklamekunder finder man mærker som BMW og Samsung der stoler på hans kastilianske spanske stemme.</p>
            """
        },
        "documentaries_page": {
            "title": "Dokumentarfortælling på Spansk",
            "meta_desc": "Spansk fortællerstemme til dokumentarer. Kastiliansk spansk stemme til natur-, historie- og videnskabsdokumentarer.",
            "content": """
                <p>Dokumentarfortælling på kastiliansk spansk er et af de områder hvor Guillermo virkelig udmærker sig. Hans varme spanske stemme guider seeren gennem fascinerende historier.</p>
                <p>Han har lånt sin spanske stemme til dokumentarer for Netflix, Discovery Channel og National Geographic fra Spanien.</p>
                <p>Med over 20 års erfaring som spansk fortæller mestrer Guillermo enhver nuance for mindeværdige audiovisuelle oplevelser.</p>
            """
        },
        "radio_page": {
            "title": "Spansk Radiostemme",
            "meta_desc": "Professionel spansk stemmeskuespiller til radio. Radiospots og programmer på kastiliansk spansk.",
            "content": """
                <p>Radio på spansk forbliver et af de mest kraftfulde medier. Guillermo bidrager med sin professionelle kastilianske spanske stemme til radiospots, jingler og programmer.</p>
                <p>Som spansk stemmeprofessionel mestrer han de specifikke rytmer. Hans kastilianske spanske tilpasser sig naturligt alle radioformater.</p>
                <p>Han samarbejder med radiostationer i Spanien og Latinamerika og leverer optagelser på spansk af høj kvalitet.</p>
            """
        },
        "corporate_page": {
            "title": "Spansk Virksomhedsstemme",
            "meta_desc": "Spansk stemmeskuespiller til virksomhedsfilm. Kastiliansk spansk stemme til præsentationer og virksomhedskommunikation.",
            "content": """
                <p>Virksomhedsfilm på spansk kræver en stemme der formidler professionalisme og troværdighed. Guillermo tilbyder sin kastilianske spanske stemme til præsentationer og virksomhedskommunikation.</p>
                <p>Multinationale virksomheder stoler på hans spanske stemme til kommunikation på kastiliansk spansk. Hans spanske fra Spanien er det perfekte valg.</p>
                <p>Hvert spansk virksomhedsprojekt får personlig opmærksomhed fra hans studie i Spanien.</p>
            """
        },
        "audiobooks_page": {
            "title": "Lydbøger på Spansk",
            "meta_desc": "Spansk lydbogfortæller. Kastiliansk spansk stemme til skønlitterære og faglitterære lydbøger.",
            "content": """
                <p>Lydbogfortælling på kastiliansk spansk er en kunst der kræver alsidighed og perfekt diktion. Guillermo er en erfaren spansk fortæller der giver sin varme kastilianske stemme til hver lydbok.</p>
                <p>En god lydbok på spansk behøver en fortæller der holder opmærksomheden i timer. Guillermo mestrer disse nuancer for lytteoplevelser på kastiliansk spansk.</p>
                <p>Hans studie i Spanien er akustisk behandlet til lange optagelsessessioner på spansk.</p>
            """
        },
        "studio_page": {
            "title": "Professionelt Optagelsesstudie i Spanien",
            "meta_desc": "Professionelt stemmeoptagelsesstudie i Spanien. Source-Connect og ISDN til spanske voice-over fjernsessioner.",
            "content": """
                <p>Guillermos optagelsesstudie ligger i Spanien og er udstyret med professionelt udstyr til spanske voice-over-produktioner af højeste kvalitet.</p>
                <p>Studiet i Spanien har high-end mikrofoner og Source-Connect til spanske realtidssessioner med kunder fra hele verden.</p>
                <p>Placeringen i Spanien muliggør arbejdstider kompatible med Europa, Amerika og Asien for kastiliansk spanske produktioner.</p>
            """
        },
        "composer_page": {
            "title": "Musikkomponist — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, spansk musikkomponist til audiovisuelle produktioner. Originalmusik fra Spanien.",
            "content": """
                <p>Udover sin karriere som spansk stemmeskuespiller er Guillermo komponist af originalmusik til audiovisuelle produktioner. Hans dobbelttalent som spansk stemme og komponist giver komplette lydløsninger.</p>
                <p>Hans kompositioner spænder fra filmmusik til musik for spanske reklamefilm. Hver komposition er designet til audiovisuel produktion.</p>
                <p>Guillermo arbejder fra sit studie i Spanien og kombinerer kastiliansk spansk stemme med musikproduktion.</p>
            """
        },
        "contact_page": {
            "title": "Kontakt — Spansk Stemmeskuespiller Guillermo A. Brazález",
            "meta_desc": "Kontakt Guillermo A. Brazález, professionel spansk stemmeskuespiller. WhatsApp, e-mail og telefon til spanske voice-over-projekter.",
            "content": """
                <p>Leder du efter en professionel spansk stemme til dit næste projekt? Guillermo er tilgængelig for optagelser på kastiliansk spansk fra sit studie i Spanien. Uanset om du har brug for en spansk stemme til reklame, dokumentar eller virksomhedsfilm, leverer Guillermo kvaliteten dit projekt fortjener.</p>
                <p>Kontakt ham via WhatsApp, e-mail eller telefon. Guillermo svarer personligt på alle henvendelser om spansk voice-over.</p>
            """,
            "form_name": "Navn",
            "form_email": "E-mail",
            "form_message": "Besked",
            "form_send": "Send Besked",
            "form_subject": "Emne",
        }
    },
    "nl": {
        "site_title": "Guillermo A. Brazález — Professionele Spaanse Stemacteur",
        "hero_tagline": "De Stem Beweegt de Wereld",
        "hero_subtitle": "Professionele Spaanse stemacteur · Castiliaans Spaanse stem met meer dan 20 jaar ervaring",
        "hero_badge": "De Spaanse stem van de Trivago-reclames",
        "homepage_intro": """
            <p>Guillermo A. Brazález is een professionele Spaanse stemacteur gevestigd in Spanje, gespecialiseerd in eersteklas Castiliaans Spaans. Met meer dan twee decennia ervaring in de stembranch heeft Guillermo zijn authentieke Spaanse stem geleend aan honderden internationale projecten voor 's werelds meest gerenommeerde merken.</p>
            <p>Zijn Spaanse stem onderscheidt zich door warmte, autoriteit en veelzijdigheid. Van reclamefilms voor televisie tot natuurdocumentaires, bedrijfsvideo's, radiospots en luisterboeken — zijn Castiliaans Spaanse stem bereikt Spaanstalig publiek over de hele wereld. Hij heeft samengewerkt met productiebedrijven in Spanje en Latijns-Amerika.</p>
            <p>Als geboren Spaanse stemacteur uit Spanje werkt Guillermo vanuit zijn eigen professionele studio uitgerust met de nieuwste technologie. Zijn Castiliaans Spaans is de voorkeurskeuze van internationale merken zoals Netflix, Discovery Channel en National Geographic.</p>
            <p>Op zoek naar een professionele Spaanse stem voor uw volgende project? Guillermo biedt remote sessies in real-time, opname in zijn studio in Spanje en persoonlijke aandacht die uitzonderlijke resultaten garandeert.</p>
        """,
        "services_heading": "Stemacteur Diensten in het Spaans",
        "services": {
            "spots": {"title": "Reclamespot", "desc": "Professionele Spaanse voice-over voor tv-campagnes en digitale reclame.", "icon": "📺"},
            "documentaries": {"title": "Documentaires", "desc": "Vertellerstem in Castiliaans Spaans voor natuur-, geschied- en wetenschapsdocumentaires.", "icon": "🎬"},
            "radio": {"title": "Radio", "desc": "Professionele Spaanse stem voor radiospots, jingles en programma's.", "icon": "📻"},
            "corporate": {"title": "Bedrijfsvideo", "desc": "Spaanse bedrijfsstem voor presentaties, training en interne communicatie.", "icon": "🏢"},
            "audiobooks": {"title": "Luisterboeken", "desc": "Luisterboekvertelling in Castiliaans Spaans met perfecte dictie.", "icon": "📚"},
            "studio": {"title": "Studio", "desc": "Professionele opnamestudio in Spanje met Source-Connect en ISDN.", "icon": "🎙️"},
        },
        "composer_title": "Componist",
        "composer_text": """
            <p>Naast zijn werk als Spaanse stemacteur is Guillermo A. Brazález componist van originele muziek. Hij creëert filmmuziek en composities voor audiovisuele producties die zijn Spaanse stemwerk aanvullen.</p>
            <p>Zijn composities variëren van ambientmuziek voor documentaires tot originele stukken voor Spaanse reclamefilms. Zijn dubbele talent als Spaanse stem en componist maakt hem uniek.</p>
        """,
        "contact_title": "Contact",
        "contact_text": "Heeft u een professionele Spaanse stem nodig? Neem contact op met Guillermo om uw Spaans voice-over project te bespreken.",
        "nav": {"voice_actor": "Stemacteur", "composer": "Componist", "contact": "Contact"},
        "footer_text": "Professionele Spaanse stemacteur · Castiliaans Spaanse stem vanuit Spanje",
        "cta_contact": "Contact",
        "cta_listen": "Beluister Demo",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "Professionele Spaanse Stemacteur",
            "meta_desc": "Guillermo A. Brazález, professionele Spaanse stemacteur met Castiliaanse stem. Meer dan 20 jaar ervaring in reclame, documentaires en bedrijfsfilm in het Spaans.",
            "content": """
                <p>Guillermo A. Brazález is een van Spanje's meest erkende professionele Spaanse stemacteurs. Zijn Castiliaans Spaanse stem heeft honderden audiovisuele producties tot leven gebracht, van grote reclamecampagnes tot internationale documentaires.</p>
                <p>Als Spaanse stemprofessional met meer dan 20 jaar ervaring beheerst Guillermo alle stemregisters. Zijn Spaans staat synoniem voor professionaliteit en onberispelijke dictie.</p>
                <p>Hij werkt vanuit zijn professionele studio in Spanje, uitgerust met Source-Connect voor Spaanse remote sessies in real-time.</p>
            """
        },
        "spots_page": {
            "title": "Spaanse Voice-Over voor Reclamespots",
            "meta_desc": "Spaanse stemacteur voor tv-reclame. Professionele Castiliaans Spaanse stem voor internationale merkcampagnes.",
            "content": """
                <p>Reclamefilm in het Spaans is een van Guillermos specialiteiten. Zijn Castiliaans Spaanse stem is gekozen door toonaangevende internationale merken voor campagnes gericht op de Spaanse en Latijns-Amerikaanse markt.</p>
                <p>Een succesvolle reclamespot in het Spaans vereist een stem die vertrouwen en professionaliteit uitstraalt. Guillermo biedt precies dat: een veelzijdige Spaanse stem vanuit Spanje.</p>
                <p>Tot zijn reclameklanten behoren merken als BMW en Samsung die vertrouwen op zijn Castiliaans Spaanse stem.</p>
            """
        },
        "documentaries_page": {
            "title": "Documentairevertelling in het Spaans",
            "meta_desc": "Spaanse vertellerstem voor documentaires. Castiliaans Spaanse stem voor natuur-, geschied- en wetenschapsdocumentaires.",
            "content": """
                <p>Documentairevertelling in Castiliaans Spaans is een van de gebieden waar Guillermo werkelijk uitblinkt. Zijn warme Spaanse stem leidt de kijker door fascinerende verhalen.</p>
                <p>Hij heeft zijn Spaanse stem geleend aan documentaires voor Netflix, Discovery Channel en National Geographic. Zijn Castiliaans Spaans brengt uitzonderlijke vertelkwaliteit vanuit Spanje.</p>
                <p>Met meer dan 20 jaar ervaring als Spaanse verteller beheerst Guillermo elke nuance voor onvergetelijke audiovisuele ervaringen.</p>
            """
        },
        "radio_page": {
            "title": "Spaanse Radiostem",
            "meta_desc": "Professionele Spaanse stemacteur voor radio. Radiospots en programma's in Castiliaans Spaans.",
            "content": """
                <p>Radio in het Spaans blijft een van de krachtigste media. Guillermo draagt bij met zijn professionele Castiliaans Spaanse stem aan radiospots, jingles en programma's.</p>
                <p>Als Spaanse stemprofessional beheerst hij de specifieke ritmes van het radiomedium. Zijn Castiliaans Spaans past zich natuurlijk aan elk radioformaat aan.</p>
                <p>Hij werkt samen met radiostations in Spanje en Latijns-Amerika en levert opnames in het Spaans van hoge kwaliteit.</p>
            """
        },
        "corporate_page": {
            "title": "Spaanse Bedrijfsstem",
            "meta_desc": "Spaanse stemacteur voor bedrijfsvideo. Castiliaans Spaanse stem voor presentaties en bedrijfscommunicatie.",
            "content": """
                <p>Bedrijfsvideo in het Spaans vereist een stem die professionaliteit en geloofwaardigheid uitstraalt. Guillermo biedt zijn Castiliaans Spaanse stem voor presentaties en bedrijfscommunicatie.</p>
                <p>Multinationale bedrijven vertrouwen op zijn Spaanse stem voor communicatie in Castiliaans Spaans. Zijn Spaans vanuit Spanje is de perfecte keuze voor een professioneel imago.</p>
                <p>Elk Spaans bedrijfsproject krijgt persoonlijke aandacht vanuit zijn studio in Spanje.</p>
            """
        },
        "audiobooks_page": {
            "title": "Luisterboeken in het Spaans",
            "meta_desc": "Spaanse luisterboekverteller. Castiliaans Spaanse stem voor fictie en non-fictie luisterboeken.",
            "content": """
                <p>Luisterboekvertelling in Castiliaans Spaans is een kunst die veelzijdigheid en perfecte dictie vereist. Guillermo is een ervaren Spaanse verteller die zijn warme Castiliaanse stem leent aan elk luisterboek.</p>
                <p>Een goed luisterboek in het Spaans heeft een verteller nodig die urenlang de aandacht vasthoudt. Als professionele Spaanse verteller beheerst Guillermo deze nuances.</p>
                <p>Zijn studio in Spanje is akoestisch behandeld voor lange opnamesessies in het Spaans.</p>
            """
        },
        "studio_page": {
            "title": "Professionele Opnamestudio in Spanje",
            "meta_desc": "Professionele stemopnamestudio in Spanje. Source-Connect en ISDN voor Spaanse voice-over remote sessies.",
            "content": """
                <p>Guillermos opnamestudio bevindt zich in Spanje en is uitgerust met professionele apparatuur voor Spaanse voice-over producties van de hoogste kwaliteit.</p>
                <p>De studio in Spanje beschikt over high-end microfoons en Source-Connect voor Spaanse real-time sessies met klanten wereldwijd.</p>
                <p>De locatie in Spanje maakt werktijden mogelijk die compatibel zijn met Europa, Amerika en Azië voor Castiliaans Spaanse producties.</p>
            """
        },
        "composer_page": {
            "title": "Muziekcomponist — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, Spaanse muziekcomponist voor audiovisuele producties. Originele muziek vanuit Spanje.",
            "content": """
                <p>Naast zijn carrière als Spaanse stemacteur is Guillermo componist van originele muziek voor audiovisuele producties. Zijn dubbele talent als Spaanse stem en componist biedt complete audiooplossingen.</p>
                <p>Zijn composities variëren van filmmuziek tot muziek voor Spaanse reclamefilms. Elke compositie is ontworpen voor audiovisuele productie.</p>
                <p>Guillermo werkt vanuit zijn studio in Spanje en combineert Castiliaans Spaanse stem met muziekproductie.</p>
            """
        },
        "contact_page": {
            "title": "Contact — Spaanse Stemacteur Guillermo A. Brazález",
            "meta_desc": "Neem contact op met Guillermo A. Brazález, professionele Spaanse stemacteur. WhatsApp, e-mail en telefoon voor Spaanse voice-over projecten.",
            "content": """
                <p>Op zoek naar een professionele Spaanse stem voor uw volgende project? Guillermo is beschikbaar voor opnames in Castiliaans Spaans vanuit zijn studio in Spanje. Of u nu een Spaanse stem nodig heeft voor reclame, documentaire of bedrijfsvideo — Guillermo levert de kwaliteit die uw project verdient.</p>
                <p>Neem contact met hem op via WhatsApp, e-mail of telefoon. Guillermo antwoordt persoonlijk op elke vraag over Spaanse voice-over.</p>
            """,
            "form_name": "Naam",
            "form_email": "E-mail",
            "form_message": "Bericht",
            "form_send": "Bericht Versturen",
            "form_subject": "Onderwerp",
        }
    },
    "el": {
        "site_title": "Guillermo A. Brazález — Επαγγελματίας Ισπανός Εκφωνητής",
        "hero_tagline": "Η Φωνή Κινεί τον Κόσμο",
        "hero_subtitle": "Επαγγελματίας ισπανός εκφωνητής · Καστιλιάνικη ισπανική φωνή με πάνω από 20 χρόνια εμπειρίας",
        "hero_badge": "Η ισπανική φωνή των διαφημίσεων της Trivago",
        "homepage_intro": """
            <p>Ο Guillermo A. Brazález είναι ένας επαγγελματίας ισπανός εκφωνητής με έδρα την Ισπανία, ειδικευμένος σε πρώτης ποιότητας καστιλιάνικα ισπανικά. Με πάνω από δύο δεκαετίες εμπειρίας στον κλάδο της εκφώνησης, ο Guillermo έχει δανείσει την αυθεντική ισπανική του φωνή σε εκατοντάδες διεθνή projects για τα πιο αναγνωρισμένα brands παγκοσμίως.</p>
            <p>Η ισπανική του φωνή ξεχωρίζει για τη ζεστασιά, την εξουσία και την ευελιξία της. Από τηλεοπτικά διαφημιστικά σποτ μέχρι ντοκιμαντέρ φύσης, εταιρικά βίντεο, ραδιοφωνικά σποτ και ηχητικά βιβλία — η καστιλιάνικη ισπανική φωνή του φτάνει σε ισπανόφωνο κοινό σε ολόκληρο τον κόσμο. Έχει συνεργαστεί με εταιρείες παραγωγής στην Ισπανία και τη Λατινική Αμερική.</p>
            <p>Ως γηγενής ισπανός εκφωνητής από την Ισπανία, ο Guillermo εργάζεται από το δικό του επαγγελματικό στούντιο εξοπλισμένο με τεχνολογία αιχμής. Τα καστιλιάνικα ισπανικά του είναι η προτιμώμενη επιλογή διεθνών brands όπως το Netflix, το Discovery Channel και το National Geographic.</p>
            <p>Αναζητάτε μια επαγγελματική ισπανική φωνή για το επόμενο project σας; Ο Guillermo προσφέρει απομακρυσμένες συνεδρίες σε πραγματικό χρόνο, εγγραφή στο στούντιό του στην Ισπανία και εξατομικευμένη προσοχή που εγγυάται εξαιρετικά αποτελέσματα.</p>
        """,
        "services_heading": "Υπηρεσίες Εκφώνησης στα Ισπανικά",
        "services": {
            "spots": {"title": "Διαφημιστικά Σποτ", "desc": "Επαγγελματική ισπανική εκφώνηση για τηλεοπτικές καμπάνιες και ψηφιακή διαφήμιση.", "icon": "📺"},
            "documentaries": {"title": "Ντοκιμαντέρ", "desc": "Αφηγηματική φωνή σε καστιλιάνικα ισπανικά για ντοκιμαντέρ φύσης, ιστορίας και επιστήμης.", "icon": "🎬"},
            "radio": {"title": "Ραδιόφωνο", "desc": "Επαγγελματική ισπανική φωνή για ραδιοφωνικά σποτ, jingles και προγράμματα.", "icon": "📻"},
            "corporate": {"title": "Εταιρικό Βίντεο", "desc": "Ισπανική εταιρική φωνή για παρουσιάσεις, εκπαίδευση και εσωτερική επικοινωνία.", "icon": "🏢"},
            "audiobooks": {"title": "Ακουστικά Βιβλία", "desc": "Αφήγηση ηχητικών βιβλίων σε καστιλιάνικα ισπανικά με τέλεια εκφορά.", "icon": "📚"},
            "studio": {"title": "Στούντιο", "desc": "Επαγγελματικό στούντιο εγγραφής στην Ισπανία με Source-Connect και ISDN.", "icon": "🎙️"},
        },
        "composer_title": "Συνθέτης",
        "composer_text": """
            <p>Εκτός από τη δουλειά του ως ισπανός εκφωνητής, ο Guillermo A. Brazález είναι συνθέτης πρωτότυπης μουσικής. Δημιουργεί μουσική επένδυση και συνθέσεις για οπτικοακουστικές παραγωγές που συμπληρώνουν την ισπανική εκφωνητική του εργασία.</p>
            <p>Οι συνθέσεις του εκτείνονται από ambient μουσική για ντοκιμαντέρ μέχρι πρωτότυπα κομμάτια για ισπανικά διαφημιστικά. Ο συνδυασμός του ταλέντου του ως ισπανική φωνή και συνθέτης τον καθιστά μοναδικό.</p>
        """,
        "contact_title": "Επικοινωνία",
        "contact_text": "Χρειάζεστε μια επαγγελματική ισπανική φωνή; Επικοινωνήστε με τον Guillermo για να συζητήσετε το ισπανικό voice-over project σας.",
        "nav": {"voice_actor": "Εκφωνητής", "composer": "Συνθέτης", "contact": "Επικοινωνία"},
        "footer_text": "Επαγγελματίας ισπανός εκφωνητής · Καστιλιάνικη ισπανική φωνή από την Ισπανία",
        "cta_contact": "Επικοινωνία",
        "cta_listen": "Ακούστε Demo",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "Επαγγελματίας Ισπανός Εκφωνητής",
            "meta_desc": "Guillermo A. Brazález, επαγγελματίας ισπανός εκφωνητής με καστιλιάνικη φωνή. Πάνω από 20 χρόνια εμπειρίας σε διαφημιστικά, ντοκιμαντέρ και εταιρικό βίντεο στα ισπανικά.",
            "content": """
                <p>Ο Guillermo A. Brazález είναι ένας από τους πιο αναγνωρισμένους επαγγελματίες ισπανούς εκφωνητές της Ισπανίας. Η καστιλιάνικη ισπανική φωνή του έχει δώσει ζωή σε εκατοντάδες οπτικοακουστικές παραγωγές.</p>
                <p>Ως επαγγελματίας ισπανικής φωνής με πάνω από 20 χρόνια εμπειρίας, ο Guillermo κατέχει όλα τα φωνητικά μητρώα. Τα ισπανικά του είναι συνώνυμο επαγγελματισμού και άψογης εκφοράς.</p>
                <p>Εργάζεται από το επαγγελματικό του στούντιο στην Ισπανία, εξοπλισμένο με Source-Connect για ισπανικές απομακρυσμένες συνεδρίες σε πραγματικό χρόνο.</p>
            """
        },
        "spots_page": {
            "title": "Ισπανική Εκφώνηση για Διαφημιστικά Σποτ",
            "meta_desc": "Ισπανός εκφωνητής για τηλεοπτική διαφήμιση. Επαγγελματική καστιλιάνικη ισπανική φωνή για διεθνείς καμπάνιες.",
            "content": """
                <p>Η εκφώνηση διαφημιστικών σποτ στα ισπανικά είναι μία από τις ειδικότητες του Guillermo. Η καστιλιάνικη ισπανική φωνή του έχει επιλεγεί από κορυφαία διεθνή brands για καμπάνιες στην ισπανική και λατινοαμερικανική αγορά.</p>
                <p>Ένα πετυχημένο διαφημιστικό στα ισπανικά απαιτεί μια φωνή που εκπέμπει εμπιστοσύνη και επαγγελματισμό. Ο Guillermo προσφέρει ακριβώς αυτό: μια ευέλικτη ισπανική φωνή από την Ισπανία.</p>
                <p>Ανάμεσα στους διαφημιστικούς πελάτες του βρίσκονται brands όπως η BMW και η Samsung που εμπιστεύονται την καστιλιάνικη ισπανική φωνή του.</p>
            """
        },
        "documentaries_page": {
            "title": "Αφήγηση Ντοκιμαντέρ στα Ισπανικά",
            "meta_desc": "Ισπανός αφηγητής ντοκιμαντέρ. Καστιλιάνικη ισπανική φωνή για ντοκιμαντέρ φύσης, ιστορίας και επιστήμης.",
            "content": """
                <p>Η αφήγηση ντοκιμαντέρ σε καστιλιάνικα ισπανικά είναι ένας τομέας όπου ο Guillermo πραγματικά ξεχωρίζει. Η ζεστή ισπανική φωνή του οδηγεί τον θεατή μέσα από συναρπαστικές ιστορίες.</p>
                <p>Έχει δανείσει την ισπανική φωνή του σε ντοκιμαντέρ για το Netflix, το Discovery Channel και το National Geographic. Τα καστιλιάνικα ισπανικά του προσφέρουν εξαιρετική αφηγηματική ποιότητα από την Ισπανία.</p>
                <p>Με πάνω από 20 χρόνια εμπειρίας ως ισπανός αφηγητής, ο Guillermo κατέχει κάθε απόχρωση για αξέχαστες οπτικοακουστικές εμπειρίες.</p>
            """
        },
        "radio_page": {
            "title": "Ισπανική Ραδιοφωνική Φωνή",
            "meta_desc": "Επαγγελματίας ισπανός εκφωνητής ραδιοφώνου. Ραδιοφωνικά σποτ και προγράμματα σε καστιλιάνικα ισπανικά.",
            "content": """
                <p>Το ραδιόφωνο στα ισπανικά παραμένει ένα από τα πιο δυνατά μέσα. Ο Guillermo συνεισφέρει την επαγγελματική του καστιλιάνικη ισπανική φωνή σε ραδιοφωνικά σποτ, jingles και προγράμματα.</p>
                <p>Ως ισπανός φωνητικός επαγγελματίας κατέχει τους ειδικούς ρυθμούς του ραδιοφωνικού μέσου. Τα καστιλιάνικα ισπανικά του προσαρμόζονται φυσικά σε κάθε ραδιοφωνικό format.</p>
                <p>Συνεργάζεται με ραδιοφωνικούς σταθμούς στην Ισπανία και τη Λατινική Αμερική, παρέχοντας εγγραφές στα ισπανικά υψηλής ποιότητας.</p>
            """
        },
        "corporate_page": {
            "title": "Ισπανική Εταιρική Φωνή",
            "meta_desc": "Ισπανός εκφωνητής για εταιρικό βίντεο. Καστιλιάνικη ισπανική φωνή για παρουσιάσεις και εταιρική επικοινωνία.",
            "content": """
                <p>Το εταιρικό βίντεο στα ισπανικά απαιτεί μια φωνή που εκπέμπει επαγγελματισμό και αξιοπιστία. Ο Guillermo προσφέρει την καστιλιάνικη ισπανική φωνή του για παρουσιάσεις και εταιρική επικοινωνία.</p>
                <p>Πολυεθνικές εταιρείες εμπιστεύονται την ισπανική φωνή του για επικοινωνία σε καστιλιάνικα ισπανικά. Τα ισπανικά του από την Ισπανία αποτελούν την τέλεια επιλογή.</p>
                <p>Κάθε ισπανικό εταιρικό project λαμβάνει εξατομικευμένη προσοχή από το στούντιό του στην Ισπανία.</p>
            """
        },
        "audiobooks_page": {
            "title": "Ακουστικά Βιβλία στα Ισπανικά",
            "meta_desc": "Ισπανός αφηγητής ακουστικών βιβλίων. Καστιλιάνικη ισπανική φωνή για μυθιστορηματικά και μη μυθιστορηματικά ακουστικά βιβλία.",
            "content": """
                <p>Η αφήγηση ακουστικών βιβλίων σε καστιλιάνικα ισπανικά είναι μια τέχνη που απαιτεί ευελιξία και τέλεια εκφορά. Ο Guillermo είναι ένας έμπειρος ισπανός αφηγητής που δανείζει τη ζεστή καστιλιάνικη φωνή του σε κάθε ακουστικό βιβλίο.</p>
                <p>Ένα καλό ακουστικό βιβλίο στα ισπανικά χρειάζεται αφηγητή που κρατά την προσοχή για ώρες. Ο Guillermo κατέχει αυτές τις αποχρώσεις.</p>
                <p>Το στούντιό του στην Ισπανία είναι ακουστικά επεξεργασμένο για μεγάλες συνεδρίες εγγραφής στα ισπανικά.</p>
            """
        },
        "studio_page": {
            "title": "Επαγγελματικό Στούντιο Εγγραφής στην Ισπανία",
            "meta_desc": "Επαγγελματικό στούντιο εγγραφής φωνής στην Ισπανία. Source-Connect και ISDN για ισπανικές voice-over απομακρυσμένες συνεδρίες.",
            "content": """
                <p>Το στούντιο εγγραφής του Guillermo βρίσκεται στην Ισπανία και είναι εξοπλισμένο με επαγγελματικό εξοπλισμό για ισπανικές voice-over παραγωγές υψηλότατης ποιότητας.</p>
                <p>Το στούντιο στην Ισπανία διαθέτει μικρόφωνα υψηλής ποιότητας και Source-Connect για ισπανικές συνεδρίες σε πραγματικό χρόνο με πελάτες παγκοσμίως.</p>
                <p>Η τοποθεσία στην Ισπανία επιτρέπει ωράρια εργασίας συμβατά με Ευρώπη, Αμερική και Ασία.</p>
            """
        },
        "composer_page": {
            "title": "Μουσικός Συνθέτης — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, ισπανός μουσικός συνθέτης για οπτικοακουστικές παραγωγές. Πρωτότυπη μουσική από την Ισπανία.",
            "content": """
                <p>Πέρα από την καριέρα του ως ισπανός εκφωνητής, ο Guillermo είναι συνθέτης πρωτότυπης μουσικής για οπτικοακουστικές παραγωγές. Το διπλό ταλέντο του ως ισπανική φωνή και συνθέτης προσφέρει ολοκληρωμένες ηχητικές λύσεις.</p>
                <p>Οι συνθέσεις του εκτείνονται από μουσική κινηματογράφου μέχρι μουσική για ισπανικά διαφημιστικά. Κάθε σύνθεση σχεδιάζεται για οπτικοακουστική παραγωγή.</p>
                <p>Ο Guillermo εργάζεται από το στούντιό του στην Ισπανία, συνδυάζοντας καστιλιάνικη ισπανική φωνή με μουσική παραγωγή.</p>
            """
        },
        "contact_page": {
            "title": "Επικοινωνία — Ισπανός Εκφωνητής Guillermo A. Brazález",
            "meta_desc": "Επικοινωνήστε με τον Guillermo A. Brazález, επαγγελματία ισπανό εκφωνητή. WhatsApp, email και τηλέφωνο για ισπανικά voice-over projects.",
            "content": """
                <p>Αναζητάτε μια επαγγελματική ισπανική φωνή για το επόμενο project σας; Ο Guillermo είναι διαθέσιμος για εγγραφές σε καστιλιάνικα ισπανικά από το στούντιό του στην Ισπανία. Είτε χρειάζεστε ισπανική φωνή για διαφήμιση, ντοκιμαντέρ ή εταιρικό βίντεο, ο Guillermo παρέχει την ποιότητα που το ισπανικό project σας αξίζει.</p>
                <p>Επικοινωνήστε μαζί του μέσω WhatsApp, email ή τηλεφώνου. Ο Guillermo απαντά προσωπικά σε κάθε αίτημα για ισπανική εκφώνηση.</p>
            """,
            "form_name": "Όνομα",
            "form_email": "Email",
            "form_message": "Μήνυμα",
            "form_send": "Αποστολή Μηνύματος",
            "form_subject": "Θέμα",
        }
    },
    "zh": {
        "site_title": "Guillermo A. Brazález — 专业西班牙语配音演员",
        "hero_tagline": "声音撼动世界",
        "hero_subtitle": "专业西班牙语配音演员 · 卡斯蒂利亚西班牙语配音，超过20年从业经验",
        "hero_badge": "Trivago广告的西班牙语配音",
        "homepage_intro": """
            <p>Guillermo A. Brazález是一位驻西班牙的专业西班牙语配音演员，专注于一流的卡斯蒂利亚西班牙语配音。凭借超过二十年的配音行业经验，Guillermo已将其正宗的西班牙语声音献给了数百个国际项目，服务于全球最知名的品牌。</p>
            <p>他的西班牙语声音以温暖、权威和多功能性著称。从电视广告到自然纪录片，从企业视频到广播广告和有声书——他的卡斯蒂利亚西班牙语声音触达全球西班牙语受众。他曾与西班牙和拉丁美洲的制作公司合作，始终提供无可挑剔的西班牙语发音标准。</p>
            <p>作为来自西班牙的母语西班牙语配音演员，Guillermo在自己配备尖端技术的专业录音棚工作，能够以最快的交付时间提供最高质量的西班牙语录音。他的卡斯蒂利亚西班牙语是Netflix、Discovery Channel和National Geographic等国际品牌的首选。</p>
            <p>正在为下一个项目寻找专业西班牙语配音？Guillermo提供实时远程录音、西班牙录音棚录制以及个性化服务，确保每个西班牙语配音项目都能获得卓越的成果。</p>
        """,
        "services_heading": "西班牙语配音服务",
        "services": {
            "spots": {"title": "广告配音", "desc": "为电视广告和数字营销提供专业西班牙语配音服务。", "icon": "📺"},
            "documentaries": {"title": "纪录片", "desc": "为自然、历史和科学纪录片提供卡斯蒂利亚西班牙语旁白。", "icon": "🎬"},
            "radio": {"title": "广播", "desc": "为广播广告、jingle和节目提供专业西班牙语配音。", "icon": "📻"},
            "corporate": {"title": "企业视频", "desc": "为演示文稿、培训和内部沟通提供西班牙语企业配音。", "icon": "🏢"},
            "audiobooks": {"title": "有声书", "desc": "以完美的发音提供卡斯蒂利亚西班牙语有声书朗读。", "icon": "📚"},
            "studio": {"title": "录音棚", "desc": "位于西班牙的专业录音棚，配备Source-Connect和ISDN。", "icon": "🎙️"},
        },
        "composer_title": "作曲家",
        "composer_text": """
            <p>除了西班牙语配音工作外，Guillermo A. Brazález还是一位原创音乐作曲家。他为视听作品创作电影配乐和音乐作品，以定制音乐补充其西班牙语配音工作，提升每部作品的品质。</p>
            <p>他的作品范围从纪录片的氛围音乐到西班牙语广告的原创主题曲。他作为西班牙语配音演员和作曲家的双重才华使他独一无二。</p>
        """,
        "contact_title": "联系我们",
        "contact_text": "需要专业西班牙语配音？联系Guillermo讨论您的西班牙语配音项目。",
        "nav": {"voice_actor": "配音演员", "composer": "作曲家", "contact": "联系"},
        "footer_text": "专业西班牙语配音演员 · 来自西班牙的卡斯蒂利亚西班牙语",
        "cta_contact": "联系我们",
        "cta_listen": "试听Demo",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "专业西班牙语配音演员",
            "meta_desc": "Guillermo A. Brazález，专业西班牙语配音演员，拥有卡斯蒂利亚发音。超过20年广告、纪录片和企业视频西班牙语配音经验。",
            "content": """
                <p>Guillermo A. Brazález是西班牙最受认可的专业西班牙语配音演员之一。他的卡斯蒂利亚西班牙语声音已为数百部视听作品注入生命力，从大型广告活动到国际纪录片。</p>
                <p>作为拥有20多年经验的西班牙语配音专业人士，Guillermo精通所有声音风格。他的西班牙语是专业性和完美发音的代名词，能够触达全球西班牙语受众。</p>
                <p>他在位于西班牙的专业录音棚工作，配备Source-Connect用于西班牙语实时远程录音。</p>
            """
        },
        "spots_page": {
            "title": "西班牙语广告配音",
            "meta_desc": "西班牙语电视广告配音演员。为国际品牌活动提供专业卡斯蒂利亚西班牙语配音。",
            "content": """
                <p>西班牙语广告配音是Guillermo的专长之一。他的卡斯蒂利亚西班牙语声音被全球领先品牌选用，用于面向西班牙和拉丁美洲市场的广告活动。</p>
                <p>成功的西班牙语广告需要一个传达信任和专业性的声音。Guillermo提供的正是如此：一个来自西班牙的多功能西班牙语声音。</p>
                <p>他的广告客户包括BMW和三星等品牌，它们信赖他的卡斯蒂利亚西班牙语配音。</p>
            """
        },
        "documentaries_page": {
            "title": "西班牙语纪录片旁白",
            "meta_desc": "西班牙语纪录片旁白演员。为自然、历史和科学纪录片提供卡斯蒂利亚西班牙语配音。",
            "content": """
                <p>卡斯蒂利亚西班牙语纪录片旁白是Guillermo真正出色的领域。他温暖的西班牙语声音引领观众穿越引人入胜的故事。</p>
                <p>他曾为Netflix、Discovery Channel和National Geographic的纪录片提供西班牙语配音。他的卡斯蒂利亚西班牙语从西班牙带来了卓越的叙事品质。</p>
                <p>凭借20多年作为西班牙语旁白演员的经验，Guillermo精通每一个细微差别，创造难忘的视听体验。</p>
            """
        },
        "radio_page": {
            "title": "西班牙语广播配音",
            "meta_desc": "专业西班牙语广播配音演员。卡斯蒂利亚西班牙语广播广告和节目。",
            "content": """
                <p>西班牙语广播仍然是触达西班牙语受众最有力的媒体之一。Guillermo以其专业的卡斯蒂利亚西班牙语声音为广播广告、jingle和节目贡献力量。</p>
                <p>作为西班牙语配音专业人士，他精通广播媒体的特定节奏。他的卡斯蒂利亚西班牙语自然适应各种广播格式。</p>
                <p>他与西班牙和拉丁美洲的广播电台合作，提供高质量的西班牙语录音。</p>
            """
        },
        "corporate_page": {
            "title": "西班牙语企业配音",
            "meta_desc": "西班牙语企业视频配音演员。为演示文稿和企业沟通提供卡斯蒂利亚西班牙语配音。",
            "content": """
                <p>西班牙语企业视频需要一个传达专业性和可信度的声音。Guillermo为演示文稿和企业沟通提供他的卡斯蒂利亚西班牙语配音。</p>
                <p>跨国公司信赖他的西班牙语声音用于卡斯蒂利亚西班牙语企业沟通。来自西班牙的他的西班牙语是在西班牙语市场树立专业形象的完美选择。</p>
                <p>每个西班牙语企业项目都会从他在西班牙的录音棚获得个性化关注。</p>
            """
        },
        "audiobooks_page": {
            "title": "西班牙语有声书",
            "meta_desc": "西班牙语有声书朗读者。为虚构和非虚构有声书提供卡斯蒂利亚西班牙语配音。",
            "content": """
                <p>卡斯蒂利亚西班牙语有声书朗读是一门需要多功能性和完美发音的艺术。Guillermo是一位经验丰富的西班牙语朗读者，为每本有声书贡献他温暖的卡斯蒂利亚声音。</p>
                <p>一本好的西班牙语有声书需要一位能够数小时保持听众注意力的朗读者。作为专业的西班牙语朗读者，Guillermo精通这些细微差别。</p>
                <p>他在西班牙的录音棚经过声学处理，适合长时间的西班牙语录音。</p>
            """
        },
        "studio_page": {
            "title": "西班牙专业录音棚",
            "meta_desc": "位于西班牙的专业录音棚。配备Source-Connect和ISDN，支持西班牙语配音远程录制。",
            "content": """
                <p>Guillermo的录音棚位于西班牙，配备专业设备，可提供最高质量的西班牙语配音制作。</p>
                <p>西班牙录音棚配备高端麦克风和Source-Connect，可与全球客户进行西班牙语实时远程录音。</p>
                <p>位于西班牙的地理位置使工作时间与欧洲、美洲和亚洲兼容，可按最高技术标准制作卡斯蒂利亚西班牙语作品。</p>
            """
        },
        "composer_page": {
            "title": "音乐作曲家 — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález，西班牙音乐作曲家，为视听作品创作原创音乐。来自西班牙的原创配乐。",
            "content": """
                <p>除了西班牙语配音事业外，Guillermo还是视听作品的原创音乐作曲家。他作为西班牙语配音演员和作曲家的双重才华提供完整的音频解决方案。</p>
                <p>他的作品从电影配乐到西班牙语广告音乐不等。每首作品都专为视听制作而设计。</p>
                <p>Guillermo在西班牙的录音棚工作，将卡斯蒂利亚西班牙语配音与音乐制作相结合。</p>
            """
        },
        "contact_page": {
            "title": "联系 — 西班牙语配音演员 Guillermo A. Brazález",
            "meta_desc": "联系Guillermo A. Brazález，专业西班牙语配音演员。WhatsApp、邮件和电话咨询西班牙语配音项目。",
            "content": """
                <p>正在为您的下一个项目寻找专业西班牙语配音？Guillermo可以在西班牙的录音棚提供卡斯蒂利亚西班牙语录音服务。无论您需要广告、纪录片还是企业视频的西班牙语配音，Guillermo都能提供您的项目所需的品质。</p>
                <p>通过WhatsApp、邮件或电话联系他。Guillermo会亲自回复每一个关于西班牙语配音的咨询。</p>
            """,
            "form_name": "姓名",
            "form_email": "邮箱",
            "form_message": "留言",
            "form_send": "发送留言",
            "form_subject": "主题",
        }
    },
    "ru": {
        "site_title": "Guillermo A. Brazález — Профессиональный Испанский Диктор",
        "hero_tagline": "Голос Движет Миром",
        "hero_subtitle": "Профессиональный испанский диктор · Кастильский испанский голос с более чем 20-летним опытом",
        "hero_badge": "Испанский голос рекламных роликов Trivago",
        "homepage_intro": """
            <p>Guillermo A. Brazález — профессиональный испанский диктор, базирующийся в Испании, специализирующийся на первоклассном кастильском испанском. С более чем двадцатилетним опытом в индустрии озвучивания, Guillermo предоставил свой аутентичный испанский голос для сотен международных проектов крупнейших мировых брендов.</p>
            <p>Его испанский голос выделяется теплотой, авторитетностью и универсальностью. От телевизионной рекламы до документальных фильмов о природе, корпоративных видео, радиороликов и аудиокниг — его кастильский испанский голос достигает испаноязычной аудитории по всему миру. Он сотрудничал с продюсерскими компаниями Испании и Латинской Америки.</p>
            <p>Как носитель испанского языка из Испании, Guillermo работает в собственной профессиональной студии, оснащённой передовыми технологиями. Его кастильский испанский — предпочтительный выбор международных брендов, таких как Netflix, Discovery Channel и National Geographic.</p>
            <p>Ищете профессиональный испанский голос для следующего проекта? Guillermo предлагает удалённые сессии в реальном времени, запись в своей студии в Испании и персональный подход, гарантирующий исключительные результаты.</p>
        """,
        "services_heading": "Услуги Озвучивания на Испанском",
        "services": {
            "spots": {"title": "Рекламные Ролики", "desc": "Профессиональная испанская озвучка для ТВ-кампаний и цифровой рекламы.", "icon": "📺"},
            "documentaries": {"title": "Документальные Фильмы", "desc": "Закадровый голос на кастильском испанском для документальных фильмов о природе, истории и науке.", "icon": "🎬"},
            "radio": {"title": "Радио", "desc": "Профессиональный испанский голос для радиороликов, джинглов и программ.", "icon": "📻"},
            "corporate": {"title": "Корпоративное Видео", "desc": "Испанский корпоративный голос для презентаций, обучения и внутренних коммуникаций.", "icon": "🏢"},
            "audiobooks": {"title": "Аудиокниги", "desc": "Озвучивание аудиокниг на кастильском испанском с идеальной дикцией.", "icon": "📚"},
            "studio": {"title": "Студия", "desc": "Профессиональная студия звукозаписи в Испании с Source-Connect и ISDN.", "icon": "🎙️"},
        },
        "composer_title": "Композитор",
        "composer_text": """
            <p>Помимо работы испанским диктором, Guillermo A. Brazález является композитором оригинальной музыки. Он создаёт саундтреки и музыкальные композиции для аудиовизуальных проектов, дополняя свою работу по испанскому озвучиванию индивидуальной музыкой.</p>
            <p>Его композиции варьируются от эмбиентной музыки для документальных фильмов до оригинальных тем для испанских рекламных роликов. Сочетание таланта испанского диктора и композитора делает его уникальным.</p>
        """,
        "contact_title": "Контакт",
        "contact_text": "Нужен профессиональный испанский голос? Свяжитесь с Guillermo для обсуждения вашего проекта озвучивания на испанском.",
        "nav": {"voice_actor": "Диктор", "composer": "Композитор", "contact": "Контакт"},
        "footer_text": "Профессиональный испанский диктор · Кастильский испанский голос из Испании",
        "cta_contact": "Связаться",
        "cta_listen": "Послушать Демо",
        "cta_whatsapp": "WhatsApp",
        "voice_actor_page": {
            "title": "Профессиональный Испанский Диктор",
            "meta_desc": "Guillermo A. Brazález, профессиональный испанский диктор с кастильским голосом. Более 20 лет опыта в рекламе, документальных фильмах и корпоративном видео на испанском.",
            "content": """
                <p>Guillermo A. Brazález — один из самых признанных профессиональных испанских дикторов Испании. Его кастильский испанский голос оживил сотни аудиовизуальных продукций, от крупных рекламных кампаний до международных документальных фильмов.</p>
                <p>Как профессионал испанского озвучивания с более чем 20-летним опытом, Guillermo владеет всеми голосовыми регистрами. Его испанский — синоним профессионализма и безупречной дикции, которая достигает испаноязычной аудитории по всему миру.</p>
                <p>Он работает из своей профессиональной студии в Испании, оснащённой Source-Connect для испанских удалённых сессий в реальном времени.</p>
            """
        },
        "spots_page": {
            "title": "Испанская Озвучка Рекламных Роликов",
            "meta_desc": "Испанский диктор для ТВ-рекламы. Профессиональный кастильский испанский голос для международных рекламных кампаний.",
            "content": """
                <p>Озвучка рекламных роликов на испанском — одна из специализаций Guillermo. Его кастильский испанский голос выбран ведущими международными брендами для кампаний, ориентированных на испанский и латиноамериканский рынок.</p>
                <p>Успешный рекламный ролик на испанском требует голоса, внушающего доверие и профессионализм. Guillermo предлагает именно это: универсальный испанский голос из Испании.</p>
                <p>Среди его рекламных клиентов — бренды BMW и Samsung, доверяющие его кастильскому испанскому голосу.</p>
            """
        },
        "documentaries_page": {
            "title": "Озвучивание Документальных Фильмов на Испанском",
            "meta_desc": "Испанский рассказчик документальных фильмов. Кастильский испанский голос для документальных фильмов о природе, истории и науке.",
            "content": """
                <p>Озвучивание документальных фильмов на кастильском испанском — область, в которой Guillermo действительно выделяется. Его тёплый испанский голос ведёт зрителя через захватывающие истории.</p>
                <p>Он озвучивал документальные фильмы для Netflix, Discovery Channel и National Geographic. Его кастильский испанский привносит исключительное качество повествования из Испании.</p>
                <p>С более чем 20-летним опытом испанского рассказчика, Guillermo владеет каждым нюансом для незабываемых аудиовизуальных впечатлений.</p>
            """
        },
        "radio_page": {
            "title": "Испанский Голос для Радио",
            "meta_desc": "Профессиональный испанский диктор для радио. Радиоролики и программы на кастильском испанском.",
            "content": """
                <p>Радио на испанском остаётся одним из самых мощных медиа. Guillermo предоставляет свой профессиональный кастильский испанский голос для радиороликов, джинглов и программ.</p>
                <p>Как профессионал испанского озвучивания, он владеет специфическими ритмами радио. Его кастильский испанский естественно адаптируется к любому радиоформату.</p>
                <p>Он сотрудничает с радиостанциями Испании и Латинской Америки, обеспечивая высококачественные записи на испанском.</p>
            """
        },
        "corporate_page": {
            "title": "Испанский Корпоративный Голос",
            "meta_desc": "Испанский диктор для корпоративного видео. Кастильский испанский голос для презентаций и корпоративных коммуникаций.",
            "content": """
                <p>Корпоративное видео на испанском требует голоса, передающего профессионализм и доверие. Guillermo предлагает свой кастильский испанский голос для презентаций и корпоративных коммуникаций.</p>
                <p>Международные компании доверяют его испанскому голосу для коммуникаций на кастильском испанском. Его испанский из Испании — идеальный выбор для профессионального имиджа.</p>
                <p>Каждый испанский корпоративный проект получает персональное внимание из его студии в Испании.</p>
            """
        },
        "audiobooks_page": {
            "title": "Аудиокниги на Испанском",
            "meta_desc": "Испанский чтец аудиокниг. Кастильский испанский голос для художественных и научно-популярных аудиокниг.",
            "content": """
                <p>Озвучивание аудиокниг на кастильском испанском — искусство, требующее универсальности и совершенной дикции. Guillermo — опытный испанский чтец, привносящий свой тёплый кастильский голос в каждую аудиокнигу.</p>
                <p>Хорошая аудиокнига на испанском нуждается в чтеце, способном удерживать внимание часами. Как профессиональный испанский чтец, Guillermo мастерски владеет этими нюансами.</p>
                <p>Его студия в Испании акустически обработана для длительных сессий записи на испанском.</p>
            """
        },
        "studio_page": {
            "title": "Профессиональная Студия Звукозаписи в Испании",
            "meta_desc": "Профессиональная студия звукозаписи в Испании. Source-Connect и ISDN для удалённых сессий испанского озвучивания.",
            "content": """
                <p>Студия звукозаписи Guillermo расположена в Испании и оснащена профессиональным оборудованием для производства испанского озвучивания высочайшего качества.</p>
                <p>Студия в Испании оборудована микрофонами высокого класса и Source-Connect для испанских сессий в реальном времени с клиентами по всему миру.</p>
                <p>Расположение в Испании позволяет работать в часовых поясах, совместимых с Европой, Америкой и Азией.</p>
            """
        },
        "composer_page": {
            "title": "Композитор — Guillermo A. Brazález",
            "meta_desc": "Guillermo A. Brazález, испанский композитор для аудиовизуальных продукций. Оригинальная музыка из Испании.",
            "content": """
                <p>Помимо карьеры испанского диктора, Guillermo — композитор оригинальной музыки для аудиовизуальных продукций. Его двойной талант испанского голоса и композитора обеспечивает комплексные аудиорешения.</p>
                <p>Его композиции варьируются от киномузыки до музыки для испанских рекламных роликов. Каждая композиция создана для аудиовизуального производства.</p>
                <p>Guillermo работает из своей студии в Испании, сочетая кастильский испанский голос с музыкальным производством.</p>
            """
        },
        "contact_page": {
            "title": "Контакт — Испанский Диктор Guillermo A. Brazález",
            "meta_desc": "Свяжитесь с Guillermo A. Brazález, профессиональным испанским диктором. WhatsApp, email и телефон для проектов озвучивания на испанском.",
            "content": """
                <p>Ищете профессиональный испанский голос для вашего следующего проекта? Guillermo доступен для записи на кастильском испанском из своей студии в Испании. Будь то реклама, документальный фильм или корпоративное видео — Guillermo обеспечит качество, которого заслуживает ваш проект на испанском.</p>
                <p>Свяжитесь с ним через WhatsApp, email или по телефону. Guillermo лично отвечает на каждый запрос об испанском озвучивании.</p>
            """,
            "form_name": "Имя",
            "form_email": "Email",
            "form_message": "Сообщение",
            "form_send": "Отправить Сообщение",
            "form_subject": "Тема",
        }
    },
}


# ─── SVG Logo ─────────────────────────────────────────────────────────────────

SVG_LOGO = '<img src="{asset_path}/logo-white.png" alt="Guillermo A. Brazález" class="logo-img" height="36">'

SVG_LOGO_SMALL = '<img src="{asset_path}/logo-white.png" alt="GAB" class="logo-img-small" height="28">'


# ─── Helper functions ─────────────────────────────────────────────────────────

def get_path_prefix(lang):
    """Get the URL path prefix for a language."""
    if lang == "es":
        return ""
    return f"/{LANGUAGES[lang]['dir']}"


def get_asset_prefix(lang, page_depth=0):
    """Get relative path to assets from a given page depth."""
    if page_depth == 0:
        return "assets"
    return "../" * page_depth + "assets"


def get_root_prefix(lang, page_depth=0):
    """Get relative path to root from a given page depth."""
    if page_depth == 0:
        return "."
    return "../" * page_depth


def get_page_url(lang, page_key=None, sub_key=None):
    """Get the canonical URL for a page."""
    if page_key is None:
        # Homepage
        if lang == "es":
            return f"{SITE_URL}/"
        return f"{SITE_URL}/{LANGUAGES[lang]['dir']}/"
    
    slug = SLUGS[lang]
    lang_prefix = LANGUAGES[lang]['dir']
    
    if lang == "es" and page_key in slug:
        base = f"{SITE_URL}/es/{slug[page_key]}/"
    elif lang != "es" and page_key in slug:
        base = f"{SITE_URL}/{lang_prefix}/{slug[page_key]}/"
    else:
        return f"{SITE_URL}/"
    
    if sub_key and sub_key in slug:
        return f"{base}{slug[sub_key]}/"
    return base


def get_relative_url(lang, page_key=None, sub_key=None, from_depth=0):
    """Get relative URL from current page to target."""
    root = get_root_prefix(lang, from_depth)
    if root.endswith("/"):
        root = root[:-1]
    if not root:
        root = "."
    
    if page_key is None:
        if lang == "es":
            return f"{root}/index.html"
        return f"{root}/{LANGUAGES[lang]['dir']}/index.html"
    
    slug = SLUGS[lang]
    lang_prefix = "es" if lang == "es" else LANGUAGES[lang]['dir']
    
    if sub_key and sub_key in slug:
        return f"{root}/{lang_prefix}/{slug[page_key]}/{slug[sub_key]}/index.html"
    return f"{root}/{lang_prefix}/{slug[page_key]}/index.html"


def hreflang_tags(page_key=None, sub_key=None):
    """Generate hreflang link tags for all languages."""
    tags = []
    for lang_code in LANGUAGES:
        url = get_page_url(lang_code, page_key, sub_key)
        # Use lang_code for hreflang (es, en, fr, etc.)
        hreflang_code = lang_code
        tags.append(f'  <link rel="alternate" hreflang="{hreflang_code}" href="{url}" />')
    # x-default points to Spanish
    url_default = get_page_url("es", page_key, sub_key)
    tags.append(f'  <link rel="alternate" hreflang="x-default" href="{url_default}" />')
    return "\n".join(tags)


def schema_person(lang):
    """Generate Person schema JSON-LD."""
    c = CONTENT[lang]
    job_titles = {
        "es": "Locutor Profesional Español",
        "en": "Professional Spanish Voice-Over Artist",
        "fr": "Comédien Vocal Espagnol Professionnel",
        "de": "Professioneller Spanischer Sprecher",
        "it": "Doppiatore Spagnolo Professionista",
        "pt": "Locutor Espanhol Profissional",
        "sv": "Professionell Spansk Röstskådespelare",
        "no": "Profesjonell Spansk Stemmeskuespiller",
        "da": "Professionel Spansk Stemmeskuespiller",
        "nl": "Professionele Spaanse Stemacteur",
        "el": "Επαγγελματίας Ισπανός Εκφωνητής",
        "zh": "专业西班牙语配音演员",
        "ru": "Профессиональный Испанский Диктор",
    }
    descriptions = {
        "es": "Guillermo A. Brazález es locutor profesional español, voz en español de los spots de Trivago. Más de 20 años de experiencia en locución en castellano.",
        "en": "Guillermo A. Brazález is a professional Spanish voice-over artist, the Spanish voice of Trivago commercials. 20+ years of experience in Castilian Spanish voice-over.",
        "fr": "Guillermo A. Brazález est comédien vocal espagnol professionnel, la voix espagnole des spots Trivago. Plus de 20 ans d'expérience.",
        "de": "Guillermo A. Brazález ist professioneller spanischer Sprecher, die spanische Stimme der Trivago-Werbespots. Über 20 Jahre Erfahrung.",
        "it": "Guillermo A. Brazález è doppiatore spagnolo professionista, la voce spagnola degli spot Trivago. Oltre 20 anni di esperienza.",
        "pt": "Guillermo A. Brazález é locutor espanhol profissional, a voz espanhola dos anúncios da Trivago. Mais de 20 anos de experiência.",
        "sv": "Guillermo A. Brazález är professionell spansk röstskådespelare, den spanska rösten i Trivagos reklamfilmer. Över 20 års erfarenhet.",
        "no": "Guillermo A. Brazález er profesjonell spansk stemmeskuespiller, den spanske stemmen i Trivagos reklamefilmer. Over 20 års erfaring.",
        "da": "Guillermo A. Brazález er professionel spansk stemmeskuespiller, den spanske stemme i Trivagos reklamefilm. Over 20 års erfaring.",
        "nl": "Guillermo A. Brazález is professionele Spaanse stemacteur, de Spaanse stem van de Trivago-reclames. Meer dan 20 jaar ervaring.",
        "el": "Ο Guillermo A. Brazález είναι επαγγελματίας ισπανός εκφωνητής, η ισπανική φωνή των διαφημίσεων της Trivago.",
        "zh": "Guillermo A. Brazález是专业西班牙语配音演员，Trivago广告的西班牙语配音。超过20年从业经验。",
        "ru": "Guillermo A. Brazález — профессиональный испанский диктор, испанский голос рекламных роликов Trivago. Более 20 лет опыта.",
    }
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Guillermo A. Brazález",
        "jobTitle": job_titles[lang],
        "description": descriptions[lang],
        "url": SITE_URL,
        "telephone": "+34606350350",
        "email": "info@guillermobrazalez.es",
        "address": {
            "@type": "PostalAddress",
            "addressCountry": "ES"
        },
        "knowsAbout": ["Voice-over", "Spanish voice acting", "Trivago commercials", "TV advertising", "Documentary narration"],
        "sameAs": [
            "https://wa.me/34606350350"
        ]
    }, ensure_ascii=False)


def schema_service(lang, service_name, description):
    """Generate ProfessionalService schema JSON-LD."""
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": service_name,
        "description": description,
        "provider": {
            "@type": "Person",
            "name": "Guillermo A. Brazález"
        },
        "areaServed": "Worldwide",
        "availableLanguage": "Spanish"
    }, ensure_ascii=False)



def schema_faq(lang, page_type):
    """Generate FAQPage schema JSON-LD."""
    faq_key = f"{page_type}_faq"
    if lang not in FAQ_CONTENT or faq_key not in FAQ_CONTENT[lang]:
        return None
    faqs = FAQ_CONTENT[lang][faq_key]
    if not faqs:
        return None
    entities = []
    for faq in faqs:
        entities.append({
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq["a"]
            }
        })
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }, ensure_ascii=False)


def schema_video_list(lang, service_key, page_title):
    """Generate VideoObject schema JSON-LD for pages with Vimeo embeds."""
    if service_key not in VIMEO:
        return None
    
    video_names = {
        "spots": {
            "es": "Demo Spot Publicitario",
            "en": "TV Commercial Demo",
            "fr": "Démo Spot Publicitaire",
            "de": "Werbespot-Demo",
            "it": "Demo Spot Pubblicitario",
            "pt": "Demo Spot Publicitário",
            "sv": "Reklamfilmsdemo",
            "no": "Reklamefilmdemo",
            "da": "Reklamefilmdemo",
            "nl": "Reclamespotdemo",
            "el": "Demo Διαφημιστικού Σποτ",
            "zh": "广告配音演示",
            "ru": "Демо Рекламного Ролика",
        },
        "documentaries": {
            "es": "Demo Documental",
            "en": "Documentary Demo",
            "fr": "Démo Documentaire",
            "de": "Dokumentarfilm-Demo",
            "it": "Demo Documentario",
            "pt": "Demo Documentário",
            "sv": "Dokumentärdemo",
            "no": "Dokumentardemo",
            "da": "Dokumentardemo",
            "nl": "Documentairedemo",
            "el": "Demo Ντοκιμαντέρ",
            "zh": "纪录片配音演示",
            "ru": "Демо Документального Фильма",
        },
        "corporate": {
            "es": "Demo Vídeo Corporativo",
            "en": "Corporate Video Demo",
            "fr": "Démo Vidéo Corporate",
            "de": "Unternehmensvideo-Demo",
            "it": "Demo Video Aziendale",
            "pt": "Demo Vídeo Corporativo",
            "sv": "Företagsfilmsdemo",
            "no": "Bedriftsfilmdemo",
            "da": "Virksomhedsfilmdemo",
            "nl": "Bedrijfsvideodemo",
            "el": "Demo Εταιρικού Βίντεο",
            "zh": "企业视频演示",
            "ru": "Демо Корпоративного Видео",
        },
    }
    
    videos = VIMEO[service_key]
    video_objects = []
    base_name = video_names.get(service_key, {}).get(lang, f"Demo {service_key}")
    
    for i, vid_id in enumerate(videos, 1):
        video_objects.append({
            "@type": "VideoObject",
            "name": f"{base_name} #{i} — Guillermo A. Brazález",
            "description": page_title,
            "thumbnailUrl": f"https://vumbnail.com/{vid_id}.jpg",
            "contentUrl": f"https://vimeo.com/{vid_id}",
            "embedUrl": f"https://player.vimeo.com/video/{vid_id}",
            "uploadDate": "2024-01-01",
            "publisher": {
                "@type": "Person",
                "name": "Guillermo A. Brazález",
                "url": "https://spanishvoiceover.net"
            }
        })
    
    return json.dumps({
        "@context": "https://schema.org",
        "@graph": video_objects
    }, ensure_ascii=False)


def schema_breadcrumb(lang, items):
    """Generate BreadcrumbList schema JSON-LD."""
    list_items = []
    for i, (name, url) in enumerate(items, 1):
        list_items.append({
            "@type": "ListItem",
            "position": i,
            "name": name,
            "item": url
        })
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": list_items
    }, ensure_ascii=False)


def vimeo_embed(video_id):
    """Generate responsive Vimeo embed."""
    return f'''<div class="video-embed">
      <iframe src="https://player.vimeo.com/video/{video_id}?badge=0&amp;autopause=0&amp;player_id=0" 
              frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen
              loading="lazy" title="Demo reel"></iframe>
    </div>'''


def whatsapp_button():
    """WhatsApp floating button HTML."""
    return '''<a href="https://wa.me/34606350350" class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">
    <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  </a>'''


def lang_switcher(current_lang, page_key=None, sub_key=None, from_depth=0):
    """Generate language switcher HTML."""
    root = get_root_prefix(current_lang, from_depth)
    if root.endswith("/"):
        root = root[:-1]
    if not root:
        root = "."
    
    items = []
    options = []
    for lang_code, lang_info in LANGUAGES.items():
        if page_key is None:
            # Homepage
            if lang_code == "es":
                href = f"{root}/index.html"
            else:
                href = f"{root}/{lang_info['dir']}/index.html"
        else:
            slug = SLUGS[lang_code]
            lang_prefix = "es" if lang_code == "es" else lang_info['dir']
            if sub_key and sub_key in slug:
                href = f"{root}/{lang_prefix}/{slug[page_key]}/{slug[sub_key]}/index.html"
            elif page_key in slug:
                href = f"{root}/{lang_prefix}/{slug[page_key]}/index.html"
            else:
                if lang_code == "es":
                    href = f"{root}/index.html"
                else:
                    href = f"{root}/{lang_info['dir']}/index.html"
        
        active = ' class="active"' if lang_code == current_lang else ''
        items.append(f'<a href="{href}"{active} hreflang="{lang_code}">{lang_code.upper()}</a>')
        selected = ' selected' if lang_code == current_lang else ''
        options.append(f'<option value="{href}"{selected}>{lang_code.upper()} — {lang_info["name"]}</option>')
    
    desktop = '<div class="lang-switcher">' + " ".join(items) + '</div>'
    mobile = '<select class="lang-select-mobile" onchange="if(this.value)window.location.href=this.value">' + "".join(options) + '</select>'
    return desktop + mobile


def nav_dropdown(lang, from_depth=0):
    """Generate the dropdown items for the voice actor nav."""
    c = CONTENT[lang]
    services = c["services"]
    root = get_root_prefix(lang, from_depth)
    if root.endswith("/"):
        root = root[:-1]
    if not root:
        root = "."
    
    slug = SLUGS[lang]
    lang_prefix = "es" if lang == "es" else LANGUAGES[lang]['dir']
    
    items = []
    for key in ["spots", "documentaries", "radio", "corporate", "audiobooks", "studio"]:
        href = f"{root}/{lang_prefix}/{slug['voice_actor']}/{slug[key]}/index.html"
        items.append(f'<a href="{href}">{services[key]["title"]}</a>')
    
    # Trivago dedicated page link
    trivago_href = f"{root}/{lang_prefix}/{slug['voice_actor']}/{slug['trivago']}/index.html"
    items.append(f'<a href="{trivago_href}">Trivago</a>')
    
    return "\n            ".join(items)


def build_header(lang, page_key=None, sub_key=None, from_depth=0):
    """Build the site header HTML."""
    c = CONTENT[lang]
    root = get_root_prefix(lang, from_depth)
    if root.endswith("/"):
        root = root[:-1]
    if not root:
        root = "."
    
    slug = SLUGS[lang]
    lang_prefix = "es" if lang == "es" else LANGUAGES[lang]['dir']
    
    if lang == "es":
        home_href = f"{root}/index.html"
    else:
        home_href = f"{root}/{LANGUAGES[lang]['dir']}/index.html"
    
    va_href = f"{root}/{lang_prefix}/{slug['voice_actor']}/index.html"
    comp_href = f"{root}/{lang_prefix}/{slug['composer']}/index.html"
    contact_href = f"{root}/{lang_prefix}/{slug['contact']}/index.html"
    
    logo_html = f'<img src="{root}/assets/logo-white.png" alt="Guillermo A. Brazález" class="logo-img" height="36">'
    logo_small_html = f'<img src="{root}/assets/logo-white.png" alt="GAB" class="logo-img-small" height="28">'
    
    return f'''<header class="site-header">
    <div class="header-inner">
      <a href="{home_href}" class="logo-link" aria-label="Home">
        {logo_html}
        {logo_small_html}
      </a>
      <nav class="main-nav" aria-label="Main navigation">
        <div class="nav-item has-dropdown">
          <a href="{va_href}" class="nav-parent">{c["nav"]["voice_actor"]}</a>
          <button class="dropdown-toggle" aria-label="Toggle submenu" aria-expanded="false">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M3 4.5L6 7.5L9 4.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
          <div class="dropdown">
            {nav_dropdown(lang, from_depth)}
          </div>
        </div>
        <a href="{comp_href}">{c["nav"]["composer"]}</a>
        <a href="{contact_href}" class="nav-cta">{c["nav"]["contact"]}</a>
      </nav>
      {lang_switcher(lang, page_key, sub_key, from_depth)}
      <button class="mobile-toggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>'''


def build_footer(lang, from_depth=0):
    """Build the site footer HTML."""
    c = CONTENT[lang]
    return f'''<footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <img src="/assets/logo-white.png" alt="Guillermo A. Brazález" class="logo-img" height="28" style="margin-bottom:0.75rem;opacity:0.7;">
        <p>{c["footer_text"]}</p>
      </div>
      <div class="footer-contact">
        <p><a href="mailto:info@guillermobrazalez.es">info@guillermobrazalez.es</a></p>
        <p><a href="tel:+34606350350">+34 606 350 350</a></p>
        <p><a href="https://wa.me/34606350350" target="_blank" rel="noopener noreferrer">{c["cta_whatsapp"]}</a></p>
      </div>
      <div class="footer-copy">
        <p>&copy; 2026 Guillermo A. Brazález</p>
      </div>
    </div>
  </footer>'''


def build_page(lang, title, meta_desc, canonical, body_content, page_key=None, sub_key=None, 
               from_depth=0, extra_schema=None):
    """Build a complete HTML page."""
    c = CONTENT[lang]
    locale = LANGUAGES[lang]['locale']
    lang_code = lang
    
    asset_prefix = get_asset_prefix(lang, from_depth)
    # Fix: asset prefix needs to be relative from the file location
    # For homepage (depth 0): assets/
    # For /es/locutor/ (depth 2): ../../assets/
    # etc.
    
    root = get_root_prefix(lang, from_depth)
    if root.endswith("/"):
        root = root[:-1]
    if not root:
        root = "."
    asset_path = f"{root}/assets"
    
    schema_json = schema_person(lang)
    schemas = f'<script type="application/ld+json">{schema_json}</script>'
    if extra_schema:
        if isinstance(extra_schema, list):
            for es in extra_schema:
                if es:
                    schemas += f'\n  <script type="application/ld+json">{es}</script>'
        elif extra_schema:
            schemas += f'\n  <script type="application/ld+json">{extra_schema}</script>'
    
    return f'''<!DOCTYPE html>
<html lang="{lang_code}" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="{canonical}" />
{hreflang_tags(page_key, sub_key)}
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{meta_desc}" />
  <meta property="og:locale" content="{locale}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:site_name" content="Guillermo A. Brazález" />
  <link rel="icon" type="image/png" href="{asset_path}/logo-white.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300..700;1,9..40,300..700&family=Instrument+Serif:ital@0;1&family=Noto+Sans+SC:wght@400;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{asset_path}/style.css" />
  {schemas}
</head>
<body>
  <!-- GSAP + Lenis -->
  <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/lenis@1/dist/lenis.min.js"></script>
  <div class="page-loader" id="pageLoader">
    <div class="loader-bars">
      <div class="loader-bar"></div>
      <div class="loader-bar"></div>
      <div class="loader-bar"></div>
    </div>
  </div>
  <a href="#main-content" class="sr-only">Skip to content</a>
  {build_header(lang, page_key, sub_key, from_depth)}
  <main id="main-content">
    {body_content}
  </main>
  {build_footer(lang, from_depth)}
  {whatsapp_button()}
  <div class="custom-cursor" id="customCursor"></div>
  <script src="{asset_path}/main.js" defer></script>
</body>
</html>'''


# ─── Page builders ────────────────────────────────────────────────────────────

def build_homepage(lang):
    """Build homepage content."""
    c = CONTENT[lang]
    slug = SLUGS[lang]
    lang_prefix = "es" if lang == "es" else LANGUAGES[lang]['dir']
    
    if lang == "es":
        root = "."
    else:
        root = ".."
    
    # Build service cards
    service_cards = ""
    for key in ["spots", "documentaries", "radio", "corporate", "audiobooks", "studio"]:
        svc = c["services"][key]
        href = f"{root}/{lang_prefix}/{slug['voice_actor']}/{slug[key]}/index.html"
        service_cards += f'''
        <a href="{href}" class="service-card">
          <span class="service-icon">{svc["icon"]}</span>
          <h3>{svc["title"]}</h3>
          <p>{svc["desc"]}</p>
        </a>'''
    
    comp_href = f"{root}/{lang_prefix}/{slug['composer']}/index.html"
    contact_href = f"{root}/{lang_prefix}/{slug['contact']}/index.html"
    va_href = f"{root}/{lang_prefix}/{slug['voice_actor']}/index.html"
    
        # FAQ section
    faq_headings = {
        "es": "Preguntas Frecuentes",
        "en": "Frequently Asked Questions",
        "fr": "Questions Fréquentes",
        "de": "Häufig Gestellte Fragen",
        "it": "Domande Frequenti",
        "pt": "Perguntas Frequentes",
        "sv": "Vanliga Frågor",
        "no": "Vanlige Spørsmål",
        "da": "Ofte Stillede Spørgsmål",
        "nl": "Veelgestelde Vragen",
        "el": "Συχνές Ερωτήσεις",
        "zh": "常见问题",
        "ru": "Часто Задаваемые Вопросы",
    }
    faq_items_html = ""
    if lang in FAQ_CONTENT and "homepage_faq" in FAQ_CONTENT[lang]:
        for faq in FAQ_CONTENT[lang]["homepage_faq"]:
            faq_items_html += f"""
          <details class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
            <summary itemprop="name">{faq["q"]}</summary>
            <div class="faq-answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
              <p itemprop="text">{faq["a"]}</p>
            </div>
          </details>"""
    
    faq_section = ""
    if faq_items_html:
        faq_section = f"""
    <section class="section faq-section">
      <div class="container narrow">
        <h2>{faq_headings.get(lang, "FAQ")}</h2>
        <div class="faq-list">
          {faq_items_html}
        </div>
      </div>
    </section>"""
    
    body = f'''
    <section class="hero">
      <div class="hero-inner">
        <div class="hero-soundwave" aria-hidden="true">
          <svg viewBox="0 0 200 60" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g stroke="var(--color-primary)" stroke-width="2" stroke-linecap="round" opacity="0.3">
              {"".join(f'<line x1="{i*4}" y1="50" x2="{i*4}" y2="{50 - (20 + (i*7 % 30))}" />' for i in range(50))}
            </g>
          </svg>
        </div>
        <p class="hero-eyebrow">Guillermo A. Brazález</p>
        <h1>{c["hero_tagline"]}</h1>
        <p class="hero-subtitle">{c["hero_subtitle"]}</p>
        <p class="hero-badge"><span class="hero-badge-icon">▶</span> {c["hero_badge"]}</p>
        <div class="hero-ctas">
          <a href="{va_href}" class="btn btn-primary">{c["cta_listen"]}</a>
          <a href="{contact_href}" class="btn btn-outline">{c["cta_contact"]}</a>
        </div>
      </div>
    </section>

    <section class="section intro-section">
      <div class="container narrow">
        {c["homepage_intro"]}
      </div>
    </section>

    <section class="section services-section">
      <div class="container">
        <h2>{c["services_heading"]}</h2>
        <div class="services-grid">
          {service_cards}
        </div>
      </div>
    </section>

    <section class="section composer-section">
      <div class="container narrow">
        <h2>{c["composer_title"]}</h2>
        {c["composer_text"]}
        <a href="{comp_href}" class="btn btn-outline">{c["composer_title"]}</a>
      </div>
    </section>

    {faq_section}

    <section class="section cta-section">
      <div class="container narrow" style="text-align:center;">
        <h2 class="animate-words">{c["contact_title"]}</h2>
        <p>{c["contact_text"]}</p>
        <div class="hero-ctas" style="justify-content:center;">
          <a href="{contact_href}" class="btn btn-primary">{c["cta_contact"]}</a>
          <a href="https://wa.me/34606350350" class="btn btn-whatsapp" target="_blank" rel="noopener noreferrer">{c["cta_whatsapp"]}</a>
        </div>
      </div>
    </section>'''
    
    depth = 0 if lang == "es" else 1
    # Collect schemas for homepage
    homepage_schemas = []
    faq_s = schema_faq(lang, "homepage")
    if faq_s:
        homepage_schemas.append(faq_s)
    # Breadcrumb
    bc = schema_breadcrumb(lang, [
        (CONTENT[lang]["site_title"], get_page_url(lang)),
    ])
    homepage_schemas.append(bc)
    
    return build_page(
        lang=lang,
        title=c["site_title"],
        meta_desc=c["voice_actor_page"]["meta_desc"][:160],
        canonical=get_page_url(lang),
        body_content=body,
        page_key=None,
        sub_key=None,
        from_depth=depth,
        extra_schema=homepage_schemas if homepage_schemas else None,
    )


def build_voice_actor_main(lang):
    """Build voice actor main page."""
    c = CONTENT[lang]
    slug = SLUGS[lang]
    lang_prefix = "es" if lang == "es" else LANGUAGES[lang]['dir']
    depth = 2
    root = "../.."
    
    service_links = ""
    for key in ["spots", "documentaries", "radio", "corporate", "audiobooks", "studio"]:
        svc = c["services"][key]
        href = f"{root}/{lang_prefix}/{slug['voice_actor']}/{slug[key]}/index.html"
        service_links += f'''
        <a href="{href}" class="service-card">
          <span class="service-icon">{svc["icon"]}</span>
          <h3>{svc["title"]}</h3>
          <p>{svc["desc"]}</p>
        </a>'''
    
    page_data = c["voice_actor_page"]
    
    body = f'''
    <section class="page-hero">
      <div class="container narrow">
        <h1>{page_data["title"]}</h1>
      </div>
    </section>
    <section class="section">
      <div class="container narrow">
        {page_data["content"]}
      </div>
    </section>
    <section class="section services-section">
      <div class="container">
        <h2>{c["services_heading"]}</h2>
        <div class="services-grid">
          {service_links}
        </div>
      </div>
    </section>'''
    
    # Collect schemas
    va_schemas = [schema_service(lang, page_data["title"], page_data["meta_desc"])]
    faq_s = schema_faq(lang, "voice_actor")
    if faq_s:
        va_schemas.append(faq_s)
    bc = schema_breadcrumb(lang, [
        (CONTENT[lang]["site_title"], get_page_url(lang)),
        (page_data["title"], get_page_url(lang, "voice_actor")),
    ])
    va_schemas.append(bc)
    
    return build_page(
        lang=lang,
        title=page_data["title"] + " — Guillermo A. Brazález",
        meta_desc=page_data["meta_desc"],
        canonical=get_page_url(lang, "voice_actor"),
        body_content=body,
        page_key="voice_actor",
        from_depth=depth,
        extra_schema=va_schemas,
    )


def build_service_page(lang, service_key):
    """Build a service subpage."""
    c = CONTENT[lang]
    page_data = c[f"{service_key}_page"]
    depth = 3
    root = "../../.."
    
    # Video embeds
    videos_html = ""
    if service_key in VIMEO:
        videos = VIMEO[service_key]
        videos_html = '<div class="video-grid">'
        for vid in videos:
            videos_html += vimeo_embed(vid)
        videos_html += '</div>'
    
    # Studio images gallery
    studio_gallery_html = ""
    if service_key == "studio":
        studio_titles = {
            "es": "Galería del Estudio",
            "en": "Studio Gallery",
            "fr": "Galerie du Studio",
            "de": "Studio-Galerie",
            "it": "Galleria dello Studio",
            "pt": "Galeria do Estúdio",
            "sv": "Studiogalleri",
            "no": "Studiogalleri",
            "da": "Studiogalleri",
            "nl": "Studiogalerij",
            "el": "Γκαλερί Στούντιο",
            "zh": "录音棚展示",
            "ru": "Галерея студии",
        }
        gallery_title = studio_titles.get(lang, "Studio Gallery")
        studio_gallery_html = f'''
    <section class="section studio-gallery-section">
      <div class="container">
        <h2 class="animate-words">{gallery_title}</h2>
        <div class="studio-gallery">
          <div class="studio-gallery-item parallax-wrap">
            <img src="{root}/assets/studio/digi-desk.jpg" alt="Digi desk — professional recording studio equipment" class="parallax-img" loading="lazy" width="800" height="600">
          </div>
          <div class="studio-gallery-item parallax-wrap">
            <img src="{root}/assets/studio/microphone.jpg" alt="Neumann microphone — professional voice recording" class="parallax-img" loading="lazy" width="800" height="600">
          </div>
        </div>
      </div>
    </section>'''
    
    # SoundCloud for composer is handled separately
    
    body = f'''
    <section class="page-hero">
      <div class="container narrow">
        <h1>{page_data["title"]}</h1>
      </div>
    </section>
    <section class="section">
      <div class="container narrow">
        {page_data["content"]}
      </div>
    </section>'''
    
    if studio_gallery_html:
        body += studio_gallery_html
    
    if videos_html:
        body += f'''
    <section class="section">
      <div class="container">
        {videos_html}
      </div>
    </section>'''
    
    # Collect schemas
    svc_schemas = [schema_service(lang, page_data["title"], page_data["meta_desc"])]
    # FAQ schema for spots and documentaries
    faq_s = schema_faq(lang, service_key)
    if faq_s:
        svc_schemas.append(faq_s)
    # VideoObject schema for pages with videos
    vid_s = schema_video_list(lang, service_key, page_data["title"])
    if vid_s:
        svc_schemas.append(vid_s)
    # Breadcrumb
    va_page = CONTENT[lang]["voice_actor_page"]
    bc = schema_breadcrumb(lang, [
        (CONTENT[lang]["site_title"], get_page_url(lang)),
        (va_page["title"], get_page_url(lang, "voice_actor")),
        (page_data["title"], get_page_url(lang, "voice_actor", service_key)),
    ])
    svc_schemas.append(bc)
    
    return build_page(
        lang=lang,
        title=page_data["title"] + " — Guillermo A. Brazález",
        meta_desc=page_data["meta_desc"],
        canonical=get_page_url(lang, "voice_actor", service_key),
        body_content=body,
        page_key="voice_actor",
        sub_key=service_key,
        from_depth=depth,
        extra_schema=svc_schemas,
    )


def build_composer_page(lang):
    """Build composer page."""
    c = CONTENT[lang]
    page_data = c["composer_page"]
    depth = 2
    
    body = f'''
    <section class="page-hero">
      <div class="container narrow">
        <h1>{page_data["title"]}</h1>
      </div>
    </section>
    <section class="section">
      <div class="container narrow">
        {page_data["content"]}
      </div>
    </section>
    <section class="section">
      <div class="container narrow">
        <div class="soundcloud-embed">
          {SOUNDCLOUD_EMBED}
        </div>
      </div>
    </section>'''
    
    return build_page(
        lang=lang,
        title=page_data["title"] + " — Guillermo A. Brazález",
        meta_desc=page_data["meta_desc"],
        canonical=get_page_url(lang, "composer"),
        body_content=body,
        page_key="composer",
        from_depth=depth,
    )


def build_contact_page(lang):
    """Build contact page."""
    c = CONTENT[lang]
    page_data = c["contact_page"]
    depth = 2
    
    body = f'''
    <section class="page-hero">
      <div class="container narrow">
        <h1>{page_data["title"]}</h1>
      </div>
    </section>
    <section class="section">
      <div class="container narrow">
        {page_data["content"]}
      </div>
    </section>
    <section class="section">
      <div class="container narrow">
        <div class="contact-grid">
          <div class="contact-info">
            <div class="contact-item">
              <h3>WhatsApp</h3>
              <a href="https://wa.me/34606350350" class="btn btn-whatsapp" target="_blank" rel="noopener noreferrer">+34 606 350 350</a>
            </div>
            <div class="contact-item">
              <h3>Email</h3>
              <a href="mailto:info@guillermobrazalez.es">info@guillermobrazalez.es</a>
            </div>
            <div class="contact-item">
              <h3>{c["nav"]["contact"]}</h3>
              <a href="tel:+34606350350">+34 606 350 350</a>
            </div>
          </div>
          <form class="contact-form" action="#" method="post" onsubmit="return false;">
            <div class="form-group">
              <label for="name">{page_data["form_name"]}</label>
              <input type="text" id="name" name="name" required />
            </div>
            <div class="form-group">
              <label for="email">{page_data["form_email"]}</label>
              <input type="email" id="email" name="email" required />
            </div>
            <div class="form-group">
              <label for="subject">{page_data["form_subject"]}</label>
              <input type="text" id="subject" name="subject" />
            </div>
            <div class="form-group">
              <label for="message">{page_data["form_message"]}</label>
              <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">{page_data["form_send"]}</button>
          </form>
        </div>
      </div>
    </section>'''
    
    return build_page(
        lang=lang,
        title=page_data["title"] + " — Guillermo A. Brazález",
        meta_desc=page_data["meta_desc"],
        canonical=get_page_url(lang, "contact"),
        body_content=body,
        page_key="contact",
        from_depth=depth,
    )


# ─── CSS ──────────────────────────────────────────────────────────────────────

def generate_css():
    return '''/* ═══════════════════════════════════════════════════════════════
   spanishvoiceover.net — Style System
   ═══════════════════════════════════════════════════════════════ */

/* ── Reset & Base ───────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html {
  -moz-text-size-adjust: none;
  -webkit-text-size-adjust: none;
  text-size-adjust: none;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
  scroll-behavior: smooth;
  scroll-padding-top: 5rem;
}

:root {
  /* Type Scale */
  --text-xs: clamp(0.75rem, 0.7rem + 0.25vw, 0.875rem);
  --text-sm: clamp(0.875rem, 0.8rem + 0.35vw, 1rem);
  --text-base: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
  --text-lg: clamp(1.125rem, 1rem + 0.75vw, 1.5rem);
  --text-xl: clamp(1.5rem, 1.2rem + 1.25vw, 2.25rem);
  --text-2xl: clamp(2rem, 1.2rem + 2.5vw, 3.5rem);
  --text-3xl: clamp(2.5rem, 1rem + 4vw, 5rem);

  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.25rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-20: 5rem;
  --space-24: 6rem;
  --space-32: 8rem;

  /* Colors — Cinematic Dark Studio */
  --color-bg: #0F1117;
  --color-surface: #1A1D27;
  --color-surface-2: #242836;
  --color-text: #E8E6E1;
  --color-text-muted: #9A9890;
  --color-text-faint: #5A5957;
  --color-primary: #C8956C;
  --color-primary-hover: #E0AB82;
  --color-primary-active: #B07E56;
  --color-border: #2A2E3A;
  --color-border-light: rgba(200, 149, 108, 0.12);

  /* Fonts */
  --font-display: 'Instrument Serif', Georgia, serif;
  --font-body: 'DM Sans', 'Noto Sans SC', 'Helvetica Neue', system-ui, sans-serif;

  /* Radii */
  --radius-sm: 0.375rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;

  /* Transitions */
  --transition-interactive: 180ms cubic-bezier(0.16, 1, 0.3, 1);
  --transition-slow: 400ms cubic-bezier(0.16, 1, 0.3, 1);

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.2);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.3);
  --shadow-lg: 0 12px 32px rgba(0,0,0,0.4);

  /* Content widths */
  --content-narrow: 740px;
  --content-default: 1060px;
  --content-wide: 1280px;
}

body {
  min-height: 100dvh;
  line-height: 1.6;
  font-family: var(--font-body);
  font-size: var(--text-base);
  color: var(--color-text);
  background-color: var(--color-bg);
}

img, picture, video, canvas, svg { display: block; max-width: 100%; height: auto; }
ul[role='list'], ol[role='list'] { list-style: none; }
input, button, textarea, select { font: inherit; color: inherit; }
h1, h2, h3, h4, h5, h6 { text-wrap: balance; line-height: 1.15; }
p, li, figcaption { text-wrap: pretty; max-width: 72ch; }

::selection {
  background: rgba(200, 149, 108, 0.25);
  color: var(--color-text);
}

:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 3px;
  border-radius: var(--radius-sm);
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

button { cursor: pointer; background: none; border: none; }

a, button, [role='button'], [role='link'], input, textarea, select {
  transition: color var(--transition-interactive),
              background var(--transition-interactive),
              border-color var(--transition-interactive),
              box-shadow var(--transition-interactive);
}

.sr-only {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border-width: 0;
}

/* ── Layout ─────────────────────────────────────────────────── */

.container {
  width: 100%;
  max-width: var(--content-default);
  margin: 0 auto;
  padding-inline: var(--space-6);
}

.container.narrow {
  max-width: var(--content-narrow);
}

.container.wide {
  max-width: var(--content-wide);
}

.section {
  padding-block: clamp(var(--space-12), 6vw, var(--space-24));
}

/* ── Header ─────────────────────────────────────────────────── */

.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(15, 17, 23, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--color-border);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: var(--content-wide);
  margin: 0 auto;
  padding: var(--space-4) var(--space-6);
  gap: var(--space-4);
}

.logo-link {
  color: var(--color-text);
  text-decoration: none;
  flex-shrink: 0;
}

.logo-img {
  height: 36px;
  width: auto;
  display: block;
}

.logo-img-small {
  display: none;
  height: 28px;
  width: auto;
}

@media (max-width: 600px) {
  .logo-img { display: none; }
  .logo-img-small { display: block; }
}

.main-nav {
  display: flex;
  align-items: center;
  gap: var(--space-6);
}

.main-nav a {
  color: var(--color-text-muted);
  text-decoration: none;
  font-size: var(--text-sm);
  font-weight: 500;
  letter-spacing: 0.01em;
}

.main-nav a:hover {
  color: var(--color-text);
}

.nav-cta {
  color: var(--color-primary) !important;
  font-weight: 600 !important;
}

.nav-cta:hover {
  color: var(--color-primary-hover) !important;
}

/* Dropdown */
.nav-item { position: relative; display: flex; align-items: center; gap: 2px; }

.dropdown-toggle {
  display: none; /* Hidden on desktop, shown on mobile */
  background: none;
  border: none;
  color: var(--color-text-muted);
  padding: var(--space-1);
  cursor: pointer;
  transition: transform var(--transition-interactive);
}

.dropdown-toggle.open {
  transform: rotate(180deg);
}

.nav-item .dropdown {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(8px);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-2);
  min-width: 220px;
  opacity: 0;
  visibility: hidden;
  transition: opacity var(--transition-interactive), visibility var(--transition-interactive), transform var(--transition-interactive);
  box-shadow: var(--shadow-lg);
}

.nav-item:hover .dropdown,
.nav-item:focus-within .dropdown {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
}

.dropdown a {
  display: block;
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-md);
  color: var(--color-text-muted) !important;
  font-size: var(--text-sm);
}

.dropdown a:hover {
  background: var(--color-surface-2);
  color: var(--color-text) !important;
}

/* Language Switcher */
.lang-switcher {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
  background: var(--color-surface);
  border-radius: var(--radius-md);
  padding: var(--space-1);
}

.lang-switcher a {
  display: block;
  padding: 2px 5px;
  font-size: 0.65rem;
  font-weight: 600;
  text-decoration: none;
  color: var(--color-text-muted);
  border-radius: var(--radius-sm);
  transition: all var(--transition-interactive);
  line-height: 1.4;
}

/* Mobile: show dropdown select instead */
.lang-select-mobile {
  display: none;
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: var(--space-1) var(--space-2);
  font-size: var(--text-xs);
  font-weight: 600;
  cursor: pointer;
}

@media (max-width: 768px) {
  .lang-switcher { display: none; }
  .lang-select-mobile { display: block; }
}

.lang-switcher a:hover {
  color: var(--color-text);
  background: var(--color-surface-2);
}

.lang-switcher a.active {
  color: var(--color-bg);
  background: var(--color-primary);
}

/* Mobile toggle */
.mobile-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  padding: var(--space-2);
}

.mobile-toggle span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--color-text);
  border-radius: 2px;
  transition: all var(--transition-interactive);
}

@media (max-width: 768px) {
  .mobile-toggle { display: flex; }
  
  .main-nav {
    position: fixed;
    top: 0;
    right: -100%;
    width: 280px;
    height: 100dvh;
    background: var(--color-surface);
    flex-direction: column;
    align-items: flex-start;
    padding: var(--space-20) var(--space-6) var(--space-8);
    gap: var(--space-2);
    transition: right var(--transition-slow);
    z-index: 200;
    border-left: 1px solid var(--color-border);
  }
  
  .main-nav.open { right: 0; }
  
  .main-nav a {
    font-size: var(--text-base);
    padding: var(--space-3) 0;
  }
  
  .dropdown-toggle {
    display: flex;
    align-items: center;
    padding: var(--space-2) var(--space-3);
    color: var(--color-text-muted);
  }

  .nav-item {
    flex-wrap: wrap;
  }

  .nav-item .nav-parent {
    flex: 1;
  }

  .nav-item .dropdown {
    position: static;
    transform: none;
    background: transparent;
    border: none;
    box-shadow: none;
    padding: 0 0 0 var(--space-4);
    min-width: 0;
    width: 100%;
    /* Collapsed by default on mobile */
    opacity: 0;
    visibility: hidden;
    max-height: 0;
    overflow: hidden;
    transition: opacity 0.3s ease, max-height 0.3s ease, visibility 0.3s ease;
  }

  .nav-item .dropdown.mobile-open {
    opacity: 1;
    visibility: visible;
    max-height: 500px;
  }
  
  .dropdown a {
    padding: var(--space-3) 0;
    font-size: var(--text-base);
    display: block;
  }
  
  .lang-switcher {
    order: -1;
    margin-bottom: var(--space-4);
  }
  
  .site-header {
    z-index: 300;
  }

  .mobile-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.5);
    z-index: 150;
    opacity: 0;
    visibility: hidden;
    transition: opacity var(--transition-slow), visibility var(--transition-slow);
  }
  
  .mobile-overlay.open {
    opacity: 1;
    visibility: visible;
  }
}

/* ── Hero ────────────────────────────────────────────────────── */

.hero {
  position: relative;
  padding: clamp(var(--space-20), 12vw, var(--space-32)) var(--space-6);
  overflow: hidden;
  text-align: left;
}

.hero-inner {
  max-width: var(--content-narrow);
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.hero-soundwave {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  opacity: 0.5;
  pointer-events: none;
}

.hero-soundwave svg {
  width: 100%;
  height: 100%;
}

.hero-eyebrow {
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--color-primary);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: var(--space-4);
}

.hero h1 {
  font-family: var(--font-display);
  letter-spacing: -0.03em;
  font-size: var(--text-3xl);
  font-weight: 400;
  color: var(--color-text);
  margin-bottom: var(--space-6);
  font-style: italic;
}

.hero-subtitle {
  font-size: var(--text-lg);
  color: var(--color-text-muted);
  margin-bottom: var(--space-4);
  max-width: 540px;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5em;
  font-family: var(--font-body);
  font-size: var(--text-sm);
  font-weight: 500;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--color-primary);
  background: rgba(196, 167, 125, 0.1);
  border: 1px solid rgba(196, 167, 125, 0.25);
  border-radius: 100px;
  padding: 0.45em 1.2em;
  margin-bottom: var(--space-8);
}

.hero-badge-icon {
  font-size: 0.6em;
  opacity: 0.7;
}

.hero-ctas {
  display: flex;
  gap: var(--space-4);
  flex-wrap: wrap;
}

/* ── Page Hero ──────────────────────────────────────────────── */

.page-hero {
  padding: clamp(var(--space-16), 8vw, var(--space-24)) var(--space-6) var(--space-8);
  border-bottom: 1px solid var(--color-border);
}

.page-hero h1 {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: 400;
  font-style: italic;
}

/* ── Buttons ─────────────────────────────────────────────────── */

.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  border: none;
  transition: all var(--transition-interactive);
}

.btn-primary {
  background: var(--color-primary);
  color: var(--color-bg);
}

.btn-primary:hover {
  background: var(--color-primary-hover);
}

.btn-outline {
  background: transparent;
  color: var(--color-text);
  border: 1px solid var(--color-border);
}

.btn-outline:hover {
  border-color: var(--color-primary);
  color: var(--color-primary);
}

.btn-whatsapp {
  background: #25D366;
  color: #fff;
}

.btn-whatsapp:hover {
  background: #20BD5A;
}

/* ── Content ─────────────────────────────────────────────────── */

.intro-section {
  border-bottom: 1px solid var(--color-border);
}

.intro-section p {
  color: var(--color-text-muted);
  margin-bottom: var(--space-4);
  line-height: 1.75;
}

.intro-section p:last-child {
  margin-bottom: 0;
}

.section h2 {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: 400;
  font-style: italic;
  margin-bottom: var(--space-8);
}

.section p {
  color: var(--color-text-muted);
  margin-bottom: var(--space-4);
  line-height: 1.75;
}

/* ── Services Grid ──────────────────────────────────────────── */

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: var(--space-4);
}

.service-card {
  display: block;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  text-decoration: none;
  transition: all var(--transition-interactive);
}

.service-card:hover {
  border-color: var(--color-primary);
  background: var(--color-surface-2);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.service-icon {
  font-size: 1.75rem;
  display: block;
  margin-bottom: var(--space-4);
}

.service-card h3 {
  font-family: var(--font-display);
  font-size: var(--text-lg);
  font-weight: 400;
  font-style: italic;
  color: var(--color-text);
  margin-bottom: var(--space-2);
}

.service-card p {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  line-height: 1.6;
}

/* ── Composer Section ───────────────────────────────────────── */

.composer-section {
  background: var(--color-surface);
  border-top: 1px solid var(--color-border);
  border-bottom: 1px solid var(--color-border);
}

.soundcloud-embed {
  border-radius: var(--radius-lg);
  overflow: hidden;
  margin-top: var(--space-8);
}

.soundcloud-embed iframe {
  width: 100%;
  border-radius: var(--radius-lg);
}

/* ── Video Grid ─────────────────────────────────────────────── */

.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: var(--space-6);
}

@media (max-width: 500px) {
  .video-grid {
    grid-template-columns: 1fr;
  }
}

.video-embed {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
  overflow: hidden;
  border-radius: var(--radius-lg);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
}

.video-embed iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

/* ── CTA Section ────────────────────────────────────────────── */

.cta-section {
  background: var(--color-surface);
  border-top: 1px solid var(--color-border);
}

.cta-section h2 {
  text-align: center;
}

.cta-section p {
  text-align: center;
  margin-inline: auto;
  margin-bottom: var(--space-8);
}

/* ── Contact ────────────────────────────────────────────────── */

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1.5fr;
  gap: var(--space-12);
  align-items: start;
}

@media (max-width: 768px) {
  .contact-grid {
    grid-template-columns: 1fr;
    gap: var(--space-8);
  }
}

.contact-item {
  margin-bottom: var(--space-6);
}

.contact-item h3 {
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--color-text-faint);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: var(--space-2);
}

.contact-item a {
  color: var(--color-primary);
  text-decoration: none;
  font-size: var(--text-lg);
  font-weight: 500;
}

.contact-item a:hover {
  color: var(--color-primary-hover);
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.form-group label {
  display: block;
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--color-text-muted);
  margin-bottom: var(--space-1);
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: var(--space-3) var(--space-4);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-size: var(--text-base);
  color: var(--color-text);
  transition: border-color var(--transition-interactive);
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--color-primary);
}

.form-group textarea {
  resize: vertical;
  min-height: 120px;
}

/* ── Footer ─────────────────────────────────────────────────── */

.site-footer {
  border-top: 1px solid var(--color-border);
  padding: var(--space-12) var(--space-6);
}

.footer-inner {
  max-width: var(--content-wide);
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: var(--space-8);
  align-items: start;
}

@media (max-width: 768px) {
  .footer-inner {
    grid-template-columns: 1fr;
    gap: var(--space-6);
  }
}

.footer-brand .logo-img {
  height: 28px;
  margin-bottom: var(--space-3);
  opacity: 0.7;
}

.footer-brand p {
  font-size: var(--text-sm);
  color: var(--color-text-faint);
}

.footer-contact p {
  margin-bottom: var(--space-2);
}

.footer-contact a {
  color: var(--color-text-muted);
  text-decoration: none;
  font-size: var(--text-sm);
}

.footer-contact a:hover {
  color: var(--color-primary);
}

.footer-copy p {
  font-size: var(--text-xs);
  color: var(--color-text-faint);
}

/* ── WhatsApp Float ─────────────────────────────────────────── */

.whatsapp-float {
  position: fixed;
  bottom: var(--space-6);
  right: var(--space-6);
  z-index: 90;
  width: 56px;
  height: 56px;
  background: #25D366;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.3);
  transition: transform var(--transition-interactive), box-shadow var(--transition-interactive);
}

.whatsapp-float:hover {
  transform: scale(1.08);
  box-shadow: 0 6px 24px rgba(37, 211, 102, 0.4);
}

/* ── Decorative Sound Wave ──────────────────────────────────── */

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(ellipse at 20% 50%, rgba(200, 149, 108, 0.06) 0%, transparent 60%),
    radial-gradient(ellipse at 80% 20%, rgba(200, 149, 108, 0.03) 0%, transparent 50%);
  pointer-events: none;
}

/* Subtle decorative line on page heroes */
.page-hero::after {
  content: '';
  display: block;
  width: 60px;
  height: 2px;
  background: var(--color-primary);
  margin-top: var(--space-6);
  opacity: 0.6;
}


/* ── FAQ Section ─────────────────────────────────────────── */

.faq-section h2 {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  margin-bottom: var(--space-8);
}

.faq-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.faq-item {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: border-color var(--transition-interactive);
}

.faq-item:hover {
  border-color: var(--color-primary);
}

.faq-item summary {
  padding: var(--space-5) var(--space-6);
  cursor: pointer;
  font-weight: 500;
  font-size: var(--text-base);
  list-style: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--space-4);
}

.faq-item summary::-webkit-details-marker { display: none; }

.faq-item summary::after {
  content: "+";
  font-size: 1.25rem;
  color: var(--color-primary);
  flex-shrink: 0;
  transition: transform var(--transition-interactive);
}

.faq-item[open] summary::after {
  content: "−";
}

.faq-answer {
  padding: 0 var(--space-6) var(--space-5);
  color: var(--color-text-muted);
  line-height: 1.7;
}

.faq-answer p {
  margin: 0;
}


/* ── Studio Gallery ────────────────────────────────────────── */

.studio-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 400px), 1fr));
  gap: var(--space-6);
  margin-top: var(--space-8);
}

.studio-gallery-item {
  border-radius: var(--radius-lg);
  overflow: hidden;
  aspect-ratio: 4/3;
}

.studio-gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s cubic-bezier(0.16,1,0.3,1);
}

.studio-gallery-item:hover img {
  transform: scale(1.03);
}

.studio-gallery-section h2 {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: 400;
  font-style: italic;
  letter-spacing: -0.02em;
}

/* ── Custom Cursor ─────────────────────────────────────────── */

.custom-cursor {
  position: fixed;
  top: -16px;
  left: -16px;
  width: 32px;
  height: 32px;
  border: 1.5px solid var(--color-primary);
  border-radius: 50%;
  pointer-events: none;
  z-index: 9999;
  transition: width 0.3s cubic-bezier(0.16,1,0.3,1), height 0.3s cubic-bezier(0.16,1,0.3,1), border-color 0.3s ease, opacity 0.3s ease;
  opacity: 0.6;
  mix-blend-mode: difference;
}

.custom-cursor.cursor-hover {
  width: 48px;
  height: 48px;
  top: -24px;
  left: -24px;
  border-color: var(--color-text);
  opacity: 0.9;
}

@media (hover: none) {
  .custom-cursor { display: none; }
}

/* ── Smooth Scroll Body ────────────────────────────────────── */

html.lenis, html.lenis body {
  height: auto;
}

.lenis.lenis-smooth {
  scroll-behavior: auto !important;
}

/* ── Header Auto-Hide ──────────────────────────────────────── */

.site-header {
  transition: transform 0.4s cubic-bezier(0.16,1,0.3,1);
}

.site-header.header-hidden {
  transform: translateY(-100%);
}

/* ── Word Animation ────────────────────────────────────────── */

.animate-words .word {
  display: inline-block;
}

/* ── Parallax Container ────────────────────────────────────── */

.parallax-wrap {
  overflow: hidden;
  position: relative;
}

.parallax-img {
  width: 100%;
  height: 120%;
  object-fit: cover;
  will-change: transform;
}

/* ── Video Grid Enhancement ────────────────────────────────── */

.video-embed {
  will-change: opacity, transform;
}

/* ── Hero Enhancements ─────────────────────────────────────── */

.hero-title {
  will-change: transform, opacity;
}

.hero-tagline {
  font-size: clamp(var(--text-lg), 2.5vw, var(--text-xl));
  opacity: 0.8;
  letter-spacing: -0.01em;
  max-width: 600px;
}

/* ── Section Divider (cinematic line) ──────────────────────── */

.section-divider {
  width: 60px;
  height: 1px;
  background: var(--color-primary);
  margin: var(--space-2) 0 var(--space-6);
  opacity: 0.5;
}

/* ── Horizontal Scroll Gallery (for portfolio) ─────────────── */

.h-scroll-gallery {
  display: flex;
  gap: var(--space-4);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding: var(--space-4) 0;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.h-scroll-gallery::-webkit-scrollbar { display: none; }

.h-scroll-gallery .gallery-item {
  flex: 0 0 min(80vw, 400px);
  scroll-snap-align: center;
  border-radius: var(--radius-lg);
  overflow: hidden;
  aspect-ratio: 16/9;
}

/* ── Page Load Transition ──────────────────────────────────── */

.page-loader {
  position: fixed;
  inset: 0;
  background: var(--color-bg);
  z-index: 10000;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.6s cubic-bezier(0.16,1,0.3,1), visibility 0.6s;
}

.page-loader.loaded {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.loader-bars {
  display: flex;
  gap: 4px;
  align-items: center;
  height: 40px;
}

.loader-bar {
  width: 3px;
  height: 10px;
  background: var(--color-primary);
  border-radius: 2px;
  animation: loader-pulse 1s ease-in-out infinite;
}

.loader-bar:nth-child(2) { animation-delay: 0.15s; }
.loader-bar:nth-child(3) { animation-delay: 0.3s; }

@keyframes loader-pulse {
  0%, 100% { height: 10px; opacity: 0.4; }
  50% { height: 30px; opacity: 1; }
}

/* ── Responsive ─────────────────────────────────────────────── */

@media (max-width: 480px) {
  .hero h1 {
    font-size: clamp(2rem, 1rem + 4vw, 3rem);
  }
  
  .hero-ctas {
    flex-direction: column;
  }
  
  .hero-ctas .btn {
    width: 100%;
    justify-content: center;
  }
  
  .services-grid {
    grid-template-columns: 1fr;
  }
  
  .video-grid {
    grid-template-columns: 1fr;
  }
}

/* ── Print ───────────────────────────────────────────────────── */

@media print {
  .site-header, .site-footer, .whatsapp-float, .lang-switcher, .mobile-toggle { display: none; }
  body { color: #000; background: #fff; }
}
'''


# ─── JavaScript ───────────────────────────────────────────────────────────────

def generate_js():
    return '''// spanishvoiceover.net — Main JS

(function() {
  'use strict';

  // ── Page Loader ──
  var loader = document.getElementById('pageLoader');
  function dismissLoader() {
    if (loader) { setTimeout(function() { loader.classList.add('loaded'); }, 300); }
  }
  if (document.readyState === 'complete') { dismissLoader(); }
  else { window.addEventListener('load', dismissLoader); }

  // ── Lenis Smooth Scroll ──
  var lenis;
  if (typeof Lenis !== 'undefined') {
    lenis = new Lenis({
      duration: 1.2,
      easing: function(t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      touchMultiplier: 2,
      infinite: false
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
  }

  // ── Custom Cursor ──
  var cursor = document.getElementById('customCursor');
  if (cursor && window.matchMedia('(hover: hover)').matches) {
    var cx = -100, cy = -100;
    document.addEventListener('mousemove', function(e) {
      cx = e.clientX; cy = e.clientY;
      cursor.style.transform = 'translate(' + cx + 'px,' + cy + 'px)';
    });
    document.querySelectorAll('a, button, [role=button], .service-card, .faq-item summary').forEach(function(el) {
      el.addEventListener('mouseenter', function() { cursor.classList.add('cursor-hover'); });
      el.addEventListener('mouseleave', function() { cursor.classList.remove('cursor-hover'); });
    });
  }

  // ── Mobile Navigation ──
  var toggle = document.querySelector('.mobile-toggle');
  var nav = document.querySelector('.main-nav');
  var overlay;

  if (toggle && nav) {
    overlay = document.createElement('div');
    overlay.className = 'mobile-overlay';
    document.body.appendChild(overlay);

    toggle.addEventListener('click', function() {
      var isOpen = nav.classList.contains('open');
      nav.classList.toggle('open');
      overlay.classList.toggle('open');
      toggle.setAttribute('aria-expanded', !isOpen);
      if (!isOpen) {
        toggle.children[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        toggle.children[1].style.opacity = '0';
        toggle.children[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        toggle.children[0].style.transform = '';
        toggle.children[1].style.opacity = '';
        toggle.children[2].style.transform = '';
      }
    });

    overlay.addEventListener('click', function() {
      nav.classList.remove('open');
      overlay.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.children[0].style.transform = '';
      toggle.children[1].style.opacity = '';
      toggle.children[2].style.transform = '';
    });
  }

  // ── Mobile dropdown toggle ──
  var dropdownToggle = document.querySelector('.dropdown-toggle');
  if (dropdownToggle) {
    dropdownToggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      var dropdown = this.parentElement.querySelector('.dropdown');
      var isOpen = dropdown.classList.contains('mobile-open');
      dropdown.classList.toggle('mobile-open');
      this.classList.toggle('open');
      this.setAttribute('aria-expanded', !isOpen);
    });
  }

  // ── Lazy load Vimeo iframes ──
  var vimeoFrames = document.querySelectorAll('.video-embed iframe');
  if ('IntersectionObserver' in window && vimeoFrames.length) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var iframe = entry.target;
          if (iframe.dataset.src) { iframe.src = iframe.dataset.src; }
          observer.unobserve(iframe);
        }
      });
    }, { rootMargin: '200px' });

    vimeoFrames.forEach(function(iframe) {
      if (iframe.src && !iframe.dataset.src) {
        iframe.dataset.src = iframe.src;
        iframe.removeAttribute('src');
      }
      observer.observe(iframe);
    });
  }

  // ── Smooth scroll for anchor links (via Lenis) ──
  document.querySelectorAll('a[href^="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var href = this.getAttribute('href');
      var target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        if (lenis) { lenis.scrollTo(target); }
        else { target.scrollIntoView({ behavior: 'smooth' }); }
      }
    });
  });

  // ── GSAP ScrollTrigger ──
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);

    // Connect Lenis to ScrollTrigger
    if (lenis) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(function(time) { lenis.raf(time * 1000); });
      gsap.ticker.lagSmoothing(0);
    }

    // Reveal sections on scroll
    gsap.utils.toArray('.section').forEach(function(section) {
      gsap.from(section, {
        opacity: 0, y: 40,
        duration: 0.8, ease: 'power2.out',
        scrollTrigger: { trigger: section, start: 'top 85%', toggleActions: 'play none none none' }
      });
    });

    // Word-by-word animation
    document.querySelectorAll('.animate-words').forEach(function(el) {
      var text = el.textContent.trim();
      var words = text.split(/\\s+/);
      el.innerHTML = words.map(function(w) { return '<span class="word">' + w + '</span>'; }).join(' ');
      gsap.from(el.querySelectorAll('.word'), {
        opacity: 0, y: 20, filter: 'blur(4px)',
        duration: 0.6, ease: 'power2.out',
        stagger: 0.08,
        scrollTrigger: { trigger: el, start: 'top 80%', toggleActions: 'play none none none' }
      });
    });

    // Parallax on images
    gsap.utils.toArray('.parallax-img').forEach(function(img) {
      gsap.fromTo(img,
        { y: -30 },
        { y: 30, ease: 'none',
          scrollTrigger: { trigger: img.parentElement, start: 'top bottom', end: 'bottom top', scrub: true }
        }
      );
    });

    // Video embeds reveal
    gsap.utils.toArray('.video-embed').forEach(function(vid) {
      gsap.from(vid, {
        opacity: 0, scale: 0.95,
        duration: 0.6, ease: 'power2.out',
        scrollTrigger: { trigger: vid, start: 'top 85%', toggleActions: 'play none none none' }
      });
    });

    // CTA section entrance
    var ctaSection = document.querySelector('.cta-section');
    if (ctaSection) {
      gsap.from(ctaSection.querySelectorAll('h2, p, .btn'), {
        opacity: 0, y: 30,
        duration: 0.7, ease: 'power2.out',
        stagger: 0.15,
        scrollTrigger: { trigger: ctaSection, start: 'top 80%', toggleActions: 'play none none none' }
      });
    }

    // FAQ cascade reveal
    gsap.utils.toArray('.faq-item').forEach(function(item, i) {
      gsap.from(item, {
        opacity: 0, x: -20,
        duration: 0.5, ease: 'power2.out',
        delay: i * 0.05,
        scrollTrigger: { trigger: item, start: 'top 90%', toggleActions: 'play none none none' }
      });
    });

    // Service cards stagger
    gsap.utils.toArray('.service-card').forEach(function(card, i) {
      gsap.from(card, {
        opacity: 0, y: 30,
        duration: 0.6, ease: 'power2.out',
        delay: i * 0.08,
        scrollTrigger: { trigger: card, start: 'top 88%', toggleActions: 'play none none none' }
      });
    });

    // Studio gallery items
    gsap.utils.toArray('.studio-gallery-item').forEach(function(item, i) {
      gsap.from(item, {
        opacity: 0, scale: 0.9,
        duration: 0.8, ease: 'power2.out',
        delay: i * 0.15,
        scrollTrigger: { trigger: item, start: 'top 85%', toggleActions: 'play none none none' }
      });
    });
  }

  // ── Header hide/show on scroll ──
  var header = document.querySelector('.site-header');
  if (header && lenis) {
    var lastScroll = 0;
    lenis.on('scroll', function(e) {
      var currentScroll = e.animatedScroll;
      if (currentScroll > 100) {
        if (currentScroll > lastScroll) {
          header.classList.add('header-hidden');
        } else {
          header.classList.remove('header-hidden');
        }
      } else {
        header.classList.remove('header-hidden');
      }
      lastScroll = currentScroll;
    });
  }

})();
'''


# ─── Sitemap & Robots ────────────────────────────────────────────────────────

def generate_sitemap():
    """Generate XML sitemap."""
    urls = []
    
    for lang in LANGUAGES:
        # Homepage
        urls.append(get_page_url(lang))
        # Voice actor main
        urls.append(get_page_url(lang, "voice_actor"))
        # Service pages
        for svc in ["spots", "documentaries", "radio", "corporate", "audiobooks", "studio", "trivago"]:
            urls.append(get_page_url(lang, "voice_actor", svc))
        # Composer
        urls.append(get_page_url(lang, "composer"))
        # Contact
        urls.append(get_page_url(lang, "contact"))
    
    xml_urls = ""
    for url in urls:
        xml_urls += f"""  <url>
    <loc>{url}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""
    
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_urls}</urlset>'''


def generate_robots():
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


def generate_redirects():
    """Generate redirect map for old WordPress URLs."""
    return """# Redirect map — old WordPress URLs to new structure
/locucion-en-espanol/   /es/locutor/   301
/spanish-voice-over/    /en/voice-actor/   301
/voix-off-espagnol/     /fr/comédien-vocal/   301
/spanischer-sprecher/   /de/sprecher/   301
/doppiatore-spagnolo/   /it/doppiatore/   301
/locutor-espanhol/      /pt/locutor/   301
/estudio/               /es/locutor/estudio/   301
/spots/                 /es/locutor/spots/   301
/documentales/          /es/locutor/documentales/   301
/radio/                 /es/locutor/radio/   301
/corporativo/           /es/locutor/corporativo/   301
/audiolibros/           /es/locutor/audiolibros/   301
/compositor/            /es/compositor/   301
/contacto/              /es/contacto/   301
/en/                    /en/   301
/fr/                    /fr/   301
/de/                    /de/   301
/it/                    /it/   301
/pt/                    /pt/   301
/sv/                    /sv/   301
/no/                    /no/   301
/da/                    /da/   301
/nl/                    /nl/   301
/el/                    /el/   301
/zh/                    /zh/   301
/ru/                    /ru/   301
"""


# ─── Main Generator ──────────────────────────────────────────────────────────

def ensure_dir(path):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)


def write_file(path, content):
    """Write content to file."""
    ensure_dir(os.path.dirname(path))
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ {path}")


def build_trivago_page(lang):
    """Build the dedicated Trivago page."""
    import json as _json
    c = CONTENT[lang]
    tc = TRIVAGO_CONTENT[lang]
    slug = SLUGS[lang]
    depth = 3
    lang_prefix = "es" if lang == "es" else LANGUAGES[lang]["dir"]
    
    canonical = get_page_url(lang, "voice_actor", "trivago")
    
    # YouTube embeds
    videos_html = '<div class="video-grid">'
    for yt_id in TRIVAGO_YOUTUBE:
        videos_html += f'''
        <div class="video-embed">
          <iframe width="100%" height="315" 
            src="https://www.youtube.com/embed/{yt_id}" 
            title="Trivago Spain Commercial" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen loading="lazy"></iframe>
        </div>'''
    videos_html += '</div>'
    
    # FAQ section
    faqs = tc.get("faq", [])
    faq_html = ""
    if faqs:
        faq_html = '<div class="faq-list">'
        for faq in faqs:
            faq_html += f'''
            <details class="faq-item">
              <summary>{faq["q"]}</summary>
              <p>{faq["a"]}</p>
            </details>'''
        faq_html += '</div>'
    
    # FAQPage + VideoObject schema
    faq_schema_obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": faq["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq["a"]
                }
            } for faq in faqs
        ]
    }
    
    video_schema_list = []
    yt_titles = [
        "Trivago España Corto 2025 — Jürgen Klopp",
        "Trivago Versión Doblada 2025",
        "Campaña Trivago 2024 TV Nacional España",
    ]
    for i, yt_id in enumerate(TRIVAGO_YOUTUBE):
        video_schema_list.append({
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": yt_titles[i] if i < len(yt_titles) else f"Trivago Spain Commercial {i+1}",
            "description": tc["meta_desc"],
            "thumbnailUrl": f"https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg",
            "embedUrl": f"https://www.youtube.com/embed/{yt_id}",
            "uploadDate": "2025-01-01",
        })
    
    extra_schema = [_json.dumps(faq_schema_obj, ensure_ascii=False)]
    for vs in video_schema_list:
        extra_schema.append(_json.dumps(vs, ensure_ascii=False))
    
    # Contact link
    root = "../../.."
    contact_href = f"{root}/{lang_prefix}/{slug['contact']}/index.html"
    
    body = f'''
    <section class="page-hero">
      <div class="container narrow">
        <p class="hero-eyebrow">Guillermo A. Brazález × Trivago</p>
        <h1 class="animate-words">{tc["h1"]}</h1>
      </div>
    </section>
    <section class="section">
      <div class="container narrow">
        {tc["intro"]}
      </div>
    </section>
    <section class="section">
      <div class="container">
        <h2 class="animate-words">{tc["section_videos"]}</h2>
        {videos_html}
      </div>
    </section>
    <section class="section">
      <div class="container narrow">
        <h2 class="animate-words">{tc["section_about"]}</h2>
        {tc["about_text"]}
      </div>
    </section>'''
    
    if faq_html:
        faq_heading = {"es": "Preguntas Frecuentes", "en": "FAQ", "fr": "FAQ", "de": "Häufige Fragen", "it": "FAQ", "pt": "Perguntas Frequentes", "sv": "Vanliga Frågor", "no": "Ofte Stilte Spørsmål", "da": "Ofte Stillede Spørgsmål", "nl": "Veelgestelde Vragen", "el": "Συχνές Ερωτήσεις", "zh": "常见问题", "ru": "Часто Задаваемые Вопросы"}
        body += f'''
    <section class="section">
      <div class="container narrow">
        <h2 class="animate-words">{faq_heading.get(lang, "FAQ")}</h2>
        {faq_html}
      </div>
    </section>'''
    
    body += f'''
    <section class="section cta-section">
      <div class="container narrow" style="text-align:center;">
        <h2>{tc["cta_text"]}</h2>
        <a href="{contact_href}" class="btn btn-primary">{c["cta_contact"]}</a>
      </div>
    </section>'''
    
    return build_page(
        lang=lang,
        title=tc["meta_title"],
        meta_desc=tc["meta_desc"],
        canonical=canonical,
        body_content=body,
        page_key="trivago",
        from_depth=depth,
        extra_schema=extra_schema,
    )


def main():
    print("═══════════════════════════════════════════")
    print("  spanishvoiceover.net — Static Site Generator")
    print("═══════════════════════════════════════════\n")
    
    # Assets
    print("→ Generating assets...")
    write_file(str(BASE_DIR / "assets" / "style.css"), generate_css())
    write_file(str(BASE_DIR / "assets" / "main.js"), generate_js())
    
    # Root files
    print("\n→ Generating root files...")
    write_file(str(BASE_DIR / "sitemap.xml"), generate_sitemap())
    write_file(str(BASE_DIR / "robots.txt"), generate_robots())
    write_file(str(BASE_DIR / "_redirects"), generate_redirects())
    
    file_count = 0
    
    for lang in LANGUAGES:
        lang_info = LANGUAGES[lang]
        slug = SLUGS[lang]
        print(f"\n→ Generating {lang_info['name']} pages...")
        
        # Homepage
        if lang == "es":
            write_file(str(BASE_DIR / "index.html"), build_homepage(lang))
        else:
            write_file(str(BASE_DIR / lang_info['dir'] / "index.html"), build_homepage(lang))
        file_count += 1
        
        # Voice actor main
        lang_prefix = "es" if lang == "es" else lang_info['dir']
        va_dir = BASE_DIR / lang_prefix / slug['voice_actor']
        write_file(str(va_dir / "index.html"), build_voice_actor_main(lang))
        file_count += 1
        
        # Service subpages
        for svc in ["spots", "documentaries", "radio", "corporate", "audiobooks", "studio"]:
            svc_dir = va_dir / slug[svc]
            write_file(str(svc_dir / "index.html"), build_service_page(lang, svc))
            file_count += 1
        
        # Trivago dedicated page
        trivago_dir = va_dir / slug['trivago']
        write_file(str(trivago_dir / "index.html"), build_trivago_page(lang))
        file_count += 1
        
        # Composer
        comp_dir = BASE_DIR / lang_prefix / slug['composer']
        write_file(str(comp_dir / "index.html"), build_composer_page(lang))
        file_count += 1
        
        # Contact
        contact_dir = BASE_DIR / lang_prefix / slug['contact']
        write_file(str(contact_dir / "index.html"), build_contact_page(lang))
        file_count += 1
    
    print(f"\n═══════════════════════════════════════════")
    print(f"  ✅ Generated {file_count} HTML pages + assets")
    print(f"  📁 Output: {BASE_DIR}")
    print(f"═══════════════════════════════════════════")


if __name__ == "__main__":
    main()
