import consul
import socket
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


def register_service():
    """Register this service with Consul"""
    try:
        c = consul.Consul(host=settings.CONSUL_HOST, port=settings.CONSUL_PORT)
        
        # Obtenir l'IP correcte du conteneur
        service_host = socket.gethostbyname(socket.gethostname())
        print(f"🔍 Enregistrement du service avec IP: {service_host}")
        
        # Supprimer l'ancien enregistrement s'il existe
        try:
            c.agent.service.deregister('trajet-v1')
            print("Ancien service supprimé")
        except:
            pass
        
        # Enregistrer avec la bonne IP
        c.agent.service.register(
            name='trip-service',
            service_id='trip-service-1',
            address=service_host,
            port=8002,
            tags=['trip', 'django'],
            check=consul.Check.http(
                f'http://{service_host}:8002/api/health/',
                interval='10s',
                timeout='5s'
            )
        )
        
        logger.info("Trip Service registered with Consul")
        print(f"✅ Trip Service enregistré à {service_host}:8002")
        
    except Exception as e:
        logger.error(f"Failed to register with Consul: {e}")
        print(f"❌ Erreur: {e}")


def deregister_service():
    """Deregister this service from Consul"""
    try:
        c = consul.Consul(host=settings.CONSUL_HOST, port=settings.CONSUL_PORT)
        c.agent.service.deregister('trip-service-1')
        logger.info("Trip Service deregistered from Consul")
        print("✅ Service désenregistré")
    except Exception as e:
        logger.error(f"Failed to deregister: {e}")
        print(f"❌ Erreur: {e}")