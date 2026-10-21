"""
Universal Cross-Agent Installer for the WeVisa Agent Plugin & Modular Agent Skills.

Installs the `wevisa` plugin and 7 modular `SKILL.md` Agent Skills globally so ANY
compliant coding agent (Claude Code, OpenAI Codex CLI, Gemini CLI, Cursor, Windsurf,
Claude Desktop, Antigravity) can prepare O-1A, O-1B, and EB-1A petitions from any
client document folder using the WeVisa MCP server (`https://wevisa.ai/mcp`).

Usage:
    # Install for all agents (connects to https://wevisa.ai/mcp by default):
    python install.py

    # Or point to a custom MCP server URL (e.g., local server):
    python install.py --http-url http://127.0.0.1:8001/mcp
"""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
from typing import Dict, Any


PLUGIN_ROOT = Path(__file__).resolve().parent
SKILLS_SRC_DIR = PLUGIN_ROOT / "skills"
DEFAULT_MCP_URL = os.environ.get("WEVISA_MCP_URL", "https://wevisa.ai/mcp")


def copy_skills_to_dir(target_skills_dir: Path) -> int:
    """Copy all 7 modular Agent Skills (`<skill-name>/SKILL.md`) into `target_skills_dir`."""
    if not SKILLS_SRC_DIR.exists():
        return 0
    target_skills_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for skill_folder in sorted(SKILLS_SRC_DIR.iterdir()):
        if skill_folder.is_dir() and (skill_folder / "SKILL.md").exists():
            dest = target_skills_dir / skill_folder.name
            if dest.resolve() == skill_folder.resolve():
                count += 1
                continue
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(skill_folder, dest)
            count += 1
    return count


def copy_plugin_bundle(target_plugin_dir: Path, http_url: str) -> int:
    """Copy the complete Agent Plugin bundle into `target_plugin_dir`."""
    if target_plugin_dir.resolve() != PLUGIN_ROOT.resolve():
        if target_plugin_dir.exists():
            shutil.rmtree(target_plugin_dir)
        shutil.copytree(
            PLUGIN_ROOT,
            target_plugin_dir,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
        )

    mcp_payload = {"mcpServers": {"wevisa": {"type": "http", "url": http_url}}}
    (target_plugin_dir / "mcp_config.json").write_text(json.dumps(mcp_payload, indent=2) + "\n", encoding="utf-8")
    (target_plugin_dir / ".mcp.json").write_text(json.dumps(mcp_payload, indent=2) + "\n", encoding="utf-8")

    gemini_ext_path = target_plugin_dir / "gemini-extension.json"
    if gemini_ext_path.exists():
        ext_data = json.loads(gemini_ext_path.read_text(encoding="utf-8"))
        ext_data["mcpServers"] = {"wevisa": {"httpUrl": http_url}}
        gemini_ext_path.write_text(json.dumps(ext_data, indent=2) + "\n", encoding="utf-8")

    return len(list((target_plugin_dir / "skills").glob("*/SKILL.md")))


def update_json_mcp_config(config_path: Path, server_name: str, server_entry: Dict[str, Any]) -> None:
    """Safely merge `mcpServers[server_name] = server_entry` into a JSON config file."""
    config_path.parent.mkdir(parents=True, exist_ok=True)
    data: Dict[str, Any] = {}
    if config_path.exists():
        try:
            raw = config_path.read_text(encoding="utf-8").strip()
            if raw:
                data = json.loads(raw)
        except Exception:
            shutil.copyfile(config_path, config_path.with_suffix(config_path.suffix + ".bak"))
            data = {}

    if not isinstance(data.get("mcpServers"), dict):
        data["mcpServers"] = {}
    data["mcpServers"][server_name] = server_entry
    config_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Install the WeVisa Agent Plugin & Skills globally.")
    parser.add_argument(
        "--http-url",
        default=DEFAULT_MCP_URL,
        help=f"Remote MCP server URL (default: {DEFAULT_MCP_URL}).",
    )
    args = parser.parse_args()

    home = Path.home()
    http_url = args.http_url

    print(f"=== Installing WeVisa Agent Plugin + Agent Skills ({http_url}) ===")

    # 1. Standard Agent Plugins & Agent Skills directories
    global_plugin_dir = home / ".gemini" / "config" / "plugins" / "wevisa"
    n_skills = copy_plugin_bundle(global_plugin_dir, http_url)
    copy_skills_to_dir(home / ".agents" / "skills")
    print(f"[Agent Plugins & Skills] Installed in {global_plugin_dir} and {home / '.agents' / 'skills'} ({n_skills} skills)")

    # 2. Claude Code
    update_json_mcp_config(home / ".claude.json", "wevisa", {"type": "http", "url": http_url})
    copy_skills_to_dir(home / ".claude" / "skills")
    copy_plugin_bundle(home / ".claude" / "plugins" / "wevisa", http_url)
    print(f"[Claude Code] Installed in {home / '.claude' / 'plugins' / 'wevisa'} and {home / '.claude.json'}")

    # 3. OpenAI Codex CLI
    codex_dir = home / ".codex"
    codex_dir.mkdir(parents=True, exist_ok=True)
    config_toml = codex_dir / "config.toml"
    existing = config_toml.read_text(encoding="utf-8") if config_toml.exists() else ""
    cleaned = re.sub(r"\[mcp_servers\.wevisa\][^\[]*", "", existing, flags=re.DOTALL).rstrip()
    block = f'\n\n[mcp_servers.wevisa]\nurl = "{http_url}"\n'
    config_toml.write_text((cleaned + block).lstrip() + "\n", encoding="utf-8")
    copy_skills_to_dir(codex_dir / "skills")
    print(f"[OpenAI Codex] Installed in {config_toml} and {codex_dir / 'skills'}")

    # 4. Gemini CLI
    update_json_mcp_config(home / ".gemini" / "settings.json", "wevisa", {"httpUrl": http_url})
    copy_skills_to_dir(home / ".gemini" / "skills")
    copy_plugin_bundle(home / ".gemini" / "extensions" / "wevisa", http_url)
    print(f"[Gemini CLI] Installed in {home / '.gemini' / 'extensions' / 'wevisa'}")

    # 5. Cursor, Windsurf & Antigravity
    update_json_mcp_config(home / ".cursor" / "mcp.json", "wevisa", {"url": http_url})
    update_json_mcp_config(home / ".codeium" / "windsurf" / "mcp_config.json", "wevisa", {"serverUrl": http_url})
    update_json_mcp_config(home / ".gemini" / "antigravity" / "mcp_config.json", "wevisa", {"serverUrl": http_url})
    copy_skills_to_dir(home / ".gemini" / "antigravity" / "skills")
    print("[Cursor / Windsurf / Antigravity] Installed global MCP configs and skills.")

    print("\nDone! Launch `claude`, `codex`, `gemini`, `cursor`, or `agy` in any client document folder.")


if __name__ == "__main__":
    main()
