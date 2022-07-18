import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { UsersComponent } from './users/users.component';
import { UsersService } from './service/users.service';

@NgModule({
  declarations: [
    AppComponent,
    UsersComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [HttpClientModule, UsersService],
  bootstrap: [AppComponent]
})
export class AppModule { }
