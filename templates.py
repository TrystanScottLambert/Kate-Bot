"""
Storing the templates for emails. 
"""

from dataclasses import dataclass
import textwrap


@dataclass
class NormalInvite:
    """
    Standard invite for visitors to ICRAR.
    """
    possible_speaker: str
    my_name: str
    co_organizer: str

    @property
    def message(self) -> str:
        """
        Creates the body template
        """
        string = textwrap.dedent(f"""Dear {self.possible_speaker},
        
        {self.co_organizer} (CC'ed) and I organise the seminar series at ICRAR-UWA. Your name was suggested as a potential speaker whose work would be of interest to the regular attendees, so I'm reaching out to see if you are interested in presenting a talk at some point.   
        ICRAR-UWA has a broad range of research interests and expertise — extragalactic survey science (UV → Radio and IFS), galaxy formation/evolution, simulations, data-intensive astronomy. Our seminars normally target an expert audience, similar to the level one would pitch to an interdisciplinary conference. The talks are standard length: about 45 minutes plus questions; shorter talks of around 30 minutes are also perfectly fine.   

        We nominally have two usual seminar slots at 3:30pm on Tuesdays, or 11:30am on Thursdays (both in AWST time zone).
        Please let us know if you would be interested in giving a talk and we can discuss a suitable date and time.
                
        Sincerely,
        {self.my_name} & {self.co_organizer}.""")
                
        return string
