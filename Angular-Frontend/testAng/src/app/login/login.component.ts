import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {HttpClient} from '@angular/common/http';
import {Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router
  ) {
    this.form = this.formBuilder.group({
      username: '',
      password: ''
    });

  }

  ngOnInit(): void {
  }

  submit(): void {
    this.http.post('http://localhost:8000/users/login/', this.form.getRawValue(), {
      withCredentials: true
    }).subscribe((response) => {
      console.log('Response from API:', response);
      console.log('Login successful!');
      const username = this.form.get('username')?.value;
      this.router.navigate(['/', username]);
    });
  }
}