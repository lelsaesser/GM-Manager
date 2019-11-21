import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NotificationService } from '../../utils/notification.service'

import {
  API_URL,
  API_ESO_GET_CONSTANTS,
  API_ESO_GET_DUNGEON_RUNS
} from './../env'

@Component({
  selector: 'app-eso',
  templateUrl: './eso.component.html',
  styleUrls: ['./eso.component.css']
})
export class EsoComponent implements OnInit {

  esoConstantsSet: boolean = false;
  esoDungeonDataSet: boolean = false;

  esoConstants: JSON;
  esoDungeonData: JSON;

  constructor(private httpClient: HttpClient, private notifyService: NotificationService) { }

  fetchEsoConstants() {
    this.httpClient.get(API_URL + API_ESO_GET_CONSTANTS).subscribe(data => {
      this.esoConstants = data as JSON;
      this.esoConstantsSet = true;
    },
      response => {
        this.notifyService.showFailure("Backend is not reachable.", "Error")
      })
  }

  fetchRecordedDungeonRuns() {
    this.httpClient.get(API_URL + API_ESO_GET_DUNGEON_RUNS).subscribe(data => {
      this.esoDungeonData = data as JSON;
      this.esoDungeonDataSet = true;
    },
      response => {
        this.notifyService.showFailure("Backend is not reachable.", "Error")
      })
  }

  ngOnInit() {
    this.fetchEsoConstants();
  }

}
