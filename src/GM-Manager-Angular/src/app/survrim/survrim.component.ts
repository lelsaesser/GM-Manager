import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL, API_SURVRUN_GET_TARGET_LOCATION, API_SURVRIM_GET_CLASS_DATA, API_SURVRUN_GET_ALL_DB_RUN_DATA } from './../env';

@Component({
  selector: 'app-survrim',
  templateUrl: './survrim.component.html',
  styleUrls: ['./survrim.component.css']
})
export class SurvrimComponent {

  show_targets: boolean = false;
  show_class: boolean = false;
  show_queryResultSurvrunData: boolean = false;
  survrunJson: JSON;
  survrimClassData: JSON;
  queryResultSurvrunData: JSON;

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
      this.survrimClassData = data as JSON;
      this.show_class = true;
      console.log("GET call fetchSurvrimClass() successful. Value returned in body: ", data);
    })
  }

  querySurvrunTableGetAllRuns() {
    this.httpClient.get(API_URL + API_SURVRUN_GET_ALL_DB_RUN_DATA).subscribe(data => {
      this.queryResultSurvrunData = data as JSON;
      this.show_queryResultSurvrunData = true;
      console.log("GET call querySurvrunTableGetAllRuns() successfull. Value returned in body: ", data)
    })
  }

}
