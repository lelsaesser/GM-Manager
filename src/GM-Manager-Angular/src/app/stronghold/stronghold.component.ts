import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL, SHC_API } from './../env';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-stronghold',
  templateUrl: './stronghold.component.html',
  styleUrls: ['./stronghold.component.css']
})
export class StrongholdComponent {

  show_ai_battle: boolean = false;
  shcJson: JSON;
  SHC_API_URL = `${API_URL}` + `${SHC_API}`;

  formSubmitWinningTeam = new FormGroup({
    formWinningTeamSelection: new FormControl('')
  })

  constructor(private httpClient: HttpClient) { }

  fetchShcBattleDataWithPlayerCount(ai_count) {
    this.httpClient.post(this.SHC_API_URL,
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
        () => {
        });
  }

  onSubmitWinningTeam() {
    console.log("onSubmitWinningTeam triggered");
  }
}
