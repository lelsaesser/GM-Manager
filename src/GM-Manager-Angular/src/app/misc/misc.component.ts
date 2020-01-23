import { Component, OnInit } from '@angular/core';
import { NotificationService } from '../../utils/notification.service'
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

import {
  API_MISC_GET_CONSTANTS,
  API_MISC_BRAINSTORM_GET_EXERCISE_LIST,
  API_URL
} from './../env'
import { type } from 'os';

@Component({
  selector: 'app-misc',
  templateUrl: './misc.component.html',
  styleUrls: ['./misc.component.css']
})
export class MiscComponent implements OnInit {

  miscConstantsSet: boolean = false;
  formRequestExerciseSubmitted: boolean = false;
  brainstormExercisesSet: boolean = false;
  brainstormExercisesFormatted: boolean = false;

  miscConstants: JSON;

  formRequestExerciseData: any;
  brainstormExercises: any;
  brainstormCorrectInput: any;
  brainstormUserInput: any;
  formattedBrainstormExercises: any;


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
        this.brainstormExercisesSet = true;
      },
        response => {
          console.log("POST call in error", response);
          this.notifyService.showFailure("Backend is not reachable.", "Error")
        },
        () => {
          if (this.decodeBrainstormExercises()) {
            this.brainstormExercisesFormatted = true;
          }
          console.log("The POST observable is now completed.");
        });
  }

  decodeBrainstormExercises() {
    /*
    Take a number array containing a encoded brainstom exercise and format it to a string array for display in UI
    returns: true on success, false if backend exercise request failed
    */
    if (this.brainstormExercisesSet) {
      var len = 0;
      var exercise_data = this.brainstormExercises['exercises'][0]['exercise'];
      var formatted_string = String(exercise_data[0]);

      if (exercise_data[1] == 0) {
        formatted_string += " + ";
      }
      else if (exercise_data[1] == 1) {
        formatted_string += " * ";
      }

      formatted_string += String(exercise_data[2]);
      this.formattedBrainstormExercises = formatted_string;

      return true;
    } else {
      return false;
    }
  }

  onSubmitExercise() {
    //at the moment, every time the user clicks the button the list will be cleared - otherwise all exercises just get appended
    if (this.formattedBrainstormExercises) {
      this.formattedBrainstormExercises = [];
    }
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
