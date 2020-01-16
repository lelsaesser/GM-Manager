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
  brainstormExercisesFormatted: boolean = false;

  miscConstants: JSON;

  formRequestExerciseData: any;
  brainstormExercises: any;
  brainstormCorrectInput: any;
  brainstormUserInput: any;

  formattedBrainstormExercises = [];


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
    if (this.brainstormExercisesSet) {
      var len = 0;
      for (let element of this.brainstormExercises['exercises']['exercise']) {
        console.log("EEEEEEEEE:", element)
        var exercise_string = element[0]

        if (element[1] == 0) {
          exercise_string += " + ";
        }
        else if (element[1] == 1) {
          exercise_string += " * ";
        }
        else if (element[1] == 2) {
          exercise_string += " - ";
        }
        else if (element[1] == 3) {
          exercise_string += " / ";
        }
        else {
          exercise_string += " <ERROR> ";
        }

        exercise_string += element[2];
        len = this.formattedBrainstormExercises.push(exercise_string)
      }
      if (len > 0) {
        return true;
      } else {
        return false;
      }
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
