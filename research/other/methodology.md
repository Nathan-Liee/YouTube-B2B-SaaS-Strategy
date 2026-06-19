# Research Methodology

## Topic

**YouTube content strategy for B2B SaaS**

I chose this topic because YouTube is becoming a serious content channel for B2B SaaS companies. It is not only used for brand awareness, but also for buyer education, trust-building, demand generation, and repurposing long-form content into shorter assets for LinkedIn, newsletters, sales enablement, and founder-led content.

## Expert Selection Criteria

The experts were selected based on four criteria:

1. **Direct relevance to B2B SaaS or B2B marketing**  
   I prioritized people who create content about B2B SaaS, demand generation, positioning, content strategy, or B2B growth.

2. **Practitioner credibility**  
   I focused on people who have built, led, advised, or operated inside B2B companies rather than people who only write generic marketing advice.

3. **Useful source material**  
   I selected experts with public YouTube videos, interviews, podcasts, or LinkedIn content that can support a future playbook.

4. **Varied perspective**  
   The list includes SaaS founders, content marketers, CMOs, consultants, and B2B media operators so the research is not based on only one type of opinion.

## Collection Process

### YouTube Transcripts

I used a Python workflow to collect YouTube transcripts:

- `yt-dlp` was used to discover relevant videos and metadata.
- `youtube-transcript-api` was used to collect transcripts from YouTube videos.
- Transcripts were saved as Markdown files and organized by expert under `/research/youtube-transcripts/`.

This makes the research easy to inspect, cite, and analyze later.

### LinkedIn Posts

LinkedIn posts are organized under `/research/linkedin-posts/` by author. Because LinkedIn content is harder to collect reliably through public APIs, these posts are intended to be collected manually from each expert's profile or saved from publicly accessible post URLs.

### Additional Notes

The goal of this repository is not to collect the largest possible dataset. The focus is on high-signal sources that can support a practical B2B SaaS YouTube strategy playbook later.

## Current Dataset

- 10 expert profiles documented in `/research/sources.md`
- 17 YouTube transcripts collected and organized by expert
- Additional analysis notes in `/research/other/`

## Limitations

- Some YouTube videos may not provide public transcripts.
- LinkedIn post collection may require manual review because LinkedIn restricts scraping and API access.
- Subscriber counts and public profile details can change over time, so expert credibility is evaluated more by relevance and practical experience than raw follower count.
