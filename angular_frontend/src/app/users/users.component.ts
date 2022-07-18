import { Component, OnInit, ViewChild } from '@angular/core';
import { UsersService } from '../service/users.service';
import { UserModel } from '../models/user.model';
import { NgForOf } from '@angular/common';
import { FormGroup, NgForm } from '@angular/forms';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {
  user = {} as UserModel;

  constructor(private usersService: UsersService) { }
  
  ngOnInit(): void {

  }

  cadastrar() {
    console.log(this.user);

    this.usersService.cadastrarUser(this.user).subscribe(data => {
      this.user = data;
    },
    error=> {
      console.log(error);
    });
  }

}
