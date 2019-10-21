import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './../env';

@Component({
  selector: 'app-survrim',
  templateUrl: './survrim.component.html',
  styleUrls: ['./survrim.component.css']
})
export class SurvrimComponent {

  survrunJson: JSON;
  SURVRIM_API_URL = `${API_URL}` + '/api/survrim';

  constructor(private httpClient: HttpClient) {}

  fetchSurvrunData() {
    this.httpClient.get(this.SURVRIM_API_URL).subscribe(data => {
      this.survrunJson = data as JSON;
    })
  }

}
