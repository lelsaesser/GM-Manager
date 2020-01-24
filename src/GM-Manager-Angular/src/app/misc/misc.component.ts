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

  currentWinStreak: number = 0;
  totalSolved: number = 0;
  totalSolvedCorrectly: number = 0;

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

    if (Number(exercise_solution) == Number(user_solution)) {
      return true;
    } else {
      return false;
    }
  }

  checkWinStreak() {
    /*
    Keeps track of the exercises the user solves correctly in a row and displays MOBA like alert messages
    */
    this.currentWinStreak += 1;
    
    if (this.currentWinStreak == 5) {
      this.notifyService.showInfo("5 solved in a row", "Killing Spree!");
    }
    else if (this.currentWinStreak == 10) {
      this.notifyService.showInfo("10 solved in a row","Elegant!");
    }
    else if (this.currentWinStreak == 20) {
      this.notifyService.showInfo("20 solved in a row", "Dominating!");
    }
    else if (this.currentWinStreak == 30) {
      this.notifyService.showInfo("30 solved in a row", "Impressive!");
    }
    else if (this.currentWinStreak == 50) {
      this.notifyService.showInfo("50 solved in a row", "Genius!");
    }
    else if (this.currentWinStreak == 75) {
      this.notifyService.showInfo("75 solved in a row", "Unbelievable!");
    }
    else if (this.currentWinStreak == 100) {
      this.notifyService.showInfo("100 solved in a row", "Godlike!");
    }
    else if (this.currentWinStreak == 150) {
      this.notifyService.showInfo("150 solved in a row", "Legendary!");
    }
    else if (this.currentWinStreak == 200) {
      this.notifyService.showInfo("200 solved in a row", "Way beyond Godlike!");
    }
    else if (this.currentWinStreak == 250) {
      this.notifyService.showInfo("250 solved in a row", "Math Overlord!");
    }
    else if (this.currentWinStreak == 300) {
      this.notifyService.showInfo("300 solved in a row", "Grand Shining Five Star!");
    }
    else if (this.currentWinStreak == 350) {
      this.notifyService.showInfo("350 solved in a row", "Grandmaster MVP!");
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
      this.checkWinStreak();
      this.totalSolved += 1;
      this.totalSolvedCorrectly += 1;
    } else {
      this.currentWinStreak = 0;
      this.totalSolved += 1;
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
