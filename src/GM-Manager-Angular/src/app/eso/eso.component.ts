import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NotificationService } from '../../utils/notification.service'

import {
  API_URL,
  API_ESO_GET_CONSTANTS,
  API_ESO_GET_DUNGEON_RUNS,
  API_ESO_POST_DUNGEON_RUN,
  API_ESO_DELETE_DUNGEON_RUN,
  API_ESO_GET_RAID_RUNS,
  API_ESO_POST_RAID_RUN,
  API_ESO_DELETE_RAID_RUN
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
  esoRaidDataSet: boolean = false;
  formSubmitDungeonRunSubmitted: boolean = false;
  formDeleteDungeonRunSubmitted: boolean = false;
  formSubmitRaidRunSubmitted: boolean = false;
  formDeleteRaidRunSubmitted: boolean = false;

  esoConstants: JSON;
  esoDungeonData: JSON;
  esoRaidData: JSON;

  formSubmitDungeonRunData: any;
  formSubmitDeleteDungeonRunById: any;
  formSubmitRaidRunData: any;
  formSubmitDeleteRaidRunById: any;

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

  formSubmitRaidRun = new FormGroup({
    formRaidName: new FormControl(''),
    formPlayerCount: new FormControl('', Validators.compose([Validators.required, Validators.min(1), Validators.max(12)])),
    formTimeNeeded: new FormControl('', Validators.compose([Validators.required, Validators.min(1), Validators.max(999)])),
    formHardmode: new FormControl(''),
    formFlawless: new FormControl(''),
    formWipes: new FormControl('', Validators.compose([Validators.required, Validators.min(0), Validators.max(999)])),
    formClassOne: new FormControl(''),
    formClassTwo: new FormControl(''),
    formClassThree: new FormControl(''),
    formClassFour: new FormControl(''),
    formClassFive: new FormControl(''),
    formClassSix: new FormControl(''),
    formClassSeven: new FormControl(''),
    formClassEight: new FormControl(''),
    formClassNine: new FormControl(''),
    formClassTen: new FormControl(''),
    formClassEleven: new FormControl(''),
    formClassTwelve: new FormControl('')
  });

  formDeleteDungeonRun = new FormGroup({
    formIdToDelete: new FormControl('', Validators.compose([Validators.required, Validators.min(1)]))
  });

  formDeleteRaidRun = new FormGroup({
    formIdToDelete: new FormControl('', Validators.compose([Validators.required, Validators.min(1)]))
  });

  constructor(private httpClient: HttpClient, private notifyService: NotificationService) { }

  fetchEsoConstants() {
    this.httpClient.get(API_URL + API_ESO_GET_CONSTANTS).subscribe(data => {
      this.esoConstants = data as JSON;
      this.esoConstantsSet = true;
    },
      response => {
        this.notifyService.showFailure("Backend is not reachable.", "Error")
      });
  }

  fetchRecordedDungeonRuns() {
    this.httpClient.get(API_URL + API_ESO_GET_DUNGEON_RUNS).subscribe(data => {
      this.esoDungeonData = data as JSON;
      this.esoDungeonDataSet = true;
    },
      response => {
        this.notifyService.showFailure("Backend is not reachable.", "Error")
      });
  }

  fetchRecordedRaidRuns() {
    this.httpClient.get(API_URL + API_ESO_GET_RAID_RUNS).subscribe(data => {
      this.esoRaidData = data as JSON;
      this.esoRaidDataSet = true;
    },
      response => {
        this.notifyService.showFailure("Backend is not reachable.", "Error")
      });
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

  postRaidRunToDatabase() {
    this.httpClient.post(API_URL + API_ESO_POST_RAID_RUN,
      {
        'submitRaidRunFormData': this.formSubmitRaidRunData
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
          this.fetchRecordedRaidRuns();
        });
  }

  deleteDungeonRunById() {
    this.httpClient.post(API_URL + API_ESO_DELETE_DUNGEON_RUN,
      {
        'delete_row_id': this.formSubmitDeleteDungeonRunById.formIdToDelete
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
          this.fetchRecordedDungeonRuns();
        });
  }

  deleteRaidRunById() {
    this.httpClient.post(API_URL + API_ESO_DELETE_RAID_RUN,
      {
        'delete_row_id': this.formSubmitDeleteRaidRunById.formIdToDelete
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
          this.fetchRecordedRaidRuns();
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

  onSubmitRaidRun() {
    this.formSubmitRaidRunSubmitted = true;
    // input validation: stop here if form is missing required fields
    if (this.formSubmitRaidRun.invalid) {
      return;
    }

    this.formSubmitRaidRunData = this.formSubmitRaidRun.value as JSON;

    //set default values for selectors, like they are displayed in ui
    if (this.formSubmitRaidRunData.formRaidName == "") {
      this.formSubmitRaidRunData.formRaidName = this.esoConstants["eso_constants"][0]["LIST_ESO_RAIDS"][0]
    }
    if (this.formSubmitRaidRunData.formHardmode == "") {
      this.formSubmitRaidRunData.formHardmode = this.booleanDropdownValues[0]
    }
    if (this.formSubmitRaidRunData.formFlawless == "") {
      this.formSubmitRaidRunData.formFlawless = this.booleanDropdownValues[0]
    }
    if (this.formSubmitRaidRunData.formClassOne == "") {
      this.formSubmitRaidRunData.formClassOne = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitRaidRunData.formClassTwo == "") {
      this.formSubmitRaidRunData.formClassTwo = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitRaidRunData.formClassThree == "") {
      this.formSubmitRaidRunData.formClassThree = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitRaidRunData.formClassFour == "") {
      this.formSubmitRaidRunData.formClassFour = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitRaidRunData.formClassFive == "") {
      this.formSubmitRaidRunData.formClassFive = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitRaidRunData.formClassSix == "") {
      this.formSubmitRaidRunData.formClassSix = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitRaidRunData.formClassSeven == "") {
      this.formSubmitRaidRunData.formClassSeven = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitRaidRunData.formClassEight == "") {
      this.formSubmitRaidRunData.formClassEight = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitRaidRunData.formClassNine == "") {
      this.formSubmitRaidRunData.formClassNine = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitRaidRunData.formClassTen == "") {
      this.formSubmitRaidRunData.formClassTen = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitRaidRunData.formClassEleven == "") {
      this.formSubmitRaidRunData.formClassEleven = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }
    if (this.formSubmitRaidRunData.formClassTwelve == "") {
      this.formSubmitRaidRunData.formClassTwelve = this.esoConstants["eso_constants"][0]["LIST_ESO_CLASSES"][0]
    }

    this.postRaidRunToDatabase();
  }

  onSubmitDelete() {
    this.formDeleteDungeonRunSubmitted = true;
    // input validation: stop here if form is missing required fields
    if (this.formDeleteDungeonRun.invalid) {
      return;
    }
    this.formSubmitDeleteDungeonRunById = this.formDeleteDungeonRun.value as JSON;
    this.deleteDungeonRunById();
  }

  ngOnInit() {
    this.fetchEsoConstants();
  }

}
