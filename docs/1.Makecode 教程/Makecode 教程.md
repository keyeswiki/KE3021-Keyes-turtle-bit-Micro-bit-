# Makecode 教程

## 代码与编程

以下的步骤说明基于Windows操作系统，如果你使用的是其他操作系统，可以将其作为参考。

快速开始 

本节介绍如何为micro：bit编写程序以及如何将其下载到micro：bit。
micro：bit官方网站上有非常详细的教程，
您可以参考：[Https://microbitorg/guide/quick/](https://microbitorg/guide/quick/)

Step 1: 连接micro：bit

USB线将micro：bit连接到电脑，（[使用移动动设备对micro:bit进行编码，请移步查看](https://microbitorg/guide/mobile/)：<https://microbitorg/get-started/user-guide/mobile/>）
Macs、PCs、 Chromebooks and Linux系统（包括Raspberry Pi）都支持micro：bit。

![](media/f00f946e1f194811b1c84725e0eb5d16.png)

![](media/18c70cf16dcf8c9694a1af8b12530cf9.png)

micro:bit主板背后的红色LED会显示，表明micro:bit主板有电了。

Micro:bit
将在您的电脑上显示为一个名为'MICROBIT'的驱动器。但请注意，它不是普通的USB磁盘！如下图：

![](media/a2b53f93f4c24b81fc5cdb5986fd100d.png)

Step 2: 编写程序

，然后单击“新建项目”，出现“创建项目”对话框，在对话框中输入“heartbeat”，单击“创建”并开始编程。

App进行编程，这与在浏览器上进行编程完全相同:
[https://wwwmicrosoftcom/zh-cn/p/makecode-for-micro-bit/9pjc7sv48lcx?ocid=badgep&rtc=1&activetab=pivot:overviewtab](https://wwwmicrosoftcom/zh-cn/p/makecode-for-micro-bit/9pjc7sv48lcx?ocid=badgep&rtc=1#activetab=pivot:overviewtab)

（以下是以Google Chrome为例，其他浏览器类似）

![](media/f7a321023281fc7221a9506b10f2eaaa.png)

![](media/e07644b623697bf2510f032a516f407a.png)

使用MakeCode编辑器，写一个micro:bit代码。
例如，从模块区拖放一些指令方块放入代码编辑区，然后在MakeCode编辑器中的Simulator上尝试你的程序，如下演示了如何对heartbeat进行编程的全过程。

下一节将进一步介绍Makecode。

如果你的编程界面是英文界面需要切换到中文界面

操作：如下图点击右上角1（设置）图标，再点击2 Language,然后选择简体中文，这样就切换到中问界面了

![](media/77f06b2f0aaecae7c5f6a462e6ed344e.png)

![](media/122bb510e3a3515916407fe327bb59fe.png)

![](media/227be9e17bf4fba3e7dc9840d592794d.png)

1点击基础拖出两个
显示图标方块放入无线循环中，点击第二个方块下拉按钮换成

![](media/6f4ee722b59db324b57fba6c5d72e5d7.png)

图标，效果如图一

2点击“ JS JavaScript”，你可以看到对应的JavaScript语言代码程序，如下图二

![](media/0d620a83693f3f968b1b22becc6875b4.png)

图一

![](media/32e69bb2fc03fc9fcdb472db5798b2a2.png)

图二

你还可以点击“JavaScript
”，再点击下拉按钮选择“Python”，你还可以看到对应的Python语言代码程序，如下图：

![](media/70678f6683d14388675619b1cd772a7a.png)

Step 3: 下载代码

如果使用Windows 10 App编写程序，则只需单击“下载”按钮，该代码程序将直接下载到micro:bit主板，而无需任何其他操作。

如果使用浏览器编写程序，请按照以下步骤操作：

单击编辑器中的“下载”按钮。
这将下载一个“hex”文件，该文件是micro：bit可以读取的紧凑程序格式。
十六进制文件下载后，将其复制到你的micro：bit，就像将文件复制到USB驱动器一样。
在Windows上，你还可以右键单击并选择“发送到→MICROBIT（E）”将“hex”文件拷贝到micro：bit。

![](media/3eb47cbc010bcea42b28fafebd4b32ca.png)

也可以将“hex”文件直接拖入MICROBIT（E）磁盘中。

![](media/b2d4f28020d7d9bb7ac61fc3323b6f56.png)

![](media/b4f3602c0e192646f77b150e2acaf947.png)

将下载好的“hex”文件拷贝到micro：bit过程中，micro:bit主板背面的电源信号灯会闪烁，当拷贝完成后电源信号灯停止闪烁，保持长亮。

Step 4: 运行程序

代码程序上传micro: bit 主板后，通过micro USB线或外接电源供电给micro: bit 主板供电，micro: bit主板上5 x 5 LED点阵显示heartbeat的图案。

![](media/672bfb4d87b938fc586a849bff0229fe.png)

![](media/d61a26d2f2367f0378974832f679efe1.png)

micro USB线供电 外接电源供电（3V）

每次编程时，MICROBIT驱动器都会自动弹出并返回，但是你的hex文件将会消失。
micro:bit 只能接收hex文件，不会存储任何其他文件！

本小节向你展示了如何开始使用micro:bit，但是除了MakeCode之外，您还可以使用Python和基于文本的JavaScript来编写micro:bit。转到：<https://microbitorg/code/>查看不同的语言，或查看：<https://microbitorg/projects/>，了解你可能想要尝试的一些内容。

Makecode

，打开makecode在线版本

![](media/f7a321023281fc7221a9506b10f2eaaa.png)

Project”,出现“创建项目”对话框，在对话框中输入“heartbeat”，单击“创建”进入Makecode
编译器，Makecode 编译器如下:

![](media/28d226fea6fb6074c37309e9ee5ff026.png) 

在代码编辑区中，有两个固定的指令方块“当开机时”和“无限循环”。

上电或复位后，“当开机时”指令方块中的代码将仅执行一次；并且“无限循环”指令方块中的代码将循环执行。

快速下载

如前所述，如果使用makecode的Windows 10 App，则可以通过单击“下载”按钮将代码快速下载到micro:bit主板。

使用makecode的浏览器版本下载编写好的代码程序可能需要更多步骤。
但是，如果您将Google Chrome 用于Android，ChromeOS，Linux，macOS和Windows 10系统，则可以实现快速下载功能。

USB硬件设备。
我们将按照以下步骤完成micro：bit设备与网页的连接和配对。

配对装置

用micro USB线连接电脑和micro：bit。

单击“下载”后面的“”，然后单击“设备配对”。

![](media/ab19d85820cb53a685bd527d141a5f50.png)

然后继续单击“设备配对”按钮。

![](media/71c4b9e19eb7ce45d5330067d82c3829.png)![](media/f44115ad31df7258fa6fbc0eebaab216.png)

在弹出窗口中选中“设备”，然后单击“连接”按钮。
如果弹出窗口中没有设备，请参考以下内容：[https://makecodemicrobitorg/device/usb/webusb/troubleshoot](https://makecodemicrobitorg/device/usb/webusb/troubleshoot)

当然，如果你不想点击链接进入相关页面中查看，你也可以本教程的文件夹中直接阅读“Troubleshooting downloads with WebUSBpdf”。

https://microbitorg/guide/firmware/](https://microbitorg/guide/firmware/)

![](media/4873ac4ea99490bc30a7684822343ab5.png)

连接成功后，单击“下载”按钮，程序将直接下载到Micro:
bit，同时还会出现“下载成功!”提示语。

![](media/5cdddd9e43b14a0d6662590469c82c9d.png)

Makecode扩展

为了轻松使用turtle-bit，我们为turtle-bit制作了一个makecode扩展

turtle-bit
扩展

您可以通过以下方法添加turtle-bit扩展。

打开makecode，在任何项目下，先点击右上角的齿轮图标（设置），再点击扩展。

![](media/666fe797f5044a440e18475974eda4af.png)

https://githubcom/Keyes-team/pxt-turtle-bit](https://githubcom/mworkfun/pxt-turtle-bitgit)

然后单击搜索。
其中，可以在不输入链接的情况下直接添加蓝牙，Servo，neopixel等扩展库，只需在扩展首页上单击相应扩展库库的图标即可。

![](media/fee2d1bcda1f89f5d93b2b3dcc575860.png)

单击搜索结果turtle-bit以下载并安装。
该过程可能需要几秒钟。

![](media/ac27b51dc82dba8e4ed1b68af64282f6.png)

安装完成后，您可以在左侧找到K-bit扩展库（包括K_Bit、IrRemote、Neopixel）。

![](media/0db5c8b88b3b5ea45e74ceae02c6b1f3.png)

![](media/b4a95d2b84a70f40d96cded1f2b79eeb.png)

注意：

添加到项目中的扩展库仅对该项目有效，而不会出现在其他项目中。
因此，当您创建K-bit的新项目时，需要再次添加K-bit扩展库。

更新或删除turtle-bit扩展

如果您需要更新或删除turtle-bit扩展程序，请按照以下说明进行操作。

点击 "Js JavaScript" 按钮切换到文本代码。

![](media/81d2daffae58cd189aad4b06800f986b.png)

点击左边的 资源管理器

![](media/59355927a4be29f802e61752449bfd63.png)

在扩展列表中找到扩展。

单击垃圾箱图标以删除turtle-bit扩展程序（包括turtleBit、IrRemote、Neopixel）。
单击刷新图标以更新turtle-bit扩展程序。

![](media/342dbe2178781130c9c24985a93d1ec3.png)

资源和代码

该工具包的资源和代码可以在下面查看和下载：
https://panbaiducom/s/1LBZKBWd5IF8YSzgnhyZ3hA   
提取码：zusy

KE3021（KE3022）
Keyes套件 turtle-bit Micro bit 小乌龟 多功能 智能小车”的文件夹。
您可以将其放在电脑磁盘上的任何位置。

导入代码

我们为每个项目提供十六进制文件（项目文件）。
十六进制文件包含项目的所有内容，可以直接导入，您也可以手动完成项目代码。如果选择通过拖动代码块来完成代码，则可能需要添加必要的扩展库。

对于简单项目，建议通过拖动代码块来完成项目。

对于复杂的项目，建议通过导入十六进制代码文件来完成项目

接下来，我们以“
Heatbeat”项目为例，介绍如何加载代码。

打开Web版本的makecode。

![](media/3164be38e1fd17c715e467ea15939d29.png)

在弹出的对话框中，单击“导入文件”。

![](media/bb45f50bf206f01ef76e8de959f9eb2d.png)

![](media/1cff104dda5bf82aec0899d988c97d14.png)

/1Makecode
教程\micro：bit测试程序\81：闪烁的心\microbit-Heartbeat hex”。
然后点击“继续！”

![](media/6bd717c47746abb9415b086651f90ba7.png)

![](media/8db5f5f8652e71e5ae4af64f67e41a74.png)

除了上述将提供的项目代码程序文件直接导入到Makecode
编译器中的方法之外，也可以将提供的项目代码程序文件直接拖入到Makecode
编译器中，如下图所示：

![](media/ab535a6e61c8d887b516a13407922db1.png)

几秒钟后，项目成功加载。

![](media/5cdddd9e43b14a0d6662590469c82c9d.png)

注意：如果你的电脑系统是Windows7/8而不是Windows 10，则在Google Chrome中是无法进行设备配对，从而读取不了一些传感器/模块的数字信号或模拟信号，可是又需要读取相应的传感器/模块的数字信号或模拟信号，那怎么办呢？这里就可以使用CoolTerm软件来读取串口的，下面是CoolTerm安装方法。

CoolTerm安装方法：

1  现在，让我们来安装CoolTerm程序，这里我们是以PC     Window系统为例，选择下载安装CoolTerm Win，下载后解压并打开。（PC     Mac系统和PC Linux系统也类似）

![](media/97f831d38df9ee01dcfedac244bfe281.png)

![](media/e77548d01727e523e9e8c900d2fa962d.png)

（2）左键双击程序文件

![](media/5f29eed25fc16602cfc0716f047c2da1.png)

。（注意：必须保证micro:bit驱动已安装和micro:bit已用micro USB数据线连接到电脑上）

![](media/74fd81c83f0c0a26b4e299b93ce4ede4.png)

The functions of each button on the Toolbar are listed below:

![](media/70bebd79d7cd20336ae394c916500a28.png)

|![](media/2b728375ed2b8cd288c884e553418001.png)|Opens up a new Terminal|
|-|-|
|![](media/5f972f2eac5050ca0107416b2be067c2.png)|Opens a saved Connection|
|![](media/be6f8b560e0afc447f9c32b4474f633f.png)|Saves the current Connection to disk|
|![](media/52257d028694a313fc4eea4d9c2469d7.png)|Opens the 串行 Connection|
|![](media/6ad366842b18084553a142ab82a613cf.png)|Closes the 串行 Connection|
|![](media/8fa3ac342549d33b6c9aa5a9e4688bea.png)|Clears the Received Data|
|![](media/c8d1dd8c3356b4938e143de1022e5842.png)|Opens the Connection Options Dialog|
|![](media/36e13c266fd4b9723d9db40fe30cd203.png)|Displays the Terminal Data in Hexadecimal 顺序|
|![](media/b505c71c3344036730b1d67f0c62a354.png)|Displays the Help Window|

## 课程介绍

实验81至812是使用micro：bit主板自带的传感器模块和LED点阵。

### 1：闪烁的心

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

1  实验说明：

首先先来练习一个不需要其他辅助元件，只需要一块micro：bit主板和一根micro USB数据线的简单实验，让micro：bit显示“闪烁的心”，这是一个让micro：bit主板和PC机通信的实验，这也是一个入门实验，希望可以带领大家进入micro：bit的魔幻世界。

2  准备：

（1）通过micro USB线连接micro：bit主板和电脑。

（2）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

如果要一一拖动代码块，请单击“新建项目”。

![](media/226913d0639a68b9ff36d9b4767de937.png)

3  实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|bit测试程序完整版\81：闪烁的心|microbit-Heart beathex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“基础”模块，找到并拖出指令方块“显示图标”放入“无线循环”指令方块中，再复制指令方块“显示图标”1次也放入“无线循环”指令方块中并且点击“❤”图案后面的下拉三角形按钮选择“

![](media/04fdfc9060943954e7938bb1a741d626.png)

”图案

![](media/16001e58c56e0618ba8590216ea0a690.png)

完整的代码程序：

![](media/0abb62345db204d1eb6014aaeaa77ae4.png)

①“无限循环”指令方块仅运行一次以启动程序。

②在“当开机时”指令方块之内，程序循环运行。

③LED点阵显示“❤”图案

④LED点阵显示“![](media/04fdfc9060943954e7938bb1a741d626.png)”图案

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/32e69bb2fc03fc9fcdb472db5798b2a2.png)

4  实验结果:

按照之前的方式将代码下载到micro：bit，micro USB数据线不要拔下来，利用micro USB数据线上电，micro:bit主板上的LED点阵屏切换显示“❤”图案和“

![](media/04fdfc9060943954e7938bb1a741d626.png)

”图案，循环进行。

(如何下载？如何快速下载？)

如果存在下载问题，请断开micro USB线和Micro：bit，然后重新连接它们并重新打开Makecode，以尝试再次下载。

### 2：LED点阵中单个LED显示

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

1  实验说明：

Micro:bit的LED点阵共由25个发光二极管组成，5个一组，分别对应X和Y方向，形成一个5×5的矩阵，且每个发光二极管是放置在行线（X）和列线（Y）的交叉点上，我们可以通过设置坐标点来实现对25个LED中某一个LED的控制。例如，想要LED点阵中第1行第1个LED点亮，可以设置坐标点为（0，0）；第1行第3个LED点亮，可以设置坐标点为（2，0）；第1列第5个LED点亮，可以设置坐标点为（0，4）；第3列第2个LED点亮，可以设置坐标点为（2，1），依此类推。

![](media/a44f7625e2b1d61819bfc1985c321796.png)

2  准备：

（1）通过micro USB线连接micro：bit主板和电脑。

（2）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

如果要一一拖动代码块，请单击“新建项目”。   3 实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\82：LED点阵中单个LED显示|microbit-LED点阵中单个LED显示hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）先点击“Led”模块，再点击“Led”模块下的“更多”，找到并拖出指令方块“led
启用
fasle”放入“”指令方块中，点击“false”后面的下拉三角形按钮选择“true”。

![](media/30a68088f02c2ce629e2c47284b0b920.png)

2  点击“Led”模块，找到并拖出指令方块“切换x 0y     0”放入“无限循环”指令方块中，将“x 0”改成“x 1”。

![](media/96c862dd956ec88820e1d6a740c02c7c.png)

3  点击“基础”模块，找到并拖出指令方块“暂停 (ms)     100”放入代码块

![](media/96c862dd956ec88820e1d6a740c02c7c.png)

中，设置延时500毫秒。

![](media/c36063ad438a4be637ca98b0b6aa8a9d.png)

4  复制代码串

![](media/c36063ad438a4be637ca98b0b6aa8a9d.png)

1次放入“无限循环”指令方块中。

![](media/b26b50cd31e20535f2d13031de67e19b.png)

5  点击“Led”模块，找到并拖出指令方块“绘图x 0y     0”放入“无限循环”指令方块中，将“x 0 y 0”改成“x 3 y 4”。

![](media/8ff3a900b4339baed15f0ca54814ae3a.png)

（6）复制指令方块“暂停 (ms) 500”1次“无限循环”指令方块中。

![](media/819ce06f005063132e92e828ecfb4dba.png)

（7）点击“Led”模块，找到并拖出指令方块“取消绘图x 0 y 0”放入“无限循环”指令方块中，将“x 0 y 0”改成“x 3 y 4”，并复制指令方块“暂停 (ms) 500”1次放入“无限循环”指令方块中。

![](media/8152da905725af0e8f5bf4ad5ccd9652.png)

完整的代码程序：

![](media/b738570ca6603597110618ddbc75d786.png)

①“当开机时”指令方块仅运行一次以启动程序。

②打开LED点阵屏。

③在“无限循环”指令方块之内，程序循环运行。

④切换处于坐标x 1 y 0的LED亮度。

⑤延时时间500毫秒。

⑥切换处于坐标x 1 y 0的LED亮度。

⑦延时时间500毫秒。

⑧点亮处于坐标x3，y4的LED。

⑨延时时间500毫秒。

⑩熄灭处于坐标x3 y4的LED。

⑪延时时间500毫秒。

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/cdbb460770bef54d313bd6ee11761813.png)

4实验结果：

按照之前的方式将代码下载到micro：bit，micro USB数据线不要拔下来，利用micro USB数据线上电，我们就可以看到切换坐标点(1,0)的LED的亮灭状态，持续05s，再次切换坐标点(1,0)的LED的亮灭状态，持续05s；点亮坐标点(3,4)的LED，持续05s，熄灭坐标点(3,4)的LED，持续05s。循环进行。

4实验结果：

按照之前的方式将代码下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，我们就可以看到切换坐标点(1,0)的LED的亮灭状态，持续05s，再次切换坐标点(1,0)的LED的亮灭状态，持续05s；点亮坐标点(3,4)的LED，持续05s，熄灭坐标点(3,4)的LED，持续05s。循环进行。

### 3：5 x 5 LED点阵图案显示

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

1  实验说明：

点阵在我们生活中很常见，很多都有用到它，比如LED广告显示屏，电梯显示楼层，公交车报站等等。

micro：bit主板的LED点阵共由25个发光二极管组成，上一课我们已经讲过通过设置坐标点来实现对LED点阵的25个LED中的某个LED的控制，这样可以通过设置多个坐标点控制多个LED的亮灭使得LED点阵能够显示图案、数字、字符串。我们也可以在特定代码中通过点击
LED点阵的灰白色小正方形点亮
LED点阵对应的LED来实现LED点阵显示图案、数字、字符串。除了上述方法还可以使用自定义图案使LED点阵显示图案。

2  准备：

（1）通过micro USB线连接micro：bit主板和电脑。

（2）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

如果要一一拖动代码块，请单击“新建项目”。

3  实验代码：

代码1：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit 测试程序完整版\83：5 x 5 LED点阵图案显示\microbit-5 x 5 LED点阵图案显示-1|microbit-Code-1hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）先点击“Led”模块，再点击“Led”模块下的“更多”，找到并拖出指令方块“led
启用
fasle”放入“当开机时”指令方块中，点击“false”后面的下拉三角形按钮选择“true”。

![](media/30a68088f02c2ce629e2c47284b0b920.png)

（2）点击“Led”模块，找到并拖出指令方块“绘图 x 0 y 0”放入“无限循环”指令方块中，复制“绘图 x 0 y 0”指令方块8次并且放入“无限循环”指令方块中，将“x 0”y 0”分别改成“x 2”y 0”、“x 2”y 1”、“x 2”y 2”、“x 2”y 3”、“x 2”y 4”、“x 1”y 3”“x 0”y 2”、“x 3”y 3”、“x 4”y 2”。

![](media/6524556e089162eb33a94e7cb5460286.png)

完整的代码程序：

![](media/2211e578fd172f9c7fb76fbe0f4407f2.png)

①“当开机时”指令方块仅运行一次以启动程序。

②打开LED点阵屏。

③在“无限循环”指令方块之内，程序循环运行。

④点亮处于坐标x 2，y 0的LED。

⑤点亮处于坐标x 2，y 1的LED。

⑥点亮处于坐标x 2，y 2的LED。

⑦点亮处于坐标x 2，y 3的LED。

⑧点亮处于坐标x 2，y 4的LED。

⑨点亮处于坐标x 1，y 3的LED。

⑩点亮处于坐标x 0，y 2的LED。

⑪点亮处于坐标x 3，y 3的LED。

⑫点亮处于坐标x 4，y 2的LED。

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/51c87937aa1d386037ec5921cdab7259.png)

代码2：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\micro：bit测试程序\83：5×5 LED点阵图案显示\5 x 5 LED点阵图案显示-2|microbit-5 x 5 LED点阵图案显示-2hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

1  点击“基础”模块，找到并拖出指令方块“显示数字”放入“当开机时”指令方块中，并且复制指令方块“显示数字”4次，将数字0分别改成1、2、3、4、5。

![](media/072fd5ff9b200606aca2f184774d4ff9.png)

2  从“基础”模块，拖出指令方块“显示LED”放入“当开机时”指令方块中，点击灰蓝色小方框变白色，点亮LED点阵对应的LED，形成“↓”图案。

![](media/38372a730d72dfcc201703d3bcdebe1b.png)

3  从“基础”模块，拖出指令方块“显示字符串Hello!”放入“当开机时”指令方块中。

![](media/6e8a6572b0f77aec96c1e6ded08c90ab.png)

4  从“基础”模块，拖出指令方块“显示图标”放入“当开机时”指令方块中。

![](media/fe14b774db3a601a7d1f467e7e5b643f.png)

5  点击“基础”模块，找到并拖出指令方块“显示箭头北”放入“当开机时”指令方块中，复制指令方块“显示箭头北”3次，点击“北”后面的下拉三角形按钮分别选择“东北”、“东南”、“西南”、“西北”。

![](media/441228dc6a6722d350b7b8438d0da428.png)

6  先点击“基础”模块，找到并拖出指令方块“清空屏幕”放入“当开机时”指令方块中，点击“基础”模块，找到并拖出指令方块“暂停
    (ms) 100”放入“当开机时”指令方块中，设置延时500毫秒。

![](media/8697fca7b6d2ca4f8afe2dd0a458ba08.png)

完整的代码程序：

![](media/8697fca7b6d2ca4f8afe2dd0a458ba08.png)

①“当开机时”指令方块仅运行一次以启动程序。

②在LED点阵显示数字1。

③在LED点阵显示数字2。

④在LED点阵显示数字3。

⑤在LED点阵显示数字4。

⑥在LED点阵显示数字5。

⑦在LED点阵点亮对应的LED，显示“↓”图案。

⑧在LED点阵滚动显示字符串“Hello!”。

⑨在LED点阵点亮对应的LED显示“❤”图案。

⑩在LED点阵点亮对应的LED显示“东北”方向箭头图案。

⑪在LED点阵点亮对应的LED显示“东南”方向箭头图案。

⑫在LED点阵点亮对应的LED显示“西南”方向箭头图案。

⑬在LED点阵点亮对应的LED显示“西北”方向箭头图案。

⑭清空屏幕。

⑮延时500毫秒。

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/2d8ee340097230ecc8b62e176faaaa3e.png)

4  实验结果：

按照之前的方式将代码1下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，我们就可以看到micro：bit主板的5×5 LED点阵显示“向下”图案

![](media/d4e278da768e447ed344d581e671f57a.png)

；

用同样的方法将代码2下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，我们就可以看到micro：bit主板的5×5 LED点阵开始显示数字1、2、3、4、5，然后循环显示“向下”图案

![](media/d4e278da768e447ed344d581e671f57a.png)和“西北”方向图案![](media/2a45fca9d836ce38674c347c70c81e02.png)

。

([How to download?](#A11) [How to quick download?](#快速下载))

### 4：micro：bit的可编程按键

![](media/06be84fb11b1fd07cd0cbb392132b903.png)

1  实验说明：

![](media/13f8f274b4c420c973de29619432bd6e.png)按键可以控制电路的通断，把按键接入电路中，不按下按键的时候电路是断开的，一按下按键电路就通啦，但是松开之后就又断了。可是为什么按下才通电呢？这得从按键的内部构造说起。没按下之前，电流从按键的一端过不去另一端，按键的两端就像两座山，中间隔着一条河，我们在这座山过不去另一座山；按下的时候，按键内部的金属片把两边连接起来让电流通过，就像搭了一座桥，把两座山连接起来。

按键内部结构如图：

![](media/d2a204e61c768f18924150db58aee093.png)

，未按下按键之前，1、2就是导通的，3、4也是导通的，但是1、3或1、4或2、3或2、4是断开（不通）的；只有按下按键时，1、3或1、4或2、3或2、4才是导通的。

micro：bit主板有三个按键，反面的是复位按钮，正面的是两个可编程按键，通过对两个可编程按键组合可以有三种组合，作为输入元件。我们结合上节课的LED点阵，一起来学习按键吧。我们做一个按键三连，分别按A、B和AB同时按，对应显示屏分别显示A、B和AB。

2  准备：

（1）通过micro USB线连接micro：bit主板和电脑。

（2）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

如果要一一拖动代码块，请单击“新建项目”。

3  实验代码：

代码1：

按下micro：bit上的按键，让micro：bit上
LED点阵显示字符串。

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\84：micro：bit的可编程按键\Code-1|microbit-micro：bit的可编程按键-1hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）先删除指令方块“当开机时”和“无限循环”，然后点击“输入”模块，找到并拖出“当按钮A被按下时”指令方块。

（2）点击“基础”模块，找到并拖出指令方块“显示数字”放入“当按钮A被按下时”指令方块中，将“Hello!”改成“A”。

![](media/09fe88931df31dc9215a4dc82bf6ded4.png)

（3）复制代码串

![](media/09fe88931df31dc9215a4dc82bf6ded4.png)

1次，点击“A”后面的下拉三角形按钮选择“B”，并将字符“A”改成“B”。

![](media/36b0b98cd3caa7f9fa33c57598113782.png)

（4）再复制代码串

![](media/09fe88931df31dc9215a4dc82bf6ded4.png)

1次，点击“A”后面的下拉三角形按钮选择“A+B”，并将字符“A”改成“AB”。

![](media/9f11601cb7e7c570c2aa2182d76204c3.png)

完整的代码程序：

![](media/6246ee12aecfc385d0600b6cbd47987f.png)

①按下micro: bit主板上的按键A。

②LED点阵显示字符“A”。

③按下micro: bit主板上的按键B。

④LED点阵显示字符“B”。

⑤同时按下micro: bit主板上的按键A和B。

⑥LED点阵显示字符“AB”

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/50c59105d5a2409eea809e6ce73cf740.png)

代码2：

按下micro：bit主板上正面按键A，条形图高度值增加5，表现为LED点阵亮的行数增加；按下正面按键B，减少条形图高度，表现为LED点阵亮的行数减少。根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\84：micro：bit的可编程按键\Code-2|microbit-micro:bit的可编程按键-2hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）先点击“Led”模块，再点击“Led”模块下的“更多”，找到并拖出指令方块“LED启用false”放入“当开机时”指令方块中，点击“false”后面的下拉三角形按钮选择“true”。

![](media/5ad6b9ff6d3457d88ab5fef92ed4c2fa.png)

2  点击“输入”模块，找到并拖出“当按钮A被按下时”指令方块。

3  点击“变量”模块，找到并拖出“以1为幅度更改item”指令方块放入“当按钮A被按下时”指令方块中。将数字1改成5。

![](media/a99f4f853f49d3215114ef2455d74679.png)

（5）复制代码串

![](media/a99f4f853f49d3215114ef2455d74679.png)

1次，先点击“A”后面的下拉三角形按钮选择“B”，再将数字5改成-5。

![](media/57acf173bbf3838fdea50c8aa25620ea.png)

4  点击“Led”模块，找到并拖出指令方块“绘制条图形”放入“无限循环”指令方块中，从“变量”模块中拖出变量指令方块“item”放入of后面的0处，再把to后面的0改成25。

![](media/4f4d11d490a9b0fa49402f20ffaf0412.png)

5  ”右侧的数字0改成25；最后从“变量”模块中拖出变量指令方块“将inem设为”放入“如果为then则”指令方块中，将数字0改成25。

![](media/d2cf1cde7961ae241c1521d754955e99.png)

（7）复制代码串1次放入

![](media/d2cf1cde7961ae241c1521d754955e99.png)

”改成“\<”，数字25都改成0。

![](media/5e406f9a3e5c02d3bd3f8b62505c4829.png)

完整的代码程序：

![](media/d1365367ca82758fbffd66038489b4d1.png)

①“当开机时”指令方块仅运行一次以启动程序。

②打开LED点阵屏。

③设置变量“item”的初始值为0。

④按下micro: bit主板上的按键A。

⑤以5为幅度更改变量值。

⑥按下micro: bit主板上的按键B。

⑦以 -5为幅度更改变量值。

⑧在“无限循环”指令方块之内，程序循环运行。

⑨点亮LED点阵中LED绘制条形图，最高点亮25个LED。

⑩当变量“item”值大于25是正确的，就运行then下的程序。

⑪将变量“item”值设置为25。

⑫当变量“item”值小于0是正确的，就运行then下的程序。

⑬将变量“item”值设置为0。

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/99dd466d69b41baa255c78f15dbb8efa.png)

4  实验结果：

按照之前的方式将代码1下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，按下micro：bit主板上正面按键A，我们可以看到5×5 LED点阵显示字符“A”；按下micro：bit主板上正面按键B，我们可以看到5×5 LED点阵显示字符“B”，同时按下micro：bit主板上正面按键A和B，我们就可以看到5×5 LED点阵显示字符“AB”。

用同样的方式将代码2下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，按下micro：bit主板上正面按键A，条形图高度值增加5，表现为LED点阵亮的行数增加；按下正面按键B，减少条形图高度，表现为LED点阵亮的行数减少。

### 5：microbit学习测温度

1  实验说明：

micro:bit主板实际上并不带温度传感器，而是采用NFR51822芯片内置的温度传感器进行温度检测，所以检测的温度更接近芯片的温度，可能与周围环境温度存在一定的误差。在这一课程中，我们先利用该传感器测试当前环境中的温度，并将测试结果在显示数据(设备)中显示，再通过设置该传感器检测的温度范围来控制LED点阵显示不同的图案。

注意：micro:bit主板的温度传感器在这里：

![](media/206c8ec1c3f11d2de8d0f42fdf5b6b47.png)

2  准备：

（1）通过micro USB线连接micro：bit主板和电脑。

（2）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

如果要一一拖动代码块，请单击“新建项目”。

3  实验代码：

代码1：

Micro:bit检测温度

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\85：microbit学习测温度\Code-1|microbit-micro:bit学习测温度-1hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“高级”下的“串行”模块，找到并拖出指令方块“串行
重定向到 USB”放入“当开机时”指令方块中。

![](media/1915e53fe6802a7fd3063810500587df.png)

（2）再点击“串行”模块，找到并拖出“串行写入数值
x=0”指令方块放入“无限循环”指令方块中。

![](media/30e319d1bd59080bad299ffbaab09d32.png)

（3）点击“输入”模块，找到并拖出指令方块“温度(℃)”放入=后面的数字0处，将x改成Temperature。

![](media/d7b5eecd80630f1c7f778b0cf7e802bb.png)

（4）点击“基础”模块，找到并拖出指令方块“暂停 (ms) 100”放入“无限循环”指令方块中，设置延时500毫秒。

![](media/53dcb9f9aa194af0292a6378d14f76e9.png)

完整的代码程序：

![](media/5e21b15aa75763aa5953b373b57f4db4.png)

①“当开机时”指令方块仅运行一次以启动程序。

②串行 重定向到USB。

③在“无限循环”指令方块之内，程序循环运行。

④串行写入数值Temperature=温度（℃）。

⑤延时时间500毫秒。

点击micro:
bit在线编程工具的“jsJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/a257f37eb9ecce6a353a7f7beec8261d.png)

按照之前的方式将代码1下载至micro: bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，接下来点击显示数据(设备)按钮：

![](media/0d3198e0cb5460c9820bc2f016c0d7c1.png)

将显示温度数据，如下图所示：

![](media/6177222069a9583f2d8314d592fdb916.png)

在以上的测试中，将Micro:bit的NFR51822芯片接触，一段时间后，温度开始慢慢上升，此时室温约为35摄氏度，与水杯外侧接触后，温度上升到37摄氏度，符合预期。

如果你的电脑系统是Windows7/8而不是Windows 10，则在Google Chrome中是不能进行设备配对，从而读取不了相应的数字信号或模拟信号，可是又需要读取相应的传感器/模块的数字信号或模拟信号，那怎么办呢？这里就可以使用CoolTerm软件来读取串口的。

打开CoolTerm，点击Options，选择串行Port，设置COM口和波特率，波特率设置为115200（经过测试，micro:bit的USB串口通讯波特率是115200），点击OK后，最后点击Connect。CoolTerm的串口监视器显示当前环境中的温度值，如下图：

![](media/b3a18bca1b2a7b5337470735e5a0c5aa.png)

![](media/f78128c148de3862a3fe10d86f063e22.png)

![](media/13238e98c31d620f4ffd7742dd71c78d.png)

![](media/9c88bb875124738a55e5e0fd5bf957ca.png)

代码2：

通过温度控制mirco：bit上点阵显示不同图案（注意：代码程序中的温度值可以根据当地环境适当的调整）

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\85：microbit学习测温度\Code-2|microbit-micro:bit学习测温度-2hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）先点击“Led”模块，再点击“Led”模块下的“更多”，找到并拖出指令方块“led
启用
fasle”放入“当开机时”指令方块中，点击“false”后面的下拉三角形按钮选择“true”。

![](media/5ad6b9ff6d3457d88ab5fef92ed4c2fa.png)

2  点击“逻辑”模块，先找到并拖出指令方块“如果为then否则”放入“无限循环”指令方块中，再拖出“=”方块放入“true”方框中。

![](media/31f5a1b70af6d5219a994dece9f6b9d9.png)

3  点击“输入”模块，找到并拖出指令方块“温度(℃)”放入“=”的左侧，点击“=”后面的下拉三角形按钮选择“≥”，再将“≥”右侧的0改成35。

![](media/4949278fb3c82e2e312cc5df6112a71b.png)

4  点击“基础”模块，找到并拖出指令方块“显示图标”放入如果为下面，又复制指令方块“显示图标”1次放入否则下面并点击“❤”图案后面的下拉三角形按钮选择“

![](media/9fa58029eb504582ee5a915f591ea583.png)

”图案。

![](media/bfdd150cb4822ad71f89af0d138bbc0d.png)

完整的代码程序：

![](media/3682d6188821c84b175e617a15b2609a.png)

①“当开机时”指令方块仅运行一次以启动程序。

②打开LED点阵屏。

③在“无限循环”指令方块之内，程序循环运行。

④当温度传感器检测到的外界温度≥35℃是正确的，就运行如果为下的程序。

⑤LED点阵显示“❤”图案

⑥当温度传感器检测到的外界温度≥35℃是不正确的，就运行否则下的程序。

⑦LED点阵显示“![](media/9fa58029eb504582ee5a915f591ea583.png)”图案

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/3aab1302cef32173d746b97ac7ed5325.png)

4  实验结果：

按照之前的方式将代码2下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，外界环境中的温度小于35℃时，micro：bit主板的5×5LED点阵中显示图案

![](media/4b1765e12b413dc5d562f2a16d32392f.png)，用手按住micro：bit主板的温度传感器，温度大于等于35℃时，5×5LED点阵中显示图案![](media/f2705fbc4886efcfaac96589ca255f66.png)

。

### 6：micro:bit的地磁传感器（磁力计/指南针）

![](media/24c31bb0174e2ac672203e5c36c6875e.png)

1  实验说明：

本实验主要介绍micro:bit地磁传感器的使用，地磁传感器除了检测地磁场强度外，还能当作指南针确定方向，同时也是航姿参考系统(AHRS)的重要组成部分。micro:bit主板采用的是FreescaleMAG3110三轴磁力计，I2C接口与外部通信，量程为±1000µT，最大数据更新速率为80Hz，与加速计结合使用可在任意姿态下计算方位。在micro:bit中，磁力检测、指南针积木块均用到了磁力计模块，本实验中，将先介绍指南针，然后查看磁力计原始数据。常见的指南针主要部件是一根磁针，在地磁场的作用下可以转动并指向北方（指南针其实是指北的），用来辨别方向。micro:bit内部的一个地磁传感器（磁力计、指南针），我们可以读取这个磁力计的读数来判断方位，得到相对于北磁极的数值。返回值是0到360之间的数值，在磁力计首次开始工作（带到新位置后）时系统会自动要求我们对micro:bit主板校准，正确的校准方式是旋转micro:bit主板。需要注意的是，附近要是有金属物件可能会影响读数和校准准确性。

一些地球物理学家们确信，地球磁场是因为固态铁质内核被液态金属“海”所包围而形成的。磁力计指向的北是地磁北极，目前地磁南北极位置位于地理南北极地区，但并不与地球的南北极点完全重合，磁北极和真正的地理北极之间存在一个磁偏角。需要指出的是磁极位置是一直在变化的，历史上还出现过地磁逆转的情况。

我们称呼上的地磁南极，其实是物理上的磁北极，而地磁北极是物理上的磁南极，磁力线从磁北极出射，从磁南极进入，即地磁场从地理南极出来从地理北极进去。地磁南北级与地理南北级基本相反，但不在同一条线上也就是说地磁南极在地理北极附近，地磁北极在地理南极附近，地理南北极的连线和地磁南北级的连线构成磁偏角，即地磁北极（指南针指的方向）与地理北极间的夹角。

2  准备：

（1）通过micro USB线连接micro：bit主板和电脑。

（2）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

如果要一一拖动代码块，请单击“新建项目”。

3  实验代码：

代码1：

按下按键A的时候，可以在屏幕上显示磁力计的读数。

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\86：microbit的地磁传感器（磁力计指南针）\Code-1|microbit-Code-1hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

1  先点击“输入”模块，再点击“输入”模块下的“更多”，找到并拖出指令方块“校准指南针”放入“当开机时”指令方块中。

![](media/b08bfbd72a4583c881f9d442684ee1e7.png)

A
被按下时”指令方块。

（3）点击“基础”模块，找到并拖出指令方块“显示数字”放入“当按扭
A
被按下时”指令方块中，再点击“输入”模块，找到并拖出指令方块“指南针朝度(℃)”放入指令方块“显示数字”中。

![](media/31b1dd0214b5a24da40fe7fca186f18a.png)

完整的代码程序：

![](media/33b23559953cc4c7eb1f802605c6492b.png)

①“当开机时”指令方块仅运行一次以启动程序。

②校准指南针。

③按下micro:bit主板上的按键A。

④LED点阵显示指南针朝向角度。

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/f9a5d93dc6aa46fa7adf1316d41e4435.png)

代码说明：首先必须对micro:bit进行校准，因为每个地方地磁场不同，对结果有比较大的的影响，如果是第一次使用指南针，micro:bit会自动提示需要校准。

按照之前的方式将代码1下载至micro: bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，按下micro:bit主板上正面按键A时，micro:bit主板首先提示校准，屏幕(LED点阵)提示:“TILT TO FILL SCREEN”,然后进入校准界面，校准方式为：旋转micro:bit主板，使得屏幕(LED点阵)画一个封闭的正方形（25个LED都点亮），如下图所示：

![](media/acf3b8c0dee027d9e555fc708831f874.jpg)

当封闭的正方形画好后，会显示一个“笑脸”图案

![](media/2c899003f048c2fa8418cad7144574a7.png)

，表示校准完成。

校准完成后，当按下按键A的时候，直接在屏幕上显示磁力计读数，北、东、南、西对应0°、90°、180°、270°。

代码2：

朝不同的方向旋转磁力计，LED点阵显示对应的方向图案。

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\86：microbit的地磁传感器（磁力计指南针）\Code-2|microbit-Code-2hex|

![](media/99b7430cb5e7695fcd0a9e294f10470a.png)

这个模块意思是，在循环中，不断读取磁力计的读数，并根据读数范围判断所指方向，让箭头指向当前的地磁北方。

![](media/d1a4e9f62bdf690ba809ae35c347b233.png)

如图所示，如果读数在2925和3375之间，就让显示屏显示一个指向右上方的箭头，由于代码里不能输入05，所以取的判断数值是293和338。之后再加入其它逻辑判断条件，就得到了完整的代码。

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）先点击“输入”模块，再点击“输入”模块下的“更多”，找到并拖出指令方块“校准指南针”放入“当开机时”指令方块中。

![](media/b08bfbd72a4583c881f9d442684ee1e7.png)

2  先点击“变量”模块，找到并拖出“将 X     设为0”放入无限循环指令模块中

![](media/082ba63b44114da2f5a4ed308fc5e4bf.png)

（3）点击“输入”模块，找到并拖出指令方块“指南针朝度(℃)”放入指令方块“将
X 设为0”中。

![](media/7f2b98f14d516f5b2c5ea906fe578c20.png)

（4）点击“逻辑”模块，找到并拖出指令方块“如果为then则”放入“无限循环”指令方块中，点击

![](media/bf972b006ad6d05686352c4785e54994.png)

标志6次。

x\<203
”、“x≥203 and x\<248 ”、“x≥248 and x\<293 ”。

![](media/dac374102ec2890cdc1ec6c9ac2c6eee.png)

（6）点击“基础”模块，找到并拖出指令方块“显示LED”放入第一个
与 下面，点击指令方块“显示
led”上灰蓝色小方框变成白色组成“

![](media/eab025b80ef24f1d5351bd3e06221bad.png)

”图案。

![](media/18b2ff873c9d02f932ccca8759edf4cf.png)

（7）再从“基础”模块，找到并拖出指令方块“显示LED”7次分别放入第二个、第三个、第四个、第五个、第六个then下面和else下面，对应的分别点击指令方块“x leds”上灰蓝色小方框变成白色组成“

![](media/4c73992fa4dfc6a2735b49ea8f000ed6.png)”图案、“![](media/d16918782eb53d860d91e4a3a115168c.png)

”图案。

完整的代码程序：

![](media/7042fa2032f4d71a8837f0437dbe09d6.png)

①“当开机时”指令方块仅运行一次以启动程序。

②校准指南针。

③在“无限循环”指令方块之内，程序循环运行。

④将指南针朝向的角度存储到变量x中。

⑤当293≤x\<338成立时，就运行与下的程序。

⑥LED点阵显示“![](media/eab025b80ef24f1d5351bd3e06221bad.png)”图案

⑦当23≤x\<68成立时，就运行与下的程序。

⑧LED点阵显示“![](media/4c73992fa4dfc6a2735b49ea8f000ed6.png)”图案

![](media/08c6ef5beeaa82779aa3a4ec675cb2a3.png)

⑨当68≤x\<113成立时，就运行与下的程序。

⑩LED点阵显示“![](media/0771b8fd797a3e945a01ec1525ba4a9d.png)”图案

⑪当113≤x\<158成立时，就运行与下的程序。

⑫LED点阵显示“![](media/41eb716a282d52483e8467704613d034.png)”图案

⑬当158≤x\<203成立时，就运行与下的程序。

⑭LED点阵显示“![](media/2cae18294b329c10ecdefd768d6954e0.png)”图案

![](media/dcdce943d4a0074f50b27770ce6b2010.png)

⑮当203≤x\<248成立时，就运行与下的程序。

⑯LED点阵显示“![](media/14b893d1a7157d72209b975d0df8d890.png)”图案

⑰当248≤x\<293成立时，就运行与下的程序。

⑱LED点阵显示“![](media/c362406f55115926523a0f60e16828b6.png)”图案

⑲当以上的x范围都不成立时，就运行 否则 下的程序。

⑳LED点阵显示“![](media/d16918782eb53d860d91e4a3a115168c.png)”图案

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/c38858ca8e12ce4ca59759cff04ac2d7.png)

![](media/1d4fdac44bf4e1629145fac97f627c24.png)

4  实验结果：

按照之前的方式将代码2下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，提示校准（校准方法请参考:上面代码1部分），校准完成后，旋转移动micro:bit主板，可以看到micro:bit主板上LED点阵显示方向图案。

### 7：micro: bit的加速度传感器（加速度计）

![](media/24c31bb0174e2ac672203e5c36c6875e.png)

1  实验说明：

micro:bit主板内置有Freescale MMA8653FC三轴加速度传感器（加速度计），I2C接口与外部通信，10位ADC精度，可设置量程为±2g、±4g,、±8g，数据最大更新速率为800Hz。

当micro:bit处于静止或匀速运动状态时，加速度计仅检测到重力加速度；将micro:bit轻微甩动，加速度计检测到甩动的加速度远小于重力加速度，可忽略不计。因此，在使用micro:bit过程中，主要是检测当姿态变化时，重力加速度在x、y、z轴上的变化，并在此基础上应用。

本实验，将介绍加速度传感器（加速度计）对几个特殊姿态的检测，之后来查看加速度传感器输出的三轴原始数据。

2  准备：

（1）通过micro USB线连接micro：bit主板和电脑。

（2）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

如果要一一拖动代码块，请单击“新建项目”。

3  实验代码：

代码1：

对micro：bit不同的操作，LED点阵显示对应的数字。

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit 测试程序完整版\87：micro bit的加速度传感器（加速度计）\Code-1|microbit-Code-1hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“输入”模块，找到并拖出指令方块“当震动”。

（2）点击“基础”模块，找到并拖出指令方块“显示数字”
放入指令方块“当震动”中，将数字0改成1。

![](media/09131188cfd5d2de777d98617247b130.png)

（3）复制代码串

![](media/09131188cfd5d2de777d98617247b130.png)

7次，先后分别点击“震动”后面的下拉三角形按钮选择“logo up”、“logo down”、“screen up”、“screen down”、“tilt left”、“tilt right”、“free fall”，再将数字1分别对应的改成2、3、4、5、6、7、8。

完整的代码程序：

![](media/f950dc88b68179018b60f9870154a7c4.png)

①振动microbit主板。

②LED点阵显示数字1。

③microbit主板的徽标朝上。

④LED点阵显示数字2。

⑤microbit主板的徽标朝下。

⑥LED点阵显示数字3。

⑦microbit主板屏幕朝上。

⑧LED点阵显示数字4。

⑨microbit主板屏幕朝下。

⑩LED点阵显示数字5。

⑪microbit主板向左倾斜。

⑫LED点阵显示数字6。

⑬microbit主板向右倾斜。

⑭LED点阵显示数字7。

⑮microbit主板自由落体。

⑯LED点阵显示数字8。

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/093bcf4a15c159fe541c5b2076df319d.png)

代码2：

检测加速度在X轴，Y轴，Z轴的不同的值

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/Makecode代码/87：micro:bit的加速度传感器（加速度计）/micro:bit的加速度传感器（加速度计）-2|microbit-micro:bit的加速度传感器（加速度计）-2hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

(1)点击“高级”下的“串行”模块，找到并拖出指令方块“串行
重定向到USB”放入“当开机时”指令方块中。

![](media/6187584e585ae7dd1e9855a5f1b90956.png)

(2)再从“串行”模块，找到并拖出指令方块“串行写入数值
x =0”放入指令方块“无限循环”中。

![](media/bfefae977b13d8ad03f019f09ce44800.png)

x
=0”中0处，并将“=”左侧的“x”改成大写的“X”。

![](media/c9be35ca55f0e3ac75d1df68d67ae24f.png)

(4)点击“基础”模块，找到并拖出指令方块“暂停(ms) 100”放入“无限循环”指令方块中，设置延时100毫秒。

![](media/95c316999efbb55ac22382a00ba28381.png)

(5)复制代码串

![](media/95c316999efbb55ac22382a00ba28381.png)

2次放入“无限循环”指令方块中，将先“=”左侧的“X”分别改成“Y”、“Z”，再分别对应的点击“x”后面的下拉三角形按钮选择“y”、“z”。

![](media/e01c5db506a5d2838d8907ec1b1a72d5.png)

完整的代码程序：

![](media/7114c02d1d0b5d2f9f5118e772f45c23.png)

①“当开机时”指令方块仅运行一次以启动程序。

②串行重定向到USB。

③在“无限循环”指令方块之内，程序循环运行。

④串行写入数值X=x轴的加数度值（mg）

⑤延时时间100毫秒。

⑥串行写入数值Y=y轴的加数度值（mg）

⑦延时时间100毫秒

⑧串行写入数值Z=z轴的加数度值（mg）

⑨延时时间100毫秒

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/287f1004bbcaf169d90e74fff054cbca.png)

按照之前的方式将代码1下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，打开数据显示(设备)按钮。

![](media/821a64a53c3a9709ff556e71b070f4dd.png)

首先，查阅MMA8653FC数据手册，以及micro:bit的硬件原理图得知，micro:bit加速度计坐标如下图所示：

![](media/c50e4615dc4ba700ecaf925c7961faab.png)

显示出如下界面：分别显示了加速度在X轴，Y轴，Z轴的分解，以及加速度的合成(重力加速度及其它外力作用的加速度合成)，如下图:
![](media/ded4e05f2b15d694e2061159628574dc.png)

实验中，先将加速计Z轴朝上，然后再将加速计X轴朝上，最后将加速计Z轴朝上，可得数据变化如上图所示

如果你的电脑系统是Windows7/8而不是Windows 10，则在Google Chrome中是不能进行设备配对，从而读取不了相应的数字信号或模拟信号，可是又需要读取相应的传感器/模块的数字信号或模拟信号，那怎么办呢？这里就可以使用CoolTerm软件来读取串口的。

打开CoolTerm，点击Options，选择串行Port，设置COM口和波特率，波特率设置为115200（经过测试，micro:bit的USB串口通讯波特率是115200），点击OK后，最后点击Connect。CoolTerm串口监视器分别显示了加速度在X轴、Y轴、Z轴的分解，以及加速度的合成(重力加速度及其它外力作用的加速度合成)，先将加速计Z轴朝上，然后再将加速计X轴朝上，最后将加速计Z轴朝上,可得数据变化如下图：

![](media/b4f4201cccf6ac0dadffb952b7596895.png)

4  实验结果：

按照之前的方式将代码1下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，将micro:bit主板晃动，则可见micro:bit显示数字1（表明只要有晃动，无论朝哪个方向晃动，该条件都将满足）。

([How to download?](#A01) [How to quick download?](#快速下载))

徽标指的是micro:bit主板上的micro:bit这几个字以及Logo，徽标朝上示意图如下所示：

![](media/62838494aee9e0f740d63bcaeb82d4aa.jpg)

由图可得，当徽标朝上的时候，能够显示数字2。

同理，徽标朝下指的是micro:bit主板上的micro:bit这几个字以及Logo朝下，徽标朝下示意图如下所示：

![](media/07bac88aebdf047b8afd6e6e141cbda5.jpg)

由图可得，当徽标朝下的时候,显示的是数字3(倒立的3)。

当屏幕朝上（指的是LED点阵朝上）时，显示数字4。

同理，当屏幕朝下（指的是LED点阵朝下）时，显示数字5。

当向左倾斜时，如下图为micro:bit向左倾斜示意图:

注意micro:bit向左倾斜为正面朝上，徽标朝前，然后再往左边倾斜，当向左倾斜时，micro:bit显示数字6。

![](media/c872f4f1c33068a7053502bd9ec4994c.jpg)

当向右倾斜时，如下图为micro:bit向右倾斜的示意图:

注意micro:bit向右倾斜为正面朝上，徽标朝前，然后再往右边倾斜，当向右倾斜时，micro:bit显示数字7。

![](media/a4401bc671f471f27c4c6b309c4c7061.jpg)

当不小心碰到micro:bit主板使其从桌面掉落，则为做自由落体运动，此时，满足自由落体的条件，将显示数字8。（注意：此方法操作时，很容易把micro:bit主板摔坏，不建议操作）

注意：（3g、6g、8g，
如果需要满足此条件，则需要达到3倍，6倍，8倍重力加速度甩动micro：bit。如果你们有兴趣的话，这部分代码可以自己添加）

### 8：micro:bit的光照强度检测

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

1  实验说明：

本实验将介绍micro:bit对外界光照强度的检测，由于micro:bit并不自带光敏传感器，对外界光照强度的检测是通过LED矩阵进行的，LED矩阵被用来感知周围的光，并反复地将LED转换成输入，并采样电压衰减时间。这样检测出来的光照强度是一个相对值。

2  准备：

（1）通过micro USB线连接micro：bit主板和电脑。

（2）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

如果要一一拖动代码块，请单击“新建项目”。

3  实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\88：microbit的光照强度检测microbit的光照强度检测|microbit-micro：bit的光照强度检测hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“高级”下的“串行”模块，找到并拖出指令方块“串行写入数值
USB”放入“当开机时”指令方块中。

![](media/6187584e585ae7dd1e9855a5f1b90956.png)

x
=0”放入指令方块“无限循环”中。

![](media/bfefae977b13d8ad03f019f09ce44800.png)

（3）点击“输入”模块，找到并拖出指令方块“亮度级别”放入指令方块“
串行写入x =0”中0处，并将“=”左侧的“x”改成大写的“Light intensity”。

![](media/dbbac74f78667f34537daa85bad2c04d.png)

（4）点击“基础”模块，找到并拖出指令方块“暂停 (ms) 100”放入“无限循环”指令方块中，设置延时100毫秒。

![](media/17ca110943710449a4d327b75caadab6.png)

完整的代码程序：

![](media/ebd01529974676325843f65c5fb916c2.png)

①“当开机时”指令方块仅运行一次以启动程序。

②串行重定向到USB。

③在“无限循环”指令方块之内，程序循环运行。

④串行写入数值Light intensity=光照强度。

⑤延时时间100毫秒。

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/0a88bf1ec3e383d9ccce2179eedebb9e.png)

4  实验结果：

按照之前的方式将代码下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，打开数据显示(设备)按钮。

![](media/04b472326485cf676cdb4dd61ca6ef1a.png)

数据显示器显示亮度级别值，用手全部遮住micro:bit的LED点阵，亮度级别约为0；然后将micro:bit的LED点阵放置于光照下，随着光照强度增强，亮度级别值也在逐渐增大。

![](media/d7f1751ea1e6f251376dee5390ed21fa.png)

如果你的电脑系统是Windows7/8而不是Windows 10，则在Google Chrome中是不能进行设备配对，从而读取不了相应的数字信号或模拟信号，可是又需要读取相应的传感器/模块的数字信号或模拟信号，那怎么办呢？这里就可以使用CoolTerm软件来读取串口的。

打开CoolTerm，点击Options，选择串行Port，设置COM口和波特率，波特率设置为115200（经过测试，micro:bit的USB串口通讯波特率是115200），点击OK后，最后点击Connect。这样，CoolTerm串口监视器显示光线亮度级别值。

![](media/77a6de8ab9b171353693610a09f3a83c.png)

### 9：扬声器

![](media/ac515b9ae8891dc32f368a29f194a2fb.png)

1实验说明：

micro:bit主板有内置扬声器，这使得在你的项目中添加声音变得非常容易。通过编程使扬声器发出各种各样的音调，例如编写一首歌曲：《欢乐颂》，让扬声器播放出来。

2准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

[(How to import?) ](#资源和代码)

如果要一一拖动代码块，请单击“新建项目”。

3实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\89：扬声器|microbit-扬声器hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）从“基础”模块中找到并拖出指令方块“显示图标”放入“当开机时”指令方块中，点击下拉三角形选择“

![](media/7f7aa904c35f83b61c7c560ad1e40d2a.png)

”图案。

![](media/a9131d0acf73ac4caca11fec179ce059.png)

（2）点击“音乐”模块，找到并拖出指令方块“播放声音
咯咯声
值到结束”放入“”指令方块中，再从“基础”模块中找到并拖出指令方块“暂停(ms) 100”放入“无限循环”指令方块中，将100改成1000。

![](media/200a76a043f9e4abe1aa9c1c77fd9904.png)

（3）复制代码串

![](media/200a76a043f9e4abe1aa9c1c77fd9904.png)

3次也放入“无限循环”指令方块中，点击下拉三角形分别选择“快乐”,”你好”,”打哈欠”。

![](media/e8cb8be5cba16b281a997dd76f6cfe86.png)

完整的代码程序：

![](media/a8ffa4409786d41f2dfeff8f560f5057.png)

①“当开机时”指令方块仅运行一次以启动程序。

②LED点阵屏显示“![](media/7f7aa904c35f83b61c7c560ad1e40d2a.png)”图案。

③在“无限循环”指令方块之内，程序循环运行。

④蜂鸣器发出“咯咯声”音

⑤延时1000毫秒

⑥蜂鸣器发出“快乐”音

⑦延时1000毫秒

⑧蜂鸣器发出“你好”音

⑨延时1000毫秒

⑩蜂鸣器发出“打哈欠”音

⑪延时1000毫秒

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/c07acaae7dabac8d2e65882007d36e5b.png)

4实验现象:

按照之前的方式将实验代码下载到micro：bit板，利用micro USB数据线上电，micro:bit主板上的扬声器发出声音且LED点阵显示音乐标志图案。

### 10：触摸感应logo

![](media/644695850097c5ade080bb4848b4b481.png)

1  实验说明：

如果你有了micro:bit主板，你可以在你的项目中使用金色的触摸感应logo作为另一个输入，这就像多了一个按钮。触摸感应采用的是电容式触摸传感器，当你手指按下（或触摸）它时，它就能感应到电场的微小变化----就像你的手机或平板电脑屏幕一样。当你像按按钮一样按下它时，你可以在程序中触发事件。

2准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

如果要一一拖动代码块，请单击“新建项目”。

3实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\810：触摸感应logo|microbit-触摸感应LOGOhex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）删除掉“当开机时”指令方块和“无限循环”指令方块。

（2）从“输入”模块中找到并拖出“当微标
被按下”指令方块，点击下拉三角形按钮选择 被触摸。

![](media/dbf69d641bd8a0cb7043147f6532e63c.png)

3  先点击“变量”模块，再点击“设置变量”按钮，在出现的对话框中输入start，点击OK，这样就创建了变量“start”。从“变量”模块中拖出变量指令方块“将start     设为 0”放入指令方块“当微标被触摸”中。

![](media/daf4edd83cd8d8a94aee60351a4c3751.png)

4  点击“输入”模块下的更多，找到并拖出“运行时间(ms)”放入变量指令方块“将start     设为 0”的数字0处。

![](media/170395914011ae23a4db9e07a27888b5.png)

5  从“基础”模块中找到并拖出指令方块“显示图标❤”放入“当微标被触摸”指令方块中。

![](media/cf51b0e625fa8149d2d6ce00387bffae.png)

6  从“输入”模块中找到并拖出“当微标被按下”指令方块，选择被松开，接着用同样的方法再创建变量“time”。从“变量”模块中拖出变量指令方块“将
    time     设为0”放入指令方块“当微标被松开”中，并从“数学”模块中找到并拖出“0-0”方块放入变量指令方块“将
    time 设为0”的数字0处。

![](media/5945d97a4953046db00e0d9ab6c83238.png)

7  点击“输入”模块下的更多，找到并拖出“运行时间(ms)”放入“0-0”方块的左侧数字0处，再从“变量”模块中拖出变量指令方块“start”放入右侧数字0处。

![](media/90985ecdd338bd4e5297449cb1bbea5a.png)

8  先从“基础”模块中找到并拖出指令方块“显示数字”放入“当微标被松开”指令方块中，再从“数学”模块中找到并拖出方块“平方根
    0 ”放入数字0处，点击下拉三角形按钮选择 整数÷。

![](media/deb92aa25372fd930364cf375eafb8cd.png)

9  从“变量”模块中找到并拖出变量指令方块“time”放入右侧数字0处，再把右侧的数字0改成1000。

![](media/2f1aeb983b01aa1c9df5752752fb7f17.png)

完整的代码程序：

![](media/7a83fbcc1d95615afa1b545a86ab208e.png)

①手触摸microbit主板上的logo标志

②将running time值赋给于变量start

③microbit主板的LED点阵显示“❤”图案

③手释放microbit主板上的logo标志

④将running time－变量start的值赋给于变量time

⑤LED点阵屏显示变量time除于1000的取整

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/200dbc88e6f0da02e512fa704f8186a8.png)

4实验现象:

按照之前的方式将实验代码下载到micro：bit板，利用micro USB数据线上电，手指按住micro:bit主板上“Logo”标志处，micro:bit主板上的LED点阵显示“❤”图案；手指松开micro:bit主板上“Logo”标志处，会出现数字。

### 11：麦克风

![](media/3073a8af772ab91ecf264843b37d3b74.png)![](media/7f0741158e734ff8449d5b87d5ba85f4.png)

1实验说明：

micro:bit
主板有一个内置麦克风，可以测量环境的声音程度。你可以使用它作为一个简单的输入---当你鼓掌时，micro:bit主板上前面内置麦克风LED指示灯会被打开。它还可以测量声音的强度，所以你可以制作一个噪音等级表或与音乐合拍的迪斯科灯光。麦克风是在micro:bit
主板的背面，而在前面，你会发现一个内置麦克风LED指示灯，还有紧挨着让声音进入麦克风的孔。当你micro:bit主板在测量声音级别时，它就会亮起来。

2准备：

（1）通过micro USB线连接micro：bit主板和电脑。

（2）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

[(How to import?) ](#资源和代码)

如果要一一拖动代码块，请单击“新建项目”。

3实验代码：

根据下表加载代码（如何加载？）如下图：

<table style="width:100%;">

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\811：麦克风\811：麦克风-1|microbit-麦克风-1hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）删除掉“当开机时”指令方块和“无限循环”指令方块。

（2）先从“输入”模块中找到并拖出“大声
声音”指令方块，再从“基础”模块中找到并拖出指令方块“显示图标”放入“但开机时”指令方块中。

![](media/c0d7f2f20c780c337c7f445986ef5946.png)

1  复制代码串

![](media/c0d7f2f20c780c337c7f445986ef5946.png)1次，点击“大声”后面的下拉三角形按钮选择“安静”，再点击❤后面的下拉三角形按钮选择![](media/9a40d2f51ed0a372a82e559cdb2ca0dd.png)

。

![](media/80861d37f15b3fd34d115ab596dd19a1.png)

完整的代码程序：

![](media/5294b7d76c40871df0b9ae907f251915.png)

①microbit主板上的麦克风检测到声音

②LED点阵屏显示“❤”图案

③microbit主板上的麦克风未检测到声音

④LED点阵屏显示“![](media/04fdfc9060943954e7938bb1a741d626.png)”图案

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/010908e5a7247a5598f56682a793ceb4.png)

4实验现象1：

USB数据线上电，当你鼓掌时，micro:bit
主板上的LED点阵显示“❤”图案；当外界环境安静时，micro:bit
主板上的LED点阵显示“

![](media/04fdfc9060943954e7938bb1a741d626.png)

”图案。

5  实验代码2:

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\811：麦克风\811：麦克风-2|microbit-麦克风-2hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“高级”下的“串行”模块，找到并拖出指令方块“串行
重新 定向到 USB”放入“当开机时”指令方块中。

![](media/1cd5710476f4682bb5f92c51072d5d24.png)

（2）先点击“变量”模块，再点击“设置变量”按钮，在出现的对话框中输入maxSound，点击OK，这样就创建了变量“maxSound”。从“变量”模块中拖出变量指令方块“将maxSound
设为 0”放入指令方块“当开机时”中。

![](media/b6de6aa6a4b130e02657dd8f6b1f413a.png)

2  先点击“逻辑”模块，找到并拖出“如果为则否则”放入“无限循环”指令方块中，再从“输入”模块中找到并拖出“当按钮
    A 被按下”指令方块放入then处。

![](media/41dfc4e19a7f130b54bd19373ddd48ca.png)

3  先从“基础”模块中找到并拖出指令方块“显示数字”放入如果为下，再从“变量”模块中拖出变量指令方块“maxSound”放入数字0处。

![](media/bc762c95edebfda41dd7f13c0cab61ca.png)

4  设为
    0”放入否则下，然后从“输入”模块中找到并拖出“声音响度”指令方块放入数字0处。

![](media/ec2bf2b85db1ae161e2dfeb917b6dd8b.png)

5  先点击“Led”模块，找到并拖出指令方块“绘制条形图值为
    0 最高
    0”也放入否则下，再从“变量”模块中拖出变量指令方块“soundLevel”放入值为后面的数字0处，然后将
    最高 后面的数字0改成255。

![](media/e714988085a64834c1ce381b0085f5fd.png)

6  则
    ”放入“否则”下，再从“逻辑”模块中拖出“0 \>
    0”方块放入then处，然后从“变量”模块中拖出变量指令方块“soundLevel”放入左侧的数字0处，最后从“变量”模块中拖出变量指令方块“maxSound”放入右侧的数字0处。

![](media/bafec879ec09f81c1fac2ca94470e397.png)

7  从“变量”模块中拖出变量指令方块“将 maxSound     设为0”放入第2个如果为下，接着又从“变量”模块中拖出变量指令方块“soundLevel”放入数字0处。

![](media/6f785f7a07207cafbd29adb26dd6c8ce.png)

完整的代码程序：

![](media/fb7685d1417d647d2a239e52c40dacf8.png)

①“当开机时”指令方块仅运行一次以启动程序。

②串行重定向到USB。

③将变量maxSound初始值为0

④在“无限循环”指令方块之内，程序循环运行

⑤如果按键A按下时，执行then下程序

⑥LED点阵屏显示麦克风检测到的此时环境中最大声音级别值

⑦上述条件不成立时，执行else下程序

⑧将声音级别值赋给于变量soundLevel

⑨LED点阵中LED点亮的亮度级别，最高亮度为255。

⑩否则如果麦克风检测到的声音级别值大于此时环境中最大声音级别值

⑪将变量麦克风检测到的声音级别值赋给于变量soundLevel

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/1b0232cc0f4e3aac5736741e85019a95.png)

6  实验现象2：

按照之前的方式将实验代码2下载到micro：bit板，利用micro USB数据线上电，点击“显示控制台(设备)”按钮：

![](media/e22507af4953df977269bbdb2463d69e.png)

串口输出数据，当外界环境的声音增大时，串口输出的声音级别值也增大，如下图所示：

![](media/50b81518d9f7925b0c20476ab1f64185.png)

LED点阵显示检测到的此时环境中最大声音级别值（这里需要注意：通过按micro:bit背面的重置按钮重置最大值。）；当鼓掌时，LED点阵显示声音级别大小图案。

### 12：micro:bit的蓝牙无线通信

![](media/55b2424d88ba1ba8a711c49418ca8dc6.png)

1  实验说明：

micro:bit主板自带了[nRF52833](https://wwwnordicsemicom/Products/Low-power-short-range-wireless/nRF52833)处理器（内置蓝牙51低功耗的BLE(Bluetooth Low Energy)设备）以及24GHz天线，可进行蓝牙无线通信和24GHz无线通信。使得micro:bit主板可以与各种蓝牙设备进行通信，包括智能手机和平板电脑。

在本实验中，主要讲解新款的micro:bit主板实现蓝牙无线通信功能，我们可以通过连接蓝牙，实现无线传输代码（信号）功能。我们利用一个苹果系统设备（手机/iPad）和micro:bit
主板连接，实现无线传输功能。设置安卓系统手机实现无线传输方法和苹果系统设备（手机/iPad）类似，这里就不一一介绍了。

2  准备：

1  通过micro     USB线将micro:bit主板连接到电脑上。

2  苹果系统设备（手机/iPad）或安卓系统手机。

3  实验步骤：

，点击“Download pairing HEX file”下载micro:bit的固件到创建的文件夹中或电脑桌面上，并将下载好的micro:bit固件烧入micro:bit主板中。（这一步只针对于苹果系统的智能手机/iPad）

![](media/cfaf7f8ae83cbe2636c39162a78adc7f.png)

![](media/4bcbd2456b3502d254617622b0f8707b.png)

![](media/ed8937c877dc004629f8afeabc8625b1.png)

（2）在苹果系统设备（手机/iPad）上打开

![](media/27924fdb3d67692df7c63d8d0fb72287.png)

bit”，然后选中micro:bit
选项，会出现下载界面（如下图所示：），点击“

![](media/962a57f92b78eea1f0e3e81463497a9c.png)

”，就可以下载安装对应的APP。

![](media/66d1f34d8d4c52e2b7c0ce10e602a063.png)

（3）苹果系统设备（手机/iPad）和micro:bit主板配对连接。

1  打开苹果系统设备（手机/iPad）上的蓝牙。

2  APP安装成功后，点击

![](media/ddfd27bdd24da96eb998ccc2e13fcf72.png)

打开APP，先确定micro     USB数据线已经将micro:bit主板和电脑连接上，再点击APP的第一项“Choose     micro:bit”，开始配对蓝牙。

![](media/34f5fbb1c0c371970d1aec6c59c5cbb5.png)

3  点击配对一个新的micro:bit，开始配对。

![](media/e20270a0ade9c00b61198b26fc2fd83b.png)

4  根据提示，首先同时按住micro:bit主板上的按键A和B，然后按下micro:bit主板后面的复位&电源按钮几秒钟（按键A和B不能松开），再松开复位&电源按钮，micro:bit主板上LED点阵会显示一个密码图案。最后松开micro：bit主板上的按键A和B，接着点击“下一步”。

![](media/c00520400ecd1f20f958c1c6d1a3c907.png)

![](media/cabc60d7f8a030f5c9d86ac7de6c7bd7.png)

5  在苹果系统手机/iPad上设置密码图案，使图案和micro:bit主板上显示的密码图案一样，点击“下一步”。

![](media/9411a5280e6f3b0d45306a31f80c1b38.png)

6  点击“下一步”，出现对话框，在对话框中点击“Pair”。几秒钟后，配对成功，同时micro:bit主板上的LED点阵显示“√”图案。

![](media/7b56c56e10415ac2881ac69448b4ad3c.png)![](media/803cb5cf5f7d595581a11f5e6b7e61ed.png)

![](media/dc570950dd81f427edb5ea58f50b3a7e.png)![](media/f72e83dc6276d520e82c349659106e1a.png)

（3）蓝牙配对成功后，开始利用APP编写代码，并上传代码。

a点击第二项“Create Code”，进入编程界面，开始编写代码程序。（点击

![](media/f3e9cc7884f7bba807fa4633c429422b.png)，出现对话框![](media/e081360be7c91b7a156b01a787e4a58c.png)

，在对话框中直接点击“Create
√”后就进入编程界面）

![](media/d54bf2d1c01cd3c18544009b1f9dc5a0.png)

![](media/5fa7ffca1ce23b1ebc9a834934638273.png)

![](media/a2258b54f29f9e9cfcb0adc3efb65eb1.png)

![](media/ce3027d92602f98c35a100435766f42a.png)

b
将代码程序项目名称设置为“1”，点击保存图案“

![](media/a32c2d832ab38d19eb623108143c744e.png)

”，保存代码程序。

![](media/f069f9fa1724e81c8ab4b1b0af1c3449.png)

c项目代码程序保存成功后，点击第三项“Flash”进入上传代码程序界面。默认选择代码程序是刚刚保存的项目名称为“1”的代码程序，然后点击“Flash”上传代码程序“1”。

![](media/c1661720ea2eaa521ff31a778501eb23.png)

![](media/350abcbb09d431d40427f34c3764f2eb.png)

![](media/4863bf826f119805a6a9bf9c12d5ec81.png)

d几秒钟后，代码程序“1”上传成功，会显示如下图。然后micro:bit主板上的LED点阵显示跳跃的“心”对应图案。

![](media/ebfd31347a0553de0be4e01636652a15.png)

上面的实验是使用micro：bit自带的传感器模块和LED点阵，接下来的实验都是micro:bit与keyes micro:bit 迷你智能乌龟车上的传感器模块、无源蜂鸣器、4个WS2812 RGB灯和2个RGB灯等的拓展实验。

USB
线与micro：bit主板的连接和关闭micro:bit电机驱动扩展板上的电源（拨动POWER拨码开关到OFF一端）；同理，micro：bit主板从小车扩展板拿下来之前也要先断开micro USB
线与micro：bit主板的连接和关闭micro:bit电机驱动扩展板上的电源（拨动POWER拨码开关到OFF一端）。）

### 13：无源蜂鸣器播放音乐

![](media/74060fac6c085d68066db94d1ada3a99.png)

1实验说明：

我们可以用micro:bit制作许多互动作品，其中最常用的是声光显示。之前所有的实验都和LED有关。然而，这个实验中的电路可以产生声音。通常情况下，实验是用蜂鸣器或扬声器进行的，而蜂鸣器更简单、更容易使用。

我们这里介绍的蜂鸣器是无源蜂鸣器。它不能由自身驱动，而是由外部脉冲频率驱动。不同的频率产生不同的声音。我们可以使用micro:bit来编码歌曲的旋律，这实际上是非常有趣和简单的。

蜂鸣器可分为有源蜂鸣器和无源蜂鸣器两种。无源蜂鸣器利用电磁感应现象，为音圈接入交变电流后形成的电磁铁与永磁铁相吸或相斥而推动振膜发声，接入直流电只能持续推动振膜而无法产生声音，只能在接通或断开时产生声音。

　　有源蜂鸣器往往比无源蜂鸣器的贵，就是因为里面多个震荡电路，只需接入额定电压的直流电即可发出指定频率的声音，频率由内部振荡电路决定，无法改变。而无源蜂鸣器内部不带振荡源，直流信号无法令其鸣叫，须用方波驱动。

　　（1）制作成本低；  
　　（2）声音频率范围宽，可高分贝的发出某些频率的超声波以及可以做出“多来米发索拉西”的效果；  
　 （3）在一些特例中，可以和LED复用一个控制IO口。

无源蜂鸣器频率是由英文和数字组成的音名，选择不同的音名就能改变不同的频率啦。声音频率的高低叫做音调。在音乐课上，老师教过我们唱“1（Do）、2（Re）、3(Mi)、4(Fa) 、5(Sol) 、6(La) 、7(Si)”是音乐当中的唱名，就对应了音调中的C、D、E、F、G、A、B这些音名。

频率（音调）高低判断时先看后面的数字，数字越大，音调越高，数字相同时看前面的字母，从C到B频率（音调）越来越高；而节拍是音符延时时间，数值越大，延时时间越长。

节拍是指每个音符持续的时间。音谱中不带线的一个音符就是一拍，延时1000毫秒，而带一条下划线的音符节拍是不带线音符节拍的1/2，带两条下划线的音符节拍是不带线音符节拍的1/4（

![](media/9280991ebf66dac53c3d692cb6acf2cf.png)

）

在本实验中，
Micro:bit电机驱动扩展板上自带有无源蜂鸣器元件，它是由micro:bit的P0接口控制。实验中我们用软件自带的库文件，让无源蜂鸣器演奏”欢乐颂“歌曲，下面是《欢乐颂》歌曲的简谱。

![](media/93f705849bec20f6c7682d1336b96120.jpg)

2  准备：

（1）将micro:bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro:bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，请单击“导入”。

如果要一一拖动代码块，请单击“新建项目”。

3  实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\813：无源蜂鸣器播放音乐|microbit-无源蜂鸣器播放音乐hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）先点击“Led”模块，再点击“Led”模块下的“更多”，找到并拖出指令方块“led
启用 fasle”放入“当开机时”指令方块中。

![](media/a3ca8c0fc07e063f9e7bec3df246f2fc.png)

2  点击“音乐”模块，找到并拖出指令方块“播放音调
    中C持续 1 节拍
    节拍”放入“无限循环”指令方块中，根据上面的“欢乐颂”歌谱，点击指令方块
    “播放音调 中C持续 1 节拍 节拍”的“中
    C”处，会出现

![](media/9007cad32767ebef4bea090871d50926.png)

图案，选择“高
    E”

![](media/756deddf009a30c923571f5b369883eb.png)

并点击，接着点击“1     节拍”选择“1”。

![](media/67a8a21795bf59085a7ccb19a189a793.png)

3  根据上面的“欢乐颂”歌谱可知，复制“无限循环”指令方块中的“播放音调
    高E 持续 1 节拍 节拍”指令方块124次，点击指令方块“播放音调 高E 持续 1     节拍 节拍”的“高 E”处和1 节处分别对应的改成：

|序号|音调|节拍|序号|音调|节拍|序号|音调|节拍|序号|音调|节拍|
|-|-|-|-|-|-|-|-|-|-|-|-|
|①|高 E|1|②|高 F|1|③|高 G|1|④|高 G|1|
|⑤|高 F|1|⑥|高 E|1|⑦|高 D|1|⑧|高 C|1|
|⑨|高 C|1|⑩|高 D|1|⑪|高 E|1|⑫|高 E|1|
|⑬|高 D|1/2|⑭|高 D|1|⑮|高 E|1|⑯|高 E|1|
|⑰|高 F|1|⑱|高 G|1|⑲|高 G|1|⑳|高 F|1|
|㉑|高 E|1|㉒|高 D|1|㉓|高 C|1|㉔|高 C|1|
|㉕|高 D|1|㉖|高 E|1|㉗|高 D|1|㉘|高 C|1/2|
|㉙|高 C|1|㉚|高 D|1|㉛|高 D|1|㉜|高 E|1|
|㉝|高 C|1|㉞|高 D|1|㉟|高 E|1/2|㊱|高 F|1/2|
|㊲|高 E|1|㊳|高 C|1|㊴|高 D|1|㊵|高 E|1/2|
|㊶|高 F|1/2|㊷|高 E|1|㊸|高 D|1|㊹|高 C|1|
|㊺|高 D|1|㊻|中 G|1|㊼|高 E|1|㊽|高 E|1|
|㊾|高 E|1|㊿|高 F|1|51|高 G|1|52|高 G|1|
|53|高 F|1|54|高 E|1|55|高 D|1|56|高 C|1|
|57|高 C|1|58|高 D|1|59|高 E|1|60|高 D|1|
|61|高 C|1/2|62|高 C|1|63|高 D|1|64|高 D|1|
|65|高 E|1|66|高 C|1|67|高 D|1|68|高 E|1/2|
|69|高 F|1/2|70|高 E|1|71|高 C|1|72|高 D|1|
|73|高 E|1/2|74|高 F|1/2|75|高 E|1|76|高 D|1|
|77|高 C|1|78|高 D|1|79|中 G|1|80|高 E|1|
|81|高 E|1|82|高 E|1|83|高 F|1|84|高 G|1|
|85|高 G|1|86|高 F|1|87|高 E|1|88|高 C|1|
|89|高 C|1|90|高 C|1|91|高 D|1|92|高 E|1|
|93|高 D|1|94|高 C|1/2|95|高 C|1|96|高 D|1|
|97|高 C|1/2|98|高 C|1|99|高 G|1|100|高 F|1|
|101|高 E|1/2|102|高 E|1|103|高 C|1|104|高 B|1|
|105|高 A|1/2|106|高 A|1|107|高 F|1/2|108|高 D|1/2|
|109|高 C|1/2|110|中 B|1/2|111|高 D|1/2|112|中 B|1/2|
|113|中 A|1/2|114|中 G|1/2|115|中 A|1/2|116|中 B|1/2|
|117|高 C|1/2|118|高 E|1/2|119|高 D|1/2|120|中 B|1/2|
|121|高 C|1|122|高 C|1/2|123|高 C|1/4|124|高 C|1|

完整的代码程序：

![](media/e70f20860d2f039263d210d9a946fb83.png)

①“当开机时”指令方块仅运行一次以启动程序。

②关闭LED点阵屏。

③在“无限循环”指令方块之内，程序循环运行

④播放音调高E持续1节拍

⑤播放音调高E持续1节拍

⑥播放音调高F持续1节拍

⑦播放音调高G持续1节拍

⑧播放音调高G持续1节拍

⑨播放音调高F持续1节拍

⑩播放音调高E持续1节拍

⑪播放音调高D持续1节拍

⑫播放音调高D持续1节拍

⑬播放音调高C持续1节拍

⑭播放音调高D持续1节拍

⑮播放音调高E持续1节拍

⑯播放音调高E持续1节拍

⑰播放音调高D持续1/2节拍

⑱播放音调高D持续1节拍

⑲播放音调高E持续1节拍

![](media/f4705d0ecbc96e954685389f3ad97327.png)

⑳播放音调高E持续1节拍

㉑播放音调高F持续1节拍

㉒播放音调高G持续1节拍

㉓播放音调高G持续1节拍

㉔播放音调高F持续1节拍

㉕播放音调高E持续1节拍

㉖播放音调高F持续1节拍

㉗播放音调高C持续1节拍

㉘播放音调高C持续1节拍

㉙播放音调高D持续1节拍

㉚播放音调高E持续1节拍

㉛播放音调高D持续1节拍

㉜播放音调高C持续1/2节拍

㉝播放音调高C持续1节拍

㉞播放音调高D持续1节拍

㉟播放音调高D持续1节拍

㊱播放音调高E持续1节拍

㊲播放音调高C持续1节拍

㊳播放音调高D持续1节拍

㊴播放音调高E持续1/2节拍

![](media/1970bb205dac957dd977cc9b5cf9adb9.png)

㊵播放音调高F持续1/2节拍

㊶播放音调高E持续1节拍

㊷播放音调高C持续1节拍

㊸播放音调高D持续1节拍

㊹播放音调高E持续1/2节拍

㊺播放音调高F持续1/2节拍

㊻播放音调高E持续1节拍

㊼播放音调高D持续1节拍

㊽播放音调高C持续1节拍

㊾播放音调高C持续1节拍

㊿播放音调中G持续1节拍

播放音调高E持续1节拍

播放音调高E持续1节拍

播放音调高E持续1节拍

播放音调高F持续1节拍

播放音调高G持续1节拍

播放音调高G持续1节拍

播放音调高F持续1节拍

播放音调高E持续1节拍

播放音调高D持续1节拍

![](media/ceafcbd1a511f0bf281b112bfe0941e4.png)

播放音调高C持续1节拍

播放音调高C持续1节拍

播放音调高D持续1节拍

播放音调高E持续1节拍

播放音调高D持续1节拍

播放音调高C持续1/2节拍

播放音调高C持续1节拍

播放音调高D持续1节拍

播放音调高D持续1节拍

播放音调高E持续1节拍

播放音调高C持续1节拍

播放音调高D持续1节拍

播放音调高E持续1/2节拍

播放音调高F持续1/2节拍

播放音调高E持续1节拍

播放音调高C持续1节拍

播放音调高D持续1节拍

播放音调高E持续1节拍

播放音调高F持续1/2节拍

播放音调高E持续1节拍

![](media/df7bea5ab76b1fcc70682b0410f29cca.png)

播放音调高D持续1节拍

播放音调高C持续1节拍

播放音调高D持续1节拍

播放音调中G持续1节拍

播放音调高E持续1节拍

播放音调高E持续1节拍

播放音调高E持续1节拍

播放音调高F持续1节拍

播放音调高G持续1节拍

播放音调高G持续1节拍

播放音调高F持续1节拍

播放音调高E持续1节拍

播放音调高C持续1节拍

播放音调高C持续1节拍

播放音调高C持续1节拍

播放音调高D持续1节拍

播放音调高E持续1节拍

播放音调高D持续1节拍

播放音调高C持续1/2节拍

播放音调高C持续1节拍

![](media/ba4533d89b9219dcc6663c9cc22710f8.png)播放音调高D持续1节拍

播放音调高D持续1节拍

播放音调高C持续1/2节拍

播放音调高C持续1节拍

播放音调高G持续1节拍

播放音调高F持续1节拍

播放音调高E持续1/2节拍

播放音调高E持续1节拍

播放音调高C持续1节拍

播放音调高B持续1节拍

播放音调高A持续1/2节拍

播放音调高A持续1节拍

播放音调高F持续1/2节拍

播放音调高D持续1/2节拍

播放音调高C持续1/2节拍

播放音调中B持续1/2节拍

播放音调高D持续1/2节拍

播放音调中B持续1/2节拍

播放音调中A持续1/2节拍

播放音调中G持续1/2节拍

播放音调中A持续1/2节拍

![](media/73950a4663f56b481d35802d137dd86c.png)

播放音调中B持续1/2节拍

播放音调高C持续1/2节拍

播放音调高E持续1/2节拍

播放音调高D持续1/2节拍

播放音调中B持续1/2节拍

播放音调高C持续1节拍

播放音调高C持续1/2节拍

播放音调高C持续1/4节拍

播放音调高C持续1节拍

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/13a99d5f6bdae837783edc06c59375a3.png)

![](media/0bb4cf490856f9da0298fe854bd4ee33.png)

![](media/9c20144ddf8d1b3c788768b480dbb07f.png)

4 实验结果：

按照以前的方式将代码下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，microbit的电机驱动扩展板上的无源蜂鸣器一直循环播放《欢乐颂》歌曲。

### 14：RGB灯实验

![](media/671b9bd2f40e6c6509399f93794fbda5.png)

1  实验说明：

![](media/ad8930da839191890e4f24bf4bb34c66.png)RGB色彩模式是工业界的一种颜色标准，是通过对红(R)、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色的，RGB即是代表红、绿、蓝三个通道的颜色，这个标准几乎包括了人类视力所能感知的所有颜色，是目前运用最广的颜色系统之一。

显示器大都是采用了RGB颜色标准，在显示器上，是通过电子枪打在屏幕的红、绿、蓝三色发光极上来产生色彩的，电脑一般都能显示32位颜色，有一千万种以上的颜色。电脑屏幕上的所有颜色，都由这红色绿色蓝色三种色光按照不同的比例混合而成的。一组红色绿色蓝色就是一个最小的显示单位。屏幕上的任何一个颜色都可以由一组RGB值来记录和表达，因此这红色绿色蓝色又称为三原色光，用英文表示就是R(red)、G(green)、B(blue)。

RGB是从颜色发光的原理来设计定的，通俗点说它的颜色混合方式就好像有红、绿、蓝三盏灯，当它们的光相互叠合的时候，色彩相混，而亮度却等于三者亮度之总和，越混合亮度越高，即加法混合。红、绿、蓝三盏灯的叠加情况，中心三色最亮的叠加区为白色，加法混合的特点：越叠加越明亮，因此被通常被人们称为七彩LED。

红、绿、蓝三个颜色通道每种色各分为256阶亮度，用数字表示为从0、1、2直到255。注意虽然数字最高是255，相当于100%，但0也是数值之一，因此共256级。在0时“灯”最弱——是关掉的，而在255时“灯”最亮。当三色灰度数值相同时，产生不同灰度值的灰色调，即三色灰度都为0时，是最暗的黑色调；三色灰度都为255时，是最亮的白色调。

|颜色样式|RGB数值（R,G,B）|颜色代码|颜色样式|RGB数值（R,G,B）|颜色代码|
|-|-|-|-|-|-|
|黑色|0,0,0|#000000|红色|255,0,0|#FF0000|
|绿色|0,255,0|#00FF00|蓝色|0,0,255|#0000FF|
|青色|0,255,255|#00FFFF|深红色|255,0,255|#FF00FF|
|黄色|255,255,0|#FFFF00|白色|255,255,255|#FFFFFF|

B
添加在一起（即所有光线反射回眼睛）可产生白色。加成色用于照明光、电视和计算机显示器。例如，显示器通过红色、绿色和蓝色荧光粉发射光线产生颜色。绝大多数可视光谱都可表示为红、绿、蓝
(RGB)
三色光在不同比例和强度上的混合。这些颜色若发生重叠，则产生青、洋红和黄。RGB灯分为共阳、共阴两种，在这个小车的扩展板上，焊接有2个RGB灯，我们可以利用这2个GRB灯做为小车的指示灯。为了节约IO口资源，我们利用1个PCA9685PW芯片的部分引脚来控制2个RGB灯。

这一课程中我们做2个实验，一个是2个RGB灯循环亮起红、绿、蓝、青、深红、黄、白7种颜色灯光，另一个是2个RGB灯渐变显示不同颜色灯光。

2  准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro:bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit扩展库。

如果选择手动拖动代码，则首先需要添加turtle-bit扩展库。

3  实验代码：

代码1

RGB灯循环亮起7种颜色光

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\814：RGB灯实验\Code-1|microbit-RGB实验-1hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“TurtleBit”模块，找到并拖出“LED brightness 0”指令方块放入“当开机时”指令方块中，数字0可以改成0至255中任意一个数字，设置数字越大，RGB就越亮，在这里就把数字0改成70。

![](media/db1dbd4e3835ede1e835f3988dc6b7fe.png)

（2）接着又点击“TurtleBit”模块，找到并拖出“set RGBled left_side R：0 G：0 B：0”指令方块放入“无限循环”指令方块中，把R后面的数字0改成255，其他的不变。

![](media/211e40079dd424ffd08cd5fc33e0b835.png)

B：0”指令方块放入“无限循环”指令方块中，点击
left_side后面的下拉三角形按钮选择right_side，把R后面的数字0改成255，其他的不变。

![](media/5ddb79e8ff2c9b817c3054072b9cec1e.png)

4)  点击“基础”模块，找到并拖出指令方块“暂停 (ms)     100”放入“无限循环”指令方块中，设置延时1000毫秒。

![](media/08bd4bfd84a897736b1eee8e62ab55fa.png)

4  复制代码串

![](media/08bd4bfd84a897736b1eee8e62ab55fa.png)

6次并且也放入“无限循环”指令方块中，将“
    R：255 G：0 B：0”对应的改成 “R：0 G：255 B：0”、“ R：0 G：0     B：255”、“ R：0 G：255 B：255”、“ R：255 G：0 B：255”、“ R：255     G：255 B：0”、“ R：255 G：0 B：255”。

![](media/6f0a2852c77658db75a7662e5ec4f799.png)

![](media/46192531af58bf0f41c14ae5c7e4d2a5.png)

![](media/a176092487d28d8d8b95f95faac32fd0.png)

完整的代码程序：

①“当开机时”指令方块仅运行一次以启动程序。

②设置小车2个RGB灯的亮度为70。

③在“无限循环”指令方块之内，程序循环运行。

④设置左边的RGB灯R：255 G：0 B：0，控制乌龟车左边的RGB灯亮红色灯

⑤设置右边的RGB灯R：255 G：0 B：0，控制乌龟车右边的RGB灯亮红色灯

⑥延时时间1000毫秒

⑦设置左边的RGB灯R：0 G：255 B：0，控制乌龟车左边的RGB灯亮绿色灯

⑧设置右边的RGB灯R：0 G：255 B：0，控制乌龟车右边的RGB灯亮绿色灯

⑨延时时间1000毫秒

![](media/63375069c8f4d8c4cf2c929c9dd7f57e.png)

![](media/fdda977cd0424f3d03f0b31401470735.png)

⑩设置左边的RGB灯R：0 G：0 B：255，控制乌龟车左边的RGB灯亮蓝色灯

⑪设置右边的RGB灯R：0 G：0 B：255，控制乌龟车右边的RGB灯亮蓝色灯

⑫延时时间1000毫秒

⑬设置左边RGB灯R：0 G：255 B：255，控制乌龟车左边的RGB灯亮青色灯

⑭设置右边RGB灯R：0 G：255 B：255，控制乌龟车右边的RGB灯亮青色灯

⑮延时时间1000毫秒

⑯设置左边RGB灯R：255 G：0 B：255，控制乌龟车左边的是RGB灯亮深红色灯

⑰设置右边RGB灯R：255 G：0 B：255，控制乌龟车右边的是RGB灯亮深红色灯

⑱延时时间1000毫秒

⑲设置左边RGB灯R：255 G：255 B：0，控制乌龟车左边的RGB灯亮黄色灯

⑳设置右边RGB灯R：255 G：255 B：0，控制乌龟车右边的RGB灯亮黄色灯

㉑延时时间1000毫秒

㉒设置左边RGB灯R：255 G：255 B：255，控制乌龟车左边的RGB灯亮白色灯

㉓设置右边RGB灯R：255 G：255 B：255，控制乌龟车右边的RGB灯亮白色灯

㉔延时时间1000毫秒

![](media/8f2c28355939fc4acaf7a9b0f3ae204b.png)

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/1868b773aa88fef0855a571a611a6c77.png)

![](media/2967654276eee586a76b518c71bd89c4.png)

![](media/7a6ac740b8f4f42110519bdba53d1440.png)

代码2：

RGB灯渐变显示不同颜色灯光

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\814：RGB灯实验\Code-2|microbit-RGB实验-2hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“TurtleBit”模块，找到并拖出“LED brightness 0”指令方块放入“当开机时”指令方块中，数字0可以改成0至255中任意一个数字，设置数字越大，RGB就越亮，在这里就把数字0改成200。

![](media/a7e99e4d40d09a961f5de01fae6c4ddb.png)

(2)先点击“变量”模块，再点击“设置变量”出现“新变量的名称：”对话框，在对话框中分别输入“led-r”，点击“OK”，建立了变量“led-r”。用同样的方法先后分别建立变量“led-g”和“led-b”，拖出指令方块“将
led-b 设为 0”放入“当开机时”指令方块中，复制指令方块“将 led-b 设为
0”2次并放入“当开机时”指令方块中，点击第1个led_b后面的下拉三角形按钮选择led_r，再点击第2个led_b后面的下拉三角形按钮选择led_g。

![](media/3418a37ed14076bfbc052462b3f80905.png)

10 次
    执行”放入“无限循环”指令方块中。

![](media/86f3d7f476a38ddbbb6fce3c3c39cc92.png)

11 先点击“TurtleBit”模块，找到并拖出“set RGBled     left_side R：0 G：0 B：0”指令方块2次并且都放入“repeat 4 times     do”指令方块中，点击第2个left_side后面的下拉三角形按钮选择right_side，再点击“变量”模块，找到并拖出变量指令方块“led-r”放入R后面的数字0处，其他的不变。

![](media/0905aaaa321890384666cc65a6a8f92e.png)

（5）点击“基础”模块，找到并拖出指令方块“暂停 (ms) 100”放入“repeat 4 times do”指令方块中，设置延时100毫秒。

![](media/a8cd3938a99ea2f65af0135227169d16.png)

（6）点击“变量”模块，找到并拖出变量指令方块以”1为幅度更改led-b”放入“重复
4 次
执行”指令方块中，点击led-b后面的下拉三角形按钮选择led-r。要使RGB红色灯逐渐变亮，R值的范围为0-255，这里设置变量“led-r”每次增加5，则需要增加51次，就将by后面的数字1改成5，把
重复 后面的数字4改成51。

![](media/bf1dc1875d292044055e4e0be08de1a1.png)

(7)复制代码串

![](media/bf1dc1875d292044055e4e0be08de1a1.png)

1次并放入“无限循环”指令方块中，要使RGB红色灯逐渐变暗，这里设置变量“led-r”每次减少5，则需要减少51次，就将by后面的数字5改成-5。

![](media/9df58e93df4be2eeed5249288c4157f4.png)

6  复制代码串

![](media/bf1dc1875d292044055e4e0be08de1a1.png)

1次并放入“无限循环”指令方块中，将R后面的变量指令方块“led-r”移到G后面的数字0处，点击led-r后面的下拉三角形按钮选择led-g，4个led-r都要改成led-g。其他的保持不变。

![](media/46a201a5e2c09a89410b5baaea10c286.png)

7  再次复制代码串

![](media/bf1dc1875d292044055e4e0be08de1a1.png)

1次并放入“无限循环”指令方块中，将R后面的变量指令方块“led-r”移到B后面的数字0处，点击led-r后面的下拉三角形按钮选择led-b，4个led-r都要改成led-b。其他的保持不变。

![](media/9c3399594f257b94fd84bf85bfdb7139.png)

完整的代码程序：

![](media/a8cba1dda8d00932230baaa4e9969c51.png)

①“当开机时”指令方块仅运行一次以启动程序。

②设置小车2个RGB灯的亮度为200。

③将led-r设为0

④将led-g设为0

⑤将led-b设为0

![](media/08040a04d2d1776aae233fd3db33424d.png)

⑥在“无限循环”指令方块之内，程序循环运行。

⑦do中的程序重复51次。

⑧设置左边RGB灯的R：led-r G：0 B：0

⑨设置右边RGB灯的R：led-r G：0 B：0

⑩延时时间100毫秒

⑪以5为幅度更改led-r

⑫do中的程序重复51次

⑬设置左边RGB灯的R：led-r G：0 B：0

⑭设置右边RGB灯的R：led-r G：0 B：0

⑮延时时间100毫秒

⑯以-5为幅度更改led-r

![](media/73d6cbe4da21b5d63b8190f62f737d2d.png)

⑰do中的程序重复51次。

⑱设置左边RGB灯的R：0 G：led-g B：0

⑲设置右边RGB灯的R：0 G：led-g B：0

⑳延时时间100毫秒

㉑以5为幅度更改led-g

㉒do中的程序重复51次。

㉓设置左边RGB灯的R：0 G：led-g B：0

㉟延时时间100毫秒

㊱以-5为幅度更改led-b

㉔设置右边RGB灯的R：0 G：led-g B：0

㉕延时时间100毫秒

㉖以-5为幅度更改led-g

![](media/e256e9baed9181f1fc974c2bfd03ecca.png)

㉗do中的程序重复51次。

㉘设置左边RGB灯的R：0 G：0 B：led-b

㉙设置右边RGB灯的R：0 G：0 B：led-b

㉚延时时间100毫秒

㉛以5为幅度更改led-b

㉜do中的程序重复51次

㉝设置左边RGB灯的R：0 G：0 B：led-b

㉞设置右边RGB灯的R：0 G：0 B：led-b

㉟延时时间100毫秒

㊱以-5为幅度更改led-b

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/d8a2e3ec5339ab77d37cf9e3201aa1d1.png)

![](media/7bb098127c5f4236a62ac09a96ca3f9e.png)

![](media/b7d31c9613724ff3fa5b756881d84f1a.png)

4实验结果：

按照之前的方式将代码1下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，乌龟车上2个RGB灯循环亮起红、绿、蓝、青、深红、黄、白7种颜色灯光。

按照之前的方式将代码2下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，乌龟车上2个RGB灯渐变显示不同颜色灯光。

### 15：4个WS2812 RGB灯亮起

![](media/b6f9010d508b3d2dadb50ae5175bd4ea.png)

1实验说明：

Micro:bit的电机驱动扩展板上自带4个WS2812 RGB灯，完全兼容micro bit控制板，是由micro bit的P8控制的。在这一课程中我们利用micro bit的P8控制端控制4个WS2812 RGB灯显示不同的状态。课程中，我们提供4个实验代码，让模块上4个WS2812 RGB灯分别显示4中不同的现象。

2  准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro：bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit扩展库。

如果选择手动拖动代码，则首先需要添加turtle-bit扩展库。

3  实验代码：

代码1：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit 测试程序完整版\815：4个WS2812 RGB灯亮起\Code-1|microbit-Code-1hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“Neopixel”模块，找到并拖出指令方块“将
strip 设为 引脚 P0初始化灯带 24 颗LED 模式 RGB(GRB
顺序)”放入指令方块“当开机时”中，由于4个WS2812 RGB灯的信号端P8对应的是由micro:bit的P8控制端控制的，所以点击P0后面的下拉三角形按钮选择P8。又因为只有4个WS2812 RGB灯，所以将leds前面的数字24改成4，点击RGB(GRB
顺序)后面的下拉三角形按钮选择RGB(GRB 顺序))。

![](media/53df28986ed7dadad82b99783ecd2584.png)

（2）点击“Neopixel”模块，找到并拖出指令方块“strip清除显示”放入指令方块“当开机时”中。

![](media/c0b03da30b597f4e492587320887696f.png)

（3）点击“Neopixel”模块，找到并拖出指令方块“strip
显示颜色 红”放入指令方块“无限循环”中。

![](media/2ef23313a263e3a7e721831d436c78c5.png)

（4）点击“基础”模块，找到并拖出指令方块“暂停 (ms) 100”放入“无限循环”指令方块中，设置延时1000毫秒。

![](media/30e5e76bf2241a8af80995cfd2fae141.png)

（5）复制代码串

![](media/30e5e76bf2241a8af80995cfd2fae141.png)

8次并放入“无限循环”指令方块中，点击red后面的下拉三角形按钮分别对应的选择橙、黄、绿、蓝、靛蓝、紫罗兰、紫、白其他的不变。

![](media/40b65ee2d1dd0c58f85800fd6f8ebca5.png)

完整的代码程序：

![](media/471f78499216b445676e27cf37b0a629.png)

①“当开机时”指令方块仅运行一次以启动程序。

②将strip设为引脚P8初始化灯带4颗LED（模式RGB（GRB顺序））

③关闭4个WS2812 RGB灯。

④在“无限循环”指令方块之内，程序循环运行。

⑤所有的RGB灯亮红色灯

⑥延时时间1000毫秒

⑦所有的RGB灯亮橙色灯

⑧延时时间1000毫秒

⑨所有的RGB灯亮黄色灯

⑩延时时间1000毫秒

⑪所有的RGB灯亮绿色灯

⑫延时时间1000毫秒

⑬所有的RGB灯亮蓝色灯

⑭延时时间1000毫秒

⑮所有的RGB灯亮靛蓝色灯

⑯延时时间1000毫秒

⑰所有的RGB灯亮紫罗兰色灯

⑱延时时间1000毫秒

⑲所有的RGB灯亮紫色灯

⑳延时时间1000毫秒

㉑所有的RGB灯亮白色灯

㉒延时时间1000毫秒

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/9235ac3f894fef7b71d4fcff347cd9e7.png)

代码2：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit 测试程序完整版\815：4个WS2812 RGB灯亮起\Code-2|microbit-Code-2hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

strip
设为 引脚 P0初始化灯带 24 颗LED 模式 RGB(GRB 顺序)(GRB
顺序)”放入指令方块“当开机时”中，由于4个WS2812 RGB灯的信号端P8对应的是由micro:bit的P8控制端控制的，所以点击P0后面的下拉三角形按钮选择P8。又因为只有4个WS2812 RGB灯，所以将leds前面的数字24改成4，点击RGB(GRB
顺序)后面的下拉三角形按钮选择RGB(GRB 顺序)。

![](media/53df28986ed7dadad82b99783ecd2584.png)

至
4执行”放入指令方块“无限循环”中，并将数字4改成3。

![](media/991b3c5367714beafe7f6282d7238035.png)

（3）点击“Neopixel”模块，找到并拖出指令方块“strip清除显示”放入指令方块“对于从
0 至 3执行”中。

![](media/9e3756ea4dd97563909f988bc7021076.png)

（4）先点击“Neopixel”模块，接着点击“Neopixel”模块下的“更多”，找到并拖出指令方块“strip
设置颜色 像素 0 为 红”放入指令方块“对于从 0 至
3执行”中，再点击“变量”模块，找到并拖出变量指令方块“index”放入指令方块“strip
设置颜色 像素 0 为 红”中的数字0处。

![](media/f86fa62c65eeb8c079158a3aa33a2e1f.png)

strip
刷新显示”放入指令方块“对于从 0 至 3执行”中。

![](media/5d9a64d94a424dd5b5f81baa33c17061.png)

（6）点击“基础”模块，找到并拖出指令方块“暂停 (ms) 100”放入“对于从 0 至 3执行”指令方块中，设置延时100毫秒。

![](media/9c6606546a555d2d1dea6311027c74d5.png)

（7）复制代码串

![](media/9c6606546a555d2d1dea6311027c74d5.png)

8次并都放入指令方块“无限循环”中，点击红后面的下拉三角形按钮分别对应的选择橙色、橙、黄、绿、蓝、靛蓝、紫罗兰、紫、白其他的不变。

完整的代码程序：

![](media/9bc67ccde913a1ce4c0f23952d6dcd8b.png)

①“当开机时”指令方块仅运行一次以启动程序。

②将strip设为引脚P8初始化灯带4颗LED（模式RGB（GRB顺序））

③在“无限循环”指令方块之内，程序循环运行。

④对于从0至3的index，执行do中的程序

⑤关闭4个WS2812 RGB灯。

⑥将4个WS2812 RGB灯设置像素index亮红色灯

⑦strip刷新显示

⑧延时时间100毫秒

⑨对于从0至3的index，执行do中的程序

⑩关闭4个WS2812 RGB灯。

⑪将4个WS2812 RGB灯设置像素index亮橙色灯

⑫strip刷新显示

⑬延时时间100毫秒

⑭对于从0至3的index，执行do中的程序

⑮关闭4个WS2812 RGB灯。

⑯将4个WS2812 RGB灯设置像素index亮黄色灯

⑰strip刷新显示

⑱延时时间100毫秒

![](media/d8f0e2255a459a41783e53ed2d4ba4ce.png)

⑲对于从0至3的index，执行do中的程序

⑳关闭4个WS2812 RGB灯

㉑将4个WS2812 RGB灯设置像素index亮绿色灯

㉒strip刷新显示

㉓延时时间100毫秒

㉔对于从0至3的index，执行do中的程序

㉕关闭4个WS2812 RGB灯

㉖将4个WS2812 RGB灯设置像素index亮蓝色灯

㉗strip刷新显示

㉘延时时间100毫秒

㉙对于从0至3的index，执行do中的程序

㉚关闭4个WS2812 RGB灯

㉛将4个WS2812 RGB灯设置像素index亮靛蓝色灯

㉜strip刷新显示

㉝延时时间100毫秒

㉞变量index的值处于0-17之间，执行do中的程序

㉟关闭条带上所有的RGB灯。

㊱将条带上18个RGB灯设置亮紫罗兰色灯

㊲条带显示所有的变化

㊳延时时间100毫秒

㊴变量index的值处于0-17之间，执行do中的程序

㊵关闭条带上所有的RGB灯。

㊶将条带上18个RGB灯设置亮紫色灯

㊷条带显示所有的变化

㊸延时时间100毫秒

㊹变量index的值处于0-17之间，执行do中的程序

㊺关闭条带上所有的RGB灯。

㊻将条带上18个RGB灯设置亮白色灯

㊼条带显示所有的变化

㊽延时时间100毫秒

![](media/27493d4a4dbf9ec2b2ec88f3185ceae2.png)

㉞对于从0至3的index，执行do中的程序

㉟关闭4个WS2812 RGB灯

㊱将4个WS2812 RGB灯设置像素index亮紫罗兰色灯

㊲strip刷新显示

㊳延时时间100毫秒

㊴对于从0至3的index，执行do中的程序

㊵关闭4个WS2812 RGB灯。

㊶将4个WS2812 RGB灯设置像素index亮紫色灯

㊷strip刷新显示

㊸延时时间100毫秒

㊹对于从0至3的index，执行do中的程序

㊺关闭4个WS2812 RGB灯

㊻将4个WS2812 RGB灯设置像素index亮白色灯

㊼strip刷新显示

㊽延时时间100毫秒

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/2e7b70f129f7d1499a1d1e5d5ae2243e.png)

![](media/7ef1503e633be63a18bb5128f0784a6e.png)

代码3：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit 测试程序完整版\815：4个WS2812 RGB灯亮起\Code-3|microbit-Code-3hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

strip
设为 引脚 P0初始化灯带 24 颗LED 模式 RGB(GRB 顺序)(GRB
顺序)”放入指令方块“当开机时”中，由于4个WS2812 RGB灯的信号端P8对应的是由micro:bit的P8控制端控制的，所以点击P0后面的下拉三角形按钮选择P8。又因为只有4个WS2812 RGB灯，所以将leds前面的数字24改成4，点击RGB(GRB
顺序)后面的下拉三角形按钮选择RGB(GRB 顺序)。

![](media/d4ca4decedd4a84c8e4da5217d34e47a.png)

（2）先点击“变量”模块，再点击“设置变量”出现“新变量的名称：”对话框，在对话框中输入R，点击“OK”，建立了变量“R”。用同样的方法分别建立变量“G”和“B”，拖出指令方块“set B to 0”放入“当开机时”指令方块中，复制指令方块“set B to 0”2次并放入“当开机时”指令方块中，点击第1个B后面的下拉三角形按钮选择R，再点击第2个B后面的下拉三角形按钮选择G。

![](media/52ce43afe66e0427f692a753d817fa61.png)

（3）点击“循环”模块，找到并拖出指令方块“对于从
0至3的 index
执行”放入指令方块“无限循环”中，并将数字4改成3”放入指令方块“无限循环”中;

![](media/a1c293cddee08ed3debaa27129a8b206.png)

设为
0”放入“对于从 0至3 的 index
执行”指令方块中，点击B后面的下拉三角形按钮选择R。再点击“数学”模块，找到并拖出方块“选取随机数，范围为0至10”放入指令方块“将
R 设为 0”中的数字0处，将数字0改成10，数字10改成255。

![](media/72563a27891fc20ca9cf8c8e84f1637f.png)

（5）复制代码块

![](media/82349f9643280908d1006a8370f4399b.png)

2次并放入“对于从
0至3 的 index
执行”指令方块中，点击R后面的下拉三角形按钮分别选择G和B，其他的不变。

![](media/e8655ffbd2579081bea09d0797ef415d.png)

（6）点击“Neopixel”模块，找到并拖出指令方块“strip
清除显示”放入指令方块“对于从 0 至 3执行”中。

![](media/5aee5f1df70e3cc4e15bf3bf405b4e88.png)

（7）先点击“Neopixel”模块，接着点击“Neopixel”模块下的“更多”，找到并拖出指令方块“strip
设置颜色 像素 0 为 红”放入指令方块“对于从 0 至
3执行”中，接着又从“Neopixel”模块下的“更多”中找到并拖出指令方块“红
255 绿 255 蓝
255”放入红处，再点击“变量”模块，找到并拖出变量指令方块“index”放入指令方块“strip
设置颜色 像素 0 为
红”中的数字0处，接着又分别拖出变量指令方块“R”放入红后面的数字255处，变量指令方块“G”放入绿后面的数字255处，变量指令方块“B”放入
蓝 后面的数字255处。

![](media/71b2fdc0f765654806dc5de95c3dae44.png)

（8）点击“基础”模块，找到并拖出指令方块“暂停 (ms) 100”放入“对于从 0 至 3执行”指令方块中，设置延时500毫秒。

![](media/4da8bdf863750067fa4ae42cb42c567c.png)

strip
刷新显示”放入指令方块“对于从 0 至 执行”中。

![](media/e065c60a06f3d9e3f6a1a55e247b1662.png)

完整的代码程序：

![](media/d9267277d9ede1ea05077d73b924c4a7.png)

①“当开机时”指令方块仅运行一次以启动程序。

②将strip设为引脚P8初始化灯带4颗LED（模式RGB（GRB顺序））

③将变量R设为0

④将变量R设为0

⑤将变量R设为0

⑥在“无限循环”指令方块之内，程序循环运行。

⑦变量index的值处于0-3之间，执行do中的程序

⑧将变量R设为10至255中的随机数

⑨将变量G设为10至255中的随机数

⑩将变量B设为10至255中的随机数

⑪关闭条带上所有的RGB灯。

⑫将4个WS2812 RGB设置颜色像素index为RGB（红R绿G蓝B）

⑬延时时间500毫秒

⑭strip刷新显示

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/71b44c0c75d36f577ac6953880d0c63e.png)

4实验结果：

按照以前的方式将代码1下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，micro:bit电机驱动扩展板上的4个WS2812RGB灯全亮，一种颜色变化，一直循环。

用同样的方法将代码2下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，micro:bit电机驱动扩展板上的4个WS2812RGB灯以流水灯的形式点亮，一条线一种颜色，一直循环；

用同样的方法将代码3下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，micro:bit电机驱动扩展板上的4个WS2812RGB灯以流水灯的形式点亮，每个灯亮起都是一种随机颜色，一直循环。

### 16：电机驱动 

![](media/f970c9eaf6017ca0ea2bad808d23b359.png)

1  实验说明：

 Keyes Micro：bit迷你智能乌龟车上配有两个直流减速电机，即[齿轮减速电机](https://baikebaiducom/item/%E9%BD%BF%E8%BD%AE%E5%87%8F%E9%80%9F%E7%94%B5%E6%9C%BA/3249233)，是在普通[直流电机](https://baikebaiducom/item/%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA/2404223)的基础上，加上配套齿轮减速箱。齿轮减速箱的作用是，提供较低的转速，较大的力矩。同时，[齿轮箱](https://baikebaiducom/item/%E9%BD%BF%E8%BD%AE%E7%AE%B1/1059341)不同的[减速比](https://baikebaiducom/item/%E5%87%8F%E9%80%9F%E6%AF%94/5341327)可以提供不同的转速和力矩。这大大提高了，直流电机在自动化行业中的使用率。[减速电机](https://baikebaiducom/item/%E5%87%8F%E9%80%9F%E7%94%B5%E6%9C%BA/3750851)是指[减速机](https://baikebaiducom/item/%E5%87%8F%E9%80%9F%E6%9C%BA/873618)和电机（马达）的集成体。这种集成体通常也可称为[齿轮马达](https://baikebaiducom/item/%E9%BD%BF%E8%BD%AE%E9%A9%AC%E8%BE%BE/7911602)或[齿轮电机](https://baikebaiducom/item/%E9%BD%BF%E8%BD%AE%E7%94%B5%E6%9C%BA/3377578)。减速电机广泛应用于钢铁行业、机械行业等。使用减速电机的优点是简化设计、节省空间。

Micro:bit电机驱动扩展板上包含PCA9685PW芯片和TB6612FNG芯片等，为了节约IO口资源，我们使用PCA9685PW芯片部分引脚来控制TB6612FNG电机芯片，并且TB6612FNG电机芯片是用来控制两个直流减速电机的转动方向和速度。我们来看一下Micro:bit电机驱动扩展板的示意图和两个芯片的电路图：

![](media/b55acb08d80cfe3315b96b7f4cdc100d.png)

PCA9685芯片由micro:bit板的llc端口控制，用于输出端口和扩展micro:bit板的IO端口。TB6612芯片由PCA9685芯片的LEDx引脚控制（引脚LED1和LED2控制左电机的方向，速度为LED0引脚；LED3和LED4引脚控制右电机的方向，速度为led5）

![](media/02e6c39452ef2e16b69eae1ba34b31e3.png)

![](media/8fe5e70058693bcfa59d040d71a328c9.png)

都已经插好在Micro:bit的电机驱动扩展板上（竖着方向），如下图所示，最好不要去改变它们的插入方向。这样，如果将我们提供的事例代码下载到microbit板后，电机转动的方向就与事例代码中设置的转动方向一致。

![](media/36c335fa3978a716de9f40996175be17.png)

如果把8个跳线帽都横着插在Micro:bit的电机驱动扩展板上，如下图所示，这样就会导致电机转动方向和事例代码中设置的方向相反，那就需要更改代码了。

![](media/a491869c9cf3c40db4a7b813c925b880.png)

2  准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro:bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit扩展库。

如果选择手动拖动代码，则首先需要添加turtle-bit扩展库。

3  实验代码：

代码1：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\816：电机驱动\Code-1|microbit-电机驱动-1hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）先点击“Led”模块，再点击“Led”模块下的“更多”，找到并拖出指令方块“led
启用
fasle”放入“当开机时”指令方块中，点击“false”后面的下拉三角形按钮选择“true”。

![](media/a27c8171ca4ab8543ab1e45070033f1b.png)

（2）点击“基础”模块，找到并拖出指令方块“显示箭头
北”放入“无限循环”指令方块中，点击 北
后面的下拉三角形按钮分别选择南。

![](media/8a73819612abdf969e72787bde2bd3ff.png)

0
%”放入“无限循环”指令方块中，数字0可以更改成0-100的任意数，这里将数字0改成100。

![](media/a1e62db6e053ed730eea11d3a6074625.png)

3  点击“基础”模块，找到并拖出指令方块“暂停 (ms)     100”放入指令方块“无限循环”中，设置延时时间为100毫秒。

![](media/c09708da87f9e6db7bd4185e19f1fdca.png)

4  复制代码串

![](media/c09708da87f9e6db7bd4185e19f1fdca.png)

1次并放入指令方块“无限循环”中，点击South后面的下拉三角形按钮选择North，又点击RunForward后面的下拉三角形按钮对应的选择RunBack，其他的不变。

![](media/106cd321ba2b12544c496e37d7d3db28.png)

（5）复制代码块“显示箭头
北”1次也放入指令方块“无限循环”中，并点击 北 后面的下拉三角形按钮选择
东 。

![](media/6e16f4ef729e594cf12a68403eee779e.png)

0
%”放入“无限循环”指令方块中，将数字0改成50；再复制代码块“LeftSide motor run Forward speed : 50
%”1次也放入“无限循环”指令方块中，点击LeftSide后面的下拉三角形按钮选择RightSide，并将数字50改成80。再复制指令方块“暂停
(ms) 1000”1次也放入指令方块“无限循环”中。

![](media/aeb6f311671c4b05fdb81884cb5818a5.png)

![](media/603eb811f6426f88e816f4cd3a688624.png)

（7）复制代码串1次并放入“无限循环”指令方块中，先点击
东 后面的下拉三角形按钮选
西，再将LeftSide后面的数字50改成100，RightSide后面的数字100改成50，其他的不变。

![](media/47e54b8c0eeaa27bc865a19abba49469.png)

![](media/69cb7be60eb7f9c9a0c1a120b4610fe2.png)

南
后面的下拉三角形按钮分别选择东和西，又点击RunForward后面的下拉三角形按钮分别对应的选择TurnLeft、TurnRight，其他的不变。

![](media/3e04d72918899c6a1e58e133919dc89e.png)

（9）点击“基础”模块，找到并拖出指令方块“显示
LED”放入指令方块“无限循环”中，点击灰蓝色小方框组成倒立的“❤”图案。

![](media/ff53ab1a94e157435f69c75a8d79a667.png)

（10）点击“K_Bit”模块，找到并拖出指令方块“car stop”放入“无限循环”指令方块中，接着复制指令方块“暂停 (ms) 1000”1次也放入指令方块“无限循环”中。

![](media/7ae2d41a4ea0782d122b7e8c7d29dcfe.png)

完整的代码程序：

![](media/2e74b9fa5e92c9602e584eed546f9a6b.png)

①“当开机时”指令方块仅运行一次以启动程序。

②打开LED点阵屏。

③在“无限循环”指令方块之内，程序循环运行。

④LED点阵显示箭头朝南的图案

⑤小车以100%速度向前走

⑥延时时间1000毫秒

⑦LED点阵显示箭头朝北的图案

⑧小车以100%速度向后走

⑨延时时间1000毫秒

⑩LED点阵显示箭头朝东的图案

⑪小车的左轮以50%速度前进

⑫小车的右轮以100%速度前进

⑬延时时间1000毫秒

⑭LED点阵显示箭头朝西的图案

⑮小车的左轮以100%速度前进

⑯小车的右轮以50%速度前进

⑰延时时间1000毫秒

⑱LED点阵显示箭头朝东的图案

⑲小车以100%速度原地左旋

⑳延时时间1000毫秒

㉑LED点阵显示箭头朝西的图案

㉒小车以100%速度原地右旋

㉓延时时间1000毫秒

㉔LED点阵显示箭头朝东的图案

㉕小车停止

㉖延时时间1000毫秒

![](media/e8ea714a0dac45f8d209ed3c00fee402.png)

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/1733cef56ab5d65bd7eed002396c0118.png)

代码2：

路线图

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\816：电机驱动\Code-2|microbit-电机驱动-2hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）先点击“Led”模块，再点击“Led”模块下的“更多”，找到并拖出指令方块“led
启用
fasle”放入“当开机时”指令方块中，点击“false”后面的下拉三角形按钮选择“true”。

![](media/a745aed806bdfa7f75e7b4ff2726ed87.png)

（2）先点击“变量”模块，再点击“设置变量”出现“新变量的名称：”对话框，在对话框中分别输入“a”，点击“OK”，建立了变量“a”。用同样的方法再建立变量“b”，拖出指令方块“将
b 设为 0”放入“当开机时”指令方块中，复制指令方块“将 b 设为
0”1次并放入“当开机时”指令方块中，点击第1个指令方块的b后面的下拉三角形按钮选择a。

![](media/7313040de88e6d636d0083b54c977584.png)

A
被按下时”，再点击“变量”模块，找到并拖出指令方块“以 1 为幅度更改
b”放入“当按钮 A
被按下时”指令方块中，点击b后面的下拉三角形按钮选择a，其他的不变。

![](media/2777cf22d12af8b0221bfe22d334023b.png)

（4）复制代码串

![](media/2777cf22d12af8b0221bfe22d334023b.png)

1次，点击A后面的下拉三角形按钮选择B，移除指令方块“以
1 为幅度更改 b”，再次点击“变量”模块，找到并拖出指令方块“将 b 设为
0”放入“当按钮 B 被按下时”指令方块中，将数字0改成1，其他的不变。

![](media/c522971810168d8e92ef00bf285f2c62.png)

（5）先点击“逻辑”模块，找到并拖出指令方块“如果为
true
则”放入“无限循环”指令方块中，接着又找到并拖出“=”方块放入true处的方框中，再点击“变量”模块，找到并拖出变量指令方块“a”放入“=”左侧，将“=”右侧的数字0改成1。

![](media/e48448464b68759cb7ace3ffe00bb809.png)

（6）点击“基础”模块，找到并拖出指令方块“显示
led”放入then下，点击灰蓝色小方框组成“L”图案。

![](media/894d29ec2ce7e12fa4fa5038a3dae40a.png)

（7）先点击“逻辑”模块，找到并拖出指令方块“如果为
true
则”放入第一个then下，接着又找到并拖出“=”方块放入true处的方框中，再点击“变量”模块，找到并拖出变量指令方块“b”放入“=”左侧，将“=”右侧的数字0改成1。

![](media/18ab430f5ed9758d8e1f3494dfd5d6e2.png)

0
%”放入第二个then下，将数字0改成80；再复制指令方块“暂停 (ms) 1000”1次也放入第二个then下。

![](media/5f21742533c6a68568eeda42aa7b89ea.png)

（9）复制代码串

![](media/0447bd87b6a8c0e23fabe872098d4caf.png)

1次也放入第二个then下，点击RunForward后面的下拉三角形按钮选择TurnLeft，将数字80改成65，再将延时1000毫秒改成延时650毫秒。

![](media/d053347b1aa0fede6e1215781c959565.png)

（10）又复制代码串

![](media/0447bd87b6a8c0e23fabe872098d4caf.png)

1次放入第二个then下，其他的不变。

![](media/f14a2352fd55af6bc02f21e3ff8831a1.png)

设为
0”也放入第二个 如果为 下。

![](media/087834535bd4bafad062359f65486b2b.png)

（12）先点击“逻辑”模块，找到并拖出指令方块“如果为
true
则”放入“无限循环”指令方块中，接着又找到并拖出“=”方块放入true处的方框中，再点击“变量”模块，找到并拖出变量指令方块“a”放入“=”左侧，将“=”右侧的数字0改成2。

![](media/6ba7fd3bac1108e573473c802e70db8d.png)

（13）点击“基础”模块，找到并拖出指令方块“刷新显示
leds”放入第三个then下，点击灰蓝色小方框组成“口”图案。

![](media/a3fe5d4d91af7df191d8b083479ace5f.png)

（14）先点击“逻辑”模块，找到并拖出指令方块“如果为
true
则”放入第三个then下，接着又找到并拖出“=”方块放入true处的方框中，再点击“变量”模块，找到并拖出变量指令方块“b”放入“=”左侧，将“=”右侧的数字0改成1。

![](media/262021dc43ab3d19af31e02e27921058.png)

（15）先点击“基础”模块，找到并拖出指令方块“暂停
(ms) 100”放入第四个then下，设置延时时间为1000毫秒；再点击“K_Bit”模块，找到并拖出指令方块“car RunForward speed: 0
%”放入第四个then下，将数字0改成80；再复制指令方块“暂停 (ms) 1000”1次也放入第四个then下。

![](media/8c5ef714f1e075c7265f53fa57e27ad9.png)

（16）
复制代码串

![](media/8c5ef714f1e075c7265f53fa57e27ad9.png)

1次也放入第四个then下，点击RunForward后面的下拉三角形按钮选择TurnLeft，将数字80改成65，再将延时1000毫秒改成延时620毫秒。

![](media/b65a16e4012badc603bec11814f77b21.png)

（17）复制代码串

![](media/b65a16e4012badc603bec11814f77b21.png)

2次也放入第四个then下，其他的不变。

![](media/d575d681aa4d003a1d41c67aad41d484.png)

（18）复制第二个then下的代码串

![](media/3df257c8d9d3cc89ff6acc6737f7350e.png)

1次放入第四个then下。

![](media/25eacf2b8ad1db7e2edb5f4dd9df7957.png)

（19）先点击“逻辑”模块，找到并拖出指令方块“如果为
true
则”放入“无限循环”指令方块中，接着又找到并拖出“=”方块放入true处的方框中，再点击“变量”模块，找到并拖出变量指令方块“a”放入“=”左侧，将“=”右侧的数字0改成3；再从“变量”模块中找到并拖出指令方块“set b to 0”放入第五个then下，点击b后面的下拉三角形按钮选择a，将数字0改成1。

![](media/4613c82d9fb3cacbbd4ff3a159213d8b.png)

完整的代码程序：

![](media/980582ef1d46052600be621d570d6058.png)

①“当开机时”指令方块仅运行一次以启动程序。

②打开LED点阵屏。

③将变量a设为0

④将变量b设为0

⑤当按钮A被按下时

⑥以1为幅度更改变量a

⑦当按钮A被按下时

⑧将变量b设为1

⑨在“无限循环”指令方块之内，程序循环运行。

⑩当变量a=1成立时，运行then下的程序

⑪LED点阵显示“L”图案

⑫当变量b=1成立时，运行then下的程序

⑬延时时间1000毫秒

⑭小车以80%速度向前走

⑮延时时间1000毫秒

⑯小车以65%速度向左旋

⑰延时时间650毫秒

![](media/ebe8ff0061cb0ab74f37ff937fd302f5.png)

⑱小车以80%速度向前走

⑲延时时间1000毫秒

⑳小车停止

㉑将变量b设为0

㉒当变量a=2成立时，运行then下的程序

㉓LED点阵显示“口”图案

㉔当变量b=1成立时，运行then下的程序

㉕延时时间1000毫秒

㉖小车以80%速度向前走

㉗延时时间1000毫秒

㉘小车以65%速度向左旋

㉙延时时间620毫秒

㉖小车以80%速度向前走

㉗延时时间1000毫秒

㉘小车以65%速度向左旋

㉙延时时间620毫秒

㉚小车以80%速度向前走

㉛延时时间1000毫秒

㉜小车以65%速度向左旋

㉝延时时间620毫秒

㉞小车以80%速度向前走

㉟延时时间1000毫秒

㊱小车停止

㊲将变量b设为0

㊳当变量a=3成立时，运行then下的程序

㊴将变量a设为1

![](media/2da3645b136395202735e76a7c36e479.png)

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/aa9523b3a85da2221c133023ab568bf0.png)

![](media/ec0b88dcfb1a273bb343879ebc1599ea.png)

4实验结果：

按照之前的方式将代码1下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，我们可以看到小车将前进1s，后退1s，左转1s，右转1s，原地左旋1s，原地左旋1s，停止1s，并且每种运动状态下LED点阵显示对应图案。一直循环。

用同样的方法将代码2下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，当我们第一次按A键时，LED点阵会显示“L”图案，再按B键，可以看到小车前进的路径是“L”；当我们第二次按A键时，LED点阵会显示“口”图案，再按B键，可以看到小车前进的路径是“口”；当我们第三次按A键时，LED点阵会显示“L”，再按B键，可以看到小车前进的路径是“L”；
；保持循环处于这种状态。

([How to download?](#A01) [How to quick download?](#快速下载))

### 17：循迹小车

#### 171：循迹传感器测试

![](media/5e907f1f6c08a05733ef2943bf2bcbf5.jpg)

1 实验说明：

keyes Micro:bit迷你智能乌龟车上包含一个3路循迹传感器模块，并且传感器模块上自带有三个电位器，用于调节循迹传感器敏感度。循迹传感器其实也是红外传感器，这里的循迹传感器模块用到的元件是TCRT5000红外对管，TCRT5000红外对管具有一个高发射功率红外发射二极管和一个高灵敏度红外接收管。当发射管的红外信号经反射被接收管接收后，接收管的电阻会发生变化，在电路上一般以电压的变化体现出来。电阻的变化取决于接收管所接收的红外信号强度，常表现在反射面的颜色和反射面接收管的距离。在检测的时候，黑色高电平有效，白色是为低电平有效。

红外对管寻迹：

当乌龟车在白色底面行驶时，装在车下的红外发射管发射红外信号，经白色发射后，被接收管接收，一旦接收管接收到信号，输出端将输出低电平（0）；当乌龟车行驶到黑线时，红外线信号被黑色吸收后，将输出高电平（1），从而实现了通过红外线检测信号的功能。将检测到的信号送到单片机的I/O口，当I/O口检测到的信号为高电平（1）时，表明乌龟车处于黑色的引线上；同理，当I/O口检测到的信号为低电平（0）时，表明乌龟车处于白色地面上。

根据上面的接线图可知，乌龟车上的3路循迹传感器模块集成端口是接在micro:bit
电机驱动扩展板上G 5V P14 P15 P16集合端口，是由micro:bit的P14、P15和P16控制的。3路循迹传感器模块上的左边TCRT5000红外对管是由micro bit的P14控制，中间TCRT5000红外对管是由micro bit的P15控制，右边TCRT5000红外对管是由micro bit的P16控制。在乌龟车底部放上白纸，我们通过旋转3路循迹传感器模块上自带的三个电位器，当传感器模块上的指示灯亮起时，再拿起小车使乌龟车上的两车轮离白纸的高度大概都是05cm，传感器模块上的指示灯熄灭，这时灵敏度就调节好了。

2  准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro：bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit扩展库。

如果选择手动拖动代码，则首先需要添加turtle-bit扩展库。

3  实验代码：

代码1：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\817：循迹小车\8171：循迹传感器测试\Code-1|microbit-循迹传感器测试-1hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“高级”下的“串行”模块，找到并拖出指令方块“串行
重定向到 USB”放入“当开机时”指令方块中。

![](media/350e57677ddb0e43992f64b32bd808c1.png)

（2）点击“高级”下的“串行”模块，找到并拖出指令方块“串行
写入数值“x”=0”放入“无限循环”指令方块中，再点击“引脚”模块，找到并拖出指令方块“数字读取引脚
P0 ”放入指令方块“串行 串行写入数值
“x”=0”中的0处，由于3路循迹传感器模块上的左边TCRT5000红外对管是由micro bit的P14控制，中间TCRT5000红外对管是由micro bit的P15控制，右边TCRT5000红外对管是由micro bit的P16控制，这里就以左边TCRT5000红外对管读取数字信号为例，点击P0后面的下拉三角形按钮选择P14，将“x”改成“digital signal”。

![](media/78ce9925ce318c002998765d5f421385.png)

（3）点击“基础”模块，找到并拖出指令方块“暂停 (ms) 100”放入“无限循环”指令方块中，设置延时200毫秒。

![](media/df7d2072e7f9462ea6b937393d7e038f.png)

完整的代码程序：

![](media/87d373733ac869edf1b8e32d4e112b87.png)

①“当开机时”指令方块仅运行一次以启动程序。

②串行重定向USB。

③在“无限循环”指令方块之内，程序循环运行。

④串行写入digital signal=P14读取的数字信号（1/0）

⑤延时时间200毫秒

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/39d009652323a629c61c699789f06e8e.png)

按照之前的方式将代码1下载到microbit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，接下来点击显示数据(设备)按钮：

([How to quick download?](#快速下载))

![](media/830072d6e2029a76637886938d22f900.png)

显示数据(设备)中显示了乌龟车上3路循迹传感器模块的左边TCRT5000红外对管检测到的数字信号，当左边TCRT5000红外对管检测到白色物体时，串口监视器窗口显示低电平（0），同时传感器模块对应的左边指示灯亮起；当左边TCRT5000红外对管检测到黑色物体或未检测到物体时，串口监视器窗口显示高电平（1），同时传感器模块对应的左边指示灯不亮。如下图：

![](media/c8fb471be9d430db24ecc3cc7162850d.png)

如果你的电脑系统是Windows7/8而不是Windows 10，则在Google Chrome中是不能进行设备配对，从而读取不了相应的数字信号或模拟信号，可是又需要读取相应的传感器/模块的数字信号或模拟信号，那怎么办呢？这里就可以使用CoolTerm软件来读取串口的。

打开CoolTerm，点击Options，选择串行Port，设置COM口和波特率，波特率设置为115200（经过测试，micro:bit的USB串口通讯波特率是115200），点击OK后，最后点击Connect。这样，CoolTerm串口监视器显示出3路循迹传感器模块上左边TCRT5000红外对管读取的数字信号。如下图：

![](media/e7703bb10f45bac4033ab44958dcb248.png)

代码2：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\817：循迹小车\8171：循迹传感器测试\Code-2|microbit-循迹传感器测试-2hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）先点击“Led”模块，再点击“Led”模块下的“更多”，找到并拖出指令方块“led
启用
fasle”放入“当开机时”指令方块中，点击“false”后面的下拉三角形按钮选择“true”。

![](media/76c0b3b54a37d6f530f555562e5efd68.png)

设为
0”2次并放入“当开机时”指令方块中，点击第1个RR后面的下拉三角形按钮选择LL，第2个RR后面的下拉三角形按钮选择CC。

![](media/94494828d530c37e06660b8e7ca96974.png)

设为
0”放入“无限循环”指令方块中，点击RR后面的下拉三角形按钮选择LL；再点击“高级”下的“引脚”模块，找到并拖出指令方块“数字读取引脚
P0”放入to后面的数字0处。复制代码块“set LL to 数字读取引脚
P0”2次也放入“无限循环”指令方块中，将第二个LL改成CC，第三个LL改成RR。由于3路循迹传感器模块上的左边TCRT5000红外对管是由micro bit的P14控制，中间TCRT5000红外对管是由micro bit的P15控制，右边TCRT5000红外对管是由micro bit的P16控制，所以把LL后面的P0改成P14，CC后面的P0改成P15，RR后面的P0改成P16。

![](media/d456b1c0d7303e08d84a3e548fae772c.png)

true
则否则”放入“无限循环”指令方块中，点击“

![](media/7498c9151101cb7e9756a8b0a5485f90.png)

”图案6次，接着找到并拖出一个“与”方块放入true处的方框中，再拖出一个“与”方块放入第一个
与 后面的方框中。

![](media/39d8e5f74783faa6189f3e1637ae4b31.png)

与
左侧，再点击“变量”模块，找到拖出变量指令方块“LL”放入“=”左侧，“=”右侧的数字0不变。接着复制代码块“LL=0”2次分别放入第一个
与
右侧的两个方框中，点击第二个LL后面的下拉三角形按钮选择CC，将数字0改成1；点击第三个LL后面的下拉三角形按钮选择RR，将数字0改成1。

![](media/ec24b956681a4cffba9092b2b1eef576.png)

（6）点击“基础”模块，找到并拖出指令方块“显示LED”放入第一个
如果为 下，点击右侧的灰蓝色小方框组成“I”图案。

![](media/cde7a80aa1910c0f65cbd186f4b85295.png)

RR=1”1次放入第一个
否则如果为
后面的方框中，将LL后面的第一个数字0改成1，将CC后面的第一个数字1改成0，其他的不变。

![](media/01e08b891ac52075ba83ae257df687d4.png)

（8）点击“基础”模块，找到并拖出指令方块“显示LED”放入第二个
如果为 下，点击中间的灰蓝色小方框组成“I”图案。

![](media/6bea1b36dd7081eacea9d659cf26e245.png)

与
RR=1”1次放入第二个否则如果为
后面的方框中，将CC后面的第一个数字0改成1，再将RR后面的数字1改成0，其他的不变。

![](media/ff2c958a86a38699bc03d47d171a66f4.png)

8  点击“基础”模块，找到并拖出指令方块“显示LED”放入第三个
    如果为 下，点击左侧的灰蓝色小方框组成“I”图案。

![](media/132354d2b2bc7486d5b8d236b6c3b767.png)

9  与
    RR=0”1次放入第三个否则如果为
    后面的方框中，将LL和CC后面数字1改成0，再将RR后面的数字0改成1，其他的不变。

![](media/73bc30ca84cb58c218cd05179173eec9.png)

10 点击“基础”模块，找到并拖出指令方块“显示图标”放入第四个
    如果为
    下，点击“❤”图案后面的下拉三角形按钮选择“

![](media/2460d7af23daf89d2ee7b245ff86553b.png)

”图案。

![](media/184d78afea155127d3e65650b375385a.png)

11 与
    RR=1”1次放入第四个否则如果为
    后面的方框中，将CC后面的第一个数字0改成1，再将RR后面的数字1改成0，其他的不变。

![](media/8c04c37d724d9642bba261838b6cdf3d.png)

12 点击“基础”模块，找到并拖出指令方块“显示图标”放入第五个
    如果为
    下，点击“❤”图案后面的下拉三角形按钮选择“

![](media/1ff4447b63b0fe664f665ff16bb0ecb5.png)

”图案。

![](media/388f825c5a6e1c222e67943620d9bb23.png)

13 与
    RR=0”1次放入第五个否则如果为
    后面的方框中，将LL后面的第一个数字0改成1，再将CC后面的第一个数字1改成0，其他的不变。

![](media/6a9cafeb569743e32a43ce87f6265576.png)

14 点击“基础”模块，找到并拖出指令方块“显示图标”放入第六个
    如果为
    下，点击“❤”图案后面的下拉三角形按钮选择“

![](media/531a60d7dfb2c47e17072a6067e970cd.png)

”图案。

![](media/b3f577d14c7aeff6b644dc83d7b47551.png)

15 与
    RR=1”1次放入第六个否则如果为
    后面的方框中，将CC和RR后面的数字0改成1，其他的不变。

![](media/bbe198fec04e5296e3e538ab89d7da43.png)

16 点击“基础”模块，找到并拖出指令方块“显示图标”放入第七个
    如果为
    下，点击“❤”图案后面的下拉三角形按钮选择“

![](media/06f2f4c6916407a5f44c77a27d1b65cb.png)

”图案，再拖出指令方块“显示图标”放入
    否则 下，其他的不变。

![](media/5822a1a033e186daf762aea5fb492dd7.png)

完整的代码程序：

![](media/dd5f49b8ddac30810040f08cd41a15e7.png)

⑭当变量LL=1和CC=1和RR=0成立时，执行then下的程序

⑮LED点阵右边显示“I”图案

⑯当变量LL=0和CC=0和RR=1成立时，执行then下的程序

⑰LED点阵右边显示“![](media/2460d7af23daf89d2ee7b245ff86553b.png)”图案

⑱当变量LL=0和CC=1和RR=0成立时，执行then下的程序

⑲LED点阵右边显示“![](media/1ff4447b63b0fe664f665ff16bb0ecb5.png)”图案

⑳当变量LL=1和CC=0和RR=0成立时，执行then下的程序

㉑LED点阵右边显示“![](media/531a60d7dfb2c47e17072a6067e970cd.png)”图案

㉒当变量LL=1和CC=1和RR=1成立时，执行then下的程序

㉓LED点阵右边显示“![](media/06f2f4c6916407a5f44c77a27d1b65cb.png)”图案

㉔当上述条件都不成立时，执行else下的程序

㉕LED点阵显示“❤”图案

①“当开机时”指令方块仅运行一次以启动程序。

②打开LED点阵。

③将变量LL设为0

④将变量CC设为0

⑤将变量RR设为0

⑥在“无限循环”指令方块之内，程序循环运行。

⑦将变量LL设为P14读取的数字信号（1/0）

⑧将变量CC设为P15读取的数字信号（1/0）

⑨将变量LL设为P16读取的数字信号（1/0）

⑩当变量LL=0和CC=1和RR=1成立时，执行then下的程序

⑪LED点阵左边显示“I”图案

⑫当变量LL=1和CC=0和RR=1成立时，执行then下的程序

⑬LED点阵中间显示“I”图案

![](media/191bb46382485907ea8128d0133c03b7.png)

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/7b7fa361f1f3d51e52ec06c1e93fa746.png)

![](media/e3d0cb549c86e517b96bb03fec7026b5.png)

代码3：

代码2看起来是不是有点儿复杂，能不能对它简化呢？回答是，可以的。我们可以利用外加的库文件中的指令方块“

![](media/1dc4bbb19e0ebf13c9f17cce2beba90e.png)

”来简化它，我们已经通过代码1实验知道循迹传感器模块中的左边TCRT5000红外对管读取的数字信号（高电平（1）和低电平（0））。由于循迹传感器模块中的3个TCRT5000红外对管组成3路巡线，所以是可以用3位二进制数来表示循迹传感器模块的3路巡线值，但是我们把用3位二进制数来表示3路巡线值转化成用1位十进制数来表示3路巡线值就更好了，如下图。这样，代码就可以大大的简化。

<table style="width:100%;">

<td colspan="3">循迹传感器模块上的左、中、右TCRT5000红外对管（电平）|二进制|十进制|
|低电平（0）|低电平（0）|高电平（1）|001|1|
|低电平（0）|高电平（1）|低电平（0）|010|2|
|低电平（0）|高电平（1）|高电平（1）|011|3|
|高电平（1）|低电平（0）|低电平（0）|100|4|
|高电平（1）|低电平（0）|高电平（1）|101|5|
|高电平（1）|高电平（1）|低电平（0）|110|6|
|高电平（1）|高电平（1）|高电平（1）|111|7|
|低电平（0）|低电平（0）|低电平（0）|000|0|

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\817：循迹小车\8171：循迹传感器测试\Code-3|microbit-循迹传感器测试-3hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“高级”下的“串行”模块，找到并拖出指令方块“串行
重定向到 USB”放入“当开机时”指令方块中。

![](media/b5f11634338b748db43490a6bdc54ab0.png)

（2）先点击“变量”模块，再点击“设置变量”出现“新变量的名称：”对话框，在对话框中输入val，点击“OK”，建立了变量“val”，拖出指令方块“将
val 设为0”放入“当开机时”指令方块中。

![](media/3b38ece951c8be3881ddb2f98afb4f7b.png)

设为
0”放入“无限循环”指令方块中，再点击“TurtleBit”模块，找到并拖出指令方块“Line Tracking”放入to后面的数字0处。

![](media/8a8954136965e14788aab4cc0c3fdc74.png)

（4）点击“高级”下的“串行”模块，找到并拖出指令方块“串行
串行写入数值
“x”=0”放入“无限循环”指令方块中，再点击“变量”模块，找到并拖出变量指令方块“val”放入指令方块“串行
串行写入数值 “x”=0”中的数字0处。

![](media/04fb5aef1463c0b015e69a7c0df839a9.png)

true
则否则”放入“无限循环”指令方块中，点击“

![](media/7498c9151101cb7e9756a8b0a5485f90.png)

”图案6次，接着找到并拖出“=”方块放入true处的方框中。

![](media/e9a3d5df4e85fceeb7b13b21a0cd524e.png)

（6）点击“变量”模块，找到并拖出变量指令方块“val”放入“=”左侧方框，将“=”右侧的数字0改成3。

![](media/12434232bb6dd63dd4f83ccbf0eb8988.png)

（7）点击“基础”模块，找到并拖出指令方块“显示LED”放入第一个
如果为 下，点击右侧的灰蓝色小方框组成“I”图案。

![](media/acc3e246363a22cae48bf7ef0f7ff44d.png)

”1次放入第一个否则如果为
后面的方框中，将“=”右侧的数字3改成5。

![](media/3c16e606d7ee58f4c727370cbeaaee2e.png)

（9）点击“基础”模块，找到并拖出指令方块“显示LED”放入第二个
如果为 下，点击中间的灰蓝色小方框组成“I”图案。

![](media/9fed17b85470c2a156918c7fd1959fda.png)

”1次放入第二个否则如果为
后面的方框中，将“=”右侧的数字5改成6。

![](media/e1a4ec167c7b6a38b5e302f28dee8664.png)

（11）点击“基础”模块，先找到并拖出指令方块“显示LED”放入第三个then下，点击左侧的灰蓝色小方框组成“I”图案。

![](media/335042c600aa55e415fd58c2e3bbef27.png)

”1次放入第三个否则如果为
后面的方框中，将“=”右侧的数字6改成1。

![](media/d0a4c4b29cef877c0dda19212b2a13a5.png)

13 点击“基础”模块，先找到并拖出指令方块“显示图标”放入第四个
    如果为
    下，点击“❤”图案后面的下拉三角形按钮选择“

![](media/c0ef63598e460f019fbc4d80b011a879.png)

”图案。

![](media/dc32be5c8af1697818ecdff8dfbb9598.png)

14 复制代码块“val=1”1次放入第四个否则如果为
    后面的方框中，将“=”右侧的数字1改成2。

![](media/7977c449e34c5fc0ff9445fabf253a90.png)

15 点击“基础”模块，先找到并拖出指令方块“显示图标”放入第五个
    如果为
    下，点击“❤”图案后面的下拉三角形按钮选择“

![](media/622e4e7a8be38473c96c703401bb5d41.png)

”图案。

![](media/42a128996e1aa7a5fe8e108a23ee7e96.png)

16 复制代码块“val=2”1次放入第五个否则如果为
    后面的方框中，将“=”右侧的数字2改成4。

![](media/a673612a14743d736a9df9c0aec55d59.png)

17 点击“基础”模块，先找到并拖出指令方块“显示图标”放入第六个
    如果为
    下，点击“❤”图案后面的下拉三角形按钮选择“

![](media/ef2f4a2a1996963693b9033b92de5c8d.png)

”图案。

![](media/dfea9df5c36654cdad830c6d9138bd66.png)

18 否则如果为
    后面的方框中，将“=”右侧的数字4改成7。

![](media/48338e14e3156839e5db00f549a05d19.png)

17 点击“基础”模块，找到并拖出指令方块“显示图标”放入第七个
    如果为
    下，点击“❤”图案后面的下拉三角形按钮选择“

![](media/06f2f4c6916407a5f44c77a27d1b65cb.png)

”图案，再拖出指令方块“显示图标”放入
    否则 下，其他的不变。

![](media/805d5146d4b19841e97f0104550b641a.png)

完整的代码程序

![](media/0e9e31f17a5f7e8bcf3fba0626c8976c.png)

①“当开机时”指令方块仅运行一次以启动程序。

②串行重定向USB。

③将变量val设为0

④在“无限循环”指令方块之内，程序循环运行。

⑤将变量val为Line Tracking

⑥串行写入数值x=val

⑦当变量val=3成立时，执行 如果为 下的程序

⑧LED点阵左边显示“I”图案

⑨当变量val=5成立时，执行 如果为 下的程序

⑩LED点阵中间显示“I”图案

⑪当变量val=6成立时，执行 如果为 下的程序

⑫LED点阵右边显示“I”图案

⑬当变量val=1成立时，执行 如果为 下的程序

⑭LED点阵显示“![](media/aaa1b518e463aef56f86c35ab6f0d1df.png)”图案

⑮当变量val=2成立时，执行 如果为 下的程序

⑯LED点阵显示“![](media/622e4e7a8be38473c96c703401bb5d41.png)”图案

⑰当变量val=4成立时，执行 如果为 下的程序

⑱LED点阵显示“![](media/ef2f4a2a1996963693b9033b92de5c8d.png)”图案

⑲当变量val=7成立时，执行 如果为 下的程序

⑳LED点阵显示“![](media/06f2f4c6916407a5f44c77a27d1b65cb.png)”图案

㉑当上述条件都不成立时，执行else下的程序

㉒LED点阵显示“❤”图案

![](media/14b06fbe3a950b2f6cac285563f7e401.png)

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/1bb8adae7e921dfbe419d3380796e8c4.png)

3实验结果：

按照之前的方式将代码2下载到micro：bit，乌龟车上的循迹传感器模块只有左边的TCRT5000红外对管检测到白色物体时，micro bit LED点阵左边显示“I”图案，同时循迹传感器模块左边的指示灯亮起；

乌龟车上的循迹传感器模块只有中间的TCRT5000红外对管检测到白色物体时，micro bit LED点阵中间显示“I”图案，同时循迹传感器模块中间的指示灯亮起；

乌龟车上的循迹传感器模块只有右边的TCRT5000红外对管检测到白色物体时，micro bit LED点阵右边显示“I”图案，同时循迹传感器模块右边的指示灯亮起；

乌龟车上的循迹传感器模块只有左边的和中间的TCRT5000红外对管检测到白色物体时，micro bit LED点阵显示“

![](media/29cf9222b824d836caec029221ef612b.png)

”图案，同时循迹传感器模块左边的和中间的指示灯都亮起；

乌龟车上的循迹传感器模块只有左边的和右边的TCRT5000红外对管检测到白色物体时，micro bit LED点阵显示“

![](media/d9020ea20c11e4dd92d59452e6a39481.png)

”图案，同时循迹传感器模块左边的和右边的指示灯都亮起；

乌龟车上的循迹传感器模块只有中间的和右边的TCRT5000红外对管检测到白色物体时，micro bit LED点阵显示“

![](media/fd3df0126ac849ed4b39d614731d9364.png)

”图案，同时循迹传感器模块中间的和右边的指示灯都亮起；

乌龟车上的循迹传感器模块左边的、中间的和右边的TCRT5000红外对管都检测到黑色物体或都未检测到物体时，micro bit LED点阵左边显示“

![](media/502de9d63a87351f5d18b914c8d529c4.png)

”图案，同时循迹传感器模块左边的、中间的和右边的指示灯都不亮；

乌龟车上的循迹传感器模块左边的、中间的和右边的TCRT5000红外对管都检测到白色物体时，micro bit LED点阵显示“❤”图案，同时循迹传感器模块左边的、中间的和右边的指示灯都亮起。

用同样的方法，将代码3下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，接下来点击显示数据(设备)按钮：

([How to quick download?](#快速下载))

![](media/936cc70790090f6553c90be6e0d3edc2.png)

乌龟车上的循迹传感器模块只有左边的TCRT5000红外对管检测到白色物体时，显示数据(设备)中显示3（如下图），micro bit LED点阵左边显示“I”图案，同时循迹传感器模块左边的指示灯亮起；

乌龟车上的循迹传感器模块只有中间的TCRT5000红外对管检测到白色物体时，显示数据(设备)中显示5（如下图），micro bit LED点阵中间显示“I”图案，同时循迹传感器模块中间的指示灯亮起；

乌龟车上的循迹传感器模块只有右边的TCRT5000红外对管检测到白色物体时，显示数据(设备)中显示6（如下图），micro bit LED点阵右边显示“I”图案，同时循迹传感器模块右边的指示灯亮起；

乌龟车上的循迹传感器模块只有左边的和中间的TCRT5000红外对管检测到白色物体时，显示数据(设备)中显示1（如下图），micro bit LED点阵显示“

![](media/29cf9222b824d836caec029221ef612b.png)

”图案，同时循迹传感器模块左边的和中间的指示灯都亮起；

乌龟车上的循迹传感器模块只有左边的和右边的TCRT5000红外对管检测到白色物体时，显示数据(设备)中显示2（如下图），micro bit LED点阵显示“

![](media/d9020ea20c11e4dd92d59452e6a39481.png)

”图案，同时循迹传感器模块左边的和右边的指示灯都亮起；

乌龟车上的循迹传感器模块只有中间的和右边的TCRT5000红外对管检测到白色物体时，显示数据(设备)中显示4（如下图），micro bit LED点阵显示“

![](media/fd3df0126ac849ed4b39d614731d9364.png)

”图案，同时循迹传感器模块中间的和右边的指示灯都亮起；

乌龟车上的循迹传感器模块左边的、中间的和右边的TCRT5000红外对管都检测到黑色物体或都未检测到物体时，显示数据(设备)中显示7（如下图），micro bit LED点阵左边显示“

![](media/502de9d63a87351f5d18b914c8d529c4.png)

”图案，同时循迹传感器模块左边的、中间的和右边的指示灯都不亮；

乌龟车上的循迹传感器模块左边的、中间的和右边的TCRT5000红外对管都检测到白色物体时，micro bit LED点阵显示“❤”图案，同时循迹传感器模块左边的、中间的和右边的指示灯都亮起。

![](media/c0b116c7489a72ed64fe419083a12e0f.png)

如果你的电脑系统是Windows7/8而不是Windows 10，则在Google Chrome中是不能进行设备配对，从而读取不了相应的数字信号或模拟信号，可是又需要读取相应的传感器/模块的数字信号或模拟信号，那怎么办呢？这里就可以使用CoolTerm软件来读取串口的。

打开CoolTerm，点击Options，选择串行Port，设置COM口和波特率，波特率设置为115200（经过测试，micro:bit的USB串口通讯波特率是115200），点击OK后，最后点击Connect。这样，CoolTerm串口监视器显示出3路循迹传感器读取的1位十进制数。

![](media/657f51412bbc33d9b89f4e74f467c3a1.jpg)

#### 172：循迹小车

![](media/14aa0a216d845607828ac77ec6d8fb62.jpg)

1实验说明：

前面的部分我们学习了循迹传感器和电机驱动的原理和应用，下面我们要结合这两个基本的循迹传感器和电机驱动来做一款循迹小车。

循迹，意思就是循着轨迹，也就是我们经常会看到的走黑线的循迹小车，原理是利用循迹传感器对路面黑色轨迹进行检测，并将路面检测信号反馈给micro bit主板。micro bit主板对采集到的信号予以分析判断，及时控制驱动电机以调整小车转向，从而使小车能够沿着黑色轨迹自动行驶，实现循迹小车自动寻迹的目的。

循迹小车行驶原理：循迹小车根据3路循迹传感器传输的巡线值采取不同的行动。

<td colspan="3">循迹传感器模块上的左、中、右TCRT5000红外对管（电平）|二进制|十进制|乌龟车的行动|
|低电平（0）|低电平（0）|高电平（1）|001|1|向右转|
|低电平（0）|高电平（1）|低电平（0）|010|2|前进|
|低电平（0）|高电平（1）|高电平（1）|011|3|前进|
|高电平（1）|低电平（0）|低电平（0）|100|4|向左转|
|高电平（1）|低电平（0）|高电平（1）|101|5|前进|
|高电平（1）|高电平（1）|低电平（0）|110|6|前进|
|高电平（1）|高电平（1）|高电平（1）|111|7|前进|
|低电平（0）|低电平（0）|低电平（0）|000|0|停止|

![](media/7abb567990baeeb9bb4694b578c1f670.png)

根据上面的接线图可知，乌龟车上的3路循迹传感器模块集成端口是接在micro:bit
电机驱动扩展板上G 5V P14 P15 P16集合端口，是由micro:bit的P14、P15和P16控制的。

2  准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro：bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit扩展库

如果选择手动拖动代码，则首先需要添加turtle-bit扩展库。

[警告：3路循迹传感器应避免在阳光等有红外干扰的环境中使用。阳光中含有大量的不可见光，如红外线和紫外线。在阳光强烈的环境下，3路循迹传感器不能正常工作。](#M11)

3  编程思路：

程序流程图：

![](media/7e620e084d9c76cf9732c45d18a6727d.png)

4  实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\817：循迹小车\8172：循迹小车|microbit-循迹小车hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

1  点击“基础”模块，找到并拖出指令方块“显示图标
    ♥”放入“当开机时”指令方块中，点击“❤”图案后面的下拉三角形按钮选择“

![](media/b9b97ec13c745120243516b57a2f2fbc.png)

”图案。

![](media/69eb2e26f9e5d4b11040290e8c5282bd.png)

2  点击“Neopixel”模块，找到并拖出指令方块“将 strip     设为 引脚 P0初始化灯带 24 颗LED 模式 RGB(GRB 顺序)(GRB     顺序)”放入指令方块“当开机时”中，由于4个WS2812RGB灯的信号端P8对应的是由micro：bit的P8控制端控制的，所以点击P0后面的下拉三角形按钮选择P8。又因为只有4个WS2812     RGB灯，所以将led前面的数字24改成4，点击 RGB(GRB     顺序)后面的下拉三角形按钮选择RGB(GRB 顺序)。

![](media/4fb61b18f09ceba0dfc0951b9d2890ca.png)

（4）又点击“Neopixel”模块，找到并拖出指令方块“strip清除显示”放入指令方块“当开机时”中。

![](media/c1b9c63b13ae7984208fa5a46e94686a.png)

设为
0”放入“无限循环”指令方块中。再点击“TurtleBit”模块，找到并拖出“Line Tracking”指令方块放入 设为 后面的数字0处。

![](media/8b964c67b1c46d378603dc1400b7d8e5.png)

true
则否则”放入“无限循环”指令方块中，点击“

![](media/08875ea2865d2ebad8c6bb016f6b4531.png)

”图案2次，接着找到并拖出1个“or”方块放入true处方框中，再拖出1个“or”方块放入or右侧方框中，拖出2个“or”方块叠在一起放入第2个or右侧方框中。

![](media/defb2cad5b8bcd97db1668721f1e3f8a.png)

或
左侧方框中，再点击“变量”模块，找到并拖出变量指令方块“tracking values”放入“=”的左侧，将“=”右侧的数字0改成2。然后复制代码块“tracking values=2”4次依次放入第1个 或
右侧4个方框中，将后面4个数字2从左到右依次改为3、5、6、7。

![](media/76be5aae11f5831430d82720f8ac95d4.png)

如果为
下，将数字0改成60；再点击“Neopixel”模块，找到并拖出指令方块“stri显示颜色
红”也放入第一个 如果为 下，并点击 红 后面的下拉三角形按钮选择 绿
。

![](media/c735b89ff040ff3e741e0e63fe527fed.png)

（9）复制代码块“tracking values=2”1次放入第一个否则如果为后面的方框中，将数字2改成4。

![](media/46b5e4a353a5209fdc0186bc7b779398.png)

如果为
下，点击Forward后面的下拉三角形按钮选择Back，又将数字0改成80；复制代码块“LeftSide motor run Back speed:
80%”1次也放入第二个then下，点击LeftSide后面的下拉三角形按钮选择RightSide，再点击Back后面的下拉三角形按钮选择Forward；再复制指令方块“strip
显示颜色 绿”1次也放入第二个 如果为 下，并点击 绿
后面的下拉三角形按钮选择 蓝 ，其他的不变。

![](media/9f90eb443acafccbdc5832d6586ceea6.png)

11 复制代码块“tracking     values=4”1次放入第二个否则如果为后面的方框中，将数字4改成1。

![](media/5aca64b13cf8704a9fa80f89016ae90c.png)

（12）复制代码串

![](media/1994d89d603d49eb2a1285af897da250.png)

1次放入第三个
如果为
下，将LeftSide后面的Back改成Forward，再将RightSide后面的Forward改成Back，点击
蓝 后面的下拉三角形按钮选择 黄 ，其他的不变。

![](media/6c08767f974a6f93d242cbf55a046e0d.png)

stop”放入
否则 下，复制指令方块“strip 显示颜色 黄”1次也放入 否则 下，并点击 黄
后面的下拉三角形按钮选择红 。

![](media/e0a526773b003e327d6f4c7c05c16854.png)

完整的代码程序：

![](media/bc734c4cf84d9086621bf804318adb95.png)

①“当开机时”指令方块仅运行一次以启动程序。

②LED点阵显示“![](media/b9b97ec13c745120243516b57a2f2fbc.png)”图案。

③将strip设为引脚P8初始化灯带4颗LED（模式RGB（GRB顺序））

④关闭条带上所有的RGB灯。

⑤在“无限循环”指令方块之内，程序循环运行。

⑥将变量tracking values设为3路循迹传感器读取的巡线值。

⑦当变量tracking values=2or3or5or6or7成立时，执行then下的程序

⑧乌龟车以60%速度前进

⑨strip上4个WS2812RGB灯亮绿色灯

⑩当变量tracking values=4成立时，执行then下的程序

⑪乌龟车的左轮以80%速度后退

⑫乌龟车的右轮以80%速度前进

⑬strip上4个WS2812RGB灯亮蓝色灯

⑭当变量tracking values=1成立时，执行then下的程序

⑮乌龟车的左轮以80%速度前进

⑯乌龟车的右轮以80%速度后退

⑰strip上4个WS2812RGB灯亮黄色灯

⑱当上述变量tracking values的值都未成立时，执行else下的程序

⑲乌龟车停止

⑳strip上4个WS2812RGB灯亮红色灯

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/46e4780e27d4491e9d822aaabc1b9054.png)

5实验结果：

按照之前的方式将代码下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，循迹小车能随着黑色轨迹前行。同时，点亮乌龟车上的4个WS2812 RGB灯。

特别注意：（1）小车循迹轨道，黑线的宽度必须大于等于3路循迹传感器模块的宽度。

（2）测试小车时，不要在阳光明媚的太阳底下测试。测试过程中，如果出现问题，可在暗一点的环境中测试。

### 18：超声波跟随小车

#### 181：超声波测距

1 实验说明：

自然界有一种叫蝙蝠的动物，蝙蝠在夜间飞行不是靠眼睛看的，而是靠耳朵和发音器官飞行的。蝙蝠在飞行时，会发出一种尖叫声，这是一种超声波信号，是人类无法听到的，因为它的音频很高。这些超声波的信号若在飞行路线上碰到其他物体，就会立刻反射回来，在接收到返回的信息之后，蝙蝠于振翅之间就完成了听、看、计算与绕开障碍物的全部过程。

超声波传感器模块的原理跟上面的原理是一样的，超声波传感器模块一触发信号后发射超声波，当超声波投射到物体而反射回来时，模块输出一回响信号，以触发信号和回响信号间的时间差，来判定物体的距离。超声波传感器有敏感范围大，无视觉盲区，不受障碍物干扰等特点，这项技术已经在商业和安全领域被使用25年多了，已经被证明是检测小物体运动最有效的方法。

我们看下超声波传感器模块的图片，两个像眼睛一样的东西，一个就是信号发射端（TRIG），一个就是信号接收端（ECHO）。

![](media/7d1365ccda9dfeff4ba6624f9413877c.png)

根据上面的接线图可知，超声波传感器模块集成端口是接在micro:bit
电机驱动扩展板上5V G P1 P2集合端口，Trig（T）引脚是接在P1处，对应的是micro:bit的P1控制的；Echo（E）引脚是接在P2处，对应的是micro:bit的P2控制的。

2工作原理：

![](media/8ff02741199a0f03d8d814a4b72f27d7.png)

10us
的高电平信号去触发；

40KHZ
的方波，并自动检测是否有信号返回；

ECHO（E）
输出一个高电平，高电平持续的时间便是超声波从发射到接收的时间。那么测试距离=高电平持续时间\*340m/s\*05。

3规格参数：

工作电压：3-55V（DC）

工作电流：15mA

工作频率：40khz

最大探测距离：3m左右

最小探测距离：2-3cm

高精度可达 02cm

感应角度：不大于15度

输入触发脉冲：10us 的 TTL 电平

TTL
电平信号（高），与射程成正比

4准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro:bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit扩展库。

如果选择手动拖动代码，则首先需要添加turtle-bit扩展库。

5  实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\818：超声波跟随小车\8181：超声波测距|microbit-超声波测距hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“高级”下的“串行”模块，找到并拖出指令方块“串行
重定向到 USB”放入“当开机时”指令方块中。

![](media/a78dbdb88086e789d6c938c680df9220.png)

1  先点击“变量”模块，再点击“设置变量”出现“新变量的名称：”对话框，在对话框中输入i，点击“OK”，建立了变量“i”，拖出指令方块“将1设为
    0”放入“当开机时”指令方块中。

![](media/548067da0aac72209faa4014cd7d0f98.png)

2  点击“变量”模块，找到并拖出指令方块“set i to     0”放入“无限循环”指令方块中。

![](media/8d27068eea5fa59f21b88ccf9ef75c9f.png)

3  先点击“高级”下的“串行”模块。找到并拖出指令方块“串行
    串行写入数值
    x=0”放入“无限循环”指令方块中，再点击“K_Bit”模块，找到并拖出“Ultrasonic”放入指令方块“串行
    串行写入数值
    x=0”中的“=”右侧的数字0处，将“=”左侧的x改成distance。

![](media/11a9f71ec123e3741b69b2a6b03da417.png)

（5）点击“逻辑”模块，先找到并拖出指令方块“如果为则”放入“无限循环”指令方块中，再找到并拖出“=”方块放入true处方框中。

![](media/8a96e385a49330e13f5d88f7a5583ca5.png)

4  再点击“K_Bit”模块，找到并拖出“Ultrasonic”指令方块放入“=”左侧，点击“=”后面的下拉三角形按钮选择“\<”，再将“\<”右侧的数字0改成10。

![](media/449164705256382cf1a3b5cf12412162.png)

（6）先点击“循环”模块，找到并拖出指令方块“当条件为
true
执行”放入then下，再点击“逻辑”模块，找到并拖出“=”方块放入true处方框中。

![](media/9878bbc7480a4a3a3ea8eb03546dbdf3.png)

5  点击“变量”模块，找到并拖出变量指令方块“i”放入“=”左侧，点击“=”后面的下拉三角形按钮选择“\<”，再将“\<”右侧的数字0改成1。

![](media/fc08c827a193b0ec796b3e9eb0301141.png)

6  先点击“音乐”模块，找到并拖出“播放音乐 中 C 持续 1     节拍”指令方块放入执行中，再点击“基础”模块，找到并拖出指令方块“暂停(ms)100”点击100后面的下拉三角形按钮选择200。

![](media/de928a7392ef79493a49ce8676bb240c.png)

7  复制代码串

![](media/de928a7392ef79493a49ce8676bb240c.png)

1次也放入执行中。

![](media/9ab366bbccc19335bafe0a81e048ab03.png)

8  点击“变量”模块，找到并拖出指令方块“以一为幅度更改i”放入
    执行 中。

![](media/2bc27e10a8bd341e86c13e1ba181462b.png)

完整的程序代码：

![](media/95006d326ffdedeb4164f5dcf3e22537.png)

①“当开机时”指令方块仅运行一次以启动程序。

②串行重定向USB

③将变量i设为0

④在“无限循环”指令方块之内，程序循环运行。

⑤将变量i设为0

⑥串行写入数值distance=Ultrasonic

⑦当Ultrasonic\<10成立时，执行then下程序

⑧当条件为变量i\<1成立时，执行do中程序

⑨播放音调中C持续1节拍

⑩延时时间200毫秒

⑪播放音调中C持续1节拍

⑫延时时间200毫秒

⑬以1为幅度更改i

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/2bff695b050961b835dc8f6d2072a128.png)

6  实验结果：

按照之前的方式将代码下载到micro：bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，这里还必须确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。否则超声波传感器是读不了距离数字。接下来点击显示数据(设备)按钮：

![](media/2cd74c16ab3623f6752d3f5e59deea2e.png)

显示数据(设备)中显示了障碍物与超声波传感器模块之间的距离（如下图），并且当障碍物与超声波传感器模块的距离小于10cm时，小车控制板上无源蜂鸣器响起声音。

![](media/422adea3e04563f038f7f28cd40efb2d.png)

如果你的电脑系统是Windows7/8而不是Windows 10，则在Google Chrome中是不能进行设备配对，从而读取不了相应的数字信号或模拟信号，可是又需要读取相应的传感器/模块的数字信号或模拟信号，那怎么办呢？这里就可以使用CoolTerm软件来读取串口的。

打开CoolTerm，点击Options，选择串行Port，设置COM口和波特率，波特率设置为115200（经过测试，micro:bit的USB串口通讯波特率是115200），点击OK后，最后点击Connect。这样，CoolTerm串口监视器显示结果，显示如下图：

![](media/c88ce484a935653373de5cdf72c727ed.png)

#### 182：超声波避障小车

![](media/079f6f0b53fa771519e18b0a4c8794b7.jpg)

1  实验说明：

前面的课程我们结合了循迹传感器和乌龟车等结合，制作了一款循迹小车；在这课程中，我们利用超声波传感器模块和乌龟车等结合，制作一个超声波避障小车。它的原理就是，通过超声波传感器测量乌龟车与前方障碍物之间的距离，
根据测试距离控制乌龟车的避障动作。这样，当乌龟车靠近前方障碍物时，让其转弯避开障碍物行走。

2  准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro:bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit扩展库。

如果选择手动拖动代码，则首先需要添加turtle-bit扩展库。

3  编程思路：

程序流程图：

![](media/61e2c216330939d99f57ec9588dc2f45.png)

4  实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\818：超声波跟随小车\8182：超声波避障小车|microbit-超声波避障小车hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“基础”模块，找到并拖出指令方块“显示图标
♥”放入“当开机时”指令方块中，点击“❤”图案后面的下拉三角形按钮选择“

![](media/b9b97ec13c745120243516b57a2f2fbc.png)

”图案。

![](media/5bd18141c11619e6fde09d4f34f9735c.png)

（2）点击“TurtleBit”模块，找到并拖出指令方块“LED brightness 0”放入“当开机时”指令方块中，将数字0改成200。

![](media/225271db4d507c8328f3ecb697168dfb.png)

（3）先点击“变量”模块，再点击“设置变量”出现“新变量的名称：”对话框，在对话框中输入distance，点击“OK”，建立了变量“distance”，拖出指令方块“将
distance 设为 0”放入“当开机时”指令方块中。

![](media/a0ae489486a4093fe972794a3fbd7487.png)

distance
设为0”放入“无限循环”指令方块中。再点击“TurtleBit”模块，找到并拖出“Ultrasonic”指令方块放入是“设为”后面的数字0处。

![](media/2ab4d6dd0e947a8c8732e6adb7b39272.png)

true
则否则”放入“无限循环”指令方块中，接着又找到并拖出“=”放入true方框中，再点击“变量”模块，找到并拖出变量指令方块“distance”放入“=”左侧方框中，点击“=”后面的下拉三角形按钮选择“＞”，接着将“大于”后面的数字0改成15。

![](media/e6623dbf302c797af66576f288de9144.png)

如果为
下，点击red后面的下拉三角形按钮选择green，再复制指令方块“set left_side RGBled green”1次也放入“则”下，点击left_side后面的下拉三角形按钮选择right_side，其他的不变。

![](media/283421b7180e4344d2d4726d14be1082.png)

speed:
0%”放入“否则”下，点击forward后面的下拉三角形按钮选择back，并将数字0改成60；再复制指令方块“LeftSide motor run back speed:
60%”也放入else下，点击LeftSide后面的下拉三角形按钮选择RightSide，接着点击back后面的下拉三角形按钮选择forward，并将数字60改成80。

![](media/f79492e67d076eb58f1657ab57381de0.png)

（7）复制代码串

![](media/fb1ee2c85bc05fd607d452300441ab31.png)

1次也放入“否则”下，点击green后面的下拉三角形按钮选择blue。

![](media/fb1ee2c85bc05fd607d452300441ab31.png)

完整的代码程序

![](media/d0728fde3eae88e3652f91fee02c2045.png)

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/eb3cf9fe4ddc8b07d03c7be7bf6fb067.png)

5  实验结果：

按照之前的方式将代码下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，乌龟车在离前方障碍物的距离大于15cm时，乌龟车向前走，同时2个RGB灯亮绿色灯；反之，乌龟车向左转，同时2个RGB亮蓝色灯。

#### 183：超声波跟随小车

![](media/c26e8f5d9583eb0537a257a9242da321.jpg)

1  实验说明：

前面的课程我们结合了循迹传感器和乌龟车等结合，制作了一款循迹小车；在这课程中，我们利用超声波模块和乌龟车等结合，制作一个超声波跟随小车。它的原理就是，通过超声波传感器模块，测试出乌龟车和前方障碍物的距离，然后根据测试距离控制小车运动状态。

2  准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro：bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit扩展库。

如果选择手动拖动代码，则首先需要添加turtle-bit扩展库。

3  编程思路：

程序流程图：

![](media/dec69f0ffaf8837f30418e0a9ba25981.png)

4  实验代码：

根据下表加载代码（如何加载？）如下图：

<table style="width:100%;">

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\818：超声波跟随小车\8183：超声波跟随小车|microbit-超声波跟随小车hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“基础”模块，找到并拖出指令方块“显示图标
♥”放入“当开机时”指令方块中，点击“❤”图案后面的下拉三角形按钮选择“

![](media/b9b97ec13c745120243516b57a2f2fbc.png)

”图案。

![](media/87419a6f7774c4d46341670941909455.png)

strip
设为 引脚 P0初始化灯带 24 颗LED 模式 RGB(GRB 顺序)(GRB
顺序)”放入指令方块“当开机时”中，由于4个WS2812 RGB灯的信号端P8是micro bit的P8控制端控制的，所以点击P0后面的下拉三角形按钮选择P8。又因为只有4个WS2812 RGB灯，所以将leds前面的数字24改成4，点击RGB(GRB
顺序)后面的下拉三角形按钮选择RGB(GRB 顺序)。

![](media/6793cfc09ae470010326a620c878fd34.png)

3  点击“Neopixel”模块下的“更多”,找到并拖出指令方块“strip     设置亮度为 255”指令方块“当开机时”中，要使4个WS2812     RGB灯亮度减弱，可以将数字255改成100。

![](media/4e2c1435ee528b165f8eabb706def39f.png)

（4）又点击“Neopixel”模块，找到并拖出指令方块“strip清除显示”放入指令方块“当开机时”中。

![](media/1fa79b659a1d7f3eefa2d29ce7a20371.png)

（5）先点击“变量”模块，再点击“设置变量”出现“新变量的名称：”对话框，在对话框中输入distance，点击“OK”，建立了变量“distance”，拖出指令方块“将
distance 设为 0”放入“当开机时”指令方块中。

![](media/83e56ede10469313197b78ba2606bd5f.png)

5  设为
    0”放入“无限循环”指令方块中。再点击“TurtleBit”模块，找到并拖出“Ultrasonic”指令方块放入设为
    后面的数字0处。

![](media/7faf759ccba6d8ebb0170b556b130ad1.png)

6  点击“逻辑”模块，先找到并拖出指令方块“如果为 true     则”放入“无限循环”指令方块中，接着找到并拖出“and”方块放入true处方框中。

![](media/08e2e5ab22221f5b72661c02ab92c129.png)

（7）先点击“逻辑”模块，找到并拖出“=”放入“与”左侧方框中，再点击“变量”模块，找到并拖出变量指令方块“distance”放入“=”左侧方框中，点击“=”后面的下拉三角形按钮选择“≥”，接着将“≥”后面的数字0改成10，再复制代码块“distance≥10”1次放入“与”右侧的方框中，点击“≥”后面的下拉三角形按钮选择“≤”，将“≤”后面的数字10改成30。

![](media/2e3cc9776470eabe3f81d290487e3ac1.png)

0
%”放入“则”下，将数字0改成80；再点击“Neopixel”模块，找到并拖出指令方块“strip show color red”放入“则”下。

![](media/c25eb5dc942327c6790b56592336e22a.png)

9  复制代码串

![](media/c25eb5dc942327c6790b56592336e22a.png)

1次放入“无限循环”指令方块中，删除代码块“distance≥10”和“与”方块，将代码块“distance≤30”放入true处方框中，将“≤”后面的数字30改成6，点击Run_forward后面的下拉三角形按钮选择Run_back，再将再Run_back后面的数字80改成60，点击“红”后面的下拉三角形按钮选择“黄”。

![](media/39582aa61251be96838cb846255e1f73.png)

10 先复制代码串
    ![](media/39582aa61251be96838cb846255e1f73.png)”，点击“TurtleBit”模块，找到并拖出指令方块“car     stop”放入“则”下，点击“黄”后面的下拉三角形按钮选择“白”。

![](media/a2cb7fd6d7647aef0e2b3c3a10c064e7.png)

完整的代码程序：

![](media/ce0ec99024dcd9dc3d904305c5cf4fcf.png)

①“当开机时”指令方块仅运行一次以启动程序。

②LED点阵显示“![](media/b9b97ec13c745120243516b57a2f2fbc.png)”图案。

③将strip设为引脚P5初始化灯带4颗LED（模式RGB（GRB顺序））

④设置4个WS2812 RGB亮度（PWM）为100

⑤关闭条带上所有的RGB灯。

⑥将变量distance设为0

⑦在“无限循环”指令方块之内，程序循环运行。

⑧将变量distance设为超声波传感器读取的距离值。

⑨当10cm≤distance≤30cm成立时，执行then下的程序

⑩小车以80%速度前进

⑪strip上4个WS2812 RGB都亮红色灯

⑫当distance≤6cm成立时，执行“则”下的程序

⑬小车以60%速度后退

⑭strip上4个WS2812RGB都亮黄色灯

⑮当6cm\<distance\<10cm或distance\>30cm成立时，执行“则”下的程序

⑯小车停止

⑰strip上4个WS2812RGB都亮白色灯

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/11efa143c4172ab86090305e3bd7491f.png)

5  实验结果：

按照之前的方式将代码下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，小车可以跟随前方障碍物的移动而移动。小车不同的运动状态，4个WS2812 RGB灯亮起不同的颜色。

注意：障碍物只能在小车的正前方移动，不能拐弯。

### 19：红外控制小车

#### 191：红外遥控解码

![](media/8abfb89f7fb64ef635b21975c7ff4d8c.jpg)

1 实验说明：

毫无疑问，红外遥控在日常生活中随处可见，以至于很难想象没有它世界会变得怎样。它被用来控制各种家电，如电视、音响、录影机和卫星信号接收器。红外遥控是由红外发射和红外接收系统组成的，也就是一个红外遥控器和红外接收模块和一个能解码的单片机组成的，我们看图示。

![](media/3ca9b64a7bf1dc6acf71cf1f60e0610a.png)

红外发射的遥控器发射的38K红外载波信号是由遥控器里的编码芯片对其进行编码。它是以一段引导码，用户码，数据码，数据反码组成，利用脉冲的时间间隔来区别是信号0还是信号1(高电平低电平之比约为1:1时被认为是信号0)，而编码就是由这些0
、1信号组成。同一个遥控器的用户码是不变的，用数据码不同来分辨遥控器按的键不同。当按下遥控器按键时，遥控器发送出红外载波信号，红外接收器接收到信号时程序对载波信号进行解码，通过数据码的不同来判断按下的是哪个键。单片机由接收到的0、1信号进行解码，由此判断遥控器按下的是什么键。

红外接收就是扩展板上自带的红外接收模块，主要由红外接收头组成，它是集接收、放大、解调一体的器件，它内部IC就已经完成了解调，能够完成从红外线接收到输出与TTL电平信号兼容的所有工作，输出的就是数字信号。它适用于红外线遥控和红外线数据传输。

根据上面的接线图可知，乌龟车上的红外接收模块的集成端口是接在micro:bit电机驱动扩展板上P11 5V G集合端口，由micro:bit的P11控制的。

2  规格参数：

工作电压：33-5V（DC）

接口：3PIN接口

输出信号：数字信号

接收角度：90度

频率：38khz

遥控范围：5米左右

3  准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro:bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit扩展库。

如果选择手动拖动代码，则首先需要添加turtle-bit扩展库。

4  实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\819：红外控制小车\8191：红外遥控解码|microbit-红外遥控解码hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“高级”下的“串行”模块，找到并拖出指令方块“串行
重定向到 USB”放入“当开机时”指令方块中。

![](media/d791341beb216c2a07535ebb72094bfe.png)

（3）点击“IrRemote”模块，找到并拖出指令方块“connect IR receiver at P0”放入“当开机时”指令方块中，由于乌龟车上的红外接收模块由micro:bit的P11控制的，所以点击P0后面的下拉三角形按钮选择P11。

![](media/bb562abe4499fef8e42d9c348f2f0d6d.png)

4  点击“变量”模块，再点击“设置变量”出现“新变量的名称：”对话框，在对话框中输入“val”，点击“OK”，建立了变量“val”,拖出指令方块“将
    val 设为0”放入指令方块“无限循环”中。

![](media/5afcfce25047f42adc939fe019a5ba98.png)

5  点击“IrRemote”模块，找到并拖出指令方块“IR     button”放入指令方块“将 val 设为 0”中的to 后面的0处。

![](media/073bf13e11b6a95d6e8eda6879433a76.png)

6  先点击“高级”下的“串行”模块，找到并拖出指令方块“串行
    串行写入数值
    “x”=0”放入“无限循环”指令方块中，将“x”改成“IR”,再点击点击“变量”模块，找到并拖出变量指令方块“val”放入“=”右侧的数字0处。

![](media/220845ce25d138805b0b4247c21c197c.png)

（7）点击“基础”模块，找到并拖出指令方块“暂停 (ms) 100”放入“无限循环”指令方块中，设置延时时间为1000毫秒。

![](media/05e360b607f16858dfd31aa837574384.png)

完整的代码程序：

![](media/50dafccf1e628874de3eb7554c478e1f.png)

①“当开机时”指令方块仅运行一次以启动程序。

②串行重定向USB。

③将IR接收器接在P11

④在“无限循环”指令方块之内，程序循环运行

⑤将val设为IR button

⑥串行写入数值IR=val

⑦延时时间1000毫秒

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/045ec035ac15d27dc8c2b0f0598c6051.png)

代码说明：没有按下红外遥控器上的按键时，串口监视器不断地刷新显示数字0。当按下红外遥控器上的按键时，串口监视器中显示出对应的按键键值。

特别注意：

1、有些红外遥控不带电池，需要自己配置，电池型号为CR2025。

2、测试前需要确保红外遥控是OK的，有一个小诀窍测试红外遥控是否OK。

打开手机摄像头拍照，红外遥控多准手机摄像头按下按键。如果在手机上看到有紫光闪烁，就代表红外遥控是OK的。

按照之前的方式将代码下载到micro:bit，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，接下来点击显示数据(设备)按钮：

![](media/e7bf712e0c8bedc4b0423427848fa395.png)

红外遥控器对准小车扩展板上的红外接收器，按下对应按键，显示数据(设备)窗口中就可以显示出对应按键的键值，显示如下图。

![](media/c7a33a4cc9d6decbf9b653d91bcb5318.png)

如果你的电脑系统是Windows7/8而不是Windows 10，则在Google Chrome中是不能进行设备配对，从而读取不了相应的数字信号或模拟信号，可是又需要读取相应的传感器/模块的数字信号或模拟信号，那怎么办呢？这里就可以使用CoolTerm软件来读取串口的。

打开CoolTerm，点击Options，选择串行Port，设置COM口和波特率，波特率设置为115200（经过测试，micro:bit的USB串口通讯波特率是115200），点击OK后，最后点击Connect。这样，CoolTerm串口监视器显示对应按键的键值，显示如下图。

![](media/08afaf57618c3d7b4b7866e6e1971e73.jpg)

我们通过得出的数值，做了一个红外遥控器按键值表，方便以后使用。

![](media/4eadf6549525d5b5a97cab2200a49e15.png)

#### 192：红外控制小车

![](media/c9ab1771ff4e84f8c11db15db570a62a.jpg)

1  实验说明：

红外遥控小车的实现主要靠的是红外信号的传递，小车接收到红外信号后经过解码会得到具体的数值，小车再依据相应的数值来执行相对应的操作。

前面的课程我们结合了循迹传感器和小车扩展板等结合，制作了一款循迹小车；在这课程中，我们利用红外遥控和小车扩展板等结合，制作一个红外控制小车。

它的原理就是，通过红外遥控发送按键信号，小车扩展板上红外接收模块接收到对用的按键信号，从而控制小车进行对应的运动状态。

2  准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro：bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit扩展库。

如果选择手动拖动代码，则首先需要添加turtle-bit扩展库。

警告：红外接收传感器和红外遥控器应避免在阳光等有红外干扰的环境中使用。阳光中含有大量的不可见光，如红外线和紫外线。在阳光强烈的环境下，红外接收传感器不能正常工作。

3  编程思路：

编程流程图：

![](media/92de5675b404af1a692eb53c16826755.png)

4  实验代码:

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\819：红外控制小车\8192：红外控制小车|microbit-红外遥控小车hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）点击“Ir Remote”模块，找到并拖出指令方块“connect IR receiver at P0”放入“当开机时”指令方块中，由于乌龟车上的红外接收器是由micro:bit的P11控制的，所以点击P0后面的下拉三角形按钮选择P11。

![](media/096e0c7463ba05373d3a712df8ef33c6.png)

strip
设为 引脚 P0初始化灯带 24 颗LED 模式 RGB(GRB 顺序)(GRB
顺序)”放入指令方块“当开机时”中，由于4个WS2812RGB灯的信号端P8对应的是由micro:
bit的P8控制端控制的，所以点击P0后面的下拉三角形按钮选择P8。又因为只有4个WS2812 RGB灯，所以将leds前面的数字24改成4，点击RGB(GRB
顺序)后面的下拉三角形按钮选择RGB(GRB 顺序)。

![](media/092cc22b9a41af93a0aec8b7bbecbdb8.png)

（3）先点击“变量”模块，再点击“设置变量”出现“新变量的名称：”对话框，在对话框中分别输入“val”，点击“OK”，建立了变量“val”。用同样的方法再建立变量“val2”，找到并拖出指令方块“将
val2 设为
0”放入“当开机时”指令方块中并复制1次也放入“当开机时”指令方块中，点击第一个val2后面的下拉三角形按钮选择val。

![](media/b3c5cfebb63329afc9369a2380377d74.png)

val2
设为
0”放入“无限循环”指令方块中，点击val2后面的下拉三角形按钮选择val，再点击“IrRemote”模块，找到并拖出指令方块“IR button”放入“设为”后面的数字0处。

![](media/02568302d355b2b79324f0921e9c756d.png)

true
则”放入“无限循环”指令方块中，接着找到并拖出“=”方块放入“true”处方框中。再点击“变量”模块，找到并拖出变量指令方块“val”放入“=”左侧，“=”右侧的数字0不变，再点击“=”后面的下拉三角形按钮选择“≠”。

![](media/dee39cb360f78c19ae976b1c80557d38.png)

val2
设为 0”放入“则”的下方，再找到并拖出变量指令方块“val”放入指令方块“将 val2
设为 0”中的“设为”后面的0处。

![](media/110de3626e6086c578be717b8d690deb.png)

7  点击“逻辑”模块，先找到并拖出指令方块“如果为则否则”放入“则”的下方，接着点击指令方块“如果为则否则”的“

![](media/a7c5c78217692a965e679b2439ab2f3a.png)”图案4次，再点击“否则”后面的“![](media/0fcc5d6332012fed7361a075bd60751f.png)

”图案1次删除“否则”，又再次找到并拖出“=”方块放入“true”处方框中。

![](media/d75e1cdb0fa8fc22fd1d399121b776fd.png)

（8）点击“变量”模块，找到并拖出变量指令方块“val2”放入“=”左侧，将“=”右侧的数字0改成70。

![](media/391b6a90a684f5cacb0f65672644cd09.png)

speed:
0%”放入第二个“则”下，将数字0改成90；再点击“Neopixel”模块，找到并拖出指令方块“strip
显示颜色红”也放入第二个“则”下，点击“红”后面的下拉三角形按钮选择“绿”。

![](media/8d705161e741930d6671f6587a9e6ae9.png)

（10）复制代码块“val2=70”1次放入第一个否则如果为
后面方框中，将“=”后面的数字70改成68。

![](media/cf6c7ada5ea4eff18b0cfdc307645654.png)

speed:
0%”放入第三个then下，将数字0改成60，接着复制指令方块“LeftSide motor run Forward speed:
60%”1次也放入第三个“则”下，点击LeftSide后面的下拉三角形按钮选择RightSide，并将数字60改成85；再点击“Neopixel”模块，找到并拖出指令方块“strip show color red”也放入第三个“则”下，点击‘红’后面的下拉三角形按钮选择“蓝”。

![](media/a78b9ef36f2765509a2693b8b1c9c554.png)

（12）先复制代码块“val2=68”1次放入第二个否则如果为
后面方框中，将“=”后面的数字68改成67；再复制代码块串

![](media/3c72eed47a0a1217ee7b6accfe400116.png)

1次放入第四个“则”下
，将LeftSide后面的数字60改成85，RightSide后面的数字85改成60，点击“蓝”后面的下拉三角形按钮选择“黄”。

![](media/81b251bbdc0f9bfedd00ddddd2186b26.png)

（13）先复制代码块“val2=67”1次放入第三个否则如果为
后面方框中，将“=”后面的数字67改成21；在复制第二个“则”下的代码串

![](media/bb4519abdbe2e7ee6bdc79d8f19b5b8d.png)

1次放入第五个“则”下，点击Run_forward后面的下拉三角形按钮选择Run_back，点击“绿”后面的下拉三角形按钮选择”紫”，其他的不变。

![](media/288690e27cd365afcbe9267c51402706.png)

（14）先复制代码块“val2=21”1次放入第四个否则如果为
后面方框中，将“=”后面的数字21改成64；接着点击“TurtleBit”模块，找到并拖出指令方块“car stop”放入第五个“则”下，复制第五个“则”下的指令方块“strip show color purple”1次放入第六个“则”下，点击”紫”后面的下拉三角形按钮选择“红”。

![](media/c8a410457deb524c6f8fd677831ad900.png)

完整的代码程序：

![](media/98e67487719e3e78e55ed38af9ac0a7f.png)

①“当开机时”指令方块仅运行一次以启动程序。

②将IR接收器接在P16

③将strip设为引脚P5初始化灯带18颗LED（模式RGB（GRB顺序））

④将变量val设为0

⑤将变量val2设为0

⑥在“无限循环”指令方块之内，程序循环运行

⑦将val设为IR button

⑧当变量val≠0成立时，执行“则”下程序

⑨将变量val2设为val

⑩当val2=70成立时，执行“则”下的程序

⑪小车以40%速度前进

⑫strip上18个RGB亮绿色灯

⑬当val2=68成立时，执行“则”下的程序

⑭小车的左轮以15%速度前进

⑮小车的右轮以35%速度前进

⑯strip上18个RGB亮蓝色灯

⑰当val2=67成立时，执行“则”下的程序

⑱小车的左轮以35%速度前进

⑲小车的右轮以15%速度前进

⑳strip上18个RGB亮黄色灯

㉑当val2=21成立时，执行“则”下的程序

㉒小车以40%速度后退

㉓strip上18个RGB亮紫色灯

㉔当val2=64成立时，执行“则”下的程序

㉕小车停止

㉖strip上18个RGB亮红色灯

![](media/9ea02c8380ae971ca3fab4bc77673f0c.png)

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/edbe9ae34b214d396c87d6f6a19e184f.png)

5实验结果：

按照之前的方式将代码下载到micro:bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，红外遥控对准扩展板的红外接收头，按下按键，即可控制小车运动。其中，

![](media/d55474f3fdf94e5d35de424c0135f554.png)按键控制小车后退，![](media/a8ef4b174911d528e2dc232c2f862b7d.png)

按键控制小车停止，同时4个WS2812RGB灯亮起对应的颜色灯。

注意：测试时，红外遥控需正对小车扩展板后面的红外接收头，距离最好不超过5米左右。

### 20：蓝牙多功能小车

#### 201：读取蓝牙数据

![](media/55b2424d88ba1ba8a711c49418ca8dc6.png)

1  实验说明：

在micro:bit控制板上自带有蓝牙，可以通过蓝牙方式与Micro:bit通讯，可以用蓝牙控制Micro:bit，或者Micro:bit通过蓝牙把信号传回手机或者电脑，我们可以利用micro:bit上自带的蓝牙和手机蓝牙APP通信，利用蓝牙手机APP控制micro:bit外接设备工作。Micro:bit上自带的蓝牙既支持安卓系统手机，也支持IOS系统设备（手机或iPad）。我们为您提供两种蓝牙APP，适用于安卓系和IOS系统。这两种APP连接Micro:bit蓝牙的方法是类似的。在这一课程中，我们主要介绍蓝牙APP的使用和APP界面上各按钮的功能，并且通过蓝牙APP连接Micro:bit上的蓝牙来读取了APP界面上各按钮发送的控制字符。

2  准备：

（1）将micro:bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro:bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit扩展库。

如果选择手动拖动代码，则首先需要添加turtle-bit扩展库。

由于micro:bit的硬件原因，蓝牙和无线电不能同时工作，所以它们的扩展库互不兼容。安装蓝牙扩展库时，系统将提示您删除无线电扩展。只需确认移除就行。

![](media/aee56e76bad3421a20cea6018ccd5e2c.png)

3 实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\820：蓝牙多功能小车\8201：读取蓝牙数据|microbit-读取蓝牙数据hex|

也可以自己通过拖动代码块来编写代码程序，操作步骤如下：

（1）先移除指令方块“无限循环”，再点击“高级”下的“串行”模块，找到并拖出指令方块“串行
重定向到 USB”放入“当开机时”指令方块中。

![](media/d72b85e26a397a2fb8f83b2db8858982.png)

（2）点击“蓝牙”模块，找到并拖出指令方块“通过蓝牙连接时”。

（3）点击“基础”模块，找到并拖出指令方块“显示图标”放入“通过蓝牙连接时”指令方块。

![](media/cef54d29e617e62f3b519aa20162b69c.png)

（4）点击“变量”模块，再点击“设置变量”出现“新变量的名称：”对话框，在对话框中输入“connected”，点击“OK”，建立了变量“connected”。找到并拖出指令方块“将
connected 设为 0”放入“通过蓝牙连接时”指令方块，将 设为
后面的数字0改成1。

![](media/e8625b71e8668bc068eb248ef50eac20.png)

（5）先点击“循环”模块，找到并拖出指令方块“当条件为
true
执行”放入“通过蓝牙连接时”指令方块，接着点击“逻辑”模块，找到并拖出“=”方块；再点击“变量”模块，找到并拖出变量指令方块“connected”放入“=”左侧方框，将右侧方块中的数字0改成1。

![](media/038839b88ae6fbd3b0688ef2021633aa.png)

（6）先点击“变量”模块，再点击“设置变量”出现“新变量的名称：”对话框，在对话框中输入“rec_data”，点击“OK”，建立了变量“rec_data”。找到并拖出指令方块“将
rec_data 设为 0”放入代码块“当条件为 connected=1
执行”中；再点击“蓝牙”模块下的“更多”，找到并拖出指令方块“读取蓝牙 uart
直至遇到 执行”放入指令方块“将 rec_data 设为 0”中 设为
后面的数字0处，并点击 执行 后面的下拉三角形按钮选择 \#。

![](media/2f3574c56fd5035f97adf8bdd447bcb4.png)

（7）先点击“高级”下的“串行”模块，找到并拖出指令方块“串行写入字符串”放入代码块“当条件为
connected=1
执行”中；再点击点击“变量”模块，找到并拖出变量指令方块“rec_data”放入指令方块“串行写入字符串”的文本框中。

![](media/93eef1d313ad9553292d539b0a78be9e.png)

（8）再次点击“高级”下的“串行”模块，找到并拖出指令方块“串行写入字符串”放入代码块“当条件为
connected=1 执行”中。

![](media/fa61d763106054cb085d99fc87c417dc.png)

（9）点击“蓝牙”模块，找到并拖出指令方块“断开蓝牙连接时”。

（10）点击“基础”模块，找到并拖出指令方块“显示图标”放入“断开蓝牙连接时”指令方块，点击“❤”图案后面的下拉三角形按钮选择“

![](media/25e0341e063286ff7828c15f09ae0ade.png)

”图案。

![](media/6e17b845e4d1379cfba848735e030680.png)

完整的代码程序

![](media/53be47e8ca1936df358789708652b6bd.png)

①“当开机时”指令方块仅运行一次以启动程序。

②串行重定向USB。

③通过蓝牙连接到micro:bit时就运行里面的代码

④LED点阵显示“❤”图案

⑤将变量connected设为1

⑥当条件为connected=1时就执行do中代码

⑦将变量rec_data设为读取蓝牙uart，直至遇到#

⑧串行写入字符串rec_data

⑨向串口写入一行空格

⑩断开蓝牙连接到micro:bit时就运行里面的代码

⑪LED点阵显示“![](media/25e0341e063286ff7828c15f09ae0ade.png)”图案

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/5128a8ec0eed8e0433006a392f16c128.png)

5实验结果：

（1）实验代码编完之后需要设置，先点击右上角的齿轮图标（设置），再单击“Project Settings”，在文本框中输入“Read the data of Bluetooth”后，将“无需配对”设置为打开状态。（如果是直接导入实验代码的就不需要此操作，而自己拖动代码块编写实验代码的就需要此操作）

![](media/01b256e5bbe9420226085513778f5173.png)

![](media/982334c8cdfb3ab43cd2db629090ca1b.png)

![](media/09767d5efdc8f05fdb331b5ae6d352b5.png)

（2）设置完之后，按照之前的方式将实验代码下载到micro：bit
，micro USB线不要从micro：bit上拔下来，利用micro USB线上电，下载之后开始下载安装手机/iPad蓝牙APP。

 IOS系统设备（手机/iPad）APP

a打开App Store。

![](media/27924fdb3d67692df7c63d8d0fb72287.png)

b在搜索框输入keyes Bit Car，点击搜索，再点击“

![](media/962a57f92b78eea1f0e3e81463497a9c.png)

”，就可以下载keyes Bit Car的蓝牙APP。

![](media/bb0985bc4d079475e1175b4b16d10b0e.png)

c下载完APP后，点击“OPEN”或点击手机/iPad桌面上的应用程序keyes Bit Car就可以打开APP，APP界面出现对话框，在对话框中点击“OK”。

![](media/6c97d9ffcde0d66cb36a017a413ce0a3.png)

![](media/a5c05f7b5844e11a8ea7a4b96df244de.png)

d先开启手机/iPad蓝牙，再点击APP界面左上角的connect按钮（控件）进行蓝牙搜索，在搜索结果中点击“BCC micro:bit”，几秒钟后，蓝牙已连接。

安卓系统APP

1  用浏览器中的扫描功能对着二维码扫描识别，识别成功后点击“go     to website”就可以进入下载keyes_Bit_Carapk页面，点击“Download     immediately”下载keyes Bit Car应用程序。

![](media/8fb53bd64d7d181ae9d24113419ac600.png)

![](media/e476860c0f534b0d9675649f02ec4d3b.png)

![](media/7566b3df9a230bc3f69993ad2d41fb85.png)

2  点击“Allow     allow”进入安装界面，点击“install”就可以安装好keyes Bit     Car应用程序。

![](media/638d0a4ae5f55ca39bff4f20a3bd14a6.png)

![](media/1b0ad4f8146ca600fd2670f1266b44ef.png)

3  点击“Open”或点击手机桌面上的应用程序keyes Bit     Car打开APP，出现对话框，在对话框中点击“Allow”打开手机蓝牙。也可以在打开APP之前先打开手机蓝牙。

![](media/c818fd71d6872374fbe177f082207fac.png)

![](media/3dab73f0e830bb5c0348af86110f3e50.png)

4  点击APP界面左上角的“CONNECT”按钮（控件）进行蓝牙搜索，在蓝牙搜索结果中点击“BCC     micro:bit”对话框中的“connect”，几秒钟后，蓝牙已连接。

（3）由于实验代码原因，在MakeCode编辑器中不会出现的“显示控制台设备”，所以读取不了读取了APP界面上各按钮发送的控制字符，这里需要使用CoolTerm程序来读取APP界面上各按钮发送的控制字符。打开CoolTerm，点击Options，选择串行Port，设置COM口和波特率，波特率设置为115200（经过测试，micro:bit的USB串口通讯波特率是115200），点击OK后，最后点击Connect。这样，对准micro：bit按下手机/ipad
蓝牙APP界面上的各按钮（控件），可以看到CoolTerm串口监视器显示出蓝牙APP界面上各按钮（控件）对应的控制字符，如下图。

![](media/3692e0ea2df357e30b51c6c83b0412f0.png)

![](media/6c1919fed6577bcf80a3564ee01e0207.png)

经过测试，我们得出了手机/ipad
蓝牙APP上各个按钮（控件）对应的功能，如下图：

![](media/d9b7b8502d84616ebfd2dd5273f1ecd1.png)

![](media/3f23a3f6f8be4be36f4c4222154c740f.png)

![](media/9384b0da3a7a3fd7eeac04b55fff862e.png)

![](media/2f05d2dac88caface2726524093ed6b1.png)

#### 202：蓝牙多功能小车

![](media/01852e885927364f074ebd5a55753cfc.jpg)

1  实验说明：

在上一课程中，我们已经介绍了蓝牙APP的使用和各按钮的功能，并且通过蓝牙APP连接Micro:bit上的蓝牙来读取了APP界面上各按钮发送的控制字符，在本课程中，主要是通过蓝牙APP连接Micro:bit上的蓝牙实现APP控制小车多种功能。

2  准备：

（1）将micro:bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro：bit主板和电脑。

（5）打开Web版本的Makecode。

如果选择通过导入Hex文件来加载项目，则无需手动添加turtle-bit和蓝牙扩展库。

如果选择手动拖动代码，则首先需要添加turtle-bit和蓝牙扩展库。

由于micro:bit的硬件原因，蓝牙和无线电不能同时工作，所以它们的扩展库互不兼容。安装蓝牙扩展库时，系统将提示您删除无线电扩展。只需确认移除就行。
![](media/aee56e76bad3421a20cea6018ccd5e2c.png)

3 实验代码：

根据下表加载代码（如何加载？）如下图：

|文件类型|路径|文件名|
|-|-|-|
|Hex file|/1Makecode 教程\Micro bit测试程序完整版\820：蓝牙多功能小车\8202：蓝牙多功能小车|microbit-蓝牙多功能小车hex|

由于这个代码程序比较复杂，步骤比较多，这里我们就不提供编写代码程序的详细操作步骤，如果你自己有兴趣的话，可以自己拖动代码块来操作下。

完整的代码程序

![](media/3c24e21af1599397dde790db781f4519.png)

![](media/fcb5f7a00479b026931cbba50c87681f.png)

![](media/6339be2b8d0d8104aeb4f30e81ff9c89.png)

点击micro:
bit在线编程工具的“JSJavaScript”,你可以看到对应的JavaScript语言代码程序：

![](media/262e4e8106f0297ff73c1a43f1a8e94c.png)

![](media/25aa4db67352a410b3824569f19f5369.png)

![](media/73fe2e3afcebceb068fa1d465648abce.png)

![](media/6881aa45dbaf627a97ebd4f50f96effb.png)

![](media/46d3355620c1becbacd0b0b296173743.png)

![](media/45fafc0831e3abfa7d3106a742d55a72.png)

![](media/b4ec11c7e91880b4618cae8e281b66ee.png)

5实验结果：

micro:bit迷你智能乌龟车执行相应的动作。
先在“项目设置”中，将“无需配对”设置为“打开”状态（如果是直接导入实验代码的就不需要此操作，自己拖动代码块编写代码就需要这里此操作）。按照之前的方式将代码下载到micro：bit，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，下载之后打开手机/ipad应用程序keyes Bit Car，然后按照前面的方法完成蓝牙连接，那你就可以操作keyes Bit Car蓝牙APP页面上的按钮（控件）来控制Keyes micro:bit迷你智能乌龟车。（因程序比较大，micro:bit的内存无法容纳，程序编译时会报错，需自己删掉一下自己用不到的功能块，方能编译下载）
