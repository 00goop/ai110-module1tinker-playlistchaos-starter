import pytest
from playlist_logic import *

def test_stats_use_all_categories():
 p=build_playlists([{'energy':9},{'energy':1},{'energy':5}],DEFAULT_PROFILE)
 s=compute_playlist_stats(p)
 assert s['hype_ratio']==pytest.approx(1/3)
 assert s['avg_energy']==5

def test_search_matches_partial_artist():
 songs=[{'artist':'Nina Simone'}]
 assert search_songs(songs,'simone')==songs
 assert search_songs(songs,'unrelated')==[]

def test_merge_does_not_mutate_inputs():
 a={'Hype':[{'title':'A'}]};b={'Hype':[{'title':'B'}]}
 merged=merge_playlists(a,b);merged['Hype'][0]['title']='Changed'
 assert a=={'Hype':[{'title':'A'}]}
 assert len(merged['Hype'])==2

def test_empty_and_mixed_random_picks():
 assert lucky_pick({}) is None
 assert lucky_pick({'Mixed':[{'title':'Only'}]})['title']=='Only'

@pytest.mark.parametrize('energy',[None,'bad',float('nan'),float('inf')])
def test_invalid_energy_is_safe(energy):
 assert normalize_song({'energy':energy})['energy']==0

def test_profile_and_case_boundaries():
 profile={**DEFAULT_PROFILE,'favorite_genre':'jazz','include_mixed':False}
 assert classify_song(normalize_song({'title':'SLEEP sounds','energy':4}),profile)=='Chill'
 assert build_playlists([{'energy':5,'genre':'pop'}],profile)['Mixed']==[]
