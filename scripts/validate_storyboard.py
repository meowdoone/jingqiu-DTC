#!/usr/bin/env python3
"""Validate a local storyboard-dtc-product-creative output directory."""

from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path
from typing import Iterable


IMAGE_EXTS = {".png", ".jpg", ".jpeg"}
PANEL_RATIO = 16 / 9
PANEL_RATIO_TOLERANCE = 0.04
FORBIDDEN_DIRECTOR_TERMS = [
    "director",
    "导演",
    "Denis Villeneuve",
    "Villeneuve",
    "David Fincher",
    "Fincher",
    "王家卫",
    "Wong Kar-wai",
    "Wong Kar Wai",
    "Wes Anderson",
]


def read_png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as file:
        header = file.read(24)
    if len(header) < 24 or not header.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def read_jpeg_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as file:
        data = file.read()
    if len(data) < 4 or data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG file")

    idx = 2
    while idx < len(data):
        if data[idx] != 0xFF:
            idx += 1
            continue
        while idx < len(data) and data[idx] == 0xFF:
            idx += 1
        if idx >= len(data):
            break
        marker = data[idx]
        idx += 1
        if marker in {0xD8, 0xD9}:
            continue
        if idx + 2 > len(data):
            break
        segment_len = struct.unpack(">H", data[idx : idx + 2])[0]
        if segment_len < 2 or idx + segment_len > len(data):
            break
        if marker in {
            0xC0,
            0xC1,
            0xC2,
            0xC3,
            0xC5,
            0xC6,
            0xC7,
            0xC9,
            0xCA,
            0xCB,
            0xCD,
            0xCE,
            0xCF,
        }:
            if idx + 7 > len(data):
                break
            height = struct.unpack(">H", data[idx + 3 : idx + 5])[0]
            width = struct.unpack(">H", data[idx + 5 : idx + 7])[0]
            return width, height
        idx += segment_len
    raise ValueError("could not find JPEG dimensions")


def read_image_size(path: Path) -> tuple[int, int]:
    suffix = path.suffix.lower()
    if suffix == ".png":
        return read_png_size(path)
    if suffix in {".jpg", ".jpeg"}:
        return read_jpeg_size(path)
    raise ValueError(f"unsupported image type: {suffix}")


def is_nonempty(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) > 0
    return True


def first_nonempty(*values: object) -> object:
    for value in values:
        if is_nonempty(value):
            return value
    return None


def get_nested(data: object, path: Iterable[object]) -> object:
    current = data
    for key in path:
        if isinstance(key, int):
            if not isinstance(current, list) or key >= len(current):
                return None
            current = current[key]
            continue
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def records_first_source_url(source_records: dict) -> object:
    records = first_nonempty(
        source_records.get("records"),
        source_records.get("source_records"),
        source_records.get("sources"),
    )
    if not isinstance(records, list):
        return None
    for record in records:
        if isinstance(record, dict) and is_nonempty(record.get("source_url")):
            return record.get("source_url")
    return None


def load_json(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as exc:
        raise ValueError(f"missing required file: {path.name}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path.name}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path.name} must contain a JSON object")
    return data


def normalize_run_metadata(run: dict, source_records: dict) -> dict:
    product_truth = first_nonempty(
        run.get("product_truth_card"),
        run.get("product_truth_lock"),
        get_nested(run, ["dtc_creative_reference_pack", "product_truth_lock"]),
    )
    if not isinstance(product_truth, dict):
        product_truth = {}

    pack = run.get("dtc_creative_reference_pack")
    if not isinstance(pack, dict):
        pack = {}

    brand_film_look_pack = run.get("brand_film_look_pack")
    if not isinstance(brand_film_look_pack, dict):
        brand_film_look_pack = {}

    creative_type = first_nonempty(
        run.get("creative_type"),
        get_nested(pack, ["creative_type", "id"]),
        pack.get("creative_type"),
    )
    scene_ref = first_nonempty(
        run.get("scene_ref"),
        get_nested(pack, ["scene_selection", "scene_ref"]),
    )
    motion_chain = first_nonempty(
        run.get("motion_chain"),
        get_nested(pack, ["motion_selection", "motion_chain"]),
    )
    model_ref = first_nonempty(
        run.get("model_ref"),
        get_nested(pack, ["model_selection", "model_ref"]),
    )
    camera_plan = first_nonempty(
        run.get("camera_plan"),
        get_nested(pack, ["camera_selection", "camera_plan"]),
    )
    brand_film_mode = first_nonempty(
        run.get("brand_film_mode"),
        pack.get("brand_film_mode"),
        brand_film_look_pack.get("brand_film_mode"),
    )
    end_frame = first_nonempty(
        run.get("end_frame"),
        pack.get("end_frame"),
    )

    output_paths = first_nonempty(run.get("output_paths"), run.get("outputs"))
    if not isinstance(output_paths, dict):
        output_paths = {}

    return {
        "source_url": first_nonempty(
            run.get("source_url"),
            get_nested(product_truth, ["source_evidence", 0, "source_url"]),
            records_first_source_url(source_records),
        ),
        "locked_terms": first_nonempty(run.get("locked_terms"), product_truth.get("locked_terms")),
        "creative_type": creative_type,
        "scene_ref": scene_ref,
        "motion_chain": motion_chain,
        "model_ref": model_ref,
        "camera_plan": camera_plan,
        "brand_film_mode": brand_film_mode,
        "brand_film_look_pack": first_nonempty(
            run.get("brand_film_look_pack"),
            run.get("brandFilmLookPack"),
        ),
        "end_frame": end_frame,
        "panel_count": first_nonempty(run.get("panel_count"), output_paths.get("panel_count")),
        "panel_aspect_ratio": first_nonempty(
            run.get("panel_aspect_ratio"), output_paths.get("panel_aspect_ratio")
        ),
        "panel_paths": first_nonempty(run.get("panel_paths"), output_paths.get("panel_paths")),
        "contact_sheet": first_nonempty(run.get("contact_sheet"), output_paths.get("contact_sheet")),
    }


def resolve_path(output_dir: Path, value: object, fallback: Path) -> Path:
    if isinstance(value, str) and value.strip():
        path = Path(value)
        return path if path.is_absolute() else output_dir / path
    return fallback


def list_panel_paths(output_dir: Path, metadata: dict) -> list[Path]:
    raw_panel_paths = metadata.get("panel_paths")
    if isinstance(raw_panel_paths, list) and raw_panel_paths:
        return [
            path if path.is_absolute() else output_dir / path
            for item in raw_panel_paths
            if isinstance(item, str)
            for path in [Path(item)]
        ]

    panels_dir = output_dir / "panels"
    if not panels_dir.exists():
        return []
    return sorted(
        path
        for path in panels_dir.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTS
    )


def validate_metadata(metadata: dict) -> list[str]:
    errors: list[str] = []
    for field in [
        "source_url",
        "locked_terms",
        "creative_type",
        "scene_ref",
        "motion_chain",
        "model_ref",
        "camera_plan",
        "brand_film_mode",
        "brand_film_look_pack",
        "end_frame",
    ]:
        if not is_nonempty(metadata.get(field)):
            errors.append(f"run.json missing non-empty `{field}`")
    camera_plan = metadata.get("camera_plan")
    if isinstance(camera_plan, dict):
        for field in [
            "opening_camera",
            "context_camera",
            "proof_camera",
            "use_camera",
            "end_frame_camera",
        ]:
            if not is_nonempty(camera_plan.get(field)):
                errors.append(f"run.json `camera_plan` missing non-empty `{field}`")
    elif "camera_plan" in metadata:
        errors.append("run.json `camera_plan` must be an object")

    brand_film_mode = metadata.get("brand_film_mode")
    if isinstance(brand_film_mode, dict):
        for field in [
            "mode_id",
            "visual_signature",
            "key_technique",
            "product_translation",
            "camera_translation",
            "lighting_translation",
            "risk",
        ]:
            if not is_nonempty(brand_film_mode.get(field)):
                errors.append(f"run.json `brand_film_mode` missing non-empty `{field}`")
        exposed_text = json.dumps(brand_film_mode, ensure_ascii=False)
        for term in FORBIDDEN_DIRECTOR_TERMS:
            if term in exposed_text:
                errors.append(f"run.json `brand_film_mode` exposes forbidden director term `{term}`")
    elif "brand_film_mode" in metadata:
        errors.append("run.json `brand_film_mode` must be an object")

    brand_film_look_pack = metadata.get("brand_film_look_pack")
    if isinstance(brand_film_look_pack, dict):
        for field in [
            "brand_film_mode",
            "brand_world_lock",
            "cinematic_grammar",
            "shot_function_map",
            "material_and_light_rules",
            "pacing_rules",
            "signature_shot",
            "end_frame_rule",
            "failure_rules",
        ]:
            if not is_nonempty(brand_film_look_pack.get(field)):
                errors.append(f"run.json `brand_film_look_pack` missing non-empty `{field}`")

        shot_function_map = brand_film_look_pack.get("shot_function_map")
        if isinstance(shot_function_map, dict):
            panels = shot_function_map.get("panels")
            if not isinstance(panels, list) or not panels:
                errors.append("run.json `brand_film_look_pack.shot_function_map.panels` must be a non-empty list")
        elif "shot_function_map" in brand_film_look_pack:
            errors.append("run.json `brand_film_look_pack.shot_function_map` must be an object")

        exposed_text = json.dumps(brand_film_look_pack, ensure_ascii=False)
        for term in FORBIDDEN_DIRECTOR_TERMS:
            if term in exposed_text:
                errors.append(f"run.json `brand_film_look_pack` exposes forbidden director term `{term}`")
    elif "brand_film_look_pack" in metadata:
        errors.append("run.json `brand_film_look_pack` must be an object")

    end_frame = metadata.get("end_frame")
    if isinstance(end_frame, dict):
        for field in [
            "product_position",
            "logo_or_label_visibility",
            "proof_memory",
            "CTA_intent",
            "camera_state",
            "lighting_state",
        ]:
            if not is_nonempty(end_frame.get(field)):
                errors.append(f"run.json `end_frame` missing non-empty `{field}`")
    elif "end_frame" in metadata:
        errors.append("run.json `end_frame` must be an object")

    if metadata.get("panel_count") not in (None, 5):
        errors.append("run.json `panel_count` must be 5 when present")
    if metadata.get("panel_aspect_ratio") not in (None, "16:9"):
        errors.append("run.json `panel_aspect_ratio` must be `16:9` when present")
    return errors


def validate_contact_sheet(output_dir: Path, metadata: dict) -> list[str]:
    errors: list[str] = []
    contact_sheet = resolve_path(
        output_dir, metadata.get("contact_sheet"), output_dir / "contact_sheet.png"
    )
    if not contact_sheet.exists():
        return [f"contact sheet not found: {contact_sheet}"]

    try:
        width, height = read_image_size(contact_sheet)
    except ValueError as exc:
        return [f"contact sheet size read failed: {exc}"]

    if width <= 0 or height <= 0:
        errors.append(f"contact sheet has invalid size: {width}x{height}")
    return errors


def validate_panels(output_dir: Path, metadata: dict) -> list[str]:
    errors: list[str] = []
    panels = list_panel_paths(output_dir, metadata)
    if len(panels) != 5:
        errors.append(f"expected 5 panel images, found {len(panels)}")
        return errors

    for panel in panels:
        if not panel.exists():
            errors.append(f"panel not found: {panel}")
            continue
        try:
            width, height = read_image_size(panel)
        except ValueError as exc:
            errors.append(f"{panel.name} size read failed: {exc}")
            continue
        if height <= 0:
            errors.append(f"{panel.name} has invalid height 0")
            continue
        ratio = width / height
        if abs(ratio - PANEL_RATIO) > PANEL_RATIO_TOLERANCE:
            errors.append(f"{panel.name} must be 16:9; got {width}x{height} ratio={ratio:.3f}")
    return errors


def validate_output(output_dir: Path) -> list[str]:
    errors: list[str] = []
    try:
        run = load_json(output_dir / "run.json")
    except ValueError as exc:
        return [str(exc)]

    try:
        source_records = load_json(output_dir / "source_records.json")
    except ValueError as exc:
        errors.append(str(exc))
        source_records = {}

    metadata = normalize_run_metadata(run, source_records)
    errors.extend(validate_metadata(metadata))
    errors.extend(validate_contact_sheet(output_dir, metadata))
    errors.extend(validate_panels(output_dir, metadata))
    return errors


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a storyboard output directory for horizontal 5-panel DTC storyboard delivery."
    )
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args(list(argv) if argv is not None else None)

    output_dir = args.output_dir.expanduser().resolve()
    if not output_dir.exists():
        print(f"ERROR: output directory not found: {output_dir}", file=sys.stderr)
        return 2
    if not output_dir.is_dir():
        print(f"ERROR: output path is not a directory: {output_dir}", file=sys.stderr)
        return 2

    errors = validate_output(output_dir)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: storyboard output valid: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
