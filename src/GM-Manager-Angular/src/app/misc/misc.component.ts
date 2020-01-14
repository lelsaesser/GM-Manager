import { Component, OnInit } from '@angular/core';
import { NotificationService } from '../../utils/notification.service'
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

import {
  API_MISC_GET_CONSTANTS,
  API_MISC_BRAINSTORM_GET_EXERCISE_LIST,
  API_URL
} from './../env'

@Component({
  selector: 'app-misc',
  templateUrl: './misc.component.html',
  styleUrls: ['./misc.component.css']
})
export class MiscComponent implements OnInit {

  miscConstantsSet: boolean = false;
  formRequestExerciseSubmitted: boolean = false;
  brainstormExercisesSet: boolean = false;

  miscConstants: JSON;

  formRequestExerciseData: any;
  brainstormExercises: any;

  formRequestExercise = new FormGroup({
    formBrainstormDifficulty: new FormControl('')
  });

  constructor(private httpClient: HttpClient, private notifyService: NotificationService) { }


  fetchMiscConstants() {
    this.httpClient.get(API_URL + API_MISC_GET_CONSTANTS).subscribe(data => {
      this.miscConstants = data as JSON;
      this.miscConstantsSet = true;
    },
      response => {
        this.notifyService.showFailure("Backend is not reachable.", "Error")
      });
  }

  requestBrainstormExercises() {
    this.httpClient.post(API_URL + API_MISC_BRAINSTORM_GET_EXERCISE_LIST,
      {
        'data': this.formRequestExerciseData
      }).subscribe(data => {
        console.log("POST call successful value returned in body", data);
        this.brainstormExercises = data;
      },
        response => {
          console.log("POST call in error", response);
          this.notifyService.showFailure("Backend is not reachable.", "Error")
        },
        () => {
          console.log("The POST observable is now completed.");
        });
    this.brainstormExercisesSet = true;
  }

  onSubmitExercise() {
    this.formRequestExerciseSubmitted = true;
    this.formRequestExerciseData = this.formRequestExercise.value as JSON;

    //set default values for selectors, like they are displayed in ui
    if (this.formRequestExerciseData.formBrainstormDifficulty == "") {
      this.formRequestExerciseData.formBrainstormDifficulty = this.miscConstants["misc_constants"][0]["LIST_DIFFICULTIES"][0]
    }

    this.requestBrainstormExercises();
  }

  ngOnInit() {
    this.fetchMiscConstants();
  }

}
