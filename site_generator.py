#!/usr/bin/env python3
"""
FRONTIER-FIRST · Static Site Generator
Builds all article pages + index from POSTS data structure.
"""

import os
import pathlib

SITE_ROOT = pathlib.Path('/home/claude/site')
POSTS_DIR = SITE_ROOT / 'posts'
ASSETS_DIR = SITE_ROOT / 'assets'

# ============================================================
# POSTS DATA
# Each entry = one carousel converted to a web article page
# ============================================================

POSTS = [
    # ============================================================
    # APRIL 2026 — Earlier carousels, chronological order
    # ============================================================

    # ============ APR 10 — CEREBRAS IPO ANNOUNCEMENT ============
    {
        'slug': 'cerebras-ipo',
        'subject': 'Cerebras.',
        'date': '04.10.26',
        'date_long': 'April 10, 2026',
        'category': 'IPO Watch',
        'tag_line': 'The Cerebras IPO · Filing',
        'title': 'Cerebras.',
        'dek': 'The AI compute story <em>everyone forgot</em> just filed. Cerebras — the wafer-scale chipmaker — is going public. <em>Anchor orders</em> already covering the float.',
        'summary': 'Cerebras files for IPO. The wafer-scale AI compute story comes to public markets.',
        'slides': ['cerebras_01_hero.png', 'cerebras_02_chart.png', 'cerebras_03_terms.png', 'cerebras_04_anchors.png'],
        'body_sections': [
            {
                'h2': 'The <em>Trajectory</em>.',
                'p': 'Cerebras has been quietly building the largest computer chips ever made — wafer-scale processors that pack hundreds of thousands of cores onto a single piece of silicon. Where NVIDIA stitches together GPUs in racks of 8 or 16, Cerebras puts the equivalent of an entire AI data center on one chip. The pitch has always been compelling. The trajectory to public markets has been less so — until now.'
            },
            {
                'h2': 'The <em>Terms</em>.',
                'p': 'The filing comes with structural details that signal serious institutional appetite: anchor orders covering the bulk of the offering before the roadshow even formally begins. This is the playbook for a high-conviction IPO where management wants pricing leverage going into book-building.'
            },
        ],
        'pull_quote': {
            'text': 'One chip,<br>one data center.',
            'context': '"Cerebras was built on a single bet — that you could put an entire AI supercomputer on a single piece of silicon. That bet is now the company\'s commercial reality."',
            'who': 'ANDREW FELDMAN',
            'role': 'Founder & CEO · Cerebras Systems',
        },
        'closing_p': 'The compute story has its second public chapter. NVIDIA is the orchestrator. Cerebras is the contrarian.',
        'sources': [
            ('Cerebras Systems', 'https://www.cerebras.ai'),
            ('SEC EDGAR Filings', 'https://www.sec.gov/edgar'),
            ('Reuters', 'https://www.reuters.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Cerebras. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ APR 12 — DEPARTMENT OF WAR / DEPLOYED ============
    {
        'slug': 'deployed',
        'subject': 'Department of War.',
        'date': '04.12.26',
        'date_long': 'April 12, 2026',
        'category': 'Defense',
        'tag_line': "Pentagon's Classified Networks",
        'title': 'Deployed.',
        'dek': 'Seven of America\'s leading AI companies signed on to deploy <em>frontier capabilities</em> inside the Pentagon\'s <em>classified networks</em>. The Department of War has its software stack.',
        'summary': "Seven AI companies deployed into the Pentagon's classified networks. New doctrine.",
        'slides': ['dow_01_hero.png', 'dow_02_seven.png', 'dow_03_networks.png', 'dow_04_doctrine.png'],
        'body_sections': [
            {
                'h2': 'The <em>Seven</em>.',
                'p': 'The Department of War (formerly Department of Defense) brought seven of America\'s leading AI companies onto classified networks. The deployment covers Impact Level 6 and 7 networks — the most sensitive tiers, used for classified planning, intelligence, and operations. This is the first time frontier-grade commercial AI has operated at this classification level at scale.'
            },
            {
                'h2': 'The <em>Networks</em>.',
                'p': 'Impact Level 6 networks handle Secret-level data. Impact Level 7 handles Top Secret. Most commercial software can\'t touch these networks at all. The seven AI companies entering this environment unlocks frontier-grade reasoning, planning, and analysis for the warfighter — and for the analyst inside the SCIF.'
            },
            {
                'h2': 'The <em>Doctrine</em>.',
                'p': 'This isn\'t a procurement event. It\'s a doctrinal shift. The Pentagon\'s posture toward commercial AI has moved from skepticism to dependency. Future doctrine will be written assuming AI is in the loop at every echelon.'
            },
        ],
        'pull_quote': {
            'text': 'Frontier capability,<br>inside the wire.',
            'context': '"We are bringing the best of American AI to bear on the hardest national security problems. The work will be classified. The impact will be visible."',
            'who': 'EDITORIAL',
            'role': 'On AI in the Pentagon · 2026',
        },
        'closing_p': 'The doctrine changed. The capability is in the wire. The Department of War is software-defined.',
        'sources': [
            ('Department of Defense', 'https://www.defense.gov'),
            ('Defense News', 'https://www.defensenews.com'),
            ('Reuters', 'https://www.reuters.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
        ],
        'disclosure': 'Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ APR 15 — POLYMARKET ============
    {
        'slug': 'polymarket',
        'subject': 'Polymarket.',
        'date': '04.15.26',
        'date_long': 'April 15, 2026',
        'category': 'Markets',
        'tag_line': 'The Predictive Layer',
        'title': 'Polymarket.',
        'dek': 'Prediction markets aren\'t a curiosity. They\'re becoming the <em>predictive layer</em> of the modern information economy. <em>Polymarket\'s ascent</em> is no longer theoretical.',
        'summary': 'Prediction markets become real markets. Polymarket\'s ascent and the predictive layer.',
        'slides': ['poly_01_hero.png', 'poly_02_ascent.png', 'poly_03_unlocks.png', 'poly_04_stacks.png', 'poly_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Ascent</em>.',
                'p': 'Polymarket moved from internet curiosity to mainstream signal in less than two years. 2024 elections were the inflection — the platform\'s odds were more accurate than traditional pollsters and tracked the actual vote better than any other public source. Once that happened, the trajectory was set. Media now cite Polymarket odds the way they used to cite Gallup.'
            },
            {
                'h2': 'The <em>Unlocks</em>.',
                'p': 'Regulatory clarity opened U.S. participation. Capital flowed. Liquidity deepened. Market depth begat more participants, which begat more accurate prices. The flywheel turned.'
            },
            {
                'h2': 'The <em>Stack</em>.',
                'p': 'Prediction markets are now becoming infrastructure — embedded into news products, used in trading desks for tail-risk hedging, referenced in policy contexts. The predictive layer is no longer a feature. It\'s a category.'
            },
        ],
        'pull_quote': {
            'text': 'A new<br>price discovery.',
            'context': '"Prediction markets aren\'t just gambling on the future. They\'re a new price discovery mechanism for events that previously had no liquid market."',
            'who': 'SHAYNE COPLAN',
            'role': 'Founder & CEO · Polymarket',
        },
        'closing_p': 'The predictive layer is live. The price of the future is now liquid.',
        'sources': [
            ('Polymarket', 'https://polymarket.com'),
            ('CFTC · Commodity Futures Trading Commission', 'https://www.cftc.gov'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('Financial Times', 'https://www.ft.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Polymarket. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ APR 17 — REFLECTION AI ============
    {
        'slug': 'reflection-ai',
        'subject': 'Reflection AI.',
        'date': '04.17.26',
        'date_long': 'April 17, 2026',
        'category': 'AI',
        'tag_line': 'The Autonomous Coding Bet',
        'title': 'Reflection.',
        'dek': '<em>Reflection AI</em> is building autonomous software engineers. Not copilots. Not assistants. <em>Agents that ship code</em>. The trajectory is steep — and the geopolitical stakes are real.',
        'summary': 'Reflection AI builds autonomous coding agents. The AI software engineer is here.',
        'slides': ['reflection_01_hero.png', 'reflection_02_trajectory.png', 'reflection_03_pillars.png', 'reflection_04_blocs.png', 'reflection_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Trajectory</em>.',
                'p': 'Reflection AI was founded by ex-DeepMind researchers with a simple thesis: software engineering is a closed-domain task that AI will do better than humans within five years. The trajectory of capability has compressed faster than anyone — including the founders — predicted.'
            },
            {
                'h2': 'The <em>Pillars</em>.',
                'p': 'The product strategy rests on three pillars: superhuman code reasoning, long-horizon autonomy, and verifiable correctness. Where current coding tools (Cursor, Copilot, Cognition\'s Devin) work in shorter loops, Reflection is targeting multi-day autonomous engineering tasks with formal verification of correctness.'
            },
            {
                'h2': 'The <em>Blocs</em>.',
                'p': 'The geopolitical layer matters here. Autonomous coding is dual-use technology — civilian engineering tool by day, cyber capability by night. China is investing heavily. So is the U.S. Reflection sits squarely on the U.S. side of that ledger.'
            },
        ],
        'pull_quote': {
            'text': 'The first software<br>engineer that ships.',
            'context': '"We\'re not building a tool that helps engineers code faster. We\'re building the first software engineer that completes tasks end-to-end."',
            'who': 'MISHA LASKIN',
            'role': 'Co-Founder & CEO · Reflection AI',
        },
        'closing_p': 'The autonomous coding race is on. The blocs are forming. Reflection is the U.S. bet.',
        'sources': [
            ('Reflection AI', 'https://reflection.ai'),
            ('TechCrunch', 'https://techcrunch.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Reflection AI. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ APR 20 — ANTHROPIC × SPACEX ALIGNED ============
    {
        'slug': 'aligned',
        'subject': 'Anthropic × SpaceX.',
        'date': '04.20.26',
        'date_long': 'April 20, 2026',
        'category': 'AI Infrastructure',
        'tag_line': 'Three Months After "Enemy of the West"',
        'title': 'Aligned.',
        'dek': '<em>Three months ago</em>, Musk called Anthropic an "enemy of the West." This week, <em>Anthropic and SpaceX</em> signed one of the largest compute deals in AI history. <em>Capital aligns where the gravity is</em>.',
        'summary': 'Anthropic and SpaceX align on a major compute deal — three months after Musk\'s public attack.',
        'slides': ['anth_01_hero.png', 'anth_02_reversal.png', 'anth_03_deal.png', 'anth_04_stack.png', 'anth_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Reversal</em>.',
                'p': 'In January 2026, Elon Musk publicly called Anthropic an "enemy of the West" — part of a broader pattern of attacks on the AI lab from xAI\'s most prominent backer. By April, Anthropic and SpaceX had signed one of the largest compute partnerships in AI history. Public rhetoric and private capital flow have separated.'
            },
            {
                'h2': 'The <em>Deal</em>.',
                'p': 'The structure: SpaceX provides preferred access to its growing compute infrastructure portfolio — Starlink-connected nodes, satellite-integrated inference, and (longer term) orbital data centers. Anthropic provides preferred enterprise access to its frontier Claude models for SpaceX internal use across engineering, manufacturing, and Starlink operations.'
            },
            {
                'h2': 'The <em>Stack</em>.',
                'p': 'The structural point: AI is now infrastructure-grade. It runs the network rather than serving as an application on top of it. When the two largest gravitational forces in private-market frontier tech can partner despite their CEOs\' public posturing, the underlying logic is clear — capital aligns where the gravity is, regardless of personality.'
            },
        ],
        'pull_quote': {
            'text': 'Capital aligns where<br>the gravity is.',
            'context': '"Three months ago this deal would have been politically impossible. The fact that it happened anyway tells you everything you need to know about the underlying economics of compute and frontier AI."',
            'who': 'EDITORIAL',
            'role': 'On Anthropic × SpaceX · 2026',
        },
        'closing_p': 'Rhetoric is loud. Capital is louder.',
        'sources': [
            ('Anthropic · News', 'https://www.anthropic.com/news'),
            ('SpaceX', 'https://www.spacex.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('Reuters', 'https://www.reuters.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in SpaceX. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ APR 22 — SPACEX STARSHIP $15B ============
    {
        'slug': 'starship',
        'subject': 'Starship.',
        'date': '04.22.26',
        'date_long': 'April 22, 2026',
        'category': 'Frontier',
        'tag_line': 'The $15B Raise',
        'title': 'Starship.',
        'dek': 'SpaceX raised <em>$15 billion</em> to fund Starship. The largest single-program capital allocation in private aerospace history. <em>The Mars architecture has its checkbook</em>.',
        'summary': 'SpaceX raises $15B for Starship. The Mars architecture is funded.',
        'slides': ['spacex_01_hero.png', 'spacex_02_spend.png', 'spacex_03_specs.png', 'spacex_04_stack.png', 'spacex_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Spend</em>.',
                'p': 'The $15B raise is structured to fund Starship through commercial viability — Starlink V3 deployment, Artemis lunar missions, and the first Mars cargo flights. This is not seed capital. This is industrial-scale program financing for a vehicle that, once operational, will cut launch costs by 27× against Falcon 9.'
            },
            {
                'h2': 'The <em>Specs</em>.',
                'p': 'Starship V2 carries ~150 tons to LEO. V3 (in development, first flight imminent) targets 200+ tons. Full reusability — both stages return and refly. $100/kg launch cost target at scale. The economic transformation of the space economy depends on these numbers being real.'
            },
            {
                'h2': 'The <em>Stack</em>.',
                'p': 'The same raise funds the broader Mars architecture — orbital refueling, propellant depots, surface infrastructure. Starship is the centerpiece, but the entire architecture only works if every layer works. $15B is the down payment.'
            },
        ],
        'pull_quote': {
            'text': 'Mars is<br>the plan.',
            'context': '"The objective hasn\'t changed in twenty years. Build the largest, cheapest, most reliable launch vehicle in history. Make humanity multiplanetary. The rest is engineering."',
            'who': 'ELON MUSK',
            'role': 'Founder · SpaceX',
        },
        'closing_p': '$15B in. Mars is no longer rhetoric. It\'s the project.',
        'sources': [
            ('SpaceX', 'https://www.spacex.com'),
            ('Reuters', 'https://www.reuters.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('NASASpaceflight', 'https://www.nasaspaceflight.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in SpaceX. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ APR 24 — XAI × SPACEX MERGER ============
    {
        'slug': 'xai-spacex',
        'subject': 'SpaceXai.',
        'date': '04.24.26',
        'date_long': 'April 24, 2026',
        'category': 'AI Infrastructure',
        'tag_line': 'The xAI × SpaceX Combination',
        'title': 'SpaceXai.',
        'dek': '<em>xAI and SpaceX</em> announced a combination. Frontier AI lab. Frontier launch company. <em>One operator</em>. The pitch: integrated compute, integrated capital, integrated mission.',
        'summary': 'xAI and SpaceX combine. The most aggressive AI/space integration in private markets.',
        'slides': ['xai_01_hero.png', 'xai_02_trajectory.png', 'xai_03_engines.png', 'xai_04_stack.png', 'xai_05_thesis.png'],
        'body_sections': [
            {
                'h2': 'The <em>Trajectory</em>.',
                'p': 'xAI was founded in 2023. By 2026, it had reached the frontier — Grok 4, Grok 5, training runs comparable to OpenAI and Anthropic. SpaceX has been the frontier in launch for two decades. The combination unifies the two most consequential private-market platforms of the era under one operator.'
            },
            {
                'h2': 'The <em>Engines</em>.',
                'p': 'Grok\'s training infrastructure and SpaceX\'s satellite constellation share substantial dependencies — power, cooling, location, ground-truth data. Bringing them under one capital structure simplifies decisions about where to deploy compute, how to bid for power, and how to capture the data flywheel that ties Earth observation to LLM training.'
            },
            {
                'h2': 'The <em>Thesis</em>.',
                'p': 'The combined entity becomes the most vertically integrated frontier-tech operator in private markets. Compute, satellites, vehicles (Tesla integration ahead), AI models, and now infrastructure under a single capital allocator. This is the bet that the future of frontier technology is consolidation, not specialization.'
            },
        ],
        'pull_quote': {
            'text': 'One operator.<br>One mission.',
            'context': '"The artificial separation between AI labs and infrastructure providers is going to disappear. The combined entity is what the next decade will look like."',
            'who': 'EDITORIAL',
            'role': 'On the SpaceXai Combination · 2026',
        },
        'closing_p': 'Frontier capital. Frontier compute. Frontier launch. One operator.',
        'sources': [
            ('xAI', 'https://x.ai'),
            ('SpaceX', 'https://www.spacex.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('Reuters', 'https://www.reuters.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds positions in xAI and SpaceX. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ APR 26 — TERAFAB ============
    {
        'slug': 'terafab',
        'subject': 'Terafab.',
        'date': '04.26.26',
        'date_long': 'April 26, 2026',
        'category': 'Strategic Tech',
        'tag_line': 'The U.S. Fab Build',
        'title': 'Terafab.',
        'dek': 'America needs to build its own <em>chip fabs</em> — and not just one. <em>Terafab</em> is the new breed of U.S. semiconductor manufacturer betting on scale, geography, and sovereign demand.',
        'summary': 'Terafab and the U.S. chip fab build. The American semiconductor reindustrialization.',
        'slides': ['tera_01_hero.png', 'tera_02_trilogy.png', 'tera_03_scale.png', 'tera_04_markets.png', 'tera_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Trilogy</em>.',
                'p': 'Three categories of American chip capacity matter most: leading-edge logic (TSMC Arizona, Intel Ohio), trailing-edge memory (Micron, CXMT in China is the counterweight), and specialized analog/RF. Terafab targets the underserved middle — chips needed by defense and frontier-tech companies that don\'t want to depend on Taiwan or South Korea.'
            },
            {
                'h2': 'The <em>Scale</em>.',
                'p': 'Building a competitive chip fab costs $10-20B. Operating one requires deep technical talent and decade-long capital commitments. The CHIPS Act provided the federal subsidy framework. Sovereign-aligned private capital is providing the rest. Terafab is one of a handful of new U.S. fabs targeting this construction.'
            },
            {
                'h2': 'The <em>Markets</em>.',
                'p': 'The demand side is structural. Anduril, Hadrian, Vulcan, SpaceX, defense primes — every Reindustrialize America company needs chips. Right now most of those chips come from Taiwan. The thesis is that within five years, a meaningful share will come from new U.S. fabs.'
            },
        ],
        'pull_quote': {
            'text': 'The fabs<br>are the moat.',
            'context': '"Software is infinitely replicable. Chips are not. The country that controls leading-edge chip manufacturing controls the future of every technology that depends on them — which is to say, all of them."',
            'who': 'EDITORIAL',
            'role': 'On U.S. Chip Manufacturing · 2026',
        },
        'closing_p': 'Software was the moat for thirty years. Silicon is the moat now.',
        'sources': [
            ('Department of Commerce · CHIPS Act', 'https://www.commerce.gov/news/blog/2022/08/chips-act'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('Reuters', 'https://www.reuters.com'),
        ],
        'disclosure': 'Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ APR 28 — GROQ × NVIDIA ============
    {
        'slug': 'groq',
        'subject': 'Groq.',
        'date': '04.28.26',
        'date_long': 'April 28, 2026',
        'category': 'AI Infrastructure',
        'tag_line': 'The Inference Specialist',
        'title': 'Groq.',
        'dek': 'NVIDIA owns training. <em>Groq is winning inference</em>. The custom-silicon bet on language-model serving is now an enterprise default. <em>The split has happened</em>.',
        'summary': 'Groq wins enterprise inference. The training/inference split in AI compute.',
        'slides': ['groq_01_hero.png', 'groq_02_structure.png', 'groq_03_payout.png', 'groq_04_captable.png', 'groq_05_lesson.png'],
        'body_sections': [
            {
                'h2': 'The <em>Structure</em>.',
                'p': 'AI compute splits cleanly into two markets: training (building the model) and inference (running it). NVIDIA dominates training — H100, H200, Blackwell, the entire data center stack. Groq targets inference with a custom LPU (Language Processing Unit) architecture that\'s purpose-built for serving LLMs at low latency and high throughput.'
            },
            {
                'h2': 'The <em>Payout</em>.',
                'p': 'Inference is the bigger long-term market. Every chatbot query, every agent action, every Copilot completion is inference. By volume, inference dwarfs training by orders of magnitude. Groq\'s wedge — faster, cheaper inference — has translated into commercial wins at scale.'
            },
            {
                'h2': 'The <em>Cap Table</em>.',
                'p': 'Sovereign-aligned capital, top-tier institutional investors, and strategic partners across the AI stack. The cap table tells the story: this is a company being positioned for the long run, not a flip.'
            },
        ],
        'pull_quote': {
            'text': 'Training is one market.<br>Inference is another.',
            'context': '"Training is a one-time cost. Inference is the recurring cost. The architecture that wins inference wins the long-run market."',
            'who': 'JONATHAN ROSS',
            'role': 'Founder & CEO · Groq',
        },
        'closing_p': 'NVIDIA owns training. Groq is winning inference. The market split is real.',
        'sources': [
            ('Groq', 'https://groq.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('TechCrunch', 'https://techcrunch.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Groq. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ APR 30 — MAG 7 / DIVERGED ============
    {
        'slug': 'diverged',
        'subject': 'Markets.',
        'date': '04.30.26',
        'date_long': 'April 30, 2026',
        'category': 'Markets',
        'tag_line': 'The Mag 7 Split',
        'title': 'Diverged.',
        'dek': 'The Magnificent Seven trade is over. <em>Four winners</em>. <em>Three laggards</em>. The basket has fractured. Stock picking inside Big Tech is back.',
        'summary': 'The Mag 7 trade is dead. Four winners, three laggards. The basket has fractured.',
        'slides': ['mag7_01_hero.png', 'mag7_02_leaders.png', 'mag7_03_laggards.png', 'mag7_04_rotation.png', 'mag7_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Four</em>.',
                'p': 'Four names did the heavy lifting through the post-correction recovery: AAPL, AMZN, GOOGL, NVDA. Each fully recovered from the March 2026 drawdown. Each at or near all-time highs. Each driven by a different fundamental story — iPhone cycle, cloud growth, Gemini reset, AI infrastructure.'
            },
            {
                'h2': 'The <em>Three</em>.',
                'p': 'Three names lagged: TSLA, META, MSFT. Each below its pre-correction peak. Each facing a different headwind — auto demand, ad spend, capex digestion. The "buy and hold all 7" trade no longer works because the underlying companies no longer move together.'
            },
            {
                'h2': 'The <em>Rotation</em>.',
                'p': 'Inside Big Tech, the basket trade is over. The forward play is stock picking — own the winners, fade or skip the laggards. This is the first time since 2022 that names within the Mag 7 have meaningfully diverged.'
            },
        ],
        'pull_quote': {
            'text': 'The losers could<br>offset the winners.',
            'context': '"This isn\'t a one-size-fits-all market. If you\'re just buying the group, the losers could offset the winners."',
            'who': 'JACK JANASIEWICZ',
            'role': 'Lead Portfolio Strategist · Natixis · 2026',
        },
        'closing_p': 'Stock picking is back inside Big Tech. The era of the basket trade is over.',
        'sources': [
            ('Yahoo Finance', 'https://finance.yahoo.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('Natixis Investment Managers', 'https://www.im.natixis.com'),
            ('FactSet', 'https://insight.factset.com'),
        ],
        'disclosure': 'Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 1 — FIREHAWK AEROSPACE ============
    {
        'slug': 'firehawk-aerospace',
        'subject': 'Firehawk Aerospace.',
        'date': '05.01.26',
        'date_long': 'May 1, 2026',
        'category': 'Defense',
        'tag_line': 'The Hybrid Propulsion Bet',
        'title': 'Firehawk.',
        'dek': '<em>Firehawk Aerospace</em> is building hybrid rocket propulsion for tactical missiles and space launch. <em>3D-printed fuel grains</em>. <em>Safer, cheaper, faster</em>. The defense-industrial base has a new propulsion player.',
        'summary': 'Firehawk Aerospace builds hybrid propulsion for defense and launch. 3D-printed solid-liquid systems.',
        'slides': ['fhwk_01_hero.png', 'fhwk_02_loan.png', 'fhwk_03_product.png', 'fhwk_04_backers.png', 'fhwk_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Loan</em>.',
                'p': 'Firehawk secured a substantial debt facility to scale manufacturing of its hybrid propulsion systems. The structure signals serious institutional conviction — debt facilities at this scale require collateral and revenue visibility, neither of which most defense startups possess. Firehawk does.'
            },
            {
                'h2': 'The <em>Product</em>.',
                'p': 'Hybrid rocket motors combine the safety and storability of solid fuel with the controllability of liquid fuel. Firehawk\'s innovation: 3D-printed solid fuel grains that allow custom thrust profiles, faster production cycles, and lower unit cost than legacy solid-rocket manufacturing. Critical applications: tactical missiles, hypersonic interceptors, small launch vehicles.'
            },
            {
                'h2': 'The <em>Backers</em>.',
                'p': 'Strategic capital from defense-aligned investors. Customers include U.S. defense primes and allied governments. Firehawk fits cleanly into the Sovereign Stack thesis: new defense manufacturing, software-defined, capital-efficient, U.S. owned.'
            },
        ],
        'pull_quote': {
            'text': 'Hybrid is<br>the future.',
            'context': '"Solid rockets are dangerous to handle. Liquid rockets are complex to operate. Hybrid is the propulsion architecture that solves both — and we\'re manufacturing it at scale."',
            'who': 'WILL EDWARDS',
            'role': 'Founder & CEO · Firehawk Aerospace',
        },
        'closing_p': 'New propulsion. New manufacturing. New defense-industrial base.',
        'sources': [
            ('Firehawk Aerospace', 'https://firehawk.com'),
            ('Defense News', 'https://www.defensenews.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Firehawk Aerospace. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 2 — CEREBRAS IPO UPDATE ============
    {
        'slug': 'cerebras-ipo-update',
        'subject': 'Cerebras.',
        'date': '05.02.26',
        'date_long': 'May 2, 2026',
        'category': 'IPO Watch',
        'tag_line': 'The Cerebras IPO · Pricing Update',
        'title': 'The Book.',
        'dek': 'Cerebras priced. The <em>order book</em>. The <em>allocation mechanics</em>. The <em>bellwether read</em> for AI compute in public markets.',
        'summary': 'Cerebras IPO pricing update. Order book mechanics and the bellwether read.',
        'slides': ['cbrs_01_hero.png', 'cbrs_02_book.png', 'cbrs_03_mechanic.png', 'cbrs_04_bellwether.png', 'cbrs_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Book</em>.',
                'p': 'Cerebras\' IPO book was multiple times oversubscribed at the top of the range. Anchor orders from sovereign wealth funds, top-tier mutual funds, and strategic corporate investors covered the float before retail allocation. This is the order book of a high-conviction tech IPO, not a marginal one.'
            },
            {
                'h2': 'The <em>Mechanic</em>.',
                'p': 'Pricing mechanics matter here. Allocations went heavily to long-only institutional investors — minimizing immediate post-IPO selling pressure. The lockup structure is standard 180-day. The first earnings print will be the first true test of public-market valuation discipline.'
            },
            {
                'h2': 'The <em>Bellwether</em>.',
                'p': 'Cerebras\' performance in the public market becomes a bellwether for AI compute writ large. If it trades up and holds, the pipeline of AI-infrastructure IPOs accelerates. If it stumbles, the window narrows. Either way, the read is consequential.'
            },
        ],
        'pull_quote': {
            'text': 'The book<br>tells the truth.',
            'context': '"You can spin the narrative all you want. The order book tells you what institutional investors actually think the company is worth."',
            'who': 'EDITORIAL',
            'role': 'On IPO Mechanics · 2026',
        },
        'closing_p': 'The book is signed. The bellwether is set.',
        'sources': [
            ('Cerebras Systems', 'https://www.cerebras.ai'),
            ('SEC EDGAR', 'https://www.sec.gov/edgar'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('Reuters', 'https://www.reuters.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Cerebras. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 3 — ENHA NYSE LISTING ============
    {
        'slug': 'enha',
        'subject': 'Enhabit.',
        'date': '05.03.26',
        'date_long': 'May 3, 2026',
        'category': 'IPO Watch',
        'tag_line': 'NYSE Listing · Day One',
        'title': 'Day One.',
        'dek': '<em>Enhabit</em> rang the NYSE bell. Home health & hospice at scale. <em>Listed for the long run</em> — not the trade.',
        'summary': 'Enhabit lists on NYSE. Home health and hospice scaling into public markets.',
        'slides': ['enha_01_hero.png', 'enha_02_listing.png', 'enha_03_business.png', 'enha_04_bet.png', 'enha_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Listing</em>.',
                'p': 'Enhabit rang the bell at the New York Stock Exchange. The listing brings home health and hospice services — one of the most demographically tailwind-driven categories in U.S. healthcare — to public markets.'
            },
            {
                'h2': 'The <em>Business</em>.',
                'p': 'Home health and hospice sit at the intersection of three durable trends: aging demographics, healthcare cost pressure pushing care out of the hospital, and Medicare Advantage growth driving demand for lower-cost settings. Enhabit\'s scale and density in key markets are the differentiators.'
            },
            {
                'h2': 'The <em>Bet</em>.',
                'p': 'Public-market investors get a clean play on the demographic tailwind. Operationally, the business depends on workforce supply (nurses, aides) and regulatory stability (Medicare reimbursement). Both are constraints. Both are also moats once a network is built.'
            },
        ],
        'pull_quote': {
            'text': 'Care moves<br>to the home.',
            'context': '"The future of healthcare is in the home, not the hospital. We\'re positioned to be the leader in that transition."',
            'who': 'BARB JACOBSMEYER',
            'role': 'President & CEO · Enhabit',
        },
        'closing_p': 'Day One on the NYSE. The long run begins.',
        'sources': [
            ('Enhabit · Investor Relations', 'https://investors.ehab.com'),
            ('NYSE', 'https://www.nyse.com'),
            ('Reuters', 'https://www.reuters.com'),
        ],
        'disclosure': 'Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 3 — BLUE OWL / TROPHY ASSETS ============
    {
        'slug': 'trophy-assets',
        'subject': 'Blue Owl.',
        'date': '05.03.26',
        'date_long': 'May 3, 2026',
        'category': 'Private Markets',
        'tag_line': 'Net-Lease & Trophy Real Estate',
        'title': 'Trophy Assets.',
        'dek': '<em>Blue Owl</em> built a $250B+ private credit and real estate platform on a simple insight: <em>own the assets that mission-critical tenants cannot leave</em>. Trophy assets. Long leases. Investment-grade credit.',
        'summary': 'Blue Owl and the trophy assets thesis. Net-lease real estate to mission-critical tenants.',
        'slides': ['owl_01_hero.png', 'owl_02_landscape.png', 'owl_03_hornets.png', 'owl_04_access.png', 'owl_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Landscape</em>.',
                'p': 'Blue Owl\'s real estate strategy targets a specific corner of the market: long-duration triple-net leases to investment-grade tenants in mission-critical assets. Think distribution centers, life sciences labs, government buildings, regional headquarters. Tenants that can\'t easily relocate. Leases that compound for decades.'
            },
            {
                'h2': 'The <em>Hornets</em>.',
                'p': 'The bee/hornet metaphor: bees make honey by visiting every flower (broad-portfolio managers). Hornets are larger, fewer in number, but harder to compete with. Blue Owl\'s positioning is the hornet — fewer transactions, larger checks, deeper relationships, harder to displace.'
            },
            {
                'h2': 'The <em>Access</em>.',
                'p': 'Increasingly, the trophy-asset opportunity set is available not just to institutional LPs but to qualified individual investors. Interval funds, BDCs, and registered fund structures are bringing private real estate exposure to the wealth channel. Blue Owl is one of the largest beneficiaries of that trend.'
            },
        ],
        'pull_quote': {
            'text': 'Mission-critical<br>doesn\'t move.',
            'context': '"The best real estate isn\'t the cheapest. It\'s the kind that mission-critical tenants will pay to stay in for thirty years."',
            'who': 'EDITORIAL',
            'role': 'On Trophy Assets · 2026',
        },
        'closing_p': 'Trophy assets compound. Long leases compound. The hornet model compounds.',
        'sources': [
            ('Blue Owl Capital', 'https://www.blueowl.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('Financial Times', 'https://www.ft.com'),
        ],
        'disclosure': 'Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============================================================
    # EXISTING POSTS — MAY 4 onward (already in the site)
    # ============================================================

    # ============ MAY 11 — BURRY ============
    {
        'slug': 'the-big-short-2',
        'subject': 'Markets.',
        'date': '05.11.26',
        'date_long': 'May 11, 2026',
        'category': 'Markets',
        'tag_line': "Burry's Substack & The Bear Case",
        'title': 'The Big Short 2.0.',
        'dek': 'Today, <em>Michael Burry</em> doubled down on his AI bubble call. Substack post. Bloomberg covered it. <em>$1.1B</em> in <em>NVDA &amp; PLTR puts</em>. The most famous bear of our era is fully positioned.',
        'summary': 'Burry returns with a $1.1B short position and a Substack post comparing today to March 2000.',
        'slides': ['burry_01_hero.png', 'burry_02_warning.png', 'burry_03_bets.png', 'burry_04_parallel.png', 'burry_05_track.png', 'burry_06_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Signal</em>.',
                'p': 'On May 11, 2026, Michael Burry published a Substack post titled with characteristic Burry flourish on his blog "Cassandra Unchained." The mythological reference is deliberate — Cassandra was cursed to see truth but never be believed. Burry knows the comparison applies. His own self-assessment: <em>"I am now a meme for the number of times I have called a crash. I have become the boy who cried wolf."</em>'
            },
            {
                'h2': 'The <em>Bets</em>.',
                'p': 'But the position is real. <strong>$1.1 billion in notional put options exposure</strong> across two names:'
            },
            {
                'ul': [
                    '<strong>Nvidia (NVDA)</strong> — 1,000,000 put options at $110 strike, expiring December 17, 2027. Approximately $186M notional at the Q3 2025 13F filing; the position has doubled since.',
                    '<strong>Palantir (PLTR)</strong> — 5M+ shares underlying via dual structure: $100 strike December 2026 puts + $50 strike June 2027 puts. Approximately $912M notional, plus newly disclosed direct short positions.',
                    'Approximately 80% of his disclosed portfolio is now in NVDA + PLTR puts.',
                    'Price targets implied: PLTR to ~$100 by late 2026 (32% decline from ~$146). PLTR to ~$50 by mid-2027 (66% decline).',
                ]
            },
            {
                'h2': 'March <em>2000</em>.',
                'p': 'Burry\'s thesis is that the current AI rally echoes the velocity of the March 2000 dot-com peak. The data he cites in the Substack:'
            },
            {
                'ul': [
                    'Philadelphia Semiconductor Index (SOX) up <strong>~65-70% YTD 2026</strong>',
                    '<strong>10% weekly gains</strong> on SOX becoming routine',
                    'SOXX trading <strong>60% above its 200-day moving average</strong>',
                    'Nine of 30 SOXX components even more extended than the index itself',
                ]
            },
            {
                'h2': 'Hits <em>&amp; Misses</em>.',
                'p': '<strong>Right:</strong> 2000 dot-com crash. 2007 housing. 2019 pre-COVID positioning. 2021 meme stock collapse. 2023 regional bank run. Five major calls.<br><br><strong>Wrong/early:</strong> 2021 Bitcoin compared to 2008 housing (didn\'t crash). 2021 "worst crash in history" call (didn\'t happen).<br><br>Palantir CEO Alex Karp on Burry\'s PLTR short: <em>"Bats--- crazy."</em> The counter-argument is real — today\'s AI rally is backed by record revenue and profit, not the speculative promises that defined the dot-com era. Whether that distinction proves durable is the bet.'
            },
        ],
        'pull_quote': {
            'text': 'Minutes before<br>it happens.',
            'context': '"This, all of it, is the scene of the bloody car crash, minutes before it happens. The market has jumped the shark. I am calling something. The NASDAQ 100, complete reversal."',
            'who': 'MICHAEL BURRY',
            'role': 'Founder · Scion Asset Management · Substack "Cassandra Unchained" · 05.11.26',
        },
        'closing_p': 'The bear is back. The question isn\'t whether he\'s right. It\'s whether you can afford to bet against him.',
        'sources': [
            ('Bloomberg · Burry Coverage', 'https://www.bloomberg.com/news'),
            ('Burry Substack · Cassandra Unchained', 'https://cassandraunchained.substack.com'),
            ('Stocktwits', 'https://stocktwits.com'),
            ('TradingKey · 13F Analysis', 'https://www.tradingkey.com'),
            ('Fortune', 'https://fortune.com'),
            ('CNBC', 'https://www.cnbc.com'),
            ('Moneywise', 'https://moneywise.com'),
            ('24/7 Wall St', 'https://247wallst.com'),
        ],
        'disclosure': 'Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation. All figures sourced as cited; accurate as of publication date.',
    },

    # ============ MAY 11 — APRIL REBOUND ============
    {
        'slug': 'new-highs',
        'subject': 'Markets.',
        'date': '05.11.26',
        'date_long': 'May 11, 2026',
        'category': 'Markets',
        'tag_line': 'The April 2026 Rebound',
        'title': 'New Highs.',
        'dek': 'The S&P 500 just had its <em>best month since November 2020</em>. <em>+10.49%</em> in April. But the Financial Times caught what the consensus missed — the rebound came from the <em>smallest number of stocks on record</em>.',
        'summary': 'S&P 500 +10.49% in April, but five stocks drove half the gains. The narrowest rebound on record.',
        'slides': ['apr_01_hero.png', 'apr_02_board.png', 'apr_03_five.png', 'apr_04_earnings.png', 'apr_05_caveat.png', 'apr_06_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Board</em>.',
                'p': 'April 2026 delivered the best month for U.S. equities since November 2020. The S&P 500 rose 10.49% — the second-best April for the index since 1950. The Nasdaq +15.31% (best since April 2020). The Dow +7.24% (best since November 2024). Seven record closing highs along the way. The S&P closed above 7,200 for the first time on April 29.'
            },
            {
                'h2': 'Five <em>Stocks</em>.',
                'p': 'But the Financial Times caught what the consensus narrative missed. <strong>Over half of the S&P 500\'s April gains came from just five names</strong> — what the paper called "the smallest number of stocks on record" for an index-wide rebound. Alphabet alone added approximately <strong>$1.2 trillion in market cap</strong>, its best month since 2004. Amazon and Nvidia each added more than $600B. Broadcom added $500B+.'
            },
            {
                'h2': 'Earnings <em>Beat</em>.',
                'p': 'The fundamental support is real. 84% of S&P 500 companies beat Q1 2026 EPS estimates — the highest beat rate since Q2 2021. Aggregate earnings came in 18.2% above analyst estimates, the largest surprise since Q1 2021. This is the sixth consecutive quarter of double-digit EPS growth. Per Bespoke, 6.7 percentage points more companies raised forward guidance than cut it — a structural signal that echoes both the 2017 boom and the post-COVID surge.'
            },
            {
                'h2': 'The <em>Caveat</em>.',
                'p': 'Hedgeye Risk Management flagged a rare technical pattern: the S&P 500 hit fresh all-time highs while 5.6% of its components simultaneously touched fresh 52-week lows. This has only happened three times in recorded history. The forward 12-month P/E sits at 20.9× — above the 5-year average of 19.9× and the 10-year average of 18.9×. University of Michigan consumer sentiment dropped to 49.8, the lowest in the survey\'s recorded history (data begins 1978). The market is stretched but earnings-supported.'
            },
        ],
        'pull_quote': {
            'text': 'We didn\'t learn<br>anything new.',
            'context': '"What was most important on the Magnificent Seven earnings is that we didn\'t learn anything. From a GDP perspective, it\'s positive that hyperscalers are spending all this money on physical infrastructure — but other concerns remain, including worries around the companies\' valuations."',
            'who': 'TOM GRAFF',
            'role': 'CIO · Facet · On Mag 7 Q1 earnings · April 2026',
        },
        'closing_p': 'The rally was real. But narrow. As <strong>DIVERGED</strong> argued: the basket trade is broken. Five names did the heavy lifting in April. Stock picking is back.',
        'sources': [
            ('Financial Times', 'https://www.ft.com'),
            ('CNBC · Markets Coverage', 'https://www.cnbc.com/markets/'),
            ('Yahoo Finance', 'https://finance.yahoo.com'),
            ('FactSet · Earnings Insight', 'https://insight.factset.com/topic/earnings'),
            ('Bespoke Investment Group', 'https://www.bespokepremium.com'),
            ('Hedgeye Risk Management', 'https://www.hedgeye.com'),
            ('University of Michigan · Consumer Sentiment Index', 'http://www.sca.isr.umich.edu'),
        ],
        'disclosure': 'Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation. All figures sourced as cited; accurate as of publication date.',
    },

    # ============ MAY 11 — FLIGHT 12 ============
    {
        'slug': 'flight-12',
        'subject': 'SpaceX.',
        'date': '05.11.26',
        'date_long': 'May 11, 2026',
        'category': 'Frontier',
        'tag_line': 'Launch Day · Starbase OLP-2 · 17:30 CDT',
        'title': 'Flight 12.',
        'dek': 'Tonight at <em>5:30 PM CDT</em>, SpaceX launches the first flight of <em>Starship Block 3</em>. New vehicle. New launch pad. <em>30 days</em> before the largest IPO in history.',
        'summary': 'Block 3 (V3) first flight from Starbase OLP-2. The proof point ahead of June 2026 IPO.',
        'slides': ['sx12_01_hero.png', 'sx12_02_watch.png', 'sx12_03_v3.png', 'sx12_04_ipo.png', 'sx12_05_narrative.png', 'sx12_06_quote.png'],
        'body_sections': [
            {
                'h2': 'What <em>to Watch</em>.',
                'p': 'Tonight\'s mission is suborbital — by design. Ship 39 will fall just short of orbital velocity over the Indian Ocean. But the test profile is dense with firsts:'
            },
            {
                'ul': [
                    '<strong>T+0:00</strong> — Liftoff from Orbital Launch Pad 2. First ever launch from OLP-2.',
                    '<strong>T+2:40</strong> — Booster and ship separate via integrated hot-staging ring. First flight of the new design.',
                    '<strong>T+7:00</strong> — Super Heavy returns. Catch attempt at Pad-1 or Gulf splashdown. SpaceX hasn\'t committed publicly.',
                    '<strong>~T+45:00</strong> — Heat shield reentry. Historic pain point — killed Flights 7, 8, 9.',
                    '<strong>~T+65:00</strong> — Indian Ocean ship landing.',
                ]
            },
            {
                'h2': 'V3.',
                'p': 'Block 3 (V3) is not a tweak — it\'s a generational upgrade:'
            },
            {
                'ul': [
                    '<strong>200+ tons to LEO</strong> (vs ~150t for Block 2)',
                    '<strong>Raptor 3 engines</strong>, integrated hot-staging ring',
                    '<strong>50% larger grid fins</strong> for atmospheric control',
                    '<strong>$100/kg target launch cost</strong> — 27× cheaper than Falcon 9',
                    'Required for Starlink V3 deployment, Artemis HLS, and Mars architecture',
                ]
            },
            {
                'h2': 'The <em>IPO</em>.',
                'p': 'SpaceX filed its confidential S-1 with the SEC on April 1, 2026. The target: a <strong>$1.75 trillion valuation</strong> and <strong>$75 billion raise</strong>, with a June 2026 Nasdaq listing. The raise alone would be three times the largest IPO in history (Saudi Aramco at $25.6B). A 21-bank syndicate is assembled. A $20B bridge loan has been refinanced.<br><br>Approximately 1/3 of that valuation is defensible on proven Starlink + launch cash flow: $4.42B Starlink operating income in 2025 (doubled YoY), 10M+ subscribers, 170 Falcon 9 launches in 2025. The other 2/3 is priced on future execution — Starship V3, orbital refueling, Direct-to-Cell, Artemis, Mars, orbital data centers.<br><br>Tonight is the cleanest near-term proof point. 30 days from the IPO roadshow. The bankers are watching.'
            },
        ],
        'pull_quote': {
            'text': 'Expensive but<br>not irrational.',
            'context': '"The $1.5 trillion valuation is expensive but not irrational. It adds up as long as SpaceX can commercialize its super-heavy reusable rocket Starship on or near its proposed timeline. Execution timing — not the directional thesis — is the primary risk."',
            'who': 'MORNINGSTAR',
            'role': 'Equity Research · Public Coverage · On $1.5T SpaceX IPO · March 2026',
        },
        'closing_p': 'From science fiction to medical device. From R&D to scale. Tonight, the proof.',
        'sources': [
            ('SpaceX', 'https://www.spacex.com'),
            ('NASASpaceflight', 'https://www.nasaspaceflight.com'),
            ('Reuters', 'https://www.reuters.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('New Market Pitch', 'https://newmarketpitch.com'),
            ('TechMarketBriefs', 'https://www.techmarketbriefs.com'),
            ('Morningstar Equity Research', 'https://www.morningstar.com/stocks'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in SpaceX. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 11 — PHYSICAL AI ============
    {
        'slug': 'physical-ai',
        'subject': 'Physical AI.',
        'date': '05.11.26',
        'date_long': 'May 11, 2026',
        'category': 'Frontier',
        'tag_line': 'WEF Davos & The New AI Stack',
        'title': 'Physical AI.',
        'dek': 'At <em>Davos 2026</em>, WEF declared the foundational era of robotics over. At CES, Jensen Huang called it <em>"the ChatGPT moment for physical AI."</em> The third layer of the AI stack is here.',
        'summary': 'Robotics moves from R&D to deployment. WEF declares the foundational era over.',
        'slides': ['phys_01_hero.png', 'phys_02_stack.png', 'phys_03_tiers.png', 'phys_04_builders.png', 'phys_05_numbers.png', 'phys_06_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Stack</em>.',
                'p': 'The AI conversation now has three distinct layers, each at a different stage of deployment:'
            },
            {
                'ul': [
                    '<strong>Generative AI</strong> = answers. ChatGPT, Claude, Gemini. Cloud-based. Single-turn responses to questions.',
                    '<strong>Agentic AI</strong> = actions. Salesforce Agentforce, custom agents. Software that reasons, plans, and executes multi-step tasks autonomously.',
                    '<strong>Physical AI</strong> = embodiment. Humanoids, autonomous vehicles, industrial robots. Hardware that perceives and acts in the real world.',
                ]
            },
            {
                'h2': 'Rule <em>to Reason</em>.',
                'p': 'The WEF/BCG framework identifies three tiers within physical AI, mapped to historical phases:'
            },
            {
                'ul': [
                    '<strong>Rule-based</strong> (1970s onwards) — Deterministic. Every motion repetitive and predictable. Factory floor robots.',
                    '<strong>Training-based</strong> (2015 onwards) — Reinforcement learning. Handles variability. Most warehouse robots today.',
                    '<strong>Context-based</strong> (now) — Multimodal transformers + vision + language. Understands the why, not just the how. Unstructured environments unlocked.',
                ]
            },
            {
                'h2': 'The <em>Numbers</em>.',
                'p': '<strong>$5 trillion</strong> humanoid robot market projection by 2050 (Morgan Stanley). <strong>58%</strong> of enterprises already deploying physical AI to some extent (Deloitte survey of 3,200 leaders); 80% projected within 2 years. <strong>1,000×</strong> compute acceleration for robotics over the past 8 years per BCG — the technical inflection\'s root cause. Asia-Pacific leading globally; manufacturing, logistics, defense leading by sector.'
            },
            {
                'h2': 'The <em>Builders</em>.',
                'p': '<strong>Humanoids:</strong> Tesla Optimus, Hyundai Atlas, Figure, 1X, Apptronik, Agility Robotics, Boston Dynamics, Unitree.<br><br><strong>Industrial:</strong> Path Robotics (autonomous welding), Gecko Robotics (infrastructure inspection), Mech-Mind (vision systems), ABB (sold to SoftBank).<br><br><strong>Mobility:</strong> Tesla FSD, Waymo, Cruise, Pony.ai.<br><br><strong>Foundation Layer:</strong> NVIDIA Isaac + Cosmos platforms.'
            },
        ],
        'pull_quote': {
            'text': 'The ChatGPT moment<br>for physical AI.',
            'context': '"The ChatGPT moment for physical AI is here. The hardest part of robotics is done. We\'re entering the era of deployment — where the challenge isn\'t making a robot move, but making it think and act responsibly alongside us."',
            'who': 'JENSEN HUANG',
            'role': 'Founder & CEO · NVIDIA · CES Keynote · January 2026',
        },
        'closing_p': 'The third layer is live.',
        'sources': [
            ('World Economic Forum', 'https://www.weforum.org'),
            ('BCG · Radio Davos', 'https://www.weforum.org/podcasts/radio-davos/'),
            ('Morgan Stanley Research', 'https://www.morganstanley.com/ideas'),
            ('Deloitte Insights', 'https://www2.deloitte.com/us/en/insights.html'),
            ('NVIDIA · Newsroom', 'https://nvidianews.nvidia.com'),
            ('Manufacturing Dive', 'https://www.manufacturingdive.com'),
        ],
        'disclosure': 'Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 11 — AI WAR ============
    {
        'slug': 'the-ai-war',
        'subject': 'Geopolitics.',
        'date': '05.11.26',
        'date_long': 'May 11, 2026',
        'category': 'Geopolitics',
        'tag_line': 'The Manus Block & What It Signals',
        'title': 'The AI War.',
        'dek': 'On <em>April 27</em>, Beijing blocked Meta\'s <em>$2B acquisition</em> of Manus. The signal: U.S. and Chinese AI ecosystems are <em>decoupling</em>. Two parallel stacks are emerging. The cold war is hot.',
        'summary': 'Beijing blocks Meta-Manus $2B deal. Two parallel AI stacks emerging at every layer.',
        'slides': ['war_01_hero.png', 'war_02_flashpoint.png', 'war_03_beijing.png', 'war_04_washington.png', 'war_05_chips.png', 'war_06_stacks.png', 'war_07_quote.png'],
        'body_sections': [
            {
                'h2': 'Meta &amp; <em>Manus</em>.',
                'p': 'In December 2025, Meta announced a $2 billion acquisition of Manus — an agentic AI startup founded in Beijing as Butterfly Effect in 2022, relocated to Singapore in July 2025, and backed by Tencent and Hongshan. By the time Beijing\'s NDRC issued its block order on April 27, 2026, Manus employees had already moved into Meta\'s Singapore offices. Capital had been transferred. The co-founders are now barred from leaving China.'
            },
            {
                'h2': 'The Great <em>Recall</em>.',
                'p': 'Beijing\'s moves are coordinated and accelerating:'
            },
            {
                'ul': [
                    '<strong>Manus deal blocked</strong> — Signal: "Singapore-washing" no longer works.',
                    '<strong>Capital wall</strong> — Moonshot AI, Stepfun, ByteDance instructed to reject U.S. capital unless explicitly approved.',
                    '<strong>IPO block</strong> — Considering rules requiring Beijing approval for any Chinese AI company seeking U.S. listing. "Red chips" restricted from Hong Kong IPOs.',
                ]
            },
            {
                'h2': 'The New <em>Policy</em>.',
                'p': 'Washington\'s response has been less coordinated but no less consequential:'
            },
            {
                'ul': [
                    '<strong>January 13, 2026:</strong> Commerce shifted H200 export review from "presumption of denial" to "case-by-case" with 25% tariff applied.',
                    '<strong>January 22, 2026:</strong> "AI Overwatch Act" passed — permanent licensing uncertainty.',
                    '<strong>February 2026:</strong> Anthropic accused DeepSeek, Moonshot, MiniMax of 16M fraudulent exchanges to extract Claude.',
                    'House Foreign Affairs Committee hearing: "Winning the AI Race Against the Chinese Communist Party."',
                ]
            },
            {
                'h2': 'Huawei <em>Rises</em>.',
                'p': 'The chip race numbers tell the structural story:'
            },
            {
                'ul': [
                    '<strong>Huawei Ascend 950PR</strong> — 800K chip orders for 2026 (~25% of NVIDIA\'s annual GPU production)',
                    '<strong>CXMT</strong> — 20M HBM stacks in 2026 (10× CFR\'s prior estimate)',
                    '<strong>Cambricon</strong> — +453% revenue growth in 2025; sold 117K chips',
                    '<strong>Alibaba T-Head</strong> — ~470K AI chips shipped, mostly external customers',
                    '<strong>DeepSeek V4</strong> (April 24, 2026) — optimized for Huawei chips, not NVIDIA',
                    '~$60B diverted annually from U.S. AI firms to Chinese chipmakers',
                ]
            },
            {
                'h2': 'Two <em>Stacks</em>.',
                'p': 'Every layer of the AI stack is now bifurcating — chips, models, capital, talent, applications.<br><br><strong>WEST:</strong> NVIDIA H200/Blackwell chips, GPT/Claude/Gemini models, capital closed to China.<br><br><strong>EAST:</strong> Huawei/Cambricon/CXMT chips, DeepSeek/Moonshot/Qwen models, capital closed to the U.S.<br><br>The compute gap is narrowing fast. Huawei chips at 60-70% of H200 capability. DeepSeek V4 nearly indistinguishable on most benchmarks. The 10× U.S. compute lead in 2026 is closing — by design.'
            },
        ],
        'pull_quote': {
            'text': 'A clarifying<br>moment.',
            'context': '"The Manus block is a clarifying moment. Manus was Singapore-incorporated with founders based here, and it still got pulled back. Beijing\'s signal is that what matters isn\'t where the legal entity sits."',
            'who': 'KE YAN',
            'role': 'Tech Analyst · DZT Research · On the Manus block · April 2026',
        },
        'closing_p': 'The cold war is hot. The decoupling is real. The bifurcation year is 2026.',
        'sources': [
            ('CNBC', 'https://www.cnbc.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('Fortune', 'https://fortune.com'),
            ('TechCrunch', 'https://techcrunch.com'),
            ('Financial Times', 'https://www.ft.com'),
            ('Council on Foreign Relations', 'https://www.cfr.org'),
            ('National Review', 'https://www.nationalreview.com'),
            ('Bureau of Industry and Security (Commerce)', 'https://www.bis.doc.gov'),
            ('DZT Research', 'https://www.bloomberg.com/news'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in xAI. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 10 — AGENTIC ============
    {
        'slug': 'agentic',
        'subject': 'Agentic AI.',
        'date': '05.10.26',
        'date_long': 'May 10, 2026',
        'category': 'AI',
        'tag_line': 'Anthropic Wall Street Launch',
        'title': 'Agentic.',
        'dek': '<em>Anthropic</em> just launched a suite of AI agents for the world\'s largest banks. <em>Jamie Dimon</em> appeared. <em>$1.5B</em> JV with Blackstone &amp; Goldman. The agentic shift is here.',
        'summary': 'The shift from generative to agentic AI is here. 78% of Fortune 500 already deploying.',
        'slides': ['agt_01_hero.png', 'agt_02_definition.png', 'agt_03_atwork.png', 'agt_04_platforms.png', 'agt_05_quote.png'],
        'body_sections': [
            {
                'h2': 'Answer <em>vs Act</em>.',
                'p': '<strong>Generative AI = answer engine.</strong> "What\'s the formula for compound interest?" Single-turn responses to questions. ChatGPT, Claude, Gemini.<br><br><strong>Agentic AI = execution engine.</strong> "Run the analysis on this portfolio, generate a comparison report, save it as a PDF, email it to the CFO, and schedule a 15-minute review." Multi-step. Autonomous.<br><br>The simple test: does it require constant prompting after each step, or does it reason, plan, and complete multi-step tasks on its own?'
            },
            {
                'h2': 'Agents <em>at Work</em>.',
                'p': 'The production deployments are the proof:'
            },
            {
                'ul': [
                    '<strong>IRS</strong> — Cut tax court case openings from 10 days to 30 minutes via Salesforce Agentforce. 50K minutes saved per division annually.',
                    '<strong>JPMorgan</strong> — 83% faster equity research with agentic workflows.',
                    '<strong>1-800Accountant</strong> — 1,000+ client engagements handled in first 24 hours. 70% autonomous resolution during tax season.',
                    '<strong>AtlantiCare</strong> — 66 minutes saved per clinician per day. Documentation time cut 42%. 80% provider adoption rate.',
                    '<strong>Salesforce Agentforce overall</strong> — 84% AI-driven resolution rate. Only 2% of cases require human escalation.',
                ]
            },
            {
                'h2': 'Who Builds <em>Them</em>.',
                'p': 'Two strategic positions are emerging: platform plays embedding agents into existing software, and foundation model APIs letting enterprises build their own custom agents.'
            },
            {
                'ul': [
                    '<strong>Salesforce Agentforce</strong> — $1.4B combined ARR, 18,500+ enterprise customers, 330% YoY ARR growth',
                    '<strong>Anthropic Claude API</strong> — $14B ARR, 3,000+ enterprise customers, Wall Street launch May 5',
                    '<strong>Microsoft Copilot</strong> — 85M monthly active users, distribution play across M365',
                    '<strong>Google Agentspace</strong>, <strong>AWS Bedrock AgentCore</strong>, <strong>ServiceNow AI Agents</strong>',
                    'Vertical specialists: <strong>Sierra</strong> (customer service), <strong>Cognition Devin</strong> (coding)',
                ]
            },
        ],
        'pull_quote': {
            'text': 'From answer engine<br>to execution engine.',
            'context': '"We\'re moving from an answer engine to an execution engine. AI agents are no longer a future concept — they are here, and they are eating software. This is the most significant shift in how work gets done since the spreadsheet."',
            'who': 'DARIO AMODEI',
            'role': 'Co-Founder & CEO · Anthropic · On the agentic shift · 2026',
        },
        'closing_p': 'The biggest shift in enterprise software since the spreadsheet. And it\'s just getting started.',
        'sources': [
            ('Salesforce · Agentforce', 'https://www.salesforce.com/agentforce'),
            ('Anthropic · News', 'https://www.anthropic.com/news'),
            ('Fortune', 'https://fortune.com'),
            ('McKinsey & Company', 'https://www.mckinsey.com'),
            ('Lyzr AI', 'https://www.lyzr.ai'),
            ('Business Insider · Tech', 'https://www.businessinsider.com/tech'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in xAI. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 9 — CHATBOT TOOLBOX ============
    {
        'slug': 'the-toolbox',
        'subject': 'AI Stack.',
        'date': '05.09.26',
        'date_long': 'May 9, 2026',
        'category': 'AI',
        'tag_line': 'The Chatbot Market in 2026',
        'title': 'The Toolbox.',
        'dek': 'The "winner take all" era of AI chatbots is over. <em>79%</em> of paying OpenAI users <em>also</em> pay for Anthropic. Enterprises run two or three platforms in parallel — not one.',
        'summary': 'ChatGPT loses 23 points of market share in 12 months. The chatbot market fragments.',
        'slides': ['bots_01_hero.png', 'bots_02_share.png', 'bots_03_who.png', 'bots_04_revenue.png', 'bots_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Slices</em>.',
                'p': 'ChatGPT\'s market share dropped from 87% to 60-68% in 12 months — the largest market share collapse in the history of generative AI. Q1 2026 web traffic share by platform:'
            },
            {
                'ul': [
                    '<strong>ChatGPT</strong> — 64% (down from 87% Jan 2025)',
                    '<strong>Google Gemini</strong> — 18.2% (up from 5.4% — 370% growth YoY)',
                    '<strong>Microsoft Copilot</strong> — 11%',
                    '<strong>Anthropic Claude</strong> — 4.5%',
                    '<strong>DeepSeek</strong> — 4%',
                    '<strong>Grok (xAI)</strong> — 3.4% web, 15.2% mobile via X Premium bundle',
                    '<strong>Perplexity</strong> — 2%',
                    '<strong>Meta AI</strong> — 1B+ MAU via Instagram/WhatsApp/Messenger (measured differently)',
                ]
            },
            {
                'h2': 'Who <em>Wins What</em>.',
                'p': 'Market share is the vanity metric. Use-case fit is what matters:'
            },
            {
                'ul': [
                    '<strong>ChatGPT</strong> — Best for general everything. Strongest consumer brand. 900M weekly active users.',
                    '<strong>Claude</strong> — Best for code, writing, long-context reasoning, enterprise workflows. Wins ~70% of head-to-head enterprise deals against OpenAI. $14B ARR.',
                    '<strong>Gemini</strong> — Best for Google ecosystem (Gmail, Docs, Workspace). Strong on research lookup. Mobile-first via Android.',
                    '<strong>Copilot</strong> — Best for M365 power users. Excel, Word, PowerPoint, Outlook.',
                    '<strong>Perplexity</strong> — Best for cited research. Real-time web with sources attached.',
                    '<strong>Grok</strong> — Best for real-time X data, social context, less filtered tone.',
                    '<strong>DeepSeek</strong> — Best for cost-conscious users. Open-source flexibility. Big in emerging markets.',
                    '<strong>Meta AI</strong> — Best for casual users embedded in Instagram, WhatsApp, Messenger.',
                ]
            },
            {
                'h2': 'Revenue <em>Tells</em>.',
                'p': 'Web traffic and weekly users are vanity metrics. The real war is being fought in enterprise revenue. OpenAI sits at ~$10B ARR. Anthropic at $14B ARR. Anthropic closed a Series G at a $380B valuation in February 2026. Anthropic has 4.5% of users but is winning ~70% of head-to-head enterprise deals — embedded in 70%+ of Fortune 100. The killer stat: 79% of paying OpenAI users <em>also</em> pay for Anthropic. The market has fragmented into three positions: consumer scale (ChatGPT), ecosystem distribution (Gemini, Copilot, Meta AI), and enterprise precision (Claude).'
            },
        ],
        'pull_quote': {
            'text': 'Starting their journeys<br>inside AI assistants.',
            'context': '"The center of gravity in digital discovery is shifting. Consumers are now starting their journeys inside AI assistants — asking questions, shaping preferences, and choosing who to trust before they reach a website."',
            'who': 'OR OFFER',
            'role': 'Co-Founder & CEO · Similarweb · On the AI chatbot shift · 2026',
        },
        'closing_p': 'The toolbox replaced the tool.',
        'sources': [
            ('Similarweb · Research', 'https://www.similarweb.com/blog/research/'),
            ('First Page Sage', 'https://firstpagesage.com'),
            ('AI Business', 'https://aibusiness.com'),
            ('Demandsage', 'https://www.demandsage.com'),
            ('Anthropic · News', 'https://www.anthropic.com/news'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in xAI. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 8 — THE LINK ============
    {
        'slug': 'the-link',
        'subject': 'Neuralink.',
        'date': '05.08.26',
        'date_long': 'May 8, 2026',
        'category': 'BCI',
        'tag_line': 'Oman Investment Authority Joins',
        'title': 'The Link.',
        'dek': '<em>Neuralink</em> hit a real inflection. Yesterday — <em>May 8, 2026</em> — Oman\'s <em>sovereign wealth fund</em> joined the cap table. This year Musk flipped the switch on <em>high-volume production</em> and automated surgery.',
        'summary': 'Neuralink hits inflection point. 21 patients, $12.7B secondary valuation, sovereign wealth piling in.',
        'slides': ['nlnk_01_hero.png', 'nlnk_02_inflection.png', 'nlnk_03_products.png', 'nlnk_04_race.png', 'nlnk_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Inflection</em>.',
                'p': 'For most of its first decade, Neuralink lived in the Musk distortion field — a moonshot venture pitched somewhere between cyberpunk and clinical trial. The first patient implant in January 2024 changed the conversation. The events of 2025 and the first months of 2026 changed the company. What\'s emerged is no longer a moonshot. It\'s a vertically-integrated brain-computer interface manufacturer with FDA Breakthrough Device designations across three product lines, sovereign wealth funds piling onto the cap table, and a clear path to $1 billion in annual revenue by 2031.'
            },
            {
                'h2': 'The <em>Numbers</em>.',
                'p': ''
            },
            {
                'ul': [
                    '<strong>21 patients</strong> implanted as of January 2026, up from 5 a year prior',
                    '<strong>$1.85B</strong> total primary funding raised. ~<strong>$12.7B</strong> implied secondary valuation',
                    '<strong>1,024 electrodes</strong> per N1 implant today. <strong>3,000</strong> by end of 2026. <strong>10,000</strong> by 2027. <strong>25,000+</strong> by 2028',
                    'Revenue target: <strong>$1B+ annually by 2031</strong>, across 5 specialized clinics',
                    'Cap table: ARK Invest · Founders Fund · Sequoia · Thrive Capital · Lightspeed · DFJ Growth · Valor Equity · G42 (UAE) · QIA (Qatar) · OIA (Oman, just added) · 1789 Capital',
                ]
            },
            {
                'h2': 'Three <em>Products</em>.',
                'p': '<strong>Telepathy</strong> is the live product. Thought-controlled cursor, video gameplay, and (via the CONVOY trial) direct connection to robotic arms. Noland Arbaugh — the first patient — has been demonstrating these capabilities in livestreams since 2024, hitting 9+ bits/sec, twice the prior BCI record.<br><br><strong>Blindsight</strong> targets vision restoration. FDA Breakthrough Device designation. First human implant pending. Projected $500M revenue by 2030 (10K procedures).<br><br><strong>Deep</strong> addresses tremor and Parkinson\'s via deep-brain stimulation, plus a parallel speech restoration program (also FDA Breakthrough).'
            },
            {
                'h2': 'The <em>Race</em>.',
                'p': 'The most underrated dimension is geopolitical. Beijing Xinzhida — Chinese state-backed via the Zhongguancun development zone — implanted its first three patients in March 2025 and is targeting a 50-patient trial in 2026. That trial pace exceeds Neuralink\'s current cadence. Plus Synchron (10 patients implanted, less invasive blood-vessel-deployed device) and Precision Neuroscience (surface-mounted approach) in the U.S. BCI is becoming a strategic technology category — not just a medical one.'
            },
        ],
        'pull_quote': {
            'text': 'Without the need<br>to remove it.',
            'context': '"Device threads will go through the dura, without the need to remove it. This is a big deal."',
            'who': 'ELON MUSK',
            'role': 'Founder · Neuralink · On automated surgery · NYE 2025',
        },
        'closing_p': 'From science fiction to medical device. From R&D to scale. From speculation to the link.',
        'sources': [
            ('Sacra · Neuralink', 'https://sacra.com/c/neuralink'),
            ('Contrary Research · Neuralink', 'https://research.contrary.com/company/neuralink'),
            ('Healthcare MEA', 'https://www.healthcaremea.com'),
            ('TSG Invest', 'https://tsginvest.com'),
            ('Fintool', 'https://fintool.com'),
            ('Neuralink', 'https://neuralink.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Neuralink. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ EARLIER POSTS — SOVEREIGN STACK TRILOGY ============
    {
        'slug': 'arsenal',
        'subject': 'Anduril.',
        'date': '05.04.26',
        'date_long': 'May 4, 2026',
        'category': 'Defense',
        'tag_line': 'The Sovereign Stack · Part I',
        'title': 'Arsenal.',
        'dek': 'America\'s new defense prime is <em>vertically integrated</em>, <em>software-first</em>, and <em>building at speed</em> the Pentagon can\'t. Anduril is no longer a startup. It\'s the new arsenal.',
        'summary': 'The new American defense prime. Software-first, vertically integrated, built at startup speed.',
        'slides': ['anduril_01_hero.png', 'anduril_02_trajectory.png', 'anduril_03_goldendome.png', 'anduril_04_stack.png', 'anduril_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Trajectory</em>.',
                'p': 'Anduril went from challenger to chosen prime in less than a decade. Lattice OS is the platform layer connecting all of Anduril\'s autonomous systems. Multiple major contracts won including Replicator (the DoD\'s autonomous systems initiative) and the upcoming Golden Dome air defense system.'
            },
            {
                'h2': 'The <em>Stack</em>.',
                'p': 'Where legacy primes (Lockheed, Boeing, Raytheon, Northrop) source from a sprawling supplier network and assemble, Anduril does software, hardware, and AI in-house. Sentry Towers · ALTIUS · Ghost · Bolt · Roadrunner · Dive-LD · Fury · Lattice OS — all vertically integrated.'
            },
        ],
        'pull_quote': {
            'text': 'The arsenal of<br>democracy, rebuilt.',
            'context': '"What we\'re building is the modern arsenal of democracy — software-first, autonomous, and producible at scale."',
            'who': 'PALMER LUCKEY',
            'role': 'Founder · Anduril Industries',
        },
        'closing_p': 'The new prime is not a startup. It\'s the arsenal.',
        'sources': [
            ('Anduril Industries', 'https://www.anduril.com'),
            ('DoD · DIU Replicator', 'https://www.diu.mil/replicator'),
            ('Defense News', 'https://www.defensenews.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Anduril. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },
    {
        'slug': 'american-made',
        'subject': 'Hadrian.',
        'date': '05.05.26',
        'date_long': 'May 5, 2026',
        'category': 'Industrial',
        'tag_line': 'The Sovereign Stack · Part II',
        'title': 'American Made.',
        'dek': 'America forgot how to <em>make things</em>. Hadrian is teaching it again. Software-defined factories producing aerospace-grade parts at the speed of code.',
        'summary': 'The software-defined factory. Aerospace-grade parts manufactured at startup speed.',
        'slides': ['hadrian_01_hero.png', 'hadrian_02_stack.png', 'hadrian_03_factories.png', 'hadrian_04_partners.png', 'hadrian_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Stack</em>.',
                'p': 'Hadrian is rebuilding the precision machining industry as a software business. The factory is software-defined — robots, CNC machines, and humans coordinated by Hadrian\'s OS layer. Aerospace-grade parts shipped in days instead of months.'
            },
            {
                'h2': 'The <em>Partners</em>.',
                'p': 'Hadrian counts SpaceX, Lockheed, Anduril, Boeing among its customers. The same customers that drive the defense and space buildout are also driving the demand for U.S.-based precision parts manufacturing.'
            },
        ],
        'pull_quote': {
            'text': 'Made in America,<br>at startup speed.',
            'context': '"We\'re building the precision manufacturing infrastructure the United States needs to compete — software-first, vertically integrated, and fast."',
            'who': 'CHRIS POWER',
            'role': 'Founder & CEO · Hadrian',
        },
        'closing_p': 'America is learning to make things again. Hadrian is the textbook.',
        'sources': [
            ('Hadrian', 'https://www.hadrian.co'),
            ('Manufacturing Dive', 'https://www.manufacturingdive.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Hadrian. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },
    {
        'slug': 'rare-earth',
        'subject': 'Vulcan Elements.',
        'date': '05.06.26',
        'date_long': 'May 6, 2026',
        'category': 'Strategic Minerals',
        'tag_line': 'The Sovereign Stack · Part III',
        'title': 'Rare Earth.',
        'dek': 'China controls <em>90%</em> of global rare earth processing. Vulcan Elements is one of <em>two</em> domestic operators rebuilding the supply chain. The strategic minerals story has begun.',
        'summary': 'America\'s rare earth supply chain rebuild. Vulcan Elements is one of two domestic operators.',
        'slides': ['vulcan_01_hero.png', 'vulcan_02_stack.png', 'vulcan_03_moat.png', 'vulcan_04_buildout.png', 'vulcan_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Moat</em>.',
                'p': 'Rare earth elements are not actually rare — they\'re abundant in the Earth\'s crust. What\'s rare is processing capability. China processes ~90% of global supply. Vulcan Elements is rebuilding domestic processing capacity for neodymium-iron-boron (NdFeB) magnets — the backbone of EVs, wind turbines, F-35s, and guided weapons.'
            },
            {
                'h2': 'The <em>Buildout</em>.',
                'p': 'Vulcan\'s first commercial-scale plant is under construction. Strategic Department of Defense backing. Partnerships with major industrial and defense customers. The Reindustrialize America thesis applies here at the most fundamental layer: minerals.'
            },
        ],
        'pull_quote': {
            'text': 'The minerals are<br>the war.',
            'context': '"You cannot have a sovereign defense industrial base without sovereign rare earth processing. Period."',
            'who': 'JOHN MAA',
            'role': 'Founder & CEO · Vulcan Elements',
        },
        'closing_p': 'Two operators. One supply chain. The strategic minerals story has begun.',
        'sources': [
            ('Vulcan Elements', 'https://www.vulcanelements.com'),
            ('DoD · Critical Materials Strategy', 'https://www.defense.gov'),
        ],
        'disclosure': 'The author is a direct early-stage investor in Vulcan Elements and a Limited Partner in 1789 Capital, which also holds a position. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ NVIDIA — THE ORCHESTRATOR ============
    {
        'slug': 'the-orchestrator',
        'subject': 'NVIDIA.',
        'date': '05.07.26',
        'date_long': 'May 7, 2026',
        'category': 'AI Infrastructure',
        'tag_line': 'The Foundation Layer',
        'title': 'The Orchestrator.',
        'dek': 'Every layer of the AI stack runs on top of <em>NVIDIA</em>. Models. Agents. Robots. Cars. Drones. The mind map of the AI economy has <em>one orchestrator</em>.',
        'summary': 'Every major AI player runs on NVIDIA. The most important platform of this decade.',
        'slides': ['nvda_01_hero.png', 'nvda_02_mindmap.png', 'nvda_03_checks.png', 'nvda_04_pivot.png', 'nvda_05_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Mind Map</em>.',
                'p': 'NVIDIA chips power: OpenAI, Anthropic, Google DeepMind, xAI, Meta AI, Mistral, Cohere, Perplexity (models). Salesforce, Microsoft, ServiceNow (agents). Tesla Optimus, Figure, 1X, Hyundai Atlas (humanoids). Tesla FSD, Waymo, Cruise (autonomous vehicles). Anduril, Skydio, Shield AI (defense autonomy). The orchestrator owns the substrate.'
            },
        ],
        'pull_quote': {
            'text': 'AI is not<br>a feature.',
            'context': '"AI is not a feature. It is the platform. And the platform runs on accelerated computing."',
            'who': 'JENSEN HUANG',
            'role': 'Founder & CEO · NVIDIA',
        },
        'closing_p': 'Every layer of the AI economy passes through one company. That\'s the trade.',
        'sources': [
            ('NVIDIA · Investor Relations', 'https://investor.nvidia.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
        ],
        'disclosure': 'Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 12 — PEAK (Cerebras IPO Frenzy) ============
    {
        'slug': 'peak',
        'subject': 'Cerebras.',
        'date': '05.12.26',
        'date_long': 'May 12, 2026',
        'category': 'IPO Watch',
        'tag_line': 'Cerebras Pricing · The Frenzy',
        'title': 'Peak.',
        'dek': 'Cerebras just raised its IPO range to <em>$150–$160</em>. <em>20× oversubscribed</em>. <em>$48.8B</em> valuation target. Pricing tomorrow. Largest global IPO of 2026. <em>Or is this the top?</em>',
        'summary': 'Cerebras IPO frenzy: $48.8B valuation, 20× oversubscribed, pricing May 13. The third post in the market-tension trilogy.',
        'slides': ['peak_01_hero.png', 'peak_02_bump.png', 'peak_03_book.png', 'peak_04_fundamentals.png', 'peak_05_tension.png', 'peak_06_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Re-Price</em>.',
                'p': 'Cerebras amended its S-1 to raise the offering range from $115–$125 to $150–$160 per share — a 28% bump on the midpoint in just 8 days. The float expanded from 28M to 30M shares with an underwriter overallotment of 4.2M more. At the top of the new range, the company would price at a $48.8B fully diluted valuation — 84% above the original filing and roughly 2× February\'s $23B private round.'
            },
            {
                'h2': 'The <em>Order Book</em>.',
                'p': 'Per Reuters, the IPO is 20× oversubscribed — the largest global IPO of 2026 by Dealogic\'s reckoning. The book has fundamentals behind it: $24.6B contracted revenue backlog at year-end 2025, a $20B+ multi-year OpenAI compute contract plus a $1B OpenAI working capital loan, and AWS as the first hyperscaler to deploy Cerebras systems.'
            },
            {
                'h2': 'The <em>Tension</em>.',
                'p': 'At the top of the range, Cerebras prices at 67× trailing sales — versus ~10× for NVIDIA. 86% of 2024 revenue came from G42 (UAE), the same CFIUS-reviewed concentration that killed the 2024 IPO attempt. Yesterday, Michael Burry called this entire moment "the scene of the bloody car crash, minutes before it happens." A 20×-oversubscribed AI IPO is the Exhibit A.'
            },
        ],
        'pull_quote': {
            'text': 'Surging interest<br>ahead of pricing.',
            'context': '"Cerebras\' IPO has drawn orders for more than 20 times the number of shares available, the people said, as the chipmaker looks to manage surging interest ahead of its May 13 pricing."',
            'who': 'REUTERS',
            'role': 'On Cerebras IPO demand · May 11, 2026',
        },
        'closing_p': 'Both bulls and bears are positioned for asymmetric outcomes. The frenzy is the story.',
        'sources': [
            ('Reuters · IPO Demand', 'https://www.reuters.com'),
            ('CNBC · CBRS Pricing', 'https://www.cnbc.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('Cerebras Amended S-1', 'https://www.sec.gov/edgar'),
            ('Dealogic', 'https://www.dealogic.com'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Cerebras. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 12 — PALANTIR (Q1 2026 Earnings) ============
    {
        'slug': 'palantir',
        'subject': 'Palantir.',
        'date': '05.12.26',
        'date_long': 'May 12, 2026',
        'category': 'Earnings Watch',
        'tag_line': 'Palantir Q1 2026 Print',
        'title': 'Palantir.',
        'dek': 'Palantir just delivered its <em>biggest quarter ever</em>. <em>+85%</em> revenue growth. <em>$1.63B</em> top line. Net income <em>quadrupled</em>. Karp shattered the Rule of 40. <em>Burry is short $912M of this stock.</em>',
        'summary': 'Palantir Q1 2026 print: $1.63B revenue (+85% YoY), $870M net income, Rule of 40 at 145. The strongest quarter since IPO.',
        'slides': ['pltr_01_hero.png', 'pltr_02_beat.png', 'pltr_03_engine.png', 'pltr_04_war.png', 'pltr_05_burry.png', 'pltr_06_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Beat</em>.',
                'p': 'Palantir reported Q1 2026 revenue of $1.63B versus $1.54B expected — up 85% year-over-year, the fastest growth rate since its 2020 IPO and the 11th consecutive quarter of accelerating revenue growth. EPS of 33¢ adjusted beat 28¢ expected, up 115% YoY. GAAP operating margin hit 46%, adjusted operating margin 60%, and net income quadrupled to $870.5M from $214M a year ago.'
            },
            {
                'h2': 'The <em>Engine</em>.',
                'p': 'U.S. commercial revenue grew 133% YoY to $595M with remaining deal value of $4.92B (+112% YoY). 42% customer count growth — with a salesforce of just 70 people. Net dollar retention sits at 150%. The AIP bootcamp model compresses enterprise sales cycles from months to days. Rule of 40 score: 145 — matched only by NVIDIA, Micron, and SK Hynix in the AI infrastructure cohort.'
            },
            {
                'h2': 'The <em>War Machine</em>.',
                'p': 'U.S. government revenue grew 84% YoY to $687M. The $10B / 10-year TITAN Army contract is the anchor, with Maven Smart System expansion DoD-wide and a just-landed USDA AI modernization deal. Karp on the call: "What makes America special right now is our lethal capabilities, our ability to fight war."'
            },
            {
                'h2': 'Vs <em>Burry</em>.',
                'p': 'Burry sits short ~$912M of PLTR puts via a dual-strike structure: $100 strike Dec 2026 (stock would need to fall 32% from current ~$146 to hit) and $50 strike June 2027 (-66%). Q1 just made that math considerably harder. FY26 guidance was raised from 61% to 71% revenue growth, with U.S. commercial guidance at +120% YoY. Karp\'s response to the short: "bats--- crazy."'
            },
        ],
        'pull_quote': {
            'text': 'We have shattered<br>the metric.',
            'context': '"Palantir\'s Rule of 40 score has soared to 145. We have shattered the metric, a feat matched only by other fellow AI infrastructure companies: NVIDIA, Micron and SK hynix. Momentum surged as we grew 85% last quarter — our highest-ever year-over-year growth rate — by more than doubling our U.S. business."',
            'who': 'ALEX KARP',
            'role': 'Co-Founder & CEO · Palantir · Q1 2026 Shareholder Letter',
        },
        'closing_p': 'The numbers vindicate the bull case. The multiple still vindicates Burry. Both can be right. One eventually won\'t be.',
        'sources': [
            ('Palantir Q1 2026 Shareholder Letter', 'https://investors.palantir.com'),
            ('CNBC', 'https://www.cnbc.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('13F Filings', 'https://www.sec.gov/edgar'),
            ('Burry Substack · Cassandra Unchained', 'https://cassandrabc.substack.com'),
        ],
        'disclosure': 'Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 12 — PERPLEXITY (Interface Layer) ============
    {
        'slug': 'perplexity',
        'subject': 'Perplexity.',
        'date': '05.12.26',
        'date_long': 'May 12, 2026',
        'category': 'AI',
        'tag_line': 'The March to the Interface Layer',
        'title': 'Perplexity.',
        'dek': 'Valuation: <em>$500M → $20B</em> in 20 months. ARR: <em>$35M → $450M</em>. Then Personal Computer dropped last week. Perplexity is no longer a <em>search startup</em>. It\'s playing for the <em>interface layer</em> of the AI web.',
        'summary': 'Perplexity\'s shift from search engine to interface layer. $20B valuation, $450M ARR, 45M MAU, plus a $34.5B standing bid for Chrome.',
        'slides': ['pplx_01_hero.png', 'pplx_02_trajectory.png', 'pplx_03_stack.png', 'pplx_04_proxy.png', 'pplx_05_chrome.png', 'pplx_06_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Trajectory</em>.',
                'p': 'Valuation 40× in 20 months: $500M at start of 2024 → $20B in September 2025 (BOND-led $200M round). ARR ~13× in 18 months: $35M mid-2024 → $450M annualized March 2026. Monthly active users doubled to 45M. 780M+ queries per month. The 2026 revenue target is $656M. Cap table: Bezos, Nvidia, NEA, IVP, Accel, SoftBank, 1789 Capital.'
            },
            {
                'h2': 'The <em>Stack</em>.',
                'p': 'Four layers, each broader than the last. Search (the flagship — 93.9% accuracy on SimpleQA, 97% citation accuracy). Browser (Comet, Chromium-based, free globally since October 2025, iOS shipped March 2026). Computer (the agentic AI workspace with Model Council orchestrating 19 frontier models). And now Personal Computer — a 24/7 always-on AI proxy running on a dedicated Mac mini, launched last week.'
            },
            {
                'h2': 'The <em>Front Door</em>.',
                'p': 'August 2025, after Google\'s DOJ antitrust loss demanded Chrome divestiture, Perplexity placed a $34.5B standing bid for Chrome — 1.7× its own valuation at the time. Industry analysts read it as strategic positioning rather than a firm acquisition, but the flag is planted. Comet already runs on Chromium. Srinivas isn\'t building a Google competitor. He\'s positioning to replace the browser layer.'
            },
        ],
        'pull_quote': {
            'text': 'The home page of<br>human curiosity.',
            'context': 'Perplexity\'s stated vision: to become "the home page of human curiosity" — the interface layer where every research question, market analysis, and product comparison begins.',
            'who': 'PERPLEXITY',
            'role': 'Stated company vision · 2026',
        },
        'closing_p': 'Not a search engine. The interface layer for everything you want to know.',
        'sources': [
            ('TFN', 'https://techfundingnews.com'),
            ('The Information', 'https://www.theinformation.com'),
            ('Stocktwits', 'https://stocktwits.com'),
            ('TSG Invest', 'https://www.tsginvest.com'),
            ('Perplexity Release Notes', 'https://www.perplexity.ai'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Perplexity. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 13 — ORBIT (Google × SpaceX Data Centers) ============
    {
        'slug': 'orbit',
        'subject': 'SpaceX.',
        'date': '05.13.26',
        'date_long': 'May 13, 2026',
        'category': 'Frontier',
        'tag_line': 'Google × SpaceX · Orbital Data Centers',
        'title': 'Orbit.',
        'dek': 'WSJ broke yesterday: <em>Google &amp; SpaceX in advanced talks</em> to launch orbital data centers. SpaceX filed for <em>1 million satellites</em>. The pitch ahead of a <em>$1.75T IPO</em>. Compute is leaving Earth.',
        'summary': 'Google and SpaceX in advanced talks for orbital data centers, ahead of SpaceX\'s $1.75T IPO. The future of the data center.',
        'slides': ['orbit_01_hero.png', 'orbit_02_talks.png', 'orbit_03_pitch.png', 'orbit_04_math.png', 'orbit_05_case.png', 'orbit_06_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Talks</em>.',
                'p': 'WSJ reported May 12 that Google is in advanced discussions with SpaceX to launch test products for orbital data centers — Google\'s "Project Suncatcher" initiative announced in November 2025. SpaceX filed an FCC application in January 2026 for up to one million satellites authorizing orbital data center deployment. Prototype satellites are targeted for 2027, with Planet Labs building the test hardware. The talks come on the heels of last week\'s SpaceX × Anthropic deal: access to 300+ MW of compute via 220,000+ NVIDIA GPUs at Colossus 1 in Memphis, with explicit option to collaborate on orbital systems.'
            },
            {
                'h2': 'The <em>Pitch</em>.',
                'p': 'SpaceX is targeting a $1.75 trillion valuation IPO later in 2026 — the largest in history if it prices at target. The combined SpaceX × xAI entity (merged February 2026) was valued at $1.25T. Google already owns 6.1% of SpaceX from a $900M investment in 2015 — now worth ~$107B at the IPO target. SpaceX also holds an option to acquire AI coding startup Cursor for $60B. The vertical stack is being assembled at full integration.'
            },
            {
                'h2': 'The <em>Math</em>.',
                'p': 'Project Suncatcher\'s break-even economics need ~$200/kg to orbit. SpaceX\'s current rideshare price: $7,000/kg — roughly 35× the threshold. Falcon 9 just launched its 34th consecutive reuse, and analysts estimate that 5-6 reuses offset production cost. The Starship economics could theoretically compress launch costs another order of magnitude. The entire orbital data center thesis rides on this curve continuing to flatten.'
            },
            {
                'h2': 'The <em>Case</em>.',
                'p': 'Why both Pichai and Musk see the same future: continuous solar power (no night cycles, no weather, no grid bottlenecks), free vacuum cooling (no water consumption, no 70°F server room constraint), and no zoning fights (bypassing the 14 U.S. states currently considering data center bans). The biggest constraints on terrestrial compute disappear in orbit — IF launch costs collapse.'
            },
        ],
        'pull_quote': {
            'text': 'A more normal way<br>to build data centers.',
            'context': 'Pichai at Project Suncatcher\'s November 2025 announcement: "There\'s no doubt to me that a decade or so away, we\'ll be viewing it as a more normal way to build data centers."',
            'who': 'SUNDAR PICHAI',
            'role': 'CEO · Alphabet / Google · November 2025',
        },
        'closing_p': 'Compute is leaving Earth. Slowly. Then suddenly.',
        'sources': [
            ('Wall Street Journal', 'https://www.wsj.com'),
            ('Bloomberg', 'https://www.bloomberg.com'),
            ('Tom\'s Hardware', 'https://www.tomshardware.com'),
            ('TechCrunch', 'https://techcrunch.com'),
            ('Project Suncatcher Whitepaper', 'https://research.google'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds positions in SpaceX and xAI. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },

    # ============ MAY 13 — CRUSOE (Terrestrial AI Infrastructure) ============
    {
        'slug': 'crusoe',
        'subject': 'Crusoe.',
        'date': '05.13.26',
        'date_long': 'May 13, 2026',
        'category': 'Infrastructure',
        'tag_line': 'The Terrestrial Answer',
        'title': 'Crusoe.',
        'dek': 'The leading <em>energy-first</em> AI infrastructure builder. Revenue: <em>$276M → $2B</em> in two years. Valuation: <em>$10B+</em>. Now serving <em>OpenAI Stargate &amp; Microsoft.</em> The terrestrial answer to compute scarcity.',
        'summary': 'Crusoe\'s rise as the leading energy-first AI infrastructure operator: $10B valuation, 45 GW pipeline, customers including OpenAI Stargate and Microsoft.',
        'slides': ['crusoe_01_hero.png', 'crusoe_02_trajectory.png', 'crusoe_03_pipeline.png', 'crusoe_04_stack.png', 'crusoe_05_partners.png', 'crusoe_06_quote.png'],
        'body_sections': [
            {
                'h2': 'The <em>Trajectory</em>.',
                'p': 'Revenue trajectory: $276M (2024) → $998M (2025 projected, +262% YoY) → $2B projected for 2026. Crusoe\'s Series E closed October 2025 at $10B+ valuation — an oversubscribed $1.375 billion round co-led by Valor Equity Partners and Mubadala Capital, with participation from NVIDIA, Founders Fund, Tiger Global, T. Rowe Price, Fidelity, 1789 Capital, and others. A $750M Brookfield credit facility — typically reserved for mature infrastructure — validates the energy-first AI thesis as bankable. COO/CFO Michael Gordon, who led MongoDB\'s 2017 IPO, joined to prepare for public markets.'
            },
            {
                'h2': 'The <em>Pipeline</em>.',
                'p': 'Crusoe\'s committed power pipeline reached 45 GW by the end of 2025 — quadrupled in a single year, enough to power New York City 8-10 times over. The Abilene, TX flagship is a 1.2 GW campus serving as anchor for OpenAI\'s $500B Stargate project, with $11.6B in financing and up to 400,000 NVIDIA GB200 GPUs. Wyoming hosts a 1.8 GW gigawatt-scale campus. And just announced: a new 900 MW Abilene campus supporting Microsoft AI Infrastructure — Crusoe now powers two of the three biggest AI buyers on Earth.'
            },
            {
                'h2': 'The <em>Stack</em>.',
                'p': 'The edge comes from vertical integration: Energy → Land → Data Center → Cloud platform, all owned by one company. Stranded gas at ~1/13 standard electricity rates. Energy is 60%+ of AI data center OpEx, and Crusoe pays 30-50% less for it than traditional hyperscalers. Traditional AI infrastructure is fragmented across power utilities, real estate developers, data center operators, and cloud providers. Crusoe collapses the whole stack — and the White House\'s "BYO Power" initiative now structurally aligns with that model.'
            },
            {
                'h2': 'The <em>Partners</em>.',
                'p': 'Customers: OpenAI (Stargate) and Microsoft (new 900 MW Abilene). Crusoe Cloud bookings grew 5× in the first nine months of 2025. Chips: expanded NVIDIA collaboration across the full AI factory stack explicitly built for "the Agentic AI Era," plus a new strategic AMD partnership for diversification. Energy storage: Redwood Materials\' EV-battery microgrid scaled 7× with 99.2% uptime, plus a 12 GWh Form Energy deal for iron-air batteries starting 2027 — 100+ hour storage, no thermal runaway risk.'
            },
        ],
        'pull_quote': {
            'text': 'Move the compute<br>to the energy.',
            'context': '"Move the compute to the energy, not the other way around. Traditional data center development follows the grid — waiting on interconnection, straining infrastructure, driving up electricity costs for communities. We take the opposite approach: we locate AI workloads near sources of abundant, often underutilized energy."',
            'who': 'CULLY CAVNESS',
            'role': 'Co-Founder & President · Crusoe · 2026',
        },
        'closing_p': 'If orbit is where compute is going (eventually), Crusoe is where compute is going (now).',
        'sources': [
            ('Crusoe Newsroom', 'https://www.crusoe.ai/resources/newsroom'),
            ('Business Wire', 'https://www.businesswire.com'),
            ('Data Center Dynamics', 'https://www.datacenterdynamics.com'),
            ('TSG Invest', 'https://tsginvest.com/crusoe-energy/'),
            ('Crusoe Blog · BYO Power', 'https://www.crusoe.ai/resources/blog/welcome-to-the-era-of-byo-power'),
        ],
        'disclosure': 'The author is a Limited Partner in 1789 Capital, which holds a position in Crusoe. Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation.',
    },
]


# ============================================================
# TEMPLATES
# ============================================================

HEAD_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Frontier-first</title>
<meta name="description" content="{summary}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../style.css">
</head>
<body>
'''


def render_post(post):
    """Render a single post HTML."""
    out = HEAD_TEMPLATE.format(
        title=post['title'],
        summary=post['summary'],
    )
    out += '<article class="page">\n'

    # Brand bar with subject company name
    out += f'''  <header class="brand-bar">
    <a href="../index.html" class="name">{post['subject']}</a>
    <div class="meta">Issue №026 · {post['date']}<small>{post['category']} · Frontier-first</small></div>
  </header>
'''

    # Eyebrow
    out += f'''
  <div class="eyebrow"><span class="dot"></span><span>{post['tag_line']} · {post['date']}</span></div>
'''

    # Title
    out += f'  <h1 class="title">{post["title"]}</h1>\n'

    # Dek
    out += f'  <p class="dek">{post["dek"]}</p>\n'

    # Byline
    out += f'''  <div class="byline">
    <span>By <span class="who">KOCH. VC.</span></span>
    <span>{post["date_long"]}</span>
  </div>
'''

    # Body content interleaved with slides
    out += '  <section class="body">\n'

    # First slide (hero) right after byline
    if post.get('slides'):
        first_slide = post['slides'][0]
        out += f'''    <figure class="slide">
      <img src="../assets/{first_slide}" alt="{post['title']} — Slide 01">
      <figcaption>Slide 01 · {post['title']}</figcaption>
    </figure>
'''

    # Body sections, with slides interspersed
    body_sections = post.get('body_sections', [])
    remaining_slides = post.get('slides', [])[1:]  # skip hero
    pull_idx = len(body_sections) // 2 if body_sections else 0

    for i, section in enumerate(body_sections):
        if section.get('h2'):
            out += f'    <h2>{section["h2"]}</h2>\n'
        if section.get('p'):
            out += f'    <p>{section["p"]}</p>\n'
        if section.get('ul'):
            out += '    <ul>\n'
            for item in section['ul']:
                out += f'      <li>{item}</li>\n'
            out += '    </ul>\n'

        # Insert a slide after each major section, if we have one
        if remaining_slides and (i + 1) < len(body_sections):
            slide_idx = i + 2  # 02, 03, etc.
            slide = remaining_slides.pop(0)
            out += f'''    <figure class="slide">
      <img src="../assets/{slide}" alt="{post['title']} — Slide {slide_idx:02d}">
      <figcaption>Slide {slide_idx:02d} · {post['title']}</figcaption>
    </figure>
'''

    # Pull quote
    if post.get('pull_quote'):
        pq = post['pull_quote']
        out += f'''
    <blockquote class="pull">
      <div class="mark">"</div>
      <div class="text">{pq['text']}"</div>
      <div class="who"><strong>{pq['who']}</strong>{pq['role']}</div>
    </blockquote>
'''
        # Context paragraph
        if pq.get('context'):
            out += f'    <p style="font-style: italic; opacity: 0.8;">{pq["context"]}</p>\n'

    # Remaining slides
    while remaining_slides:
        slide_idx = len(post['slides']) - len(remaining_slides) + 1
        slide = remaining_slides.pop(0)
        out += f'''
    <figure class="slide">
      <img src="../assets/{slide}" alt="{post['title']} — Slide {slide_idx:02d}">
      <figcaption>Slide {slide_idx:02d} · {post['title']}</figcaption>
    </figure>
'''

    # Closing paragraph
    if post.get('closing_p'):
        out += f'    <p>{post["closing_p"]}</p>\n'

    out += '  </section>\n'

    # Disclosure
    if post.get('disclosure'):
        out += f'''
  <div class="disclosure">
    <p><strong>Disclosure</strong></p>
    <p>{post["disclosure"]}</p>
  </div>
'''

    # Sources
    if post.get('sources'):
        out += '''
  <section class="sources">
    <h3>Sources</h3>
    <ol>
'''
        for source, url in post['sources']:
            out += f'      <li><a href="{url}" target="_blank" rel="noopener">{source}</a></li>\n'
        out += '''    </ol>
  </section>
'''

    # Post footer
    out += f'''
  <footer class="post-footer">
    <div class="signoff">— Frontier-first.</div>
    <div>Issue №026 · {post["date"]}</div>
  </footer>

</article>

</body>
</html>
'''
    return out


def render_index():
    """Render the archive/index page."""
    out = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Frontier-first — Archive</title>
<meta name="description" content="Editorial dispatches on the frontier of capital and technology.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<article class="page">

  <header class="brand-bar">
    <div class="name-block">
      <span class="name">KOCH.</span>
      <span class="name-sub">VENTURE CAPITAL.</span>
    </div>
    <div class="meta">Issue №026<small>Editorial Archive</small></div>
  </header>

  <div class="archive-intro">
    <h1>ARCHIVES.</h1>
    <p>Editorial dispatches on the <em>frontier of capital and technology</em>. Markets, AI, defense, frontier tech, and the companies building what comes next.</p>
  </div>

  <div class="archive-grid">
'''

    # Sort posts by date (newest first) for the archive grid
    # Date format is MM.DD.YY — parse to a sortable tuple
    def date_key(post):
        mm, dd, yy = post['date'].split('.')
        return (int(yy), int(mm), int(dd))

    sorted_posts = sorted(POSTS, key=date_key, reverse=True)

    for post in sorted_posts:
        hero_slide = post['slides'][0]
        out += f'''    <a href="posts/{post['slug']}.html" class="post-card">
      <div class="thumb"><img src="assets/{hero_slide}" alt="{post['title']}"></div>
      <div class="meta-row">
        <span>{post['category']}</span>
        <span>{post['date']}</span>
      </div>
      <h3>{post['title']}</h3>
      <p class="summary">{post['summary']}</p>
    </a>
'''

    out += '''  </div>

  <footer class="post-footer" style="margin-top: 96px;">
    <div class="signoff">— Frontier-first.</div>
    <div>Issue №026</div>
  </footer>

</article>

</body>
</html>
'''
    return out


# ============================================================
# BUILD
# ============================================================

def build():
    SITE_ROOT.mkdir(exist_ok=True)
    POSTS_DIR.mkdir(exist_ok=True)
    ASSETS_DIR.mkdir(exist_ok=True)

    # Render index
    (SITE_ROOT / 'index.html').write_text(render_index())
    print(f'wrote index.html')

    # Render each post
    for post in POSTS:
        html = render_post(post)
        (POSTS_DIR / f'{post["slug"]}.html').write_text(html)
        print(f'wrote posts/{post["slug"]}.html')

    print(f'\nBuilt {len(POSTS)} posts + 1 index page.')


if __name__ == '__main__':
    build()
