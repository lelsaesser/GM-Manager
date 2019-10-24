import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL, API_SURVRUN_GET_TARGET_LOCATION } from './../env';

@Component({
  selector: 'app-survrim',
  templateUrl: './survrim.component.html',
  styleUrls: ['./survrim.component.css']
})
export class SurvrimComponent {

  survrunJson: JSON;
  SURVRIM_API_URL = `${API_URL}` + `${API_SURVRUN_GET_TARGET_LOCATION}`;

  constructor(private httpClient: HttpClient) {}

  fetchSurvrunData() {
    this.httpClient.get(this.SURVRIM_API_URL).subscribe(data => {
      this.survrunJson = data as JSON;
    })
  }

}
