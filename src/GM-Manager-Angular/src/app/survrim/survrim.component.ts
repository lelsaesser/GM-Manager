import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormControl, FormGroup, Validators } from '@angular/forms'
import { NotificationService } from '../../utils/notification.service'

import {
  API_URL, API_SURVRUN_GET_TARGET_LOCATION,
  API_SURVRIM_GET_CLASS_DATA,
  API_SURVRUN_GET_ALL_DB_RUN_DATA,
  API_SURVRUN_GET_CONSTANTS,
  API_SURVRUN_POST_RUN,
  API_SURVRUN_DELETE_RUN,
  API_SURVRUN_GET_STATISTICS
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
  formDeleteRunSubmitted: boolean = false;
  formSubmitRunSubmitted: boolean = false;
  targetLocationsMatch: boolean = false;
  survrunStatisticsFetched: boolean = false;

  survrunJson: JSON;
  survrimClassData: JSON;
  queryResultSurvrunData: JSON;
  survrunConstants: JSON;
  survrunStatistics: JSON;

  formSubmitRunData: any;
  formSubmitDeleteId: any;

  formSubmitRun = new FormGroup({
    formTimebox: new FormControl('', Validators.compose([Validators.required, Validators.min(1)])),
    formTimeNeeded: new FormControl('', Validators.compose([Validators.required, Validators.min(1)])),
    formRcount: new FormControl('', Validators.compose([Validators.required, Validators.min(0)])),
    formPlayerClass: new FormControl(''),
    formTargetA: new FormControl(''),
    formTargetB: new FormControl(''),
    formExpectedDifficulty: new FormControl(''),
  });

  formDeleteRun = new FormGroup({
    formIdToDelete: new FormControl('', Validators.compose([Validators.required, Validators.min(1)]))
  });


  constructor(private httpClient: HttpClient, private notifyService: NotificationService) { }

  fetchSurvrunData() {
    this.httpClient.get(API_URL + API_SURVRUN_GET_TARGET_LOCATION).subscribe(data => {
      this.survrunJson = data as JSON;
      this.show_targets = true;
      console.log("GET call fetchSurvrunData() successful. Value returned in body: ", data);
    }, 
      response => {
        this.notifyService.showFailure("Backend is not reachable.", "Error")
      })
  }

  fetchSurvrimClass() {
    this.httpClient.get(API_URL + API_SURVRIM_GET_CLASS_DATA).subscribe(data => {
      this.survrimClassData = data as JSON;
      this.show_class = true;
      console.log("GET call fetchSurvrimClass() successful. Value returned in body: ", data);
    },
      response => {
        this.notifyService.showFailure("Backend is not reachable.", "Error")
      })
  }

  querySurvrunTableGetAllRuns() {
    this.httpClient.get(API_URL + API_SURVRUN_GET_ALL_DB_RUN_DATA).subscribe(data => {
      this.queryResultSurvrunData = data as JSON;
      this.show_queryResultSurvrunData = true;
      console.log("GET call querySurvrunTableGetAllRuns() successfull. Value returned in body: ", data)
    },
      response => {
        this.notifyService.showFailure("Backend is not reachable.", "Error")
      })
  }

  fetchSurvrunConstants() {
    this.httpClient.get(API_URL + API_SURVRUN_GET_CONSTANTS).subscribe(data => {
      this.survrunConstants = data as JSON;
      this.survrimConstants_set = true;
      console.log("GET call fetchSurvrunConstants() successfull. Value returned in body: ", data)
    },
      response => {
        this.notifyService.showFailure("Backend is not reachable.", "Error")
      })
  }

  fetchSurvrunStatistics() {
    this.httpClient.get(API_URL + API_SURVRUN_GET_STATISTICS).subscribe(data => {
      this.survrunStatistics = data as JSON;
      this.survrunStatisticsFetched = true;
      console.log("GET call fetchSurvrunStatistics() successfull. Value returned in body: ", data)
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
            'difficulty': this.formSubmitRunData.formExpectedDifficulty
          }
        ]
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
          this.querySurvrunTableGetAllRuns();
          this.fetchSurvrunStatistics();
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
          this.notifyService.showFailure("Given Id does not exist.", "Failure")
        },
        () => {
          console.log("The POST observable is now completed.");
          this.notifyService.showSuccess("Run deleted!", "Success")
          this.querySurvrunTableGetAllRuns();
          this.fetchSurvrunStatistics();
        });
  }

  onSubmitDelete() {
    this.formDeleteRunSubmitted = true;
    // input validation: stop here if form is missing required fields
    if (this.formDeleteRun.invalid) {
      return;
    }
    this.formSubmitDeleteId = this.formDeleteRun.value as JSON;
    this.deleteSurvruninDatabase()
  }

  onSubmit() {
    this.formSubmitRunSubmitted = true;
    // input validation: stop here if form is missing required fields
    if (this.formSubmitRun.invalid) {
      return;
    }
    this.formSubmitRunData = this.formSubmitRun.value as JSON;

    //set default values for selectors, like they are displayed in ui
    if (this.formSubmitRunData.formPlayerClass == "") {
      this.formSubmitRunData.formPlayerClass = this.survrunConstants["survrim_constants"][0]["LIST_SURVRIM_CLASSES"][0]
    }
    if (this.formSubmitRunData.formTargetA == "") {
      this.formSubmitRunData.formTargetA = this.survrunConstants["survrim_constants"][0]["LIST_SURVRUN_TARGET_LOCATIONS"][0]
    }
    if (this.formSubmitRunData.formTargetB == "") {
      this.formSubmitRunData.formTargetB = this.survrunConstants["survrim_constants"][0]["LIST_SURVRUN_TARGET_LOCATIONS"][0]
    }
    if (this.formSubmitRunData.formExpectedDifficulty == "") {
      this.formSubmitRunData.formExpectedDifficulty = this.survrunConstants["survrim_constants"][0]["LIST_SURVRUN_DIFFICULTIES"][0]
    }

    //target A and B cant be equal
    if (this.formSubmitRunData.formTargetA == this.formSubmitRunData.formTargetB) {
      this.targetLocationsMatch = true;
      return;
    }
    this.targetLocationsMatch = false;
    this.postSurvrunToDatabase()
  }

  ngOnInit() {
    this.fetchSurvrunConstants();
    this.fetchSurvrunStatistics();
  }
}
