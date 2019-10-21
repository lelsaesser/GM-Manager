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

  constructor(private httpClient: HttpClient) {}

  fetchShcBattleData() {
    this.httpClient.get(this.SHC_API_URL).subscribe(data => {
      this.shcJson = data as JSON;
    })
  }

}
