import { Component } from '@angular/core';
import { GlobalsService } from '../utils/globals.service'
import { SurvrimComponent } from '../app/survrim/survrim.component'

@Component({
  providers: [SurvrimComponent],
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'GM-Manager-Frontend';

  darkmodeEnabled: boolean = true;

  constructor(private globals: GlobalsService, private survrim: SurvrimComponent) {}

  toggleDarkmode() {
    if(this.globals.darkmodeEnabled) {
      this.darkmodeEnabled = false;
      this.globals.darkmodeEnabled = false;
      this.survrim.toggleDarkmodeSurvrun();
    } else {
      this.darkmodeEnabled = true;
      this.globals.darkmodeEnabled = true;
      this.survrim.toggleDarkmodeSurvrun();
    }
  }
}
