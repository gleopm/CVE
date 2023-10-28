import { Component } from '@angular/core';
import { ApiService } from 'src/service/ApiService';
import { ConfirmationService } from 'primeng/api';
import { cliente } from 'src/model/cliente.model';
@Component({
  selector: 'app-cliente',
  templateUrl: './cliente.component.html',
  styleUrls: ['./cliente.component.css'],
  providers: [ApiService,ConfirmationService]
})
export class ClienteComponent {
  constructor(private servicio:ApiService, private conf:ConfirmationService) {}

  visible:boolean = false;
  clientes: cliente[];
  clienteNueva: cliente =  new cliente();
  actualizar:boolean = false;
  //OPCION DE CHOICE
  estados: string[] = ["Pendiente", "Activo"];  
  //OBTENER CLIENTES
  ngOnInit():void {
    this.obtenerCliente();
  }
  
  obtenerCliente() {
    this.servicio.getClientes().subscribe(lista => {
      this.clientes = lista;
    });
  }
  //CREAR CLIENTES
  crearCliente(){
    this.clienteNueva = new cliente();
    this.visible = true;
    this.actualizar = false;
  }

  //GUARDAR CLIENTE
  guardarCliente(){
    if (this.actualizar){
      this.servicio.putCliente(this.clienteNueva).subscribe(()=>{
        this.obtenerCliente();
        this.visible = false;
      });
    } else {
      this.servicio.postCliente(this.clienteNueva).subscribe(()=>{
        this.obtenerCliente();
        this.visible = false;
      });
    }
  }
  //ELIMIAR CLIENTE
  eliminarCliente(id:number) {
    this.conf.confirm({
      message: 'Desea eliminar el Cliente??',
      header: 'Confirmacion',
      icon: 'pi pi-exclamation-triangle',
      accept: () => {
        this.servicio.deleteCliente(id.toString()).subscribe(()=>{
          this.obtenerCliente();
        });
      },
      reject: () => {}
    });
  }  
  //ACTUALIZAR CLIENTE
  actualizarCliente(id:number) {
    this.servicio.getClienteo(id.toString()).subscribe(cliente => {
      this.clienteNueva = cliente;
      this.visible = true;
      this.actualizar = true;
    });
  }

}
