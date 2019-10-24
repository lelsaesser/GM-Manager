import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL, SHC_API } from './../env';

@Component({
  selector: 'app-stronghold',
  templateUrl: './stronghold.component.html',
  styleUrls: ['./stronghold.component.css']
})
export class StrongholdComponent {

  shcJson: JSON;
  SHC_API_URL = `${API_URL}` + `${SHC_API}`;

  constructor(private httpClient: HttpClient) { }

  fetchShcBattleDataWithPlayerCount(ai_count) {
    this.httpClient.post(this.SHC_API_URL,
      {
        "shc_ai_battle_player_count": ai_count
      }).subscribe(data => {
        this.shcJson = data as JSON
        console.log("POST call successful value returned in body", data);
      },
        response => {
          console.log("POST call in error", response);
        },
        () => {
          console.log("The POST observable is now completed.");
        });
  }
}
