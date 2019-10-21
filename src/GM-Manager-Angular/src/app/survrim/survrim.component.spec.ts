import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SurvrimComponent } from './survrim.component';

describe('SurvrimComponent', () => {
  let component: SurvrimComponent;
  let fixture: ComponentFixture<SurvrimComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SurvrimComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SurvrimComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
