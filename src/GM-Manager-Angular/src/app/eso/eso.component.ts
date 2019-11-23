import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NotificationService } from '../../utils/notification.service'

import {
  API_URL,
  API_ESO_GET_CONSTANTS,
  API_ESO_GET_DUNGEON_RUNS,
  API_ESO_POST_DUNGEON_RUN
} from './../env'
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-eso',
  templateUrl: './eso.component.html',
  styleUrls: ['./eso.component.css']
})
export class EsoComponent implements OnInit {

  esoConstantsSet: boolean = false;
  esoDungeonDataSet: boolean = false;
  formSubmitDungeonRunSubmitted: boolean = false;

  esoConstants: JSON;
  esoDungeonData: JSON;

  formSubmitDungeonRunData: any;

  booleanDropdownValues = ["no", "yes"];

  formSubmitDungeonRun = new FormGroup({
    formPlayerCount: new FormControl('', Validators.compose([Validators.required, Validators.min(1), Validators.max(4)])),
    formDungeonName: new FormControl(''),
    formTimeNeeded: new FormControl('', Validators.compose([Validators.required, Validators.min(1), Validators.max(999)])),
    formHardmode: new FormControl(''),
    formFlawless: new FormControl(''),
    formWipes: new FormControl('', Validators.compose([Validators.required, Validators.min(0), Validators.max(999)])),
    formClassOne: new FormControl(''),
    formClassTwo: new FormControl(''),
    formClassThree: new FormControl(''),
    formClassFour: new FormControl('')
  });

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

  postDungeonRunToDatabase() {
    this.httpClient.post(API_URL + API_ESO_POST_DUNGEON_RUN,
      {
        'submitDungeonRunFormData': this.formSubmitDungeonRunData
      }).subscribe(data => {
        console.log("POST call successful value returned in body", data);
      },
      response => {
        console.log("POST call in error", response);
        this.notifyService.showFailure("Error: Backend or Database not reachable.", "Failure")
      },
      () => {
        console.log("The POST observable is now completed.");
        this.notifyService.showSuccess("Run submitted!", "Success")
        this.fetchRecordedDungeonRuns();
      });
  }

  onSubmit() {
    this.formSubmitDungeonRunSubmitted = true;
    // input validation: stop here if form is missing required fields
    if (this.formSubmitDungeonRun.invalid) {
      return;
    }
    this.formSubmitDungeonRunData = this.formSubmitDungeonRun.value as JSON;
    console.log("form data:", this.formSubmitDungeonRunData)

    //set default values for selectors, like they are displayed in ui
    if (this.formSubmitDungeonRunData.formDungeonName == "") {
      this.formSubmitDungeonRunData.formDungeonName = this.esoConstants["eso_constants"][0]["LIST_ESO_DUNGEONS"][0]
    }
    if (this.formSubmitDungeonRunData.formHardmode == "") {
      this.formSubmitDungeonRunData.formHardmode = this.booleanDropdownValues[0]
    }
    if (this.formSubmitDungeonRunData.formFlawless == "") {
      this.formSubmitDungeonRunData.formFlawless = this.booleanDropdownValues[0]
    }
    if (this.formSubmitDungeonRunData.formClassOne == "") {
      this.formSubmitDungeonRunData.formClassOne = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitDungeonRunData.formClassTwo == "") {
      this.formSubmitDungeonRunData.formClassTwo = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitDungeonRunData.formClassThree == "") {
      this.formSubmitDungeonRunData.formClassThree = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitDungeonRunData.formClassFour == "") {
      this.formSubmitDungeonRunData.formClassFour = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }

    this.postDungeonRunToDatabase();

  }

  ngOnInit() {
    this.fetchEsoConstants();
  }

}
