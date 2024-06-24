import { Body, Controller, Delete, Get, Param, Post, Put } from '@nestjs/common';
import { BffService } from './bff.service';

@Controller('bff')
export class BffController {
    constructor(private readonly bffService: BffService){}

    @Get('pedidos')
    getData(){
        return this.bffService.getData();
    }

    @Get('pedidos/:id')
    getById(@Param('id') id: string){
        return this.bffService.getById(id);
    }

    @Post('pedidos')
    createData(@Body() createDto: any){
        return this.bffService.createData(createDto);
    }

    @Put('pedidos/:id')
    updateData(@Param('id') id: string, @Body() updateDto: any){
        return this.bffService.updateData(id, updateDto);
    }

    @Delete('pedidos/:id')
    deleteData(@Param('id') id: string){
        return this.bffService.deleteData(id);
    }
}
