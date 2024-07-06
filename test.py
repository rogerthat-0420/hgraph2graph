from rdkit import Chem

smiles = 'c1ccc(C2=Nn3cnnc3SC2)cc1'
mol = Chem.MolFromSmiles(smiles)
if mol:
    try:
        Chem.Kekulize(mol)
        print(f"successful kekulize")
    except Chem.KekulizeException as e:
        print(f"Can't kekulize mol. Unkekulized atoms: {e}")
        for atom in mol.GetAtoms():
            if not atom.GetIsAromatic():
                print(f"Atom {atom.GetIdx()} ({atom.GetSymbol()}) is not aromatic.")
else:
    print("Failed to create molecule from SMILES.")
