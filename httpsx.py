a
    {Dc�  �                   @   s  d dl Z d dlZd dlZejdddd�Zejdddd	d
dd� ejdddddd� ejdddddd� e�� ZejZej	Z	ej
Z
g g g   ZZZdd� Zdd� Zdd� Zdd� Zd d!� Zed"k�ree j�d#kr�e�  e�e j� e �d#� e	r�e�  e�ree� e
�re�  e�  dS )$�    Nz[*] For bug bounty hunter!!!z%(prog)s -f file -o outputz&[*] %(prog)s -f file.txt -o output.txt)ZdescriptionZusageZepilogz-uz--url�urlz
submit url�arg_url�+)�metavar�help�destZnargsz-fz--file�filezsubmit input url file�arg_file)r   r   r   z-oz--output�outputzset output file name�
arg_outputc                  C   sL   d} d}d}d}| |||g}t t�|�� t d� t d� t d� t �  d S )Nz�
    __    __  __            _  __
   / /_  / /_/ /_____  ____| |/ /
  / __ \/ __/ __/ __ \/ ___/   / 
 / / / / /_/ /_/ /_/ (__  )   |  
/_/ /_/\__/\__/ .___/____/_/|_|  
             /_/                 
    z�
.__     __    __                        
|  |___/  |__/  |_______  _________  ___
|  |  \   __\   __\____ \/  ___/\  \/  /
|   Y  \  |  |  | |  |_> >___ \  >    < 
|___|  /__|  |__| |   __/____  >/__/\_ """
     \/           |__|       \/       \/
    z�
    __    __  __                 
   / /_  / /_/ /_____  ______  __
  / __ \/ __/ __/ __ \/ ___/ |/_/
 / / / / /_/ /_/ /_/ (__  )>  <  
/_/ /_/\__/\__/ .___/____/_/|_|  
             /_/                 
    a  
    
.__     __    __               ____  ___
|  |___/  |__/  |_______  _____\   \/  /
|  |  \   __\   __\____ \/  ___/\     / 
|   Y  \  |  |  | |  |_> >___ \ /     \ 
|___|  /__|  |__| |   __/____  >___/\  """
     \/           |__|       \/      \_/
    z[*] Created by Adarsh Addee!!!z&[*] Create any link full accessible!!!z7[*] You can use a file to create URL and save output!!!)�print�randomZchoice)Zbanner1Zbanner2Zbanner3Zbanner4Zbanners� r   �+d:\Code\Python\Args\httpsx\httpsx\httpsx.py�banner    s    	
r   c                 C   s8   d|  }d|  }t |� t |� t�|� t�|� d S )Nzhttps://zhttp://)r   �https_url_lst�append�http_url_lst)�make_urlZr_httpsZr_httpr   r   r   r   K   s    
r   c               
   G   s�   | D ]$}|D ]}t |�dkrt�|� qqzJt t�dkrT| D ]}|D ]}t|� qDq<t t�dkrr| D ]}t|� qdW n4 ty� } ztd� td� W Y d }~n
d }~0 0 d S )N�   z[X] Try to Add Two URLs!!!z[X] Kindly Add Two URLs!!!)�len�lstr   r   �	Exceptionr   )Z	url_entry�var�lZ	arg_tupler   �er   r   r   �
handle_urlT   s    r   c                  C   sL   t rHtt ��,} | D ]}|�d�}t|� qW d   � n1 s>0    Y  d S )N�
)r	   �open�stripr   )r   �liner   r   r   �handle_filej   s
    

r!   c                  C   s�   t r�tt d���} | �d� | �d� tD ]}| �|� | �d� q(| �d� | �d� | �d� tD ]}| �|� | �d� qd| �d� W d   � n1 s�0    Y  d S )N�azAll https links are:r   z

zAll http links are:)r   r   �writer   r   )Zoutput_fileZhtps_urlZhtp_urlr   r   r   �handle_outputq   s    






r$   �__main__r   )�sysZargparser   ZArgumentParser�parserZadd_argumentZ
parse_args�argsr   r	   r   r   r   r   r   r   r   r!   r$   �__name__r   �argv�
print_help�stderr�exitr   r   r   r   r   �<module>   sR   ���+	

