
class laptop:

    def setvalues(self,brand,model,processor,ram,storage,os,graphics_card):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.os = os
        self.graphics = graphics_card

    def getvalues(self):
        print("Brand            :" , self.brand)
        print("Model            :" , self.model)
        print("Processor        :" , self.processor)
        print("RAM              :" , self.ram)
        print("Storage          :" , self.storage)
        print("Operating system :" , self.os)
        print("Graphics Card    :" , self.graphics)

l1 = laptop()
l1.setvalues("Dell","XPS 15","Intel i7","16GB","512GB SSD","Windows 11","NVIDIA GTX 1650")
l1.getvalues()
print()

l2 = laptop()
l2.setvalues("Apple","MacBook Pro","M2","16GB","1TB SSD","macOS Ventura","Integrated M2 GPU")
l2.getvalues()
print()

l3 = laptop()
l3.setvalues("HP","Spectre x360","Intel i5","8GB","256GB SSD","Windows 11","Intel Iris Xe")
l3.getvalues()
print()

