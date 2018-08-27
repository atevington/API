from models.pick import PickModel
from models.game import GameModel
from models.playerTeam import PlayerTeamModel
from controllers.game import GameController

from models.league_type import LeagueTypes

from .game import GameController


class StandardLeagueAdvanceController:

    @classmethod
    def advance_week(cls, league):
        GameController.update_games()
        league_type_name = league.league_type.league_type_name
        week_num = GameModel.get_max_week()

        if not league_type_name == LeagueTypes.STANDARD.name:
            return {'message': 'League is not Standard.'}

        active_teams = PlayerTeamModel.get_active_teams_in_league(league.league_id)
        losing_nfl_teams = GameController.get_losers_for_week(week_num)
        deactivated_teams = []
        advancing_teams = []
        for active_team in active_teams:
            pick = PickModel.find_pick_by_week_and_team_id(week_num, active_team.team_id)
            if pick.nfl_team_name in losing_nfl_teams:
                active_team.is_active = False
                deactivated_teams.append(active_team)
            else:
                active_team.streak += 1
                advancing_teams.append(active_team)
            #active_team.upsert()

        return {
            'deactivated_teams': [deactivated_team.json() for deactivated_team in deactivated_teams],
            'advancing_teams': [advancing_team.json() for advancing_team in advancing_teams]
        }



