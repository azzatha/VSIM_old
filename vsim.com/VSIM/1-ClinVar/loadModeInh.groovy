@Grapes([
    @Grab(group='org.slf4j', module='slf4j-simple', version='1.6.1'),
          @Grab(group='org.semanticweb.elk', module='elk-owlapi', version='0.4.3'),
          @Grab(group='net.sourceforge.owlapi', module='owlapi-api', version='4.2.5'),
          @Grab(group='net.sourceforge.owlapi', module='owlapi-apibinding', version='4.2.5'),
          @Grab(group='net.sourceforge.owlapi', module='owlapi-impl', version='4.2.5'),
          @Grab(group='net.sourceforge.owlapi', module='owlapi-parsers', version='4.2.5')
        ])

import org.semanticweb.owlapi.model.parameters.*
import org.semanticweb.elk.owlapi.ElkReasonerFactory;
import org.semanticweb.elk.owlapi.ElkReasonerConfiguration
import org.semanticweb.elk.reasoner.config.*
import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.reasoner.*
import org.semanticweb.owlapi.reasoner.structural.StructuralReasoner
import org.semanticweb.owlapi.vocab.OWLRDFVocabulary;
import org.semanticweb.owlapi.model.*;
import org.semanticweb.owlapi.io.*;
import org.semanticweb.owlapi.owllink.*;
import org.semanticweb.owlapi.util.*;
import org.semanticweb.owlapi.search.*;
import org.semanticweb.owlapi.manchestersyntax.renderer.*;
import org.semanticweb.owlapi.reasoner.structural.*
import java.io.File;
import org.semanticweb.owlapi.util.OWLOntologyMerger;

IRI omim = IRI.create("http://purl.obolibrary.org/obo/hp.owl")
//def omimOnt = manager.loadOntologyFromOntologyDocument(omim)
OWLOntologyManager manager = OWLManager.createOWLOntologyManager()
OWLOntology ont = manager.loadOntologyFromOntologyDocument(omim)

OWLDataFactory fac = manager.getOWLDataFactory()
ConsoleProgressMonitor progressMonitor = new ConsoleProgressMonitor()
OWLReasonerConfiguration config = new SimpleConfiguration(progressMonitor)
ElkReasonerFactory f1 = new ElkReasonerFactory()
OWLReasoner reasoner = f1.createReasoner(ont,config)
reasoner.precomputeInferences(InferenceType.CLASS_HIERARCHY)

def map = [:].withDefault { new LinkedHashSet() }

def first = new LinkedHashSet()
reasoner.getSubClasses(fac.getOWLClass(IRI.create("http://purl.obolibrary.org/obo/HP_0000005")), false).getFlattened()?.each { node ->
  first.add(node.toString().replaceAll("<","").replaceAll(">",""))
}
//println first

new File("./1-ClinVar/diseasephenotypes.txt").splitEachLine("\t") { line ->
  def id = line[0]
  def pheno = line[1]?.replaceAll("HP:","http://purl.obolibrary.org/obo/HP_")
  if (pheno in first) {
    map[id].add(pheno)
  }
}

map.each { k, v ->
  //print "$k"
  //v.each { print "\t$it" }
  rec="http://purl.obolibrary.org/obo/HP_0000007"
  dom="http://purl.obolibrary.org/obo/HP_0000006"
  x="http://purl.obolibrary.org/obo/HP_0001417"
  if (dom in map[k])
	  print "$k\tDominant"
  else if (rec in map[k])
	  print "$k\tRecessive"
  else if (x in map[k])
	  print "$k\tX-linked"
  else
	  print "$k\tOthers"
    println ""
}