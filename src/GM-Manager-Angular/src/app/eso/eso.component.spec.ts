import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EsoComponent } from './eso.component';

describe('EsoComponent', () => {
  let component: EsoComponent;
  let fixture: ComponentFixture<EsoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EsoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EsoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
