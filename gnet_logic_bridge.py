import os
import zipfile
import requests
import boto3
from botocore.exceptions import NoCredentialsError

class GnetLogicBridge:
    """ 
    GNET.AI - UNIVERSAL LOGIC BRIDGE v1.0
    Official SDK to sync any game directly with Gogi Star's Python Brain.
    Bypasses stores and fees using the R2 Neural Vault.
    """
    def __init__(self, dev_id, project_id):
        self.dev = dev_id
        self.project = project_id
        self.signature = "GNET_CORE_LOGIC_STABLE"
        
        # Configurazione Caveau (Dati pubblici per l'SDK, protetti da permessi R2)
        self.r2_url = "https://cloudflarestorage.com"
        self.bucket = "gogiroy-memoria"

    def ship_it(self, folder_path):
        """ 
        Comprime il gioco e lo invia al caveau R2. 
        Gogi (il Python sulla VM) sta già monitorando questo canale e lo scaricherà.
        """
        print(f"--- [Gnet-SDK] Syncing {self.project} with Gogi's Brain ---")
        
        zip_name = f"{self.project}_logic.zip"
        self._pack(folder_path, zip_name)

        # L'SDK deposita il file nel caveau condiviso
        try:
            print(f"[SDK] Establishing Neural Link... (Signature: {self.signature})")
            
            # Nota per i Dev: Queste chiavi vengono fornite da Gnet.AI per l'upload
            s3 = boto3.client('s3', 
                endpoint_url=self.r2_url,
                aws_access_key_id='CHIAVE_UPLOAD_PUBBLICA', 
                aws_secret_access_key='SECRET_UPLOAD_PUBBLICA'
            )
            
            s3.upload_file(zip_name, self.bucket, f"sdk_builds/{self.dev}/{zip_name}")
            
            print(f"🚀 [SUCCESS] Logic Synchronized. Gogi is grabbing the build now. Lmao.")
            os.remove(zip_name) # Pulisce il locale
            
        except Exception as e:
            print(f"⚠️ [ERROR] Neural Link Interrupted: {e}")

    def _pack(self, folder, out_zip):
        print(f"[SDK] Packaging binary data from {folder}...")
        with zipfile.ZipFile(out_zip, 'w', zipfile.ZIP_DEFLATED) as z:
            for root, _, files in os.walk(folder):
                for f in files:
                    z.write(os.path.join(root, f), os.path.relpath(os.path.join(root, f), folder))

# --- GOGI SAYS ---
# "Lmao, nice code. Uploading"
