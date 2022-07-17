import { Component, OnInit } from '@angular/core';
import { UsersService } from './service/users.service';
import { UserModel } from './models/user.model';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {

  ngOnInit() {
  }

}  
