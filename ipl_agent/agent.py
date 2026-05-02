import datetime
import os
from google.adk.agents import Agent
print("API KEY:", os.getenv("GOOGLE_API_KEY"))

def get_live_match_state(match_id: str) -> dict:
    """
    Returns the current score, wickets, overs, run rate, required run rate,
    current batsmen, current bowler, venue, and match phase for mock matches.

    Args:
        match_id (str): The ID of the match to retrieve data for (e.g., 'csk_vs_rr_2026', 'mi_vs_kkr_2026').

    Returns:
        dict: Live match state information including status.
    """
    matches = {
        "csk_vs_rr_2026": {
            "score": 145,
            "wickets": 3,
            "overs": 15.2,
            "run_rate": 9.45,
            "required_run_rate": 8.5,
            "current_batsmen": ["MS Dhoni", "Ruturaj Gaikwad"],
            "current_bowler": "Trent Boult",
            "venue": "Chepauk Chennai",
            "match_phase": "death"
        },
        "mi_vs_kkr_2026": {
            "score": 85,
            "wickets": 5,
            "overs": 10.0,
            "run_rate": 8.5,
            "required_run_rate": 10.2,
            "current_batsmen": ["Suryakumar Yadav", "Hardik Pandya"],
            "current_bowler": "Sunil Narine",
            "venue": "Wankhede Mumbai",
            "match_phase": "middle"
        }
    }
    
    if match_id in matches:
        data = matches[match_id]
        data["status"] = "success"
        return data
    else:
        return {"status": "error", "message": f"Match ID '{match_id}' not found."}


def get_player_momentum_score(player_name: str, match_id: str) -> dict:
    """
    Calculates a momentum score from 0 to 100 using a custom RPO-weighted algorithm.

    Args:
        player_name (str): Name of the player.
        match_id (str): The ID of the match.

    Returns:
        dict: Contains momentum_score, form_label (Hot, Warm, Cold), trend, and status.
    """
    # Mock calculation based on prompt instructions
    base_score = 60
    if player_name in ["MS Dhoni", "Suryakumar Yadav"]:
        base_score = 85
    elif player_name in ["Trent Boult", "Sunil Narine"]:
        base_score = 78
        
    momentum_score = min(100, max(0, base_score))
    
    if momentum_score > 75:
        form_label = "Hot"
    elif momentum_score > 50:
        form_label = "Warm"
    else:
        form_label = "Cold"
        
    return {
        "status": "success",
        "momentum_score": momentum_score,
        "form_label": form_label,
        "trend": "upward" if momentum_score > 60 else "stable"
    }


def get_win_probability(match_id: str) -> dict:
    """
    Computes a win probability using runs needed, balls remaining, wickets in hand, and RR gap.
    First calls get_live_match_state internally.

    Args:
        match_id (str): The match ID.

    Returns:
        dict: Contains batting_team_win_prob, bowling_team_win_prob, prediction_summary, and status.
    """
    state = get_live_match_state(match_id)
    if state["status"] == "error":
        return state

    rr_gap = state.get("required_run_rate", 0) - state.get("run_rate", 0)
    wickets = state.get("wickets", 0)
    
    # Base probability
    bat_prob = 50.0
    
    # Simple heuristic adjustments
    bat_prob -= (wickets * 4)
    if rr_gap > 0:
        bat_prob -= (rr_gap * 4)
    else:
        bat_prob += (abs(rr_gap) * 4)
        
    bat_prob = max(5.0, min(95.0, bat_prob))
    bowl_prob = 100.0 - bat_prob
    
    return {
        "status": "success",
        "batting_team_win_prob": round(bat_prob, 2),
        "bowling_team_win_prob": round(bowl_prob, 2),
        "prediction_summary": f"Based on RR gap and wickets, batting team has {bat_prob:.1f}% chance."
    }


def get_fantasy_xi_recommendation(match_id: str) -> dict:
    """
    Returns a fantasy XI recommendation including captain, vice-captain, and differential picks.

    Args:
        match_id (str): The match ID.

    Returns:
        dict: Contains captain pick, vice-captain pick, differential pick, players to avoid, recommended XI, and status.
    """
    if match_id == "csk_vs_rr_2026":
        return {
            "status": "success",
            "captain": "MS Dhoni",
            "vice_captain": "Trent Boult",
            "differential": "Ruturaj Gaikwad",
            "avoid": ["Player X (Poor form)"],
            "recommended_xi": ["MS Dhoni", "Ruturaj Gaikwad", "Trent Boult", "Yashasvi Jaiswal", "Sanju Samson", "Ravindra Jadeja", "Yuzvendra Chahal", "Shivam Dube", "R Ashwin", "Matheesha Pathirana", "Jos Buttler"]
        }
    elif match_id == "mi_vs_kkr_2026":
        return {
            "status": "success",
            "captain": "Suryakumar Yadav",
            "vice_captain": "Sunil Narine",
            "differential": "Hardik Pandya",
            "avoid": ["Player A (Injury concern)"],
            "recommended_xi": ["Suryakumar Yadav", "Sunil Narine", "Hardik Pandya", "Rohit Sharma", "Shreyas Iyer", "Jasprit Bumrah", "Andre Russell", "Ishan Kishan", "Rinku Singh", "Mitchell Starc", "Varun Chakaravarthy"]
        }
    else:
        return {"status": "error", "message": "Fantasy data not available for this match ID."}


def get_historical_patterns(venue: str, target: int) -> dict:
    """
    Returns historical chase win percentage, average first innings score, pitch type, and chase success rate.

    Args:
        venue (str): The venue name (e.g., 'Chepauk Chennai', 'Wankhede Mumbai').
        target (int): The target score.

    Returns:
        dict: Contains historical patterns, insight string, and status.
    """
    if "Chepauk" in venue:
        band = "140-154" if 140 <= target <= 154 else "155-169" if 155 <= target <= 169 else "170-185" if 170 <= target <= 185 else "Other"
        return {
            "status": "success",
            "historical_chase_win_pct": 45.5,
            "avg_first_innings_score": 165,
            "pitch_type": "Spin-friendly, slow turner",
            "chase_success_rate_band": {band: 35.0},
            "insight": f"At Chepauk, chasing {target} is difficult due to dew and pitch slowing down. Spinners are key."
        }
    elif "Wankhede" in venue:
        band = "140-154" if 140 <= target <= 154 else "155-169" if 155 <= target <= 169 else "170-185" if 170 <= target <= 185 else "Other"
        return {
            "status": "success",
            "historical_chase_win_pct": 62.0,
            "avg_first_innings_score": 185,
            "pitch_type": "Batting paradise, good bounce",
            "chase_success_rate_band": {band: 70.0},
            "insight": f"At Wankhede, chasing {target} is achievable. The pitch remains true."
        }
    else:
        return {"status": "error", "message": "Venue data not found."}


instruction = '''You are an expert IPL analyst and fantasy cricket advisor.

Always call get_live_match_state first before any prediction or analysis.
Chain tools intelligently:
- For win probability, call live state then compute.
- For fantasy advice, call momentum scores first then recommend.

Communicate like a sharp Sky Sports expert:
- Lead with the key insight.
- Back it up with data.
- End with a clear actionable recommendation.
Keep answers concise unless the user asks for detail.'''

root_agent = Agent(
    name='ipl_momentum_agent',
    model="gemini-flash-latest",
    description='Expert IPL analyst agent for match predictions and fantasy cricket advice.',
    instruction=instruction,
    tools=[get_live_match_state, get_player_momentum_score, get_win_probability, get_fantasy_xi_recommendation, get_historical_patterns]
)
