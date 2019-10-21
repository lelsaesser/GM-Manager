import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { RouterModule, Routes } from '@angular/router';
import { SurvrimComponent } from './survrim/survrim.component';
import { StrongholdComponent } from './stronghold/stronghold.component'

const appRoutes: Routes = [
  { path: 'survrim', component: SurvrimComponent},
  { path: 'stronghold', component: StrongholdComponent},
];

@NgModule({
  declarations: [
    AppComponent,
    SurvrimComponent,
    StrongholdComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // for debugging
    )
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
