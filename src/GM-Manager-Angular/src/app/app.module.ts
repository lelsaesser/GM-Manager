import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { RouterModule, Routes } from '@angular/router';
import { SurvrimComponent } from './survrim/survrim.component';
import { StrongholdComponent } from './stronghold/stronghold.component';
import { ErrorPageNotFoundComponent } from './error-page-not-found/error-page-not-found.component'
import { ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ToastrModule } from 'ngx-toastr';
import { EsoComponent } from './eso/eso.component';
import { MiscComponent } from './misc/misc.component';

const appRoutes: Routes = [
  { path: '', redirectTo: '/survrim', pathMatch: 'full' },
  { path: 'survrim', component: SurvrimComponent },
  { path: 'stronghold', component: StrongholdComponent },
  { path: 'eso', component: EsoComponent },
  { path: 'misc', component: MiscComponent },
  { path: '**', component: ErrorPageNotFoundComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    SurvrimComponent,
    StrongholdComponent,
    ErrorPageNotFoundComponent,
    EsoComponent,
    MiscComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    ToastrModule.forRoot(),
    HttpClientModule,
    ReactiveFormsModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // for debugging
    )
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
