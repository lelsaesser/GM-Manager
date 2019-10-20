import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_URL } from './env';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  survrunData: JSON;
  title = 'GM-Manager-Frontend';
  SURVRIM_API_URL = `${API_URL}` + '/api/survrim';

  constructor(private httpClient: HttpClient) {}

  fetchSurvrunData() {
    this.httpClient.get(this.SURVRIM_API_URL).subscribe(data => {
      this.survrunData = data as JSON;
    })
  }
}
