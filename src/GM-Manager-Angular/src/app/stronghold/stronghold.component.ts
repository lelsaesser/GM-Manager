import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL, API_STRONGHOLD_GET_AI_BATTLE, API_SHC_RANKING_UPDATE } from './../env';
import { FormControl, FormGroup } from '@angular/forms';
import { NotificationService } from 'src/utils/notification.service';

@Component({
  selector: 'app-stronghold',
  templateUrl: './stronghold.component.html',
  styleUrls: ['./stronghold.component.css']
})
export class StrongholdComponent {

  show_ai_battle: boolean = false;
  formSubmitWinningTeamSubmitted: boolean = false;
  rankingDataFetched: boolean = false;

  shcJson: JSON;
  shcRankingJson: JSON;

  formSubmitWinningTeamData: any;
  loosingTeamData: any;
  winningTeamData: any;
  involvedPlayers: any;

  formSubmitWinningTeam = new FormGroup({
    formWinningTeamSelection: new FormControl(''),
    formMVPSelection: new FormControl(''),
    formExceptionSelection: new FormControl('')
  });

  constructor(private httpClient: HttpClient, private notifyService: NotificationService) { }

  fetchShcBattleDataWithPlayerCount(ai_count) {
    this.httpClient.post(API_URL + API_STRONGHOLD_GET_AI_BATTLE,
      {
        "shc_ai_battle_player_count": ai_count
      }).subscribe(data => {
        this.shcJson = data as JSON;
        this.involvedPlayers = this.shcJson["shcData"][0].teams[0].concat(this.shcJson["shcData"][0].teams[1]);
        this.involvedPlayers = ["None"].concat(this.involvedPlayers);
        this.show_ai_battle = true;
      },
        response => {
          console.log("POST call error:", response);
        },
      );
  }

  fetchShcRanking() {
    this.httpClient.get(API_URL + API_SHC_RANKING_UPDATE).subscribe(data => {
      this.shcRankingJson = data as JSON;
      this.rankingDataFetched = true;
    });
  }

  onSubmitWinningTeam() {
    this.formSubmitWinningTeamData = this.formSubmitWinningTeam.value as JSON;

    if (this.formSubmitWinningTeamData.formWinningTeamSelection == String(this.shcJson["shcData"][0].teams[1])) {
      this.winningTeamData = this.shcJson["shcData"][0].teams[1];
      this.loosingTeamData = this.shcJson["shcData"][0].teams[0];
    }
    else {
      this.winningTeamData = this.shcJson["shcData"][0].teams[0];
      this.loosingTeamData = this.shcJson["shcData"][0].teams[1];
    }

    if (this.formSubmitWinningTeamData.formMVPSelection == "") {
      this.formSubmitWinningTeamData.formMVPSelection = this.involvedPlayers[0];
    }
    if (this.formSubmitWinningTeamData.formExceptionSelection == "") {
      this.formSubmitWinningTeamData.formExceptionSelection = this.involvedPlayers[0];
    }

    this.httpClient.post(API_URL + API_SHC_RANKING_UPDATE,
      {
        "winning_team": this.winningTeamData,
        "loosing_team": this.loosingTeamData,
        "mvp": this.formSubmitWinningTeamData.formMVPSelection,
        "exception": this.formSubmitWinningTeamData.formExceptionSelection
      }).subscribe(data => {
        this.notifyService.showSuccess("Ranking updated", "Success");
        this.formSubmitWinningTeamSubmitted = true;
        this.fetchShcRanking();
      },
        response => {
          this.notifyService.showFailure("Backend not reachable", "Error");
          console.log("POST call error:", response);
        }
      );
  }

  ngOnInit() {
    this.fetchShcRanking();
    if (this.shcRankingJson) {
      this.rankingDataFetched = true;
    }
  }
}
