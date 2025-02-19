import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {HttpClient} from '@angular/common/http';
import {Router} from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
    form!: FormGroup 
  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router
    
  ) {
    this.form = this.formBuilder.group({
        username: '',
        email: '',
        password: ''
      })
  }
  
  

  ngOnInit(): void {
   
  }

  submit(): void {
    const body = !!this.form && this.form.getRawValue();
    console.log("#############################");
    console.log(body);
    this.http.post('http://localhost:8000/users/register/', body)
      .subscribe(() => this.router.navigate(['/login']));
  }
}