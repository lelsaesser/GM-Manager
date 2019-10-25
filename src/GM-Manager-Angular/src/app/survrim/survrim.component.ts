import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL, API_SURVRUN_GET_TARGET_LOCATION, API_SURVRIM_GET_CLASS_DATA } from './../env';

@Component({
  selector: 'app-survrim',
  templateUrl: './survrim.component.html',
  styleUrls: ['./survrim.component.css']
})
export class SurvrimComponent {

  show_targets: boolean = false;
  show_class: boolean = false;
  survrunJson: JSON;
  survrimClassData: JSON

  constructor(private httpClient: HttpClient) {}

  fetchSurvrunData() {
    this.httpClient.get(API_URL + API_SURVRUN_GET_TARGET_LOCATION).subscribe(data => {
      this.survrunJson = data as JSON;
      this.show_targets = true;
      console.log("GET call fetchSurvrunData() successful. Value returned in body: ", data);
    })
  }

  fetchSurvrimClass() {
    this.httpClient.get(API_URL + API_SURVRIM_GET_CLASS_DATA).subscribe(data => {
      this.survrimClassData = data as JSON
      this.show_class = true;
      console.log("GET call fetchSurvrimClass() successful. Value returned in body: ", data);
    })
  }

}
