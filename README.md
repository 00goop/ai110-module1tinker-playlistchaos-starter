# Playlist Chaos

A CodePath AI110 coursework project in Python and Streamlit: normalize song
metadata, group a catalog into Hype/Chill/Mixed playlists and explore the results.
The scoring rules are inspectable Python, not a trained recommendation model.

## Run

`pip install -r requirements.txt` then `streamlit run app.py`.
Run deterministic checks with `pip install pytest` and `python -m pytest -q`.

## Repairs and decisions

- Hype ratio and mean energy use the complete catalog, not just the Hype group.
- Partial artist search works in the expected direction.
- Merging playlists does not mutate its inputs; duplicates are preserved as entries.
- Empty random picks return None; any-mode includes Mixed songs.
- Invalid energy values become zero, valid values are clamped to 0–10.
- Classification handles title case and honors the include-mixed profile option.

CI checks these behaviors without external services. Session UI data is local to
Streamlit; there is no account, persistent database or published deployment claim.
