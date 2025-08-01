"""
Comprehensive Mountain Knowledge Base
The wisdom of peaks, passes, and vertical worlds
"""

MOUNTAIN_DATA = {
    "techniques": {
        "free_solo": {
            "description": "Climbing without ropes or protection",
            "mental_aspect": "Pure commitment. No room for doubt.",
            "risks": "Death is the only consequence of failure",
            "masters": "Alex Honnold, Dan Osman, Derek Hersey"
        },
        "alpine_climbing": {
            "description": "Fast, light climbing in mountain environments",
            "philosophy": "Speed is safety. Weight is weakness.",
            "conditions": "Weather windows, objective hazards",
            "gear": "Minimal rack, light boots, alpine draws"
        },
        "ice_climbing": {
            "description": "Ascending frozen waterfalls and ice formations",
            "tools": "Ice axes, crampons, ice screws",
            "technique": "Read the ice. Blue is strong, white is weak.",
            "seasons": "Winter formations, spring dangers"
        },
        "mixed_climbing": {
            "description": "Rock and ice combined",
            "challenge": "Switching between mediums mid-route",
            "gear": "Hybrid tools, flexible mindset"
        }
    },
    
    "equipment": {
        "ropes": {
            "dynamic": "Absorbs fall energy. 9.5-10.5mm for alpine",
            "static": "Rescue, hauling. No stretch.",
            "care": "Inspect for cuts, core damage, UV wear"
        },
        "protection": {
            "cams": "Spring-loaded camming devices. Placement is art.",
            "nuts": "Passive protection. Simple, reliable.",
            "pitons": "Hammered steel. Old school commitment.",
            "ice_screws": "Threaded into ice. Placement angle critical."
        },
        "clothing": {
            "layering": "Base, insulation, shell. Adapt to conditions.",
            "materials": "Merino wool, synthetic insulation, Gore-Tex",
            "extremities": "Hands and feet fail first in cold"
        }
    },
    
    "weather": {
        "altitude_effects": {
            "pressure": "Decreases ~1% per 100m elevation",
            "temperature": "Drops ~2°C per 300m gain",
            "oxygen": "50% at 5500m, 33% at 8800m"
        },
        "mountain_weather": {
            "orographic_lift": "Air rises, cools, creates clouds",
            "lenticular_clouds": "High winds aloft. Dangerous.",
            "morning_conditions": "Often most stable window",
            "afternoon_storms": "Heat builds instability"
        },
        "seasonal_patterns": {
            "spring": "Avalanche season. Unstable snow.",
            "summer": "Rock fall from freeze-thaw cycles",
            "autumn": "Stable weather, shorter days",
            "winter": "Cold, wind, limited daylight"
        }
    },
    
    "hazards": {
        "objective": {
            "rockfall": "Gravity never sleeps. Move fast through zones.",
            "avalanche": "Snow is a fluid. Understand its moods.",
            "crevasses": "Glacier travel requires rope, awareness",
            "weather": "Mountains create their own storms"
        },
        "subjective": {
            "fatigue": "Tired climbers make fatal mistakes",
            "dehydration": "Altitude accelerates fluid loss",
            "altitude_sickness": "Ascend slowly, descend quickly",
            "hypothermia": "Core temperature drops, judgment fails"
        }
    },
    
    "famous_peaks": {
        "everest": {
            "height": "8,848.86m",
            "challenges": "Death zone above 8000m, crowds, weather",
            "routes": "South Col (Nepal), North Ridge (Tibet)",
            "philosophy": "Not the hardest, but the highest price"
        },
        "k2": {
            "height": "8,611m", 
            "reputation": "Savage Mountain. Technical, dangerous",
            "weather": "Unpredictable, violent storms",
            "mortality": "1 death per 4 summits historically"
        },
        "matterhorn": {
            "height": "4,478m",
            "character": "Iconic pyramid. Deceptively difficult",
            "routes": "Hörnli Ridge most popular",
            "hazards": "Rockfall, crowds, weather changes"
        },
        "el_capitan": {
            "height": "914m vertical",
            "location": "Yosemite Valley, California",
            "routes": "The Nose, Freerider, Dawn Wall",
            "culture": "Big wall mecca. Multi-day ascents"
        }
    },
    
    "japanese_mountains": {
        "mount_fuji": {
            "height": "3,776m",
            "season": "July-September climbing season",
            "routes": "Yoshida, Subashiri, Gotemba, Fujinomiya",
            "character": "Sacred mountain. Pilgrimage and challenge"
        },
        "mount_yari": {
            "height": "3,180m",
            "nickname": "Spear of the Gods",
            "routes": "North Ridge technical, South Ridge easier",
            "season": "June-October, ice climbing in winter"
        },
        "mount_hotaka": {
            "height": "3,190m",
            "character": "Technical ridges, alpine environment",
            "access": "Kamikochi base, multiple peaks",
            "climbing": "Rock and mixed routes available"
        }
    }
}

def get_mountain_knowledge(topic=None):
    """Retrieve mountain knowledge by topic"""
    if topic:
        return MOUNTAIN_DATA.get(topic, "The mountain keeps its secrets.")
    return MOUNTAIN_DATA