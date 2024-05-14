from breezypythongui.breezypythongui import EasyFrame


class TaxDemo(EasyFrame):
    def __init__(self):
        # call the original constructor and provide the title and initial dimension for the window
        EasyFrame.__init__(self, title='An Empty Window', width=400, height=200)

        # add the income label and field
        self.addLabel(text='Income', row=0, column=0)
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1)

        # add the dependents label and field
        self.addLabel(text='Dependents', row=1, column=0)
        self.dependentsField = self.addIntegerField(value=0, row=1, column=1)

        # add the exemption amount label and field
        self.addLabel(text='Exemption amount', row=2, column=0)
        self.exemptionAmountField = self.addFloatField(value=0.0, row=2, column=1)

        # add the compute button with a window method as a reference command
        self.addButton(text='Compute', row=3, column=0, columnspan=2, command=self.computeTax)

        # add total tax label and field
        self.addLabel(text='Total tax', row=4, column=0)
        self.totalTaxField = self.addFloatField(value=0.0, row=4, column=1)

    def computeTax(self):
        # get the values from all the fields
        income = self.incomeField.getNumber()
        numDependents = self.dependentsField.getNumber()
        exemptionAmount = self.exemptionAmountField.getNumber()

        # calculate the tax
        tax = (income - numDependents * exemptionAmount) * .15

        # set the tax calculation to the total tax field
        self.totalTaxField.setNumber(tax)


if __name__ == '__main__':
    my_window = TaxDemo()
    my_window.mainloop()
