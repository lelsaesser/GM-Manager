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
  formSendSolutionSubmitted: boolean = false;

  miscConstants: JSON;

  formRequestExerciseData: any;
  brainstormExercises: any;
  brainstormCorrectInput: any;
  brainstormUserInput: any;
  formattedBrainstormExercises: any;

  formRequestExercise = new FormGroup({
    formBrainstormDifficulty: new FormControl('')
  });

  formSendSolution = new FormGroup({
    formBrainstormSolution: new FormControl('', Validators.required)
  });

  constructor(private httpClient: HttpClient, private notifyService: NotificationService) { }


  fetchMiscConstants() {
    /*
    GET request
    Get Misc constants from backend
    */
    this.httpClient.get(API_URL + API_MISC_GET_CONSTANTS).subscribe(data => {
      this.miscConstants = data as JSON;
      this.miscConstantsSet = true;
    },
      response => {
        this.notifyService.showFailure("Backend is not reachable.", "Error")
      });
  }

  requestBrainstormExercises() {
    /*
    POST request
    Get a brainstorm exercise from backend, required payload is user input data from brainstorm formgroup
    */
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

  checkExerciseSolution() {
    /*
    Check if the user solution is correct
    returns: true if solution is correct, otherwise false
    */
    var exercise_solution = this.brainstormExercises['exercises'][0]['solution'];
    var user_solution = this.formSendSolution.value.formBrainstormSolution;

    console.log(user_solution)

    if (Number(exercise_solution) == Number(user_solution)) {
      return true;
    } else {
      return false;
    }
  }

  onSubmitExercise() {
    /*
    Submit function for brainstorm panel
    Triggered if the user requests a exercise
    */
    this.formRequestExerciseSubmitted = true;
    this.formRequestExerciseData = this.formRequestExercise.value as JSON;

    //set default values for selectors, like they are displayed in ui
    if (this.formRequestExerciseData.formBrainstormDifficulty == "") {
      this.formRequestExerciseData.formBrainstormDifficulty = this.miscConstants["misc_constants"][0]["LIST_DIFFICULTIES"][0]
    }

    this.requestBrainstormExercises();
  }

  onSubmitSolution() {
    /*
    Submit function for brainstorm panel
    Triggered if the user sends his exercise solution
    */
    this.formSendSolutionSubmitted = true;

    //check if solution form is filled
    if (this.formSendSolution.invalid) {
      return;
    }

    if (this.checkExerciseSolution()) {
      this.notifyService.showSuccess("Yes!", "Correct solution");
    } else {
      var exercise_solution = this.brainstormExercises['exercises'][0]['solution'];
      this.notifyService.showFailure("No :(", "Solution is " + String(exercise_solution));
    }

    //instantly request a new exercise
    this.requestBrainstormExercises();

    //clear user input field for convinience
    this.formSendSolution.reset();
  }

  ngOnInit() {
    /*
    Executed automatically at page load
    */
    this.fetchMiscConstants();
  }
}