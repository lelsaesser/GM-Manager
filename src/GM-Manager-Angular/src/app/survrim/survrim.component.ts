import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormControl, FormGroup } from '@angular/forms'
import {
  API_URL, API_SURVRUN_GET_TARGET_LOCATION, API_SURVRIM_GET_CLASS_DATA, API_SURVRUN_GET_ALL_DB_RUN_DATA,
  API_SURVRUN_GET_CONSTANTS, API_SURVRUN_POST_RUN, API_SURVRUN_DELETE_RUN
} from './../env';

@Component({
  selector: 'app-survrim',
  templateUrl: './survrim.component.html',
  styleUrls: ['./survrim.component.css']
})
export class SurvrimComponent {

  show_targets: boolean = false;
  show_class: boolean = false;
  show_queryResultSurvrunData: boolean = false;
  survrimConstants_set: boolean = false;

  survrunJson: JSON;
  survrimClassData: JSON;
  queryResultSurvrunData: JSON;
  survrunConstants: JSON;

  formSubmitRunData: any;
  formSubmitDeleteId: any;

  formSubmitRun = new FormGroup({
    formTimebox: new FormControl(''),
    formTimeNeeded: new FormControl(''),
    formRcount: new FormControl(''),
    formPlayerClass: new FormControl(''),
    formTargetA: new FormControl(''),
    formTargetB: new FormControl(''),
  });

  formDeleteRun = new FormGroup({
    formIdToDelete: new FormControl('')
  });


  constructor(private httpClient: HttpClient) { }

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

  fetchSurvrunConstants() {
    this.httpClient.get(API_URL + API_SURVRUN_GET_CONSTANTS).subscribe(data => {
      this.survrunConstants = data as JSON;
      this.survrimConstants_set = true;
      console.log("GET call fetchSurvrunConstants() successfull. Value returned in body: ", data)
    })
  }

  postSurvrunToDatabase() {
    this.httpClient.post(API_URL + API_SURVRUN_POST_RUN,
      {
        'submitRunFormData': [
          {
            'player_class': this.formSubmitRunData.formPlayerClass,
            'target_a': this.formSubmitRunData.formTargetA,
            'target_b': this.formSubmitRunData.formTargetB,
            'timebox': this.formSubmitRunData.formTimebox,
            'time_needed': this.formSubmitRunData.formTimeNeeded,
            'r_count': this.formSubmitRunData.formRcount,
          }
        ]
      }).subscribe(data => {
        console.log("POST call successful value returned in body", data);
      },
        response => {
          console.log("POST call in error", response);
        },
        () => {
          console.log("The POST observable is now completed.");
          this.querySurvrunTableGetAllRuns()
        });
  }

  deleteSurvruninDatabase() {
    this.httpClient.post(API_URL + API_SURVRUN_DELETE_RUN,
      {
        'delete_row_id': this.formSubmitDeleteId.formIdToDelete
      }).subscribe(data => {
        console.log("POST call successful value returned in body", data);
      },
        response => {
          console.log("POST call in error", response);
        },
        () => {
          console.log("The POST observable is now completed.");
          this.querySurvrunTableGetAllRuns()
        });
  }

  onSubmitDelete() {
    this.formSubmitDeleteId = this.formDeleteRun.value as JSON;
    this.deleteSurvruninDatabase()
  }

  onSubmit() {
    this.formSubmitRunData = this.formSubmitRun.value as JSON;
    
    //set default values for selectors, like they are displayed in ui
    if(this.formSubmitRunData.formPlayerClass == "") {
      this.formSubmitRunData.formPlayerClass = this.survrunConstants["survrim_constants"][0]["LIST_SURVRIM_CLASSES"][0]
    }
    if(this.formSubmitRunData.formTargetA == "") {
      this.formSubmitRunData.formTargetA = this.survrunConstants["survrim_constants"][0]["LIST_SURVRUN_TARGET_LOCATIONS"][0]
    }
    if(this.formSubmitRunData.formTargetB == "") {
      this.formSubmitRunData.formTargetB = this.survrunConstants["survrim_constants"][0]["LIST_SURVRUN_TARGET_LOCATIONS"][0]
    }
    console.log(this.formSubmitRunData)
    this.postSurvrunToDatabase()
  }

  ngOnInit() {
    this.fetchSurvrunConstants();
  }
}
