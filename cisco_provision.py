
�Ղ]   �            *   @   sr  d  d l  Z  d  d l Z d  d l Z y d  d l m Z Wn" e k
 r\ d  d l m Z Yn Xd d �  Z d Z d Z d Z	 d Z
 d	 Z e �  Z e j d
 � e e j d d � � Z e e j d d � � Z e e j d d � � Z e e j d d � � Z e e j d d � � Z e e j d d � � Z e e j d d � � Z e e j d d � � Z e e j d d � � Z e d � y. e  j d e d e d e	 d e
 d e � Z Wn7 e k
 r�e d � e d � e d � e �  Yn Xd Z e  e j! � d k r+e  e j! d � d k r+e j! d Z n% x" e  e � d k  rOe d � Z q.We j" d  d � j" d! d � j" d" d � j" d# d � Z e j# �  Z e d k r�d$ Z e d% e d& � Z$ e$ d k r�e e$ k r�e$ Z d' Z e d( k r�d) Z e j d d � Z e d* e d+ � Z$ e$ d k r2e e$ k r2e$ Z yR e j% �  Z% e% j& d, j' e � � e% j( �  Z) e e) d  � Z* e e) d � Z+ Wn0 e k
 r�e d � e d- � e d � Yn Xe j, �  d. e Z- d/ e- d0 Z. e/ e. d1 � Z0 e0 j1 d � e0 j, �  d2 e- d0 Z2 e/ e2 d1 � Z0 e0 j1 d � e0 j, �  e/ d3 d4 � � Z3 e3 j �  Z4 Wd QRXe4 j" d5 e � Z4 e4 j" d6 e � Z4 e4 j" d7 e � Z4 e4 j" d8 e+ � Z4 e4 j" d9 e � Z4 e4 j" d: e � Z4 e4 j" d; e* � Z4 e4 j" d< e e � � Z4 e4 j" d= e e � � Z4 e4 j" d> e e � � Z4 e/ e- d? d1 � � Z3 e3 j1 e4 � Wd QRXe d � e d@ e- dA � e/ d
 d1 � Z3 e3 j1 dB � e3 j1 dC e dD � e3 j1 dE e dD � e3 j1 dF e dD � e3 j1 dG e dD � e3 j1 dH e dD � e3 j1 dI e dD � e3 j1 dJ e e � dD � e3 j1 dK e e � dD � e3 j1 dL e* dD � e3 j1 dM e e � dD � e3 j, �  d S)N�    N)�ConfigParserc             C   s;   d } y t  |  � } Wn t k
 r6 t |  � } Yn X| S)N� )�	raw_input�	Exception�input)�message�data� r	   �cisco_provision_freepbx_v1.3.py�get_raw_data   s    r   z	127.0.0.1i�  ZasteriskZSuperFasterz.123456Azlast_cisco_provision.iniZlast_configZIPPBXZMODELZSPORTZEXTENZVMAILZFIRMWZRTPSTZRTPENZ	DIRECTORYz Trying to connect to database...�host�port�db�userZpasswdr   z;Please add the user/password SuperFaster/.123456A to mysql.�   �   zMAC?: �-�.� �/�1zMODEL [(1)CP6900, (2)CP8900]? (z) (blank for [1]): zSIP69xx.9-4-1-3�2zsip8961.9-4-2SR4-1zEXT? (z) (blank for same): a�  
                    SELECT max(f.callerid) callerid, max(f.secret) secret 
                    FROM
                    (
                        SELECT if(q.keyword ='callerid',q.data,null) 
                        callerid, if(q.keyword ='secret',q.data,null) secret 
						FROM
						(
							SELECT 
							keyword ,data
							FROM `sip`
							WHERE id = '{}'
							AND keyword IN ('callerid','secret')
						)q
					)f 
				zQuery error on mysql.ZSEPZITLz.tlv�wZCTLzSEP_base_.cnf.xml�rZ_IPPBX_Z_SPORT_Z_EXTEN_Z_PASSW_Z_VMAIL_Z_FIRMW_Z
_CALLERID_Z_RTPST_Z_RTPEN_Z_DIRECTORY_z.cnf.xmlzFile z.cnf.xml has been created.z[last_config]
zIPPBX = �
zMODEL = zSPORT = zEXTEN = zVMAIL = zFIRMW = zRTPST = zRTPEN = zCALLERID = zDIRECTORY = )5ZMySQLdb�sys�os�configparserr   �ImportErrorr   Z_hostZ_portZ_db�_userZ_passwdZconfig�read�str�getZippbxZmodelZgetintZsportZextenZvmailZfirmwZrtpstZrtpenZd_url�print�connectr   r   �exitZmac�len�argv�replace�upper�tmpZcursorZexecute�formatZfetchoner   ZcalleridZpassw�close�	file_nameZitl_file�openZcnf�writeZctl_file�fileZfiledatar	   r	   r	   r
   �<module>   s�   	
.


. 6    






