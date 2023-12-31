import { Component } from '@angular/core';
import { ApiService } from 'src/service/ApiService';
import { ConfirmationService } from 'primeng/api';
import { contratos } from 'src/model/contratos.model';
@Component({
  selector: 'app-contratos',
  templateUrl: './contratos.component.html',
  styleUrls: ['./contratos.component.css'],
  providers: [ApiService,ConfirmationService]
})
export class ContratosComponent {
  constructor(private servicio:ApiService, private conf:ConfirmationService) {}

  visible:boolean = false;
  contratos: contratos[];
  contratoNueva: contratos =  new contratos();
  actualizar:boolean = false;

  //OBTENER CONTRATOS
  ngOnInit():void {
    this.obtenerContrato();
  }
  
  obtenerContrato() {
    this.servicio.getContratos().subscribe(lista => {
      this.contratos = lista;
    });
  }
  //CREAR CONTRATOS
  crearContrato(){
    this.contratoNueva = new contratos();
    this.visible = true;
    this.actualizar = false;
  }

  //GUARDAR CONTRATO
  guardarContrato(){
    if (this.actualizar){
      this.servicio.putContrato(this.contratoNueva).subscribe(()=>{
        this.obtenerContrato();
        this.visible = false;
      });
    } else {
      this.servicio.postContrato(this.contratoNueva).subscribe(()=>{
        this.obtenerContrato();
        this.visible = false;
      });
    }
  }
  //ELIMIAR CONTRATO
  eliminarContrato(id:number) {
    this.conf.confirm({
      message: 'Desea eliminar el Contrato??',
      header: 'Confirmacion',
      icon: 'pi pi-exclamation-triangle',
      accept: () => {
        this.servicio.deleteContrato(id.toString()).subscribe(()=>{
          this.obtenerContrato();
        });
      },
      reject: () => {}
    });
  }  
  //ACTUALIZAR CONTRATO
  actualizarContrato(id:number) {
    this.servicio.getContrato(id.toString()).subscribe(contrato => {
      this.contratoNueva = contrato;
      this.visible = true;
      this.actualizar = true;
    });
  }

}
