3
"�]�  �            *   @   s�  d dl Z d dlZd dlZyd dlmZ W n  ek
rH   d dlmZ Y nX dd� ZdZdZdZ	dZ
d	Ze� Zejd
� eejdd��Zeejdd��Zeejdd��Zeejdd��Zeejdd��Zeejdd��Zeejdd��Zeejdd��Zeejdd��Zed� ye jeee	e
ed�ZW n4 ek
�rZ   ed� ed� ed� e�  Y nX dZe ej!�dk�r�e ej!d �dk�r�ej!d Znxe e�dk �r�ed�Z�q�W ej"dd�j"dd�j"dd�j"dd�Zej#� Zedk�r�d Zed!e d" �Z$e$dk�ree$k�re$Zd#Zed$k�r"d%Zejdd�Zed&e d' �Z$e$dk�rVee$k�rVe$Zy<ej%� Z%e%j&d(j'e�� e%j(� Z)ee)d  �Z*ee)d �Z+W n. ek
�r�   ed� ed)� ed� Y nX ej,�  d*e Z-d+e- d, Z.e/e.d-�Z0e0j1d� e0j,�  d.e- d, Z2e/e2d-�Z0e0j1d� e0j,�  d/Z3ed$k�r4d0Z3e/e3d1��Z4e4j� Z5W dQ R X e5j"d2e�Z5e5j"d3e�Z5e5j"d4e�Z5e5j"d5e+�Z5e5j"d6e�Z5e5j"d7e�Z5e5j"d8e*�Z5e5j"d9ee��Z5e5j"d:ee��Z5e5j"d;ee��Z5e/e-d< d-��Z4e4j1e5� W dQ R X ed� ed=e- d> � e/d
d-�Z4e4j1d?� e4j1d@e dA � e4j1dBe dA � e4j1dCe dA � e4j1dDe dA � e4j1dEe dA � e4j1dFe dA � e4j1dGee� dA � e4j1dHee� dA � e4j1dIe* dA � e4j1dJee� dA � e4j,�  dS )K�    N)�ConfigParserc             C   s2   d}yt | �}W n tk
r,   t| �}Y nX |S )N� )�	raw_input�	Exception�input)�message�data� r	   �cisco_provision_freepbx_v1.3.py�get_raw_data   s    r   z	127.0.0.1i�  ZasteriskZSuperFasterz.123456Azlast_cisco_provision.iniZlast_configZIPPBXZMODELZSPORTZEXTENZVMAILZFIRMWZRTPSTZRTPENZ	DIRECTORYz Trying to connect to database...)�host�port�db�userZpasswdr   z;Please add the user/password SuperFaster/.123456A to mysql.�   �   zMAC?: �-�.� �/�1zMODEL [(1)CP6900, (2)CP8900]? (z) (blank for [1]): zSIP69xx.9-4-1-3�2zsip8961.9-4-2SR4-1zEXT? (z) (blank for same): a  
    SELECT max(f.callerid) callerid, max(f.secret) secret  FROM ( SELECT if(q.keyword ='callerid',q.data,null)  callerid, if(q.keyword ='secret',q.data,null) secret  FROM ( SELECT  keyword ,data FROM `sip` WHERE id = '{}' AND keyword IN ('callerid','secret') )q )f 
	zQuery error on mysql.ZSEPZITLz.tlv�wZCTLzSEP_base_6900.cnf.xmlzSEP_base_8900.cnf.xml�rZ_IPPBX_Z_SPORT_Z_EXTEN_Z_PASSW_Z_VMAIL_Z_FIRMW_Z
_CALLERID_Z_RTPST_Z_RTPEN_Z_DIRECTORY_z.cnf.xmlzFile z.cnf.xml has been created.z[last_config]
zIPPBX = �
zMODEL = zSPORT = zEXTEN = zVMAIL = zFIRMW = zRTPST = zRTPEN = zCALLERID = zDIRECTORY = )6ZMySQLdb�sys�os�configparserr   �ImportErrorr   Z_hostZ_portZ_db�_userZ_passwdZconfig�read�str�getZippbxZmodelZgetintZsportZextenZvmailZfirmwZrtpstZrtpenZd_url�print�connectr   r   �exitZmac�len�argv�replace�upper�tmpZcursorZexecute�formatZfetchoner   ZcalleridZpassw�close�	file_nameZitl_file�openZcnf�writeZctl_fileZSEP_BASE�fileZfiledatar	   r	   r	   r
   �<module>   s�   
$ $
  
  




 

