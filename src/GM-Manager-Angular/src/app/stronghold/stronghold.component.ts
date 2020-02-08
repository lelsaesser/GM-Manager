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

  shcJson: JSON;

  formSubmitWinningTeamData: any;

  formSubmitWinningTeam = new FormGroup({
    formWinningTeamSelection: new FormControl('')
  })

  constructor(private httpClient: HttpClient, private notifyService: NotificationService) { }

  fetchShcBattleDataWithPlayerCount(ai_count) {
    this.httpClient.post(API_URL + API_STRONGHOLD_GET_AI_BATTLE,
      {
        "shc_ai_battle_player_count": ai_count
      }).subscribe(data => {
        this.shcJson = data as JSON
        this.show_ai_battle = true
        console.log("POST call successful value returned in body", data);
      },
        response => {
          console.log("POST call error:", response);
        },
      );
  }

  onSubmitWinningTeam() {
    this.formSubmitWinningTeamData = this.formSubmitWinningTeam.value as JSON
    if (this.formSubmitWinningTeamData.formWinningTeamSelection == "") {
      this.formSubmitWinningTeamData.formWinningTeamSelection = String(this.shcJson["shcData"][0].teams[0]);
    }

    this.httpClient.post(API_URL + API_SHC_RANKING_UPDATE,
      {
        "winningTeamData": this.formSubmitWinningTeamData
      }).subscribe(data => {
        this.notifyService.showSuccess("Ranking updated", "Success");
        this.formSubmitWinningTeamSubmitted = true;
        // this.fetchRanking();
      },
        response => {
          console.log("POST call error:", response);
        }
      );
  }
}
