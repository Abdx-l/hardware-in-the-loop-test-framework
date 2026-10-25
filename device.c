#include <stdint.h>
#include <string.h>
static uint32_t registers_[16];static int opened,busy,fault;
int device_open(void){opened=1;memset(registers_,0,sizeof registers_);busy=0;fault=0;return 0;}
void device_close(void){opened=0;}
void device_reset(void){memset(registers_,0,sizeof registers_);busy=0;}
void device_fault(int mode){fault=mode;}
int device_write(int address,uint32_t value){
 if(!opened)return -1;if(address<0||address>=16)return -2;if(fault==1)return -3;
 registers_[address]=value;busy=2;return 0;
}
int device_read(int address,uint32_t *value){
 if(!opened)return -1;if(address<0||address>=16||!value)return -2;
 *value=registers_[address]^(fault==2?1:0);return 0;
}
int device_tick(void){if(busy>0&&fault!=3)busy--;return busy;}
