<<<<<<< Updated upstream
# client-project
 
=======
# CLIENT-PROJECT
<!-- Add Pictures -->
![banner](assets/images/readme/banner.png)

- [CLIENT-PROJECT](#client-project)
  - [PROJECT TYPES](#project-types)
    - [AUDIO](#audio)
      - [> PRODUCE <](#-produce-)
      - [> RECORD <](#-record-)
      - [> MIX & MASTER <](#-mix--master-)
    - [DOCS](#docs)
    - [IMAGE](#image)
    - [VIDEO](#video)
    - [WEB](#web)
  - [DESCRIPTION](#description)
  - [TESTING](#testing)
  - [DEVELOPMENT/CONTRIBUTING](#developmentcontributing)
  - [USAGE](#usage)
  - [INSTALLATION](#installation)
    - [initial structure](#initial-structure)
      - [Initial Folders](#initial-folders)
      - [Initial Files](#initial-files)
    - [before mixing completed](#before-mixing-completed)
    - [after mixing completed](#after-mixing-completed)
  - [HISTORY](#history)
  - [CREDITS](#credits)
  - [LICENCE](#licence)

---

[>>> back to top <<<](#client-projectsession)

---

## PROJECT TYPES

### AUDIO

client_name/song_title

#### > PRODUCE <

- [x] Date      :
- [x] Producer  :
- [x] Title     :
- [ ] Project_Folder_Name

#### > RECORD <

- [ ] Date      :
- [ ] Artist    :
- [ ] Title     :
- [ ] Project_Folder_Name

#### > MIX & MASTER <

- [ ] Date      :
- [ ] Artist    :
- [ ] Title     :
- [ ] Project_Folder_Name

---

[>>> back to top <<<](#client-projectsession)

---

### DOCS

---

[>>> back to top <<<](#client-projectsession)

---

### IMAGE

---

[>>> back to top <<<](#client-projectsession)

---

### VIDEO

---

[>>> back to top <<<](#client-projectsession)

---

### WEB

---

[>>> back to top <<<](#client-projectsession)

---

## DESCRIPTION

## TESTING

## DEVELOPMENT/CONTRIBUTING

## USAGE

To Run the App from terminal, run this code.  Follow the Terminal Menu's instructions.

```bash
python3 new_client_project.py
```

- audio project

  To Produce a Beat, follow the Terminal Menu's instructions.
  - produce
    ![run](assets/images/readme/run.png)
    ![main menu](assets/images/readme/main_menu.png)
    ![produce](assets/images/readme/audio_1_produce_3_produce.png)
    ![producer name](assets/images/readme/audio_1_produce_4_producer_name.png)
    ![title](assets/images/readme/audio_1_produce_5_title.png)
    ![bpm](assets/images/readme/audio_1_produce_6_bpm.png)
    ![confirm](assets/images/readme/audio_1_produce_7_confirm.png)
  - record
    ![run](assets/images/readme/run.png)
    ![main menu](assets/images/readme/main_menu.png)
    ![record](assets/images/readme/audio_2_record_3_record.png)
    ![artist name](assets/images/readme/audio_2_record_4_artist_name.png)
    ![title](assets/images/readme/audio_2_record_5_title.png)
    ![confirm](assets/images/readme/audio_2_record_6_confirm.png)
  - mix & master
    ![run](assets/images/readme/run.png)
    ![main menu](assets/images/readme/main_menu.png)
    ![mix & master](assets/images/readme/audio_3_mix_&_master_3_mix_&_master.png)
- docs project
- image project
- video project
- web project

## INSTALLATION

### initial structure

#### Initial Folders
<!-- user input for `client name` -->
- clientname folder
<!-- user input for `project name` -->
- projectname folder
<!-- based on project type create these folders -->
- projectname subfolders

#### Initial Files
<!-- auto-generated alias of final_mp3_version of the project -->
- Final.alias
<!-- auto-generated alias of instrumental of the project -->
- Instrumental.alias
<!-- stores client email addresses -->
- client_email.csv
<!-- stores client notes about current project -->
- client_notes.csv
<!-- stores changes & updates via:client notes about current project -->
- changelog.log
<!-- stores sample cues from imported samples of project -->
- sample_cue_points.txt
<!-- stores quick overview of current project -->
- README.md
<!-- stores links & metadata about current project -->
- index.html

### before mixing completed

- Send these files to client:
  - `client_notes.txt`
- Received files from client
  - `client_notes.txt`

### after mixing completed

- Update these files
  - `client_notes.txt`
  - `changelog.log`
  - `README.md`
- Convert these files
  - `final_version.pdf` from `README.md`
- Send final files to clients emails
  - `final_version.mp3`
  - `final_version.pdf`
- Prepare Stems
  - Location:
    - `src/audio/stems`
  - Stems: Gang of Four
    - Stem #1. **TV** (that’s instrumental plus chorus or background vocals).
    - Stem #2. **Lead Vocal(s)** (plus its reverb of course ---basically muting everything else).
    - Stem #3. **Full Mix** (that’s what I will use unless there is a problem, and it's also a reference to prove that #1 and #2 were made correctly).
    - Stem #4. **Instrumental** (by adding this to #1 we can reduce the chorus level. By subtracting this from #1 we can increase the chorus level. By subtracting this from #3 we can increase lead and chorus. And so on! - Bob Katz
  - Stems: Archive
    - Create `stems_gang_of_four.zip` in `src/audio/stems`
    - Copy `stems_gang_of_four.zip` in `Client Library`

## HISTORY

## CREDITS

## LICENCE
<!-- Add Badges -->
![reddit](https://img.shields.io/reddit/user-karma/combined/iomd?style=social)
![twitter](https://img.shields.io/twitter/follow/IceOnDaMixDown?style=social)
![youtube](https://img.shields.io/youtube/channel/views/UCuKlAHcp9w5KJ9IxVg3Vm8g?style=social)
![github](https://img.shields.io/github/followers/iomd?style=social)
>>>>>>> Stashed changes
