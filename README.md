# YouTube Content Strategy for B2B SaaS

This is a research project on how B2B SaaS companies can use YouTube as a serious content channel, not just a place to upload webinars or product demos.

I focused on expert-led content, buyer education, positioning, demand generation, and how long-form videos can be reused across LinkedIn, email, blogs, and sales material.

## What I Collected

- 10 experts / source profiles
- 17 YouTube transcripts
- 5 LinkedIn posts
- Notes on methodology, early patterns, and final takeaways

## Why I Picked This Topic

I picked YouTube content strategy because B2B buyers often research problems before they talk to sales. For SaaS companies, YouTube can help explain complex topics, build trust with buyers, and create long-form content that can be repurposed elsewhere.

The part I wanted to understand better was how strong B2B marketers think about YouTube as part of a wider content system.

## Expert Sources

| # | Expert / Source | Main Area | Why I Included Them |
|---|---|---|---|
| 1 | TK Kader | B2B SaaS growth | Practical SaaS GTM and content strategy advice |
| 2 | The B2B Playbook | B2B YouTube strategy | Directly covers YouTube for B2B companies |
| 3 | Dave Gerhardt | B2B SaaS marketing | Strong voice on B2B brand, content, and marketing strategy |
| 4 | Chris Walker | Demand generation | Useful perspective on demand gen and content-led growth |
| 5 | April Dunford | Positioning | Positioning is important before building any content strategy |
| 6 | Kipp Bodnar / HubSpot | B2B marketing at scale | HubSpot is a strong example of scaled B2B content |
| 7 | Amanda Natividad | Content strategy | Useful ideas around zero-click content and distribution |
| 8 | Justin Welsh | Audience building | Practical systems for content creation and audience growth |
| 9 | Benji Hyam / Grow & Convert | B2B content marketing | Strong source for content that connects to business outcomes |
| 10 | MarketScale | B2B video/media | Focuses on B2B media and expert-led content |

More detailed notes are in [`research/sources.md`](research/sources.md).

## Repository Structure

```txt
research/
├── sources.md
├── youtube-transcripts/
│   ├── tk-kader/
│   ├── b2b-playbook/
│   ├── dave-gerhardt/
│   ├── chris-walker/
│   ├── april-dunford/
│   ├── kipp-bodnar/
│   ├── amanda-natividad/
│   ├── justin-welsh/
│   ├── benji-hyam/
│   └── marketscale/
├── linkedin-posts/
│   ├── tk-kader/
│   ├── dave-gerhardt/
│   ├── april-dunford/
│   ├── kipp-bodnar/
│   └── amanda-natividad/
└── other/
    ├── methodology.md
    ├── preliminary-analysis.md
    └── final-summary.md
```

## How I Collected the Material

For YouTube, I used a small Python workflow:

- `yt-dlp` to search for relevant videos and metadata
- `youtube-transcript-api` to collect transcripts
- Markdown files to organize transcripts by expert/source

The script is included here: [`collect_transcripts.py`](collect_transcripts.py).

For LinkedIn, I collected posts manually because LinkedIn is restrictive with public scraping and API access. I picked posts that were relevant to B2B SaaS content strategy, positioning, demand generation, AI visibility, or content quality.

## Early Takeaways

### 1. Positioning has to come first

A lot of the research points back to positioning. If a company does not know its ICP, category, or point of view, its YouTube content will probably become generic.

### 2. Expert-led content is more credible

For B2B SaaS, buyers seem to trust practitioners more than polished brand content. This makes founder-led or subject-matter-expert-led videos more useful.

### 3. YouTube is useful beyond views

A YouTube video can be reused as LinkedIn posts, short clips, newsletter ideas, sales enablement, or blog content. That makes it valuable even when the direct view count is not huge.

### 4. Quality matters more as AI content increases

AI makes content easier to produce, but it also creates more generic content. Stronger opinions, better taste, and real expertise should stand out more.

### 5. B2B teams should measure influence, not only views

For B2B SaaS, useful signals include sales conversations, buyer education, inbound mentions, pipeline influence, and repurposing value.

## Files Worth Reviewing

- [`research/sources.md`](research/sources.md) — expert list with links and annotations
- [`research/other/methodology.md`](research/other/methodology.md) — how sources were selected and collected
- [`research/other/preliminary-analysis.md`](research/other/preliminary-analysis.md) — early pattern notes
- [`research/other/final-summary.md`](research/other/final-summary.md) — summary of findings
- [`collect_transcripts.py`](collect_transcripts.py) — transcript collection script

## Summary

This research collection is organized to support a future playbook on YouTube content strategy for B2B SaaS. The materials include expert sources, YouTube transcripts, LinkedIn post notes, methodology, and analysis summaries.
