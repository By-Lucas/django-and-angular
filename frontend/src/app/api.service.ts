import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseUrl = 'http://127.0.0.1:8000';
  httpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' })

  constructor(private http: HttpClient) {}

  getAllMembers() : Observable<any> {
    return this.http.get(`${this.baseUrl}/people/all`,{headers:this.httpHeaders});
  }

  getMember(id:number) : Observable<any> {
    return this.http.get(`${this.baseUrl}/people/${id}`,{headers:this.httpHeaders});
  }

  saveNewPerson(member) :Observable<any> {
    return this.http.post(`${this.baseUrl}/people/create`, member, {headers:this.httpHeaders});
  }
  
}
