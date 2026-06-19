import os
import sys
sys.path.insert(0, os.path.expanduser("~/.local/lib/python3.14/site-packages"))

from youtube_transcript_api import YouTubeTranscriptApi

api = YouTubeTranscriptApi()

expert_videos = {
    "tk-kader": [
        {"id": "YxAd96vLzCc", "title": "If I Started in 2026, Heres My B2B SaaS Content Strategy for $1M ARR"},
        {"id": "fge6vPNz2Kc", "title": "Content Marketing for B2B That Works"},
    ],
    "b2b-playbook": [
        {"id": "Lg-TPMJHrTw", "title": "The Best B2B Partnership Strategy for 2026"},
        {"id": "ARUYHzdg9-o", "title": "Our Simple 3 Step B2B Demand Generation Strategy for 2026"},
    ],
    "dave-gerhardt": [
        {"id": "-B1xZs9rdYo", "title": "The Best B2B Influencer Marketing Strategy in 2026"},
        {"id": "mTftU2VHZUE", "title": "Building Your B2B Marketing Strategy"},
    ],
    "chris-walker": [
        {"id": "L2baqhX1sMg", "title": "Demand Gen Keynote with CEO Chris Walker"},
        {"id": "peCcVsGaPKU", "title": "Demand Gen Live with CEO Chris Walker"},
    ],
    "april-dunford": [
        {"id": "cobwnnEEE-4", "title": "Market Categories, Competition, and Growth Strategy"},
        {"id": "AwGLeRJTIrA", "title": "How to Position Your B2B SaaS for Explosive Growth"},
    ],
    "kipp-bodnar": [
        {"id": "n11aBugApTE", "title": "HubSpot CMO Kipp Bodnar on B2B Creative"},
        {"id": "PW63IUpyHp8", "title": "HubSpot CMO Kipp Bodnar - Why Marketers Think Like VCs"},
    ],
    "amanda-natividad": [
        {"id": "nzSlBdBfSOo", "title": "B2B Marketers Stop Gating Your Best Content"},
        {"id": "8-ZR3fdG7K8", "title": "Why Marketers Make Content for Dashboards"},
    ],
    "justin-welsh": [
        {"id": "SkR3XB6Bvq8", "title": "Systemizing Your Content Structure with Justin Welsh"},
    ],
    "benji-hyam": [
        {"id": "zPceLkkdRpM", "title": "B2B SEO Content Teardown - Benji and Devesh"},
    ],
    "marketscale": [
        {"id": "82NUzwE3QDE", "title": "B2B Content Marketing Strategy"},
        {"id": "f0DgQg-Iecw", "title": "Holistic Storytelling in B2B Content Marketing"},
    ],
}

base_dir = os.path.expanduser("~/YouTube-B2B-SaaS-Strategy/research/youtube-transcripts")
results = []

for expert, videos in expert_videos.items():
    expert_dir = os.path.join(base_dir, expert)
    os.makedirs(expert_dir, exist_ok=True)
    
    for video in videos:
        video_id = video["id"]
        title = video["title"]
        filename = title.lower().replace(" ", "-").replace(":", "").replace("'", "").replace("$", "")[:50] + ".md"
        filepath = os.path.join(expert_dir, filename)
        
        try:
            transcript = api.fetch(video_id)
            full_text = " ".join([entry.text for entry in transcript])
            
            content = f"""# {title}

**Expert:** {expert.replace("-", " ").title()}
**Video ID:** {video_id}
**YouTube URL:** https://www.youtube.com/watch?v={video_id}
**Transcript Length:** {len(full_text)} characters

---

## Transcript

{full_text}
"""
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            results.append(f"OK {expert}/{filename[:40]}... ({len(full_text)} chars)")
            
        except Exception as e:
            results.append(f"ERR {expert}/{title[:40]}... {str(e)[:80]}")

print("=== TRANSCRIPT COLLECTION RESULTS ===")
for r in results:
    print(r)
print(f"\nTotal: {len([r for r in results if r.startswith('OK')])} collected, {len([r for r in results if r.startswith('ERR')])} failed")
