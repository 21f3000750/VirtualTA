# Topic: Sudo permission needed to create data folder in root?
**Topic ID**: 167072
**Total Posts**: 2

---

## Post #1 by vikramjncasr (Post ID: 594729)
@Jivraj
 
@carlton
 sir please help


When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?

needs sudo permission all the time…


image
2100×216 100 KB

### Image Insight:
![Image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f51040627e050b955bb243c23f1f660da36b73ae_2_690x70.png)

**Image Description:** The image shows a terminal window displaying the output of a Linux `ls /` command.  This command lists the contents of the root directory.

Here's a breakdown of the relevant information:

* **Top Lines:** These lines show the username (`vikramjncasr`), the current directory (`/mnt/c/IIT_Madras/TDS_Project_1`), and the command used (`ls /`).  This suggests the user is working within a Windows Subsystem for Linux (WSL) environment, given the `/mnt/c/...` path which is typical for WSL.

* **Directory Listing:** The core content is a listing of directories at the root level of the filesystem.  These include standard Linux directories such as:
    * `/bin`:  Binary executables.
    * `/boot`:  Boot loader files.
    * `/dev`:  Device files.
    * `/etc`:  Configuration files.
    * `/home`:  User home directories.
    * `/init`:  Initialization scripts.
    * `/lib`, `/lib64`:  System libraries.
    * `/lost+found`:  Files recovered after a filesystem check.
    * `/media`:  Mount points for removable media.
    * `/mnt`:  Mount points for other filesystems (note that the user is currently *in* a mount point under `/mnt`).
    * `/opt`:  Optional applications.
    * `/proc`:  Virtual filesystem containing process information.
    * `/root`:  The root user's home directory.
    * `/run`:  Runtime data.
    * `/sbin`, `/usr/sbin`:  System binary executables.
    * `/srv`:  Service data.
    * `/sys`:  System information.
    * `/tmp`:  Temporary files.
    * `/usr`:  User programs and libraries.
    * `/var`:  Variable data (logs, databases etc.).

* **`.usr-is-merged` directories:** The presence of `bin.usr-is-merged`, `sbin.usr-is-merged`, and `lib.usr-is-merged` suggests a system configuration where the `/usr` tree has been merged with other directories for space-saving or other reasons.  This is not standard but is a valid configuration.

In summary, the image displays a standard `ls /` command output showing the top-level directory structure of a Linux filesystem, potentially within a WSL environment, indicating a non-standard but valid filesystem merge configuration.

---

## Post #2 by carlton (Post ID: 594766)
Hi Vikram,


This is because (if you watched the session, or examined the code, you would have realised that) datagen.py was designed to run inside your docker container. And datagen.py (or a similar named file which we will not tell you ahead of time and will be provided as the query parameter in task A1) will normally be called by evaluate.py

Inside the docker container, permission for the data folder is set by the Dockerfile

which then allows your application to access the root folder inside your docker image and create the /data folder.


So the workflow is like this (for your internal testing only… please follow the Project page for deliverables and evaluation to submit project successfully):




You create your application server that serves 2 endpoints on localhost:8000


You create a docker image that runs this application server.


You run the docker image using podman as described in the project page.


For mimicking the testing conditions. You need two files:

evaluate.py and datagen.py to be in the same folder where you are running these two scripts.


Run evalute.py using uv.




If your docker image is correctly configured and your application is correctly configured, then all the tasks run by evaluate.py will correctly tell you if the application is producing the right result for each task.


Hope that gives clarity.


Kind regards

---
