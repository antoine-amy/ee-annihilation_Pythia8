#include "Pythia8/Pythia.h"
#include <iostream>
#include <cstdio>

using namespace Pythia8;

int main(){
  int nEvent=1000000; // Number of events
  Pythia pythia;
  pythia.readString("PDF:lepton = off"); //Allow no substructure in e+- beams: normal for corrected LEP data.
  pythia.readString("WeakSingleBoson:ffbar2gmZ = on"); // Process selection.
  // Switch off all Z0 decays and then switch back on those to quarks.
  pythia.readString("23:onMode = off");
  pythia.readString("23:onIfAny = 1 2 3 4 5");
  pythia.readString("PartonLevel:FSR = on");
  pythia.readString("HadronLevel:all = off");
  // LEP1 initialization at Z0 mass.
  pythia.readString("Beams:idA =  11");
  pythia.readString("Beams:idB = -11");
  pythia.readString("Beams:eCM = 150."); //in GeV
  pythia.init();

  double etaMax=4.;
  double radius=0.4;
  double pTjetMin=10.;
  int nSel=2; // Exclude neutrinos (and other invisible) from study.
  SlowJet slowJet( -1, radius, pTjetMin, etaMax, nSel, 1); // Set up SlowJet jet finder, with anti-kT clustering and pion mass assumed for non-photons..

  // Histograms. Note similarity in names, even when the two jet finders
  // do not calculate identically the same property (pT vs. ET, y vs. eta).
  Hist nJetsS("number of jets, SlowJet", 50, -0.5, 49.5);
  Hist eTjetsS("pT for jets, SlowJet", 100, 0., 500.);
  Hist phiJetsS("phi for jets, SlowJwt", 100, -M_PI, M_PI);

  // Begin event loop. Generate event. Skip if error.
  for (int iEvent = 0; iEvent < nEvent; ++iEvent) {
    if (!pythia.next()) continue;

    // Analyze Slowet jet properties. List first few.
    slowJet. analyze( pythia.event );
    slowJet.list();
    // Fill SlowJet inclusive jet distributions.
    nJetsS.fill( slowJet.sizeJet());
  
    // Get slowJet infos
    for (int i = 0; i < slowJet.sizeJet(); ++i){
      eTjetsS.fill( slowJet.pT(i) );
      phiJetsS.fill( slowJet.phi(i) );
    }
    float pT_a = slowJet.pT(0); float pT_b = slowJet.pT(1);
    float eta_a=slowJet.y(0); float eta_b = slowJet.y(1);
    float phi_a=slowJet.phi(0); float phi_b = slowJet.phi(1);

    // Making sure to get the values of the 2 more energetics jets
    if (slowJet.sizeJet()>2){
      for (int i=2; i<slowJet.sizeJet(); ++i){
        if (slowJet.pT(i)>pT_a){
          pT_a=slowJet.pT(i);
          eta_a=slowJet.y(i);
          phi_a=slowJet.phi(i);
        }
        if (slowJet.pT(i)<pT_a){
          if (slowJet.pT(i)>pT_b){
          pT_b=slowJet.pT(i);
          eta_b=slowJet.y(i);
          phi_b=slowJet.phi(i);
          }
        }
      }
    }

    float dphi=phi_b-phi_a;
    float theta1 = 2*atan(exp(-eta_a));
    float theta2 = 2*atan(exp(-eta_b));
    cout<<"theta jet pT max: "<< theta1 <<endl;
    cout<<"theta jet pT max: "<< theta2 <<endl;
    cout<<"pTmax: "<<pT_a<<endl;
    cout<<"pTmax2: "<<pT_b<<endl;
    cout<<"delta phi: "<<dphi<<endl;
  }
  pythia.stat();
  return 0;
}