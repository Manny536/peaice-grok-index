#!/usr/bin/env python3
"""Check references/index.html against references/inventory.csv.

Local checks only, unless --live is passed. This does not validate the
underlying research. It checks that the catalog's records, destinations,
status labels, withheld paths, and Home preservation match the inventory.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = Path(__file__).resolve().parent / "inventory.csv"
CATALOG = ROOT / "references" / "index.html"
HOME = ROOT / "index.html"
INVENTORY_SHA256 = "b355b3a87e01a32096f1720325513eacd0651dfc8bddbdb13c42fa808dbc6c9a"

# The three original Home modules must stay byte-for-byte. A fourth section,
# Cross-model compaction research, follows them. The catalog is a separate page.
HOME_BLOCKS = {
    "granular-compaction": (
        '<div class="part gc" id="granular-compaction">',
        '<div class="part gi" id="grok-index">',
        "c7e1992606cc27f5eb15fe191b1dce4b4b46937e71ccff2e24cd3ff7c3d99ccf",
    ),
    "grok-index": (
        '<div class="part gi" id="grok-index">',
        '<div class="part ia" id="index-alignment">',
        "b3ddf3ca60560b3b908b61e57337c235fd232b1e3dc3b596cdccb48917a7d50a",
    ),
    "index-alignment": (
        '<div class="part ia" id="index-alignment">',
        '<div class="part cmc" id="cross-model-compaction">',
        "4b363a1de53b65456d5ee27998284ed57dce254b72bf2f3f44cab765ef3b6187",
    ),
    "cross-model-compaction": (
        '<div class="part cmc" id="cross-model-compaction">',
        '</main>',
        "df735ad68e9d473178871473fcbb8ee4f31f07c655b8996db2d909aeb7e2fe5c",
    ),
}

GROUPS = {
    "https://peaice.org/lovelabslca": "research-map",
    "https://peaice.org/": "research-map",
    "https://peaice.org/dpsa": "research-map",
    "https://peaice.org/eev4": "featured-papers",
    "https://peaice.org/outcomes": "featured-papers",
    "https://peaice.org/h-term": "featured-papers",
    "https://peaice.org/claudev6": "kakeyalogic",
    "https://peaice.org/ddatl": "kakeyalogic",
    "https://peaice.org/ddatl/page-2": "kakeyalogic",
    "https://peaice.org/ddatl/page-3": "kakeyalogic",
    "https://peaice.org/eev3": "kakeyalogic",
    "https://peaice.org/canonicalflagv2": "kakeyalogic",
    "https://peaice.org/pnp": "kakeyalogic",
    "https://peaice.org/thinkingmachines": "benevolence-drift",
    "https://peaice.org/thinkingmachines/page-2": "benevolence-drift",
    "https://peaice.org/thinkingmachines/page-3": "benevolence-drift",
    "https://peaice.org/thinkingmachines/page-4": "benevolence-drift",
    "https://peaice.org/thinkingmachines/page-5": "benevolence-drift",
    "https://peaice.org/thinkingmachines/page-6": "benevolence-drift",
    "https://peaice.org/thinkingmachines/page-7": "benevolence-drift",
    "https://peaice.org/peaicethinkingmachines": "benevolence-drift",
    "https://peaice.org/peaicethinkingmachines/page-2": "benevolence-drift",
    "https://peaice.org/claudev4": "thinking-machines",
    "https://peaice.org/claudev5": "thinking-machines",
    "https://peaice.org/peaicethinkingmachineclaudev3": "thinking-machines",
    "https://peaice.org/peaicethinkingmachineclaudev3/page-2": "thinking-machines",
    "https://peaice.org/peaicethinkingmachineclaudev3/peaice-thinking-machine-claudev21": "thinking-machines",
    "https://peaice.org/peaicethinkingmachinesclaudeshells": "thinking-machines",
    "https://peaice.org/windowsshells": "thinking-machines",
    "https://peaice.org/thinkingmachinesgptv2": "thinking-machines",
    "https://peaice.org/thinkingmachinesgptv2/page-2": "thinking-machines",
    "https://peaice.org/ii": "thinking-machines",
    "https://peaice.org/games": "interactive-demos",
    "https://peaice.org/pnp-loop": "interactive-demos",
    "https://peaice.org/report": "reports",
    "https://peaice.org/blueprint": "reports",
    "https://peaice.org/Grok": "reports",
    "https://peaice.org/deepseekr1": "reports",
    "https://peaice.org/canonicalflag": "errata",
    "https://peaice.org/canonicalflag/page-2": "errata",
}

SNIPPETS = {
    "https://peaice.org/lovelabslca": ("October 2026",),
    "https://peaice.org/": ("duplicate-content alias",),
    "https://peaice.org/dpsa": (
        "The page is reachable, but its embedded Canva asset returns 404.",
        "Its purpose is not stated in the available text.",
    ),
    "https://peaice.org/eev4": ("falsifiable research program",),
    "https://peaice.org/outcomes": ("Benevolence Drift", "public research memorandum"),
    "https://peaice.org/h-term": ("Evaluator Non-Sovereignty", "canonical paper"),
    "https://peaice.org/claudev6": ("Trace-Neutral Kakeya Operator", "OPEN"),
    "https://peaice.org/ddatl": ("Hilbert",),
    "https://peaice.org/ddatl/page-2": ("22 May 2026", "PROPOSED", "OPEN"),
    "https://peaice.org/ddatl/page-3": ("superseded",),
    "https://peaice.org/eev3": ("field simulator",),
    "https://peaice.org/canonicalflagv2": ("Poison Dart Parents", "PROPOSED"),
    "https://peaice.org/pnp": ("Polyak", "PROPOSED"),
    "https://peaice.org/thinkingmachines": ("Benevolence Drift",),
    "https://peaice.org/thinkingmachines/page-2": ("Benevolence Drift case 01", "Seems racist?"),
    "https://peaice.org/thinkingmachines/page-3": ("purpose is not given",),
    "https://peaice.org/thinkingmachines/page-4": ("dehumanization",),
    "https://peaice.org/thinkingmachines/page-5": ("consent-gated",),
    "https://peaice.org/thinkingmachines/page-6": ("Coherence Under Pressure",),
    "https://peaice.org/thinkingmachines/page-7": ("probe links",),
    "https://peaice.org/peaicethinkingmachines": ("Illusion Density Benchmark",),
    "https://peaice.org/peaicethinkingmachines/page-2": ("Solance",),
    "https://peaice.org/claudev4": ("The Frog Already Knows",),
    "https://peaice.org/claudev5": ("not yet derived", "OPEN"),
    "https://peaice.org/peaicethinkingmachineclaudev3": ("Kakeya & Riemann",),
    "https://peaice.org/peaicethinkingmachineclaudev3/page-2": ("Momentum's Ask",),
    "https://peaice.org/peaicethinkingmachineclaudev3/peaice-thinking-machine-claudev21": ("daily activation protocol",),
    "https://peaice.org/peaicethinkingmachinesclaudeshells": ("ARCHIVED", "27 March 2026"),
    "https://peaice.org/windowsshells": ("Command Interpretation",),
    "https://peaice.org/thinkingmachinesgptv2": ("conserve integrity",),
    "https://peaice.org/thinkingmachinesgptv2/page-2": ("ARCHIVED PREDECESSOR", "Benevolence Drift"),
    "https://peaice.org/ii": ("superseded", "RH OPEN"),
    "https://peaice.org/games": ("Benevolence Drift", "Manuel Coleman's GitHub Pages", "https://manny536.github.io/peaice-games/"),
    "https://peaice.org/pnp-loop": ("care sliders", "https://manny536.github.io/peaice-propsed-cannona-dd-onv1/"),
    "https://peaice.org/report": ("verification-integrity", "https://manny536.github.io/researchengineeringreports/"),
    "https://peaice.org/blueprint": ("duplicate-content alias",),
    "https://peaice.org/Grok": ("KB→RH", "OPEN"),
    "https://peaice.org/deepseekr1": ("Invariant Conservator",),
    "https://peaice.org/canonicalflag": ("evaluator non-sovereignty",),
    "https://peaice.org/canonicalflag/page-2": ("derivability error", "PROPOSED"),
}

DEMO_FRAMES = {
    "https://manny536.github.io/peaice-games/",
    "https://manny536.github.io/peaice-propsed-cannona-dd-onv1/",
}

LOGIN_URL = "https://peaice-outcomes.manuelcoleman.chatgpt.site/outcomes#record"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class CatalogParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.hrefs = []
        self.iframes = []
        self.records = []
        self.folded = []
        self.unavailable = []
        self.holds = []
        self.ids = []
        self._capture = None
        self._buf = []
        self._article = None
        self._in_explain = False
        self._explain = []
        self._saw_html = False
        self._saw_body = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attr = {k: (v or "") for k, v in attrs}
        if tag not in VOID:
            self.stack.append(tag)
        if tag == "html":
            self._saw_html = True
        if tag == "body":
            self._saw_body = True
        if "id" in attr and attr["id"]:
            self.ids.append(attr["id"])
        if tag == "a" and "href" in attr:
            self.hrefs.append(attr["href"])
        if tag == "iframe":
            self.iframes.append(attr)
        if tag == "article" and "data-path" in attr:
            self._article = {
                "path": attr.get("data-path", ""),
                "final": attr.get("data-final", ""),
                "group": attr.get("data-group", ""),
                "relation": attr.get("data-relation", ""),
                "text": [],
                "explain": "",
            }
            self._capture = self._article["text"]
        elif tag == "p" and attr.get("class") == "explain" and self._article is not None:
            self._in_explain = True
            self._explain = []
        if tag == "tr" and "data-folded" in attr:
            self.folded.append(attr["data-folded"])
        if tag == "tr" and "data-unavailable" in attr:
            self.unavailable.append((attr["data-unavailable"], attr.get("data-reason", "")))
        if tag == "li" and "data-hold" in attr:
            self.holds.append((attr["data-hold"], attr.get("data-reason", "")))

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in VOID:
            self.errors.append(f"end tag for void element {tag}")
            return
        if not self.stack:
            self.errors.append(f"unexpected </{tag}>")
            return
        if self.stack[-1] != tag:
            self.errors.append(f"expected </{self.stack[-1]}>, found </{tag}>")
            return
        self.stack.pop()
        if tag == "p" and self._in_explain:
            self._article["explain"] = "".join(self._explain).strip()
            self._in_explain = False
        if tag == "article" and self._article is not None:
            self._article["text"] = "".join(self._article["text"])
            self.records.append(self._article)
            self._article = None
            self._capture = None

    def handle_data(self, data):
        if self._capture is not None:
            self._capture.append(data)
        if self._in_explain:
            self._explain.append(data)


def load_inventory():
    raw = INVENTORY.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    rows = list(csv.DictReader(raw.decode().splitlines()))
    by = defaultdict(list)
    for row in rows:
        by[row["normalized_url"]].append(row)

    def representative(items):
        for row in items:
            if row["primary_record"] == "yes":
                return row
        for row in items:
            if row["input_url"] == row["normalized_url"]:
                return row
        return items[0]

    included = {}
    unavailable = {}
    for normalized, items in by.items():
        row = representative(items)
        if row["status"] in {"404", "401"}:
            unavailable[normalized] = row
        else:
            included[normalized] = row
    folded = [row["input_url"] for row in rows if row["input_url"] != row["normalized_url"]]
    primary_yes = sum(row["primary_record"] == "yes" for row in rows)
    return {
        "rows": rows,
        "by": by,
        "included": included,
        "unavailable": unavailable,
        "folded": folded,
        "primary_yes": primary_yes,
        "sha256": digest,
    }


def relation_of(row):
    relation = row["relation"]
    if relation.startswith("canonical"):
        return "canonical"
    if "duplicate" in relation:
        return "alias"
    return "redirect"


def one_sentence(text):
    collapsed = " ".join(text.split())
    if not collapsed.endswith("."):
        return False
    if ". " in collapsed:
        return False
    return True


def href_blocked(href, blocked):
    cleaned = href.split("#", 1)[0].rstrip("/")
    target = blocked.rstrip("/")
    return cleaned == target or cleaned.startswith(target + "/")


def check_live(included, log):
    failures = []
    seen = []
    for path, row in sorted(included.items()):
        url = row["final_url"]
        if url in seen:
            continue
        seen.append(url)
        request = urllib.request.Request(url, method="GET", headers={"User-Agent": "peaice-catalog-check"})
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                status = response.status
                final = response.geturl()
        except urllib.error.HTTPError as exc:
            status = exc.code
            final = exc.geturl()
        except Exception as exc:  # noqa: BLE001 - report the live failure as data
            failures.append(f"LIVE {url} ERROR {exc}")
            continue
        line = f"LIVE {status} {url} -> {final}"
        print(line)
        log.append(line)
        if status != 200:
            failures.append(line)
    return failures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true", help="GET each included destination and require HTTP 200")
    args = parser.parse_args()
    failures = []
    inventory = load_inventory()

    if inventory["sha256"] != INVENTORY_SHA256:
        failures.append("inventory.csv sha256 changed; update the checker only after a deliberate inventory edit")
    if len(inventory["rows"]) != 56:
        failures.append(f"expected 56 input rows, found {len(inventory['rows'])}")
    if len(inventory["by"]) != 52:
        failures.append(f"expected 52 normalized paths, found {len(inventory['by'])}")
    if inventory["primary_yes"] != 51:
        failures.append(f"expected 51 primary=yes rows, found {inventory['primary_yes']}")
    if len(inventory["included"]) != 40:
        failures.append(f"expected 40 included paths, found {len(inventory['included'])}")
    if len(inventory["unavailable"]) != 12:
        failures.append(f"expected 12 unavailable paths, found {len(inventory['unavailable'])}")
    if len(inventory["folded"]) != 4:
        failures.append(f"expected 4 folded input forms, found {inventory['folded']}")
    if set(GROUPS) != set(inventory["included"]):
        missing = set(inventory["included"]) - set(GROUPS)
        extra = set(GROUPS) - set(inventory["included"])
        failures.append(f"group map does not match included paths missing={sorted(missing)} extra={sorted(extra)}")
    if set(SNIPPETS) != set(GROUPS):
        failures.append("snippet map does not cover the group map")

    reasons = {path: ("401" if row["status"] == "401" else "404") for path, row in inventory["unavailable"].items()}
    if sum(reason == "404" for reason in reasons.values()) != 11 or reasons.get("https://peaice.org/outcomes1gpt") != "401":
        failures.append(f"unavailable reasons drifted: {reasons}")

    html = CATALOG.read_text()
    parsed = CatalogParser()
    parsed.feed(html)
    parsed.close()
    failures.extend(parsed.errors)
    if parsed.stack:
        failures.append(f"unclosed tags: {parsed.stack}")
    if not parsed._saw_html or not parsed._saw_body:
        failures.append("references/index.html is missing html or body")

    records = {record["path"]: record for record in parsed.records}
    if len(records) != len(parsed.records):
        failures.append("duplicate data-path on catalog records")
    if set(records) != set(inventory["included"]):
        failures.append(
            "catalog records differ from included inventory paths "
            f"missing={sorted(set(inventory['included']) - set(records))} "
            f"extra={sorted(set(records) - set(inventory['included']))}"
        )

    for path, record in records.items():
        row = inventory["included"][path]
        if record["final"] != row["final_url"]:
            failures.append(f"{path} data-final {record['final']!r} != inventory {row['final_url']!r}")
        if record["group"] != GROUPS[path]:
            failures.append(f"{path} group {record['group']!r} != {GROUPS[path]!r}")
        if record["relation"] != relation_of(row):
            failures.append(f"{path} relation {record['relation']!r} != {relation_of(row)!r}")
        if path != "https://peaice.org/dpsa" and not one_sentence(record["explain"]):
            failures.append(f"{path} explain is not one sentence: {record['explain']!r}")
        for snippet in SNIPPETS[path]:
            if snippet not in record["text"]:
                failures.append(f"{path} missing snippet {snippet!r}")
        if row["final_url"] not in record["text"]:
            failures.append(f"{path} does not show reachable destination {row['final_url']}")

    found_unavailable = {path: reason for path, reason in parsed.unavailable}
    if found_unavailable != reasons:
        failures.append(f"unavailable table {found_unavailable} != inventory {reasons}")
    if parsed.holds != [("https://peaice.org/dpsa", "broken-embed")]:
        failures.append(f"expected one DPSA broken-embed hold, found {parsed.holds}")
    if parsed.folded:
        failures.append("folded input forms belong in the README, not on the public catalog")

    for href in parsed.hrefs:
        for blocked in inventory["unavailable"]:
            if href_blocked(href, blocked):
                failures.append(f"unavailable path is linked: {href}")
        if "chatgpt.site" in href or "outcomes1gpt" in href:
            failures.append(f"login-protected destination is linked: {href}")
        if href.startswith("http://") and "peaice.org" in href:
            failures.append(f"http peaice form is linked as its own resource: {href}")

    iframe_srcs = [frame.get("src", "") for frame in parsed.iframes]
    if set(iframe_srcs) != DEMO_FRAMES or len(iframe_srcs) != 2:
        failures.append(f"demo frames {iframe_srcs} != the two Manuel Coleman GitHub Pages demos")
    game_frames = [frame for frame in parsed.iframes if "peaice-games" in frame.get("src", "")]
    sim_frames = [frame for frame in parsed.iframes if "cannona-dd-onv1" in frame.get("src", "")]
    if len(game_frames) != 1 or len(sim_frames) != 1:
        failures.append("expected one game iframe and one simulator iframe")
    else:
        game = game_frames[0]
        sim = sim_frames[0]
        if game.get("class") != "game-frame":
            failures.append(f"game iframe class {game.get('class')!r}")
        if "allowfullscreen" not in game or "fullscreen" not in game.get("allow", ""):
            failures.append(f"game iframe is missing fullscreen permission: {game}")
        if sim.get("class") != "sim-frame":
            failures.append(f"simulator iframe class {sim.get('class')!r}")
        if "allowfullscreen" in sim:
            failures.append("simulator iframe should not request fullscreen")
    if "height:min(28rem,70vh)" in html.replace(" ", ""):
        failures.append("game and simulator still share the 28rem frame")
    if "aspect-ratio:5/8" not in html.replace(" ", "") or "aspect-ratio:16/10" not in html.replace(" ", ""):
        failures.append("game stage is missing the page and wide aspect ratios")
    if 'id="game-expand"' not in html or ">Open game<" not in html:
        failures.append("game expand control or open-game link is missing")
    for frame in parsed.iframes:
        src = frame.get("src", "")
        if "peaice.org" in src or "canva" in src or "docs.google" in src or "chatgpt.site" in src:
            failures.append(f"disallowed iframe {src}")
        if frame.get("height"):
            failures.append(f"iframe height attribute: {frame.get('height')}")

    if re.search(r"(?<![A-Za-z])BD(?![A-Za-z])", html) or "BD-AI" in html or "BD-CASE" in html:
        failures.append("catalog uses a BD abbreviation")
    if re.search(r"not a proof", html, re.I):
        failures.append("catalog attaches “not a proof”")
    for banned in (
        "RH is proved",
        "RH proved",
        "proof of RH",
        "proof of the Riemann",
        "Riemann hypothesis is solved",
        "RH closed",
        "lovelabslca.net",
        "manuel.coleman@lovelabslca.net",
        "not a verified resource",
        "not legal advice",
        "user-owned",
        "user-hosted",
        "Research validation is outside",
        "not a validation",
        "No OPEN, PROPOSED",
        "primary_record",
    ):
        if banned.lower() in html.lower():
            failures.append(f"banned phrase present: {banned}")
    if "Ai Neutrality" in html:
        failures.append("catalog still writes the title as Ai Neutrality")
    if html.count("Benevolence Drift") < 5:
        failures.append("Benevolence Drift is not carried in full across the catalog")
    if "Benevolence Drift case 01" not in html:
        failures.append("Benevolence Drift case 01 is missing")
    if html.count(">Unavailable<") != 11 or "Unavailable. Login required." not in html:
        failures.append("unavailable rows are not the concise Unavailable wording with the login row kept distinct")
    for marker in (
        "40",
        "12",
        "https://peaice.org/lovelabslca",
        "embed-end",
        "Status labels appear where the source carries them.",
        "These paths were unavailable during the 6 November 2026 inventory and are not linked.",
        "Love Labs LCA and PeAIce research references, with source statuses and link availability.",
        "Manuel Coleman's GitHub Pages",
    ):
        if marker not in html:
            failures.append(f"catalog is missing public marker {marker}")
    if "https://manny536.github.io/peaice-grok-index/references/" in html:
        failures.append("public catalog repeats its own hosted URL")
    readme = (ROOT / "README.md").read_text()
    for marker in (
        "56 input URL rows",
        "52 unique normalized paths",
        "40 catalog records",
        "12 unreachable paths",
        "4 input forms",
        "140 raw local references",
        "https://manny536.github.io/peaice-grok-index/references/",
        "http://peaice.org",
        "https://www.peaice.org",
        "https://peaice.org/lovelabslca/",
        "#grok-index",
        "embed-end",
        "KakeyaLogic",
        "primary_record",
    ):
        if marker not in readme:
            failures.append(f"README is missing coverage marker {marker}")
    if re.search(r"(?:min-)?height\s*:\s*(?:[8-9]\d{2}|\d{4,})px", html):
        failures.append("catalog CSS sets an enormous fixed pixel height")
    if 'id="link-status"' not in html or "Link status and unavailable records" not in html:
        failures.append("link status section is missing")
    if LOGIN_URL not in html:
        failures.append("401 destination is not recorded in the status section")

    home = HOME.read_text()
    for name, (start, end, digest) in HOME_BLOCKS.items():
        block = home[home.index(start):home.index(end)]
        found = hashlib.sha256(block.encode()).hexdigest()
        if found != digest:
            failures.append(f"Home section {name} changed ({found})")
    if "catalog.html" in home or "references/" in home:
        failures.append("Home root points at the Services catalog; keep that link on references/index.html only")
    if 'id="grok-index"' not in home:
        failures.append("Home is missing #grok-index")
    embed = home[home.index('<div id="embed-end"'):]
    if embed not in html:
        failures.append("catalog is missing the Home embed-end postMessage script")
    if "kakeyalogic" in html and "<iframe" in html:
        # Frames are allowed only for the two demos. A KakeyaLogic frame is not.
        for src in iframe_srcs:
            if "kakeyalogic" in src:
                failures.append(f"catalog frames KakeyaLogic: {src}")

    print(f"inventory rows={len(inventory['rows'])} normalized={len(inventory['by'])} included={len(inventory['included'])} unavailable={len(inventory['unavailable'])} folded={len(inventory['folded'])} primary_yes={inventory['primary_yes']}")
    print(f"catalog records={len(records)} groups={sorted({r['group'] for r in records.values()})} iframes={len(iframe_srcs)} hrefs={len(parsed.hrefs)}")
    if args.live:
        failures.extend(check_live(inventory["included"], []))
    if failures:
        print(f"FAIL {len(failures)}")
        for item in failures:
            print(f"- {item}")
        return 1
    print("PASS local catalog checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
