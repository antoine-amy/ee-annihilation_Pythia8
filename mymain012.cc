#include "Pythia8/Pythia.h"
#include <iostream>
#include <cstdio>

using namespace Pythia8;

int main() {
  // Initialize Pythia
  Pythia pythia;
  pythia.readString("PDF:lepton = off"); //Allow no substructure in e+- beams: normal for corrected LEP data.
  pythia.readString("WeakSingleBoson:ffbar2gmZ = on"); // Process selection.
  // Switch off all Z0 decays and then switch back on those to quarks.
  pythia.readString("23:onMode = off");
  pythia.readString("23:onIfAny = -13 13"); //1 2 3 4 5 for quarks; -13 13 for muons
  pythia.readString("PartonLevel:FSR = off");
  pythia.readString("HadronLevel:all = off");
  // LEP1 initialization at Z0 mass.
  pythia.readString("Beams:idA =  11");
  pythia.readString("Beams:idB = -11");

  //loop on sqrt(s) values
  for (int j = 50; j < 250; ++j){
  pythia.settings.parm("Beams:eCM", j);
  
  //pythia.readString("Beams:eCM = 150."); //sqrt(s) value in GeV
  pythia.init();

  // Generate events
  int n_events = 100000;
  for (int iEvent = 0; iEvent < n_events; ++iEvent){
    if (!pythia.next()) continue;
    for (int i = 0; i < pythia.event.size(); ++i)
      if (pythia.event[i].isFinal()){
          float eta = pythia.event[i].eta();
          float theta = 2*atan(exp(-eta));
          //cout<< "theta: "<< theta<<endl;
      }
  }
  pythia.stat();

  // Calculate cross section
  std::cout << "Cross section: " << pythia.info.sigmaGen() << " mbarns" << std::endl;
  } //end of sqrt(s) loop

  return 0;
}