from ipaddress import IPv4Address

class Net():
    def __init__(self, address, mask):
        self.address = address

        self.mask = self.cidr2dec(mask) if '/' in mask else mask
        self.cidr = self.dec2cidr(self.mask)

        self.subnets = self.get_subnets(address, self.mask)
        self.hosts = None

    def dec2cidr(self, mask): ##CIDR to Decimal /24 -> 255.255.255.0
        mask = mask.split('.')
        bin_mask = ''
        for group in mask:
            bin_mask += bin(int(group))
        cidr = f"/{bin_mask.count('1')}"

        return cidr

    def cidr2dec(self, cidr): ##Decimal to CIDR  255.255.255.0 -> /24  
        mask_bits = int(cidr.replace('/',''))
        bin_mask = ''

        for i in range(mask_bits):
            bin_mask += '1'
        while(len(bin_mask) != 32):
            bin_mask += '0'

        mask = int(bin_mask, 2)
        mask = str(IPv4Address(mask))

        return mask

    def ip_sum(self, address, num):
        address_splited = [int(dir) for dir in address.split('.')]
        int_dir = 0

        for i in range(4):

            int_dir = int_dir + address_splited[3-i] * (256 ** i)

        int_dir = int_dir + int(num)

        return str(IPv4Address(int_dir))

    def get_subnets(self, address, mask):
        subnets = []
        mask_splited = mask.split('.')
        address_splited = address.split('.')
        
        i=0
        try:
            while True:
                mask_splited.remove('255')

                try:
                    del address_splited[i]
                    i += 1
                except:
                    pass
        except ValueError:
            pass  

        bin_mask = ''
        for group in mask_splited:
            bin_mask += bin(int(group))

        net_bits = bin_mask.count('1')
        n_nets = 2**net_bits
        n_dirs = (2**((32 - 8*(mask.count('255')))-net_bits))

        dir = address

        subnets.append(dir)

        for i in range(n_nets - 1):
            dir = self.ip_sum(dir, n_dirs)
            subnets.append(dir)
            

        return subnets


    def get_hosts(address, mask):
        print(' ')