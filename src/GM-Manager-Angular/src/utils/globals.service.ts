import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GlobalsService {

  constructor() { }

  // global variables used by all components
  darkmodeEnabled: boolean = true;
}
