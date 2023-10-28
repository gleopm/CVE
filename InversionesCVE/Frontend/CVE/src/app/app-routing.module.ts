import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PersonalComponent } from './personal/personal.component';
import { FacturasComponent } from './facturas/facturas.component';
import { ContratosComponent } from './contratos/contratos.component';
import { ClienteComponent } from './cliente/cliente.component';
import { UsuariosComponent } from './usuarios/usuarios.component';

const routes: Routes = [
  {path:'Personal',component:PersonalComponent},
  {path:'Usuarios',component:UsuariosComponent},
  {path:'Facturas',component:FacturasComponent},
  {path:'Contratos',component:ContratosComponent},
  {path:'Cliente',component:ClienteComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
