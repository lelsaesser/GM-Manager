import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StrongholdComponent } from './stronghold.component';

describe('StrongholdComponent', () => {
  let component: StrongholdComponent;
  let fixture: ComponentFixture<StrongholdComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StrongholdComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StrongholdComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
