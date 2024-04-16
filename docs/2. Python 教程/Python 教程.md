# Python 教程

## Python

以下的步骤说明基于Windows操作系统，如果你使用的是其他操作系统，可以将其作为参考。

tutorial”的文件夹，其中保存了Micro:bit
迷你智能乌龟车的所有Python代码，Python代码文件是以“.py”结尾的文件。

Python是一种基于文本的语言，广泛应用于教育领域，也被数据科学和机器学习等领域的专业程序员使用。在庞大的教育者和计算专家社区的支持下，Python是继图形化编程之后的一个伟大的编程语言工具，是对基于文本编程的完美引入。

micro:bit使用的Python版本称为MicroPython。
非常适合那些想要继续深入学习编程的人群，用一系列代码段、各种预制图像和音乐帮助你进行编程。BBC microbit MicroPython的官方说明链接：<https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html>

Python代码有两种类型的编辑器（web版和离线版）。

资源和代码

该工具包的资源和代码可以在下面查看和下载：
https://pan.baidu.com/s/1LBZKBWd5IF8YSzgnhyZ3hA 
提取码：zusy

 KE3021（KE3022）Keyes套件 turtle-bit Micro bit 小乌龟 多功能 智能小车”的文件夹。
您可以将其放在电脑磁盘上的任何位置。

![](media/693f76f5975fc256dbc1d2880c80edeb.png)

Micro:bit官方在线代码编写平台，使用常用浏览器直接打开上述网址即可使用。

Micro:bit官方也推出了一个离线的编译工具Mu，方便在没有网络连接的时候也可以进行创意和教学

![](media/153c77edd571f12fce0e3282ab6fb530.png)(Mu软件下载链接：<https://codewith.mu/en/download>)

本教程也基于在本地离线模式使用Mu软件作为Python代码编辑器来完成项目实验。

Mu最简单和最容易的方法是通过Windows或Mac OSX的官方安装程序(Mu不再支持32位Windows)。目前推荐的版本是Mu 1.1.0-beta 2。建议你们通过每个支持的操作系统的链接更新到这个版本.

步骤1-确定版本并且下载Mu安装程序

先了解您的计算机是Windows系统还是Mac OSX系统；再打开资源管理器，鼠标右键点击”此电脑”，并选择属性，了解您的Windows系统是32位还是64位。

![](media/3a58be549e85e640654494c09f3a219f.png)

查看系统类别，类型将显示在操作系统下，64位系统或者32位系统：

![](media/e774ae15dcb81968d9a2a553af57ac96.png)

下载对应的Mu软件版本。

![](media/ceb4cfa6c81ce3959cec504412767e39.png)

步骤2-运行安装程序：

找到你刚刚下载的安装程序（它可能在你的下载文件夹中），双击打开安装程序文件。

![](media/8bcfe24cd37e0e5accae1f94cf155640.png)

这里我们概述了在windows10上的Windows安装Mu所需的额外步骤（Windows的其他版本也将类似）。

OSX系统安装Mu方法对应链接：<https://codewith.mu/en/howto/1.1/install_macos>
。

Windows 10 系统

Windows Defender将弹出一条警告消息。你应该点击“更多信息”链接。

![](media/877beb7b3f5ccf7e5d849b7aaa8d661d.png)

消息将更改，提供有关安装程序的更多信息，并显示“Run anyway”按钮。单击“Run anyway”按钮。

![](media/c87475e50dd03a0d0d2dcf166f33a837.png)

步骤3-许可协议

检查许可证，选择复选框并单击“Install”。

![](media/cc52e57332beae056b2dc9cd7fdd1651.png)

步骤4-安装

当Mu在你的电脑上安装时，需要几秒钟。

![](media/d75042c926b6e89463ef41c47220cdcc.png)

第5步-完成

安装已成功完成，请单击“完成”关闭安装程序。

![](media/62abaf11f6dfe7ba9d61b278bb7031b8.png)

第9步-启动Mu

你可以点击开始菜单中的图标启动Mu，也可以在搜索框中输入Mu(下面两种方法都有显示)。在第一次开始时，这可能需要一些时间。

![](media/c4adbdd1b2bf01cee8783ce659ac420f.png)

Mu的主界面如下图所示：

![](media/a1f68f6b14aa6ac9c9a8e7a09c30fde6.png)

## 课程介绍

实验8.1至8.12是使用micro：bit主板自带的传感器模块和LED点阵。

### 1：闪烁的心

实验说明：

首先先来练习一个不需要其他辅助元件，只需要一块micro：bit主板和一根micro USB数据线的简单实验，让micro：bit显示“闪烁的心”，这是一个让micro：bit主板和PC机通信的实验，这也是一个入门实验，希望可以带领大家进入micro：bit的魔幻世界。

准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开离线版本的Mu软件。

实验代码：

打开Mu软件，点击菜单栏中
“模式“按钮并在弹出对话框中选择“BBC micro：bit”之后，单击“OK”。

![](media/db92fd43cc800c6078ca49b30bf4eae6.png)

点击“加载”按钮，选择“microbit-Heartbeat.py”文件，然后单击“打开”。加载文件路径如下表所示：

|文件类型|路径|文件名|
|-|-|-|
|Python file|..../2. Python 教程\Python测试程序完整版\8.1：闪烁的心|microbit-Heart beat.py|

![](media/10a9c0efa5d1ed118538f93079c63bb9.png)

![](media/b0997055fb6e2966713ea4b13c4aa554.png)

除了上述Mu软件加载（导入）代码方法之外，还有一种更简单的加载代码方法：先打开Mu软件，然后选中“microbit-Heart beat.py”文件，并继续按下鼠标左键，将选中的文件拖动到Mu软件中。

![](media/64ec693d4785a329d3bcad62ce418338.png)

成功加载如下所示。你也可以自己在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/fe2b57334b6c4e1325a211608c26e3d6.png)

以下是内置图像的列表：

• Image.HEART

• Image.HEART_SMALL

• Image.HAPPY

• Image.SMILE

• Image.SAD

• Image.CONFUSED

• Image.ANGRY

• Image.ASLEEP

• Image.SURPRISED

• Image.SILLY

• Image.FABULOUS

• Image.MEH

• Image.YES

• Image.NO

• Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5,

Image.CLOCK4, Image.CLOCK3, Image.CLOCK2,Image.CLOCK1

• Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW

• Image.TRIANGLE

• Image.TRIANGLE_LEFT

• Image.CHESSBOARD

• Image.DIAMOND

• Image.DIAMOND_SMALL

• Image.SQUARE

• Image.SQUARE_SMALL

• Image.RABBIT

• Image.COW

• Image.MUSIC_CROTCHET

• Image.MUSIC_QUAVER

• Image.MUSIC_QUAVERS

• Image.PITCHFORK

• Image.PACMAN

• Image.TARGET

• Image.TSHIRT

• Image.ROLLERSKATE

• Image.DUCK

• Image.HOUSE

• Image.TORTOISE

• Image.BUTTERFLY

• Image.STICKFIGURE

• Image.GHOST

• Image.SWORD

• Image.GIRAFFE

• Image.SKULL

• Image.UMBRELLA

•
Image.SNAKE，Image.ALL_CLOCKS，Image.ALL_ARROWS

通过micro USB线连接micro：bit和电脑，点击“刷入”按钮将代码下载到micro：bit。

![](media/f00f946e1f194811b1c84725e0eb5d16.png)

![](media/18c70cf16dcf8c9694a1af8b12530cf9.png)

![](media/c3353c8be0c73aa8216dd911f04e0859.png)

如果代码有错误，也可以将代码成功下载到micro：bit，但无法正常工作。如果sleep写为sleeps，点击“加载”按钮，代码也会被下载到micro：bit。

![](media/c3353c8be0c73aa8216dd911f04e0859.png)

下载完成后，led矩阵提示一些错误信息，以及错误的行号。点击“REPL”按钮之后，再按下micro：bit的重置按钮（背面的复位按钮，不是A、B按键），错误信息将显示在REPL框中，如下所示：

![](media/4fb05eaac3f9511d329132c05af06e37.png)

再次单击“REPL”按钮，将关闭REPL模式，然后你就可以刷新新代码了。为了确保代码正确，完成代码后，单击“检查”按钮检查代码是否有错误。如下图所示，点击“检查”按钮，然后Mu将指示代码的错误。

![](media/787437f31ea29160e09a760998b42149.png)

根据错误提示，正确修改代码。然后再点击“检查”按钮，Mu在下面的栏上显示没有问题。

![](media/8e5afe58b5a338d15a2515e5cb1c134d.png)

实验结果:

代码完成之后，经过点击“检查”按钮检查代码无误后，再点击“刷入”按钮，将代码上传到micro：bit，micro USB数据线不要拔下来，利用micro USB数据线上电，就可以看到micro:bit上的LED点阵屏循环显示“❤”图案和“

![](media/04fdfc9060943954e7938bb1a741d626.png)

”图案。

### 2：LED点阵中单个LED显示

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

实验说明：

micro：bit主板的LED点阵共由25个发光二极管组成，5个一组，分别对应X和Y方向，形成一个5×5的矩阵，且每个发光二极管是放置在行线（X）和列线（Y）的交叉点上，我们可以通过设置坐标点来实现对25个LED中某一个LED的控制。例如，想要LED点阵中第1行第1个LED点亮，可以设置坐标点为（0，0）；第1行第3个LED点亮，可以设置坐标点为（2，0）；第1列第5个LED点亮，可以设置坐标点为（0，4）；第3列第2个LED点亮，可以设置坐标点为（2，1），依此类推。

![](media/a44f7625e2b1d61819bfc1985c321796.png)

准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开离线版本的Mu软件。

实验代码：

用Mu软件打开“microbit-LED点阵中单个LED显示.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.2：LED点阵中单个LED显示|microbit-Light up an LED .py|

加载完成后，如下图所示，你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/46b7bb3da75e244f77172e86739cee43.png)

您需要单击“检测”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/68230245e947fd334674b2254ae1ec79.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/29e23c53939a40399596a11dbc7e100e.png)

实验结果：

代码成功下载到micro：bit 之后，micro USB数据线不要拔下来，利用micro USB数据线上电，就可以看到micro:bit上处于坐标点(1,0)的LED的亮灭状态，持续0.5s；再次切换坐标点(3,4)的LED的亮灭状态，持续0.5s。循环进行。

参考文献：

关于休眠（延时）功能的细节，请参考链接[:
https://microbit-micropython.readthedocs.io/en/latest/utime.html](E:\\readthedocs keyes\\KE3021 Keyes套件 turtle-bit Micro bit 小乌龟 多功能 智能小车（含主板）\\docs\\2. Python 教程\\ https:\\microbit-micropython.readthedocs.io\\en\\latest\\utime.html)

### 3：5\* 5 LED点阵图案显示

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

实验说明：

点阵在我们生活中很常见，很多都有用到它，比如LED广告显示屏，电梯显示楼层，公交车报站等等。

micro：bit主板的LED点阵共由25个发光二极管组成，上一课我们已经讲过通过设置坐标点来实现对LED点阵的25个LED中的某个LED的控制，这样可以通过设置多个坐标点控制多个LED的亮灭使得LED点阵能够显示图案、数字、字符串。我们也可以在特定代码中通过点击
LED点阵的灰白色小正方形点亮
LED点阵对应的LED来实现LED点阵显示图案、数字、字符串。除了上述方法还可以使用自定义图案使LED点阵显示图案。

准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开离线版本的Mu软件。

实验代码：

代码1：

用Mu软件打开“microbit-5×5 LED Dot Matrix-1.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python 测试程序完整版\8.3：5 5 LED点阵图案显示|microbit-5× 5 LED Dot Matrix-1.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/130fb854b726386dadc9fa67cf842cdd.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/d65fc2d7299302191956848415a1e71c.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/fda1fe3e3306966f9e5a1bc894adbe21.png)

代码2：

用Mu软件打开“microbit-5×5 LED Dot Matrix-2.py“，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python 测试程序完整版\8.3：5 5 LED点阵图案显示|microbit-5×5 LED Dot Matrix-2.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/47c25839c117bcc4a073398c3e531749.png)

您需要单击“检测”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/f848ab13f28f223a9089b6ec1f9fb5d4.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/cef9ee692c3c4471daa97848aec9341c.png)

实验结果：

代码1成功下载到micro：bit 之后，micro USB数据线不要拔下来，利用micro USB数据线上电，就可以看到micro:bit上的5×5 LED点阵显示“向下”图案

![](media/d4e278da768e447ed344d581e671f57a.png)

；

代码2成功下载到micro：bit之后，micro USB数据线不要拔下来，利用micro USB数据线上电，就可以看到micro：bit主板的5×5 LED点阵开始显示数字1、2、3、4、5，然后循环显示“向下”图案

![](media/d4e278da768e447ed344d581e671f57a.png)和“西北”方向图案![](media/2a45fca9d836ce38674c347c70c81e02.png)

参考文献：

display.scroll()
：在显示器上水平滚动数值。如果值是整数或浮点，则首先使用str（）将其转换为字符串。

https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)

### 4：micro:bit的可编程按键

![](media/06be84fb11b1fd07cd0cbb392132b903.png)

实验说明：

![](media/13f8f274b4c420c973de29619432bd6e.png)按键可以控制电路的通断，把按键接入电路中，不按下按键的时候电路是断开的，一按下按键电路就通啦，但是松开之后就又断了。可是为什么按下才通电呢？这得从按键的内部构造说起。没按下之前，电流从按键的一端过不去另一端，按键的两端就像两座山，中间隔着一条河，我们在这座山过不去另一座山；按下的时候，按键内部的金属片把两边连接起来让电流通过，就像搭了一座桥，把两座山连接起来。

按键内部结构如图：

![](media/d2a204e61c768f18924150db58aee093.png)

，未按下按键之前，1、2就是导通的，3、4也是导通的，但是1、3或1、4或2、3或2、4是断开（不通）的；只有按下按键时，1、3或1、4或2、3或2、4才是导通的。

micro：bit主板有三个按键，反面的是复位按钮，正面的是两个可编程按键，通过对两个可编程按键组合可以有三种组合，作为输入元件。我们结合上节课的LED点阵，一起来学习按键吧。我们做一个按键三连，分别按A、B和AB同时按，对应显示屏分别显示A、B和AB。

准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开离线版本的Mu软件。

实验代码：

代码1：

用Mu软件打开“microbit-Programmable Buttons-1.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.4：microbit的可编程按键|microbit-Programmable Buttons-1.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/74e42332b19639f51dfb25309e723349.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/bcefe50dbfca83b8250a3238f079f023.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/a1cd5ea6edb9ad5191cf60dca37f76d5.png)

代码2：

用Mu软件打开“microbit-Programmable Buttons-2.py“文件，加载代码的路径如下：

|文件类型|路经|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.4：microbit的可编程按键|microbit- Programmable Buttons-2.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/9ab10cf9c941fab6e5ec181c65e67113.png)

![](media/94849305cba4d1cb307d2d73376f4e18.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/a59989d5f01fb5eb50a8b3271759a1cb.png)

![](media/94849305cba4d1cb307d2d73376f4e18.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/20b65aadf74277fb7c9352daceccb767.png)

![](media/94849305cba4d1cb307d2d73376f4e18.png)

实验结果：

代码1成功下载到micro：bit 之后，micro USB数据线不要拔下来，利用micro USB数据线上电，按下micro：bit主板上正面按键A，我们可以看到5×5 LED点阵显示字符“A”；按下micro：bit主板上正面按键B，我们可以看到5×5 LED点阵显示字符“B”；同时按下micro：bit主板上正面按键A和B，我们就可以看到5×5 LED点阵显示字符“AB”。

USB数据线上电，按下micro：bit主板上正面按键A，条形图高度值增加
，表现为LED点阵亮的行数增加；按下正面按键B，减少条形图高度，表现为LED点阵亮的行数减少。

### 5：micro:bit学习测温度

实验说明：

micro:bit主板实际上并不带温度传感器，而是采用nRF52833芯片内置的温度传感器进行温度检测，所以检测的温度更接近芯片的温度，可能与周围环境温度存在一定的误差。在这一课程中，我们先利用该传感器测试当前环境中的温度，并将测试结果在显示数据(设备)中显示，再通过设置该传感器检测的温度范围来控制LED点阵显示不同的图案。

注意：micro:bit主板的温度传感器在这里：

![](media/206c8ec1c3f11d2de8d0f42fdf5b6b47.png)

准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开离线版本的Mu软件。

实验代码：

代码1：

用Mu软件打开“microbit-Measurement
-1.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.5：microbit学习测温度|microbit-Measurement -1.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/263217ce26b961ec78001c641cca79eb.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/fb3f5531b6527af9b05ea1c40f064d66.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/e90ff3d8dcbf92b78d58e0c88398b668.png)

代码1成功下载到micro：bit之后，micro USB数据线不要拔下来，并且利用micro USB数据线上电。先点击“REPL”按钮，再按一下micro:bit后面的复位按钮，这样，BBC microbit REPL窗口打印并显示了micro：bit的温度传感器检测到当前环境中的温度值，如下图：（这里的字母C表示摄氏温度单位，而摄氏温度单位（℃）会导致乱码）

![](media/dcbc24360edc2e9afe241f578a04769b.png)

代码2：

用Mu软件打开“microbit-Measurement
-2.py“文件，加载代码的路径如下：

|文件类型|路经||
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.5：microbit学习测温度|microbit-Measurement -2.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

这里设置的温度值可以根据实际情况重新设置

![](media/7c4ebe8ec2879d35e5a8a4ede2ac6dd0.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/754d122ae30f07ece5cfbfe4c863af9b.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/a5cf9f0b8435ddd58cddd33c2e3422e6.png)

实验结果：

代码2成功下载到micro：bit之后，micro USB数据线不要拔下来，利用micro USB数据线上电，当外界环境中的温度小于35℃时，micro：bit主板的5×5 LED点阵中显示图案

![](media/4b1765e12b413dc5d562f2a16d32392f.png)；用手按住micro：bit主板的温度传感器，温度大于等于35℃时，5×5 LED点阵中显示图案![](media/f2705fbc4886efcfaac96589ca255f66.png)

### 6：micro:bit的地磁传感器（磁力计/指南针）

![](media/24c31bb0174e2ac672203e5c36c6875e.png)

实验说明：

磁力计原始数据。常见的指南针主要部件是一根磁针，在地磁场的作用下可以转动并指向地磁北极（地磁北极是在地理南极附近），用来辨别方向。

micro:bit内部的一个地磁传感器（磁力计、指南针），我们可以读取这个磁力计的读数来判断方位，得到相对于北磁极的数值。返回值是0到360之间的数值，在磁力计首次开始工作（带到新位置后）时系统会自动要求我们对micro:bit主板校准，正确的校准方式是旋转micro:bit主板。需要注意的是，附近要是有金属物件可能会影响读数和校准准确性。

一些地球物理学家们确信，地球磁场是因为固态铁质内核被液态金属“海”所包围而形成的。磁力计指向的北是地磁北极，目前地磁南北极位置位于地理南北极地区，但并不与地球的南北极点完全重合，磁北极和真正的地理北极之间存在一个磁偏角。需要指出的是磁极位置是一直在变化的，历史上还出现过地磁逆转的情况。

我们称呼上的地磁南极，其实是物理上的磁北极，而地磁北极是物理上的磁南极，磁力线从磁北极出射，从磁南极进入，即地磁场从地理南极出来从地理北极进去。地磁南北级与地理南北级基本相反，但不在同一条线上也就是说地磁南极在地理北极附近，地磁北极在地理南极附近，地理南北极的连线和地磁南北级的连线构成磁偏角，即地磁北极（指南针指的方向）与地理北极间的夹角。

准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开离线版本的Mu软件。

实验代码：

代码1：

按下按键A的时候，可以在屏幕上显示磁力计的读数。

sensor
-1.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.6：microbit的地磁传感器（磁力计指南针）|microbit-Magnetic sensor -1.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/e22494eb9e2acc1dbf55f9140b059a79.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/f9d9e44a14dbc538efad17b3fc34d03a.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/208848e6197bb6a6c6eda1fb983c0160.png)

代码说明：首先必须对micro:bit进行校准，因为每个地方地磁场不同，对结果有比较大的的影响，如果是第一次使用指南针，micro:bit会自动提示需要校准。

代码1成功下载到micro：bit之后，micro USB数据线不要拔下来，利用micro USB数据线上电。按下micro:bit主板上正面按键A时，micro:bit主板首先提示校准，屏幕(LED点阵)提示:“TILT TO FILL SCREEN”,然后进入校准界面，校准方式为：旋转micro:bit主板，使得屏幕(LED点阵)画一个封闭的正方形（25个LED都点亮），如下图所示：

 

![](media/4a69464afc26b36bb5d2045ce143679a.jpg)

当封闭的正方形画好后，会显示一个“笑脸”图案

![](media/2c899003f048c2fa8418cad7144574a7.png)

，表示校准完成。

校准完成后，当每次按下按键A的时候，直接在屏幕上显示磁力计读数，北、东、南、西对应0°、90°、180°、270°。

代码2：

朝不同的方向旋转磁力计，LED点阵显示对应的方向图案。

如图所示，如果读数在292.5和337.5之间，就让显示屏显示一个指向右上方的箭头，由于代码里不能输入0.5，所以取的判断数值是293和338。之后再加入其它逻辑加载完成后，如下图所示：

![](media/d1a4e9f62bdf690ba809ae35c347b233.png)

sensor
-2.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.6：microbit的地磁传感器（磁力计指南针）|microbit-Magnetic sensor -2.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/5243172aa935d6796e481d729d4c4e4d.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/f5ec49e385adbadd435d53c6c928a840.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/ef9d34aae9a8486b39e652bd5888bfd6.png)

实验结果：

代码2成功下载到micro：bit之后，micro USB数据线不要拔下来，利用micro USB数据线上电。micro:bit提示校准（校准方法请参考:上面代码1部分），校准完成后，旋转移动micro:bit主板，可以看到micro:bit主板上LED点阵显示方向图案。

### 7：micro:bit的加速度传感器（加速度计）

![](media/24c31bb0174e2ac672203e5c36c6875e.png)

实验说明：

V2主板内置有LSM303AGR
重力加速度传感器（加速度计），其具有8/10/12 bits的分辨率，代码科设置量程为1g、2g、4g,、8g。

我们常使用加速度计来检测机器的姿态。

在本实验项目中，将介绍加速度传感器（加速度计）对几个特殊姿态的检测，之后来查看加速度传感器输出的三轴原始数据。

准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开离线版本的Mu软件。

实验代码：

代码1：

对micro：bit不同的操作，LED点阵显示对应的数字。

sensor
-1.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.7：microbit的加速度传感器（加速度计）|microbit- acceleration sensor -1.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/2794645fd711d6d9818d6ec535205c21.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/413200216f1ad7f7f944f1d7945d8704.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/2f92861588428b5583cc316807ae7713.png)

代码2：

检测加速度在X轴，Y轴，Z轴的不同的值

sensor
-2.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.7：microbit的加速度传感器（加速度计）|microbit- acceleration sensor -1.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/b07ff7ff39a4625dbeb079d9f442e1dc.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/f17fce596798c9db54f7b3d56f19f9c4.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/2a756c546c3bf8993c0170115f818f37.png)

首先，查阅MMA8653FC数据手册，以及micro:bit的硬件原理图得知，micro:bit加速度计坐标如下图所示：

![](media/6303a0ac122680207fe856d9be38d01c.png)

代码2成功下载到micro：bit之后，micro USB数据线不要拔下来，利用micro USB数据线上电。先点击“REPL”按钮，再按一下micro:bit后面的复位按钮，这样，BBC microbit REPL窗口打印并显示了micro：bit的加速度在X轴、Y轴、Z轴的分解，可得数据变化如下图：

![](media/a33c0a930e943a4d97a99f4eacdaa04e.png)

实验结果：

代码1成功下载到micro：bit之后，micro USB数据线不要拔下来，利用micro USB数据线上电。将micro:bit主板晃动，则可见micro:bit显示数字1（表明只要有晃动，无论朝哪个方向晃动，该条件都将满足）。

当micro:bit主板的Logo朝上时，LED点阵显示数字2，Logo朝上示意图如下所示：

![](media/1600323e3e61e331c248cbeda5ccdcfc.jpg)

同理，micro:bit主板的Logo朝上时，LED点阵显示数字3(倒立的3)，Logo朝下示意图如下所示：

![](media/3be80acf957e53117f695801ce19c449.jpg)

当屏幕朝上（指的是LED点阵朝上）时，LED点阵显示数字4。如下图所示：

![](media/5797dd7be9a9c2d3226123e0c29db0bd.jpg)

同理，当屏幕朝下（指的是LED点阵朝下）时，LED点阵显示数字5。

当micro:bit
主板向左倾斜（是指LED点阵先朝上，然后再往左边倾斜）时，LED点阵显示数字6。如下图所示：

![](media/326095934bcff0a925b4f9a09d6cf7d2.jpg)

同理，当micro:bit主板向右倾斜（是指LED点阵先朝上，然后再往右边倾斜）时，LED点阵显示数字7。如下图所示：

![](media/185b0ac204e9b2c54dd8fa93d852568c.jpg)

当不小心碰到micro:bit主板使其从桌面掉落，则为做自由落体运动，此时，micro:bit主板满足自由落体的条件，则LED点阵显示数字8。（注意：此方法操作时，很容易把micro:bit主板摔坏，不建议操作）

注意：（3g、6g、8g，
如果需要满足此条件，则需要达到3倍，6倍，8倍重力加速度甩动micro:bit主板。如果你们有兴趣的话，这部分代码可以自己添加）

### 8：micro:bit的光照强度检测

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

实验说明：

本实验将介绍micro:bit对外界光照强度的检测，由于micro:bit并不自带光敏传感器，对外界光照强度的检测是通过LED矩阵进行的，LED矩阵被用来感知周围的光，并反复地将LED转换成输入，并采样电压衰减时间。这样检测出来的光照强度是一个相对值。

准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开离线版本的Mu软件。

实验代码：

用Mu软件打开“8.8：microbit的光照强度检测
.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.8：microbit的光照强度检测|8.8：microbit的光照强度检测.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/a9551b35b60f8e089b9d1793156fd603.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/9c43bedc74e334cdd6e8406411b96420.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/4b377e13e256213c6d120c81a5b09a78.png)

实验结果：

代码成功下载到micro：bit之后，micro USB数据线不要拔下来，利用micro USB数据线上电。先点击“REPL”按钮，再按一下micro:bit后面的复位按钮，这样，BBC microbit REPL窗口打印并显示了micro：bit中光线传感器检测到的环境中光线强度值，如下图所示。当用手全部遮住micro:bit的LED点阵，亮度级别约为0；然后将micro:bit的LED点阵放置于光照下，随着环境中的光线强度增强时，亮度级别值也在逐渐增大；反之，亮度级别值在逐渐减少。

![](media/acae8fb3199794bd1ff7a7d6988ae987.png)

代码说明：

|from microbit import*|导入micro：bit的库文件|
|-|-|
|gesture = accelerometer.current_gesture()|将accelerometer.current_gesture()赋给于变量gesture|
|while True:|这是一个永久循环，它使micro：bit永远执行这个循环中的代码。|
|Lightintensity = display.read_light_level()|将display.read_light_level()赋给于变量Lightintensity|
|print("Light intensity:", Lightintensity)|BBC microbit REPL窗口打印光线传感器检测到的光线亮度级别值|
|sleep(100)|延时100毫秒|

### 9：扬声器

![](media/ac515b9ae8891dc32f368a29f194a2fb.png)

实验说明：

micro:bit主板有内置扬声器，这使得在你的项目中添加声音变得非常容易。通过编程使扬声器发出各种各样的音调，例如编写一首歌曲：《欢乐颂》，让扬声器播放出来。

准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开离线版本的Mu软件。

实验代码：

用Mu软件打开“microbit-Speaker .py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.9：扬声器|microbit-Speaker.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/e3648645fd929cce2ef0df0a155fd2c1.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/c902884bd21abb090f1d5f956d4a0246.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/2fb842a6359f87db926d24c2679276d5.png)

实验结果：

代码成功下载到micro：bit之后，micro USB数据线不要拔下来，利用micro USB数据线上电，micro:bit主板上的扬声器发出声音且LED点阵显示音乐标志图案。

代码说明：

|from microbit import*|导入micro：bit的库文件|
|-|-|
|import audio|audio库文件|
|while True:|这是一个永久循环，它使micro：bit永远执行这个循环中的代码。|
|audio.play(Sound.GIGGLE)|发出giggle的声音|
|sleep(1000)|延时1000毫秒|

### 10：触摸感应logo

![](media/644695850097c5ade080bb4848b4b481.png)

实验说明：

如果你有了micro:bit主板，你可以在你的项目中使用金色的触摸感应logo作为另一个输入，这就像多了一个按钮。触摸感应采用的是电容式触摸传感器，当你手指按下（或触摸）它时，它就能感应到电场的微小变化----就像你的手机或平板电脑屏幕一样。当你像按按钮一样按下它时，你可以在程序中触发事件。

准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开离线版本的Mu软件。

实验代码：

用Mu软件打开“microbit-Touch Sensitive Logo .py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.10：触摸感应logo|microbit-Touch Sensitive Logo.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/18c44bfabcebdd5e1ab5229224787840.png)![](media/84b5714a76fef46bca76dab286583e2c.png)

代码说明（怎样工作的？）：（1）micro:bit以毫秒(数千分一秒)记录它被启动的时间。这被称为运行时间。

（2）当你按下按钮A时，一个名为start的变量被设置为当前运行时间。

（3）当你按下按钮B时，开始时间将从新的运行时间中减去，以计算出从你启动秒表以来已经过去了多少时间。这个差异被加到总时间中，总时间存储在一个名为time的变量中。

（4）如果你按下金色LOGO图标，程序就会在LED显示屏上显示经过的总时间。它通过除以1000将时间从毫秒(千分之一秒)转换为秒。它使用整数除法运算符给出整数(整型)的结果。

running的布尔变量来控制该程序。布尔变量只能有两个值:true或false。如果“running”为“true”，则表示秒表已经启动。如果“running”为假，则表示秒表未启动或已停止。

（6）如果“running”为真，则跳动的心脏循环显示在LED点阵屏。

“running”为假时，当你按下金色LOGO图标时，它将只显示时间。

（8）如果秒表已经启动，如果“running”为真时，则确保只有按下按钮B时，时间变量才会更改，代码还可防止错误读数。

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/c431478795c88e6bbc7abe8edb1cab56.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/4a70f7285afbb30a7133dc25cc79a0aa.png)

实验结果：

代码成功下载到micro：bit之后，micro USB数据线不要拔下来，利用micro USB数据线上电，按下按钮A开始秒表运行。当计时时，LED点阵屏上就会显示一个跳动的心脏。按按钮B停止，你可以随时启动和停止它，它会不断增加时间，就像一个真正的秒表。按下micro:bit主板前面的金色LOGO标志，以秒为单位显示测量的时间。要将时间重置为零，请按micro:bit主板背面的reset按钮。

### 11：麦克风

![](media/3073a8af772ab91ecf264843b37d3b74.png)![](media/7f0741158e734ff8449d5b87d5ba85f4.png)

实验说明：

micro:bit
主板有一个内置麦克风，可以测量环境的声音程度。你可以使用它作为一个简单的输入---当你鼓掌时，micro:bit主板上前面内置麦克风LED指示灯会被打开。它还可以测量声音的强度，所以你可以制作一个噪音等级表或与音乐合拍的迪斯科灯光。麦克风是在micro:bit
主板的背面，而在前面，你会发现一个内置麦克风LED指示灯，还有紧挨着让声音进入麦克风的孔。当你micro:bit主板在测量声音级别时，它就会亮起来。

准备：

（1）通过micro USB线连接micro：bit和电脑。

（2）打开离线版本的Mu软件。

实验代码：

代码1：

用Mu软件打开“microbit-Microphone.py“文件，加载代码的路径如下：

|文件类型|路经|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.11：麦克风|microbit-Microphone-1.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/7ce55e2eedc448f8ce6a3934ea125fdf.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/85f87aeda6750d7513f2031281b7e12b.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/3830e6e158aa91a4ac203bfb0465786e.png)

USB数据线上电。当你鼓掌时，micro:bit
主板上的LED点阵显示“❤”图案；当外界环境安静时，micro:bit
主板上的LED点阵显示“

![](media/04fdfc9060943954e7938bb1a741d626.png)

”图案。

代码2：

用Mu软件打开“microbit-
Microphone-2.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.11：麦克风|microbit- Microphone -2.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/533c15216401f099b36255e3dc644d79.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/aee92277a529d1d07124b7de44290371.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/a7f3c67a4263f54d273ba22ac3242898.png)

实验结果：

LED点阵显示检测到的此时环境中最大声音级别值（这里需要注意：通过按micro:bit背面的重置按钮重置最大值。）；当鼓掌时，测量的声音越大，LED点阵屏的25个LED就越亮。

### 12：micro:bit的蓝牙无线通信

虽然micro:bit拥有一个低功耗蓝牙模块，可以进行蓝牙连接发送数据等，但它只有16k的RAM。BLE堆栈占用了12k RAM，这意味着没有足够的空间来运行microPython；也意味着在同一时刻，microPython和蓝牙服务只能运行一个。

在将来可能配备32k RAM的版本就可以支持蓝牙服务了，在此之前，microPython还无法支持蓝牙。

[https://microbit-micropython.readthedocs.io/en/latest/ble.html](https://microbit-micropython.readthedocs.io/en/latest/ble.html)

上面的实验是使用micro：bit自带的传感器模块和LED点阵，接下来的实验都是micro：bit与Keyes Micro：bit mini smart robot car扩展板上的传感器模块、无源蜂鸣器，和2个RGB灯等的拓展实验。

USB
线与micro：bit主板的连接和关闭乌龟车扩展板上电源（拨动POWER拨码开关到OFF一端）；同理，micro：bit主板从乌龟车扩展板拿下来之前也要先断开micro USB
线与micro：bit主板的连接和关闭乌龟车扩展板上电源（拨动POWER拨码开关到OFF一端）。）

### 13：无源蜂鸣器播放音乐

![](media/74060fac6c085d68066db94d1ada3a99.png)

实验说明：

我们可以用micro：bit制作许多互动作品，其中最常用的是声光显示。之前所有的实验都和LED有关。然而，这个实验中的电路可以产生声音。通常情况下，实验是用蜂鸣器或扬声器进行的，而蜂鸣器更简单、更容易使用。

我们这里介绍的蜂鸣器是无源蜂鸣器。它不能由自身驱动，而是由外部脉冲频率驱动。不同的频率产生不同的声音。我们可以使用micro：bit来编码歌曲的旋律，这实际上是非常有趣和简单的。

蜂鸣器可分为有源蜂鸣器和无源蜂鸣器两种。无源蜂鸣器利用电磁感应现象，为音圈接入交变电流后形成的电磁铁与永磁铁相吸或相斥而推动振膜发声，接入直流电只能持续推动振膜而无法产生声音，只能在接通或断开时产生声音。

　　有源蜂鸣器往往比无源蜂鸣器的贵，就是因为里面多个震荡电路，只需接入额定电压的直流电即可发出指定频率的声音，频率由内部振荡电路决定，无法改变。而无源蜂鸣器内部不带振荡源，直流信号无法令其鸣叫，须用方波驱动。

　　（1）制作成本低；  
　　（2）声音频率范围宽，可高分贝的发出某些频率的超声波以及可以做出“多来米发索拉西”的效果；  
　 （3）在一些特例中，可以和LED复用一个控制IO口。

无源蜂鸣器频率是由英文和数字组成的音名，选择不同的音名就能改变不同的频率啦。声音频率的高低叫做音调。在音乐课上，老师教过我们唱“1（Do）、2（Re）、3(Mi)、4(Fa) 、5(Sol) 、6(La) 、7(Si)”是音乐当中的唱名，就对应了音调中的C、D、E、F、G、A、B这些音名。

|1（Do）|2（Re）|3(Mi)|4(Fa)|5(Sol)|6(La)|7(Si)|
|-|-|-|-|-|-|-|
|C|D|E|F|G|A|B|

频率（音调）高低判断时先看后面的数字，数字越大，音调越高，数字相同时看前面的字母，从C到B频率（音调）越来越高；而节拍是音符延时时间，数值越大，延时时间越长。

节拍是指每个音符持续的时间。音谱中不带线的一个音符就是一拍，延时1000毫秒，而带一条下划线的音符节拍是不带线音符节拍的1/2，带两条下划线的音符节拍是不带线音符节拍的1/4（

![](media/9280991ebf66dac53c3d692cb6acf2cf.png)

）

car
扩展板上自带无源蜂鸣器元件，它是由micro bit主板的P0接口控制。实验中我们用软件自带的库文件，让无源蜂鸣器演奏”欢乐颂“歌曲，下面是《欢乐颂》歌曲的简谱。

![](media/1e6219c9dd2104c3289be2d93f388858.jpg)

准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro：bit主板和电脑。

（5）打开离线版本的Mu软件。

实验代码：

用Mu软件打开“microbit-Passive Buzzer.py“文件，加载代码的路径如下：

|文件类型|路经|文件名|
|-|-|-|
|Python file|..2. Python 教程\Python测试程序完整版\8.13：无源蜂鸣器播放音乐|microbit-Passive Buzzer.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）
![](media/be6adda4f764f9f8084874d33106f2eb.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/71f696598e8b04043a6ca0643e8e6174.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/93ba90fd957cd821c59c44d37b19c827.png)

4 .实验结果：

代码成功下载到micro：bit之后，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。
这样，乌龟车扩展板上的无源蜂鸣器一直循环播放《欢乐颂》歌曲。

参考文献：

music.play()：是被用来演奏音乐，MicroPython有很多内置的音乐旋律。

### 14：RGB灯实验

![](media/671b9bd2f40e6c6509399f93794fbda5.png)

实验说明：

![](media/ad8930da839191890e4f24bf4bb34c66.png)RGB色彩模式是工业界的一种颜色标准，是通过对红(R)、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色的，RGB即是代表红、绿、蓝三个通道的颜色，这个标准几乎包括了人类视力所能感知的所有颜色，是目前运用最广的颜色系统之一。

显示器大都是采用了RGB颜色标准，在显示器上，是通过电子枪打在屏幕的红、绿、蓝三色发光极上来产生色彩的，电脑一般都能显示32位颜色，有一千万种以上的颜色。电脑屏幕上的所有颜色，都由这红色绿色蓝色三种色光按照不同的比例混合而成的。一组红色绿色蓝色就是一个最小的显示单位。屏幕上的任何一个颜色都可以由一组RGB值来记录和表达，因此这红色绿色蓝色又称为三原色光，用英文表示就是R(red)、G(green)、B(blue)。

RGB是从颜色发光的原理来设计定的，通俗点说它的颜色混合方式就好像有红、绿、蓝三盏灯，当它们的光相互叠合的时候，色彩相混，而亮度却等于三者亮度之总和，越混合亮度越高，即加法混合。红、绿、蓝三盏灯的叠加情况，中心三色最亮的叠加区为白色，加法混合的特点：越叠加越明亮，因此被通常被人们称为七彩LED。

红、绿、蓝三个颜色通道每种色各分为256阶亮度，用数字表示为从0、1、2...直到255。注意虽然数字最高是255，相当于100%，但0也是数值之一，因此共256级。在0时“灯”最弱——是关掉的，而在255时“灯”最亮。当三色灰度数值相同时，产生不同灰度值的灰色调，即三色灰度都为0时，是最暗的黑色调；三色灰度都为255时，是最亮的白色调。

|颜色样式|RGB数值（R,G,B）|颜色代码|颜色样式|RGB数值（R,G,B）|颜色代码|
|-|-|-|-|-|-|
|黑色|0,0,0|#000000|红色|255,0,0|#FF0000|
|绿色|0,255,0|#00FF00|蓝色|0,0,255|#0000FF|
|青色|0,255,255|#00FFFF|深红色|255,0,255|#FF00FF|
|黄色|255,255,0|#FFFF00|白色|255,255,255|#FFFFFF|
|......|.......|......|......|......|......|

B
添加在一起（即所有光线反射回眼睛）可产生白色。加成色用于照明光、电视和计算机显示器。例如，显示器通过红色、绿色和蓝色荧光粉发射光线产生颜色。绝大多数可视光谱都可表示为红、绿、蓝
(RGB)
三色光在不同比例和强度上的混合。这些颜色若发生重叠，则产生青、洋红和黄。RGB灯分为共阳、共阴两种，在这个乌龟车的扩展板上，焊接有2个RGB灯，我们可以利用这2个GRB灯做为乌龟车的指示灯。为了节约IO口资源，我们利用1个PCA9685PW芯片的部分引脚来控制2个RGB灯。

这一课程中我们做2个实验，一个是2个RGB灯循环亮起红、绿、蓝、青、深红、黄、白7种颜色灯光，另一个是2个RGB灯渐变显示不同颜色灯光。

准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro:bit主板和电脑。

（5）打开离线版本的Mu软件。

实验代码：

代码1

RGB灯循环亮起7种颜色光

用Mu软件打开“microbit-RGB experiment-1.py“文件，加载代码的路径如下：

<table style="width:100%;">

|文件类型|路经|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python 测试程序完整版\8.14：RGB灯实验|microbit-RGB experiment-1.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/6dfe686d0afd8d438258b788474a1f8b.png)

不要点击“刷入”，因为你还需要做一些额外的工作：导入“keyes_Bit_Turtle_Car.py“库文件到micro:bit中。这个库文件包含了Micro:bit
迷你智能乌龟车的控制方法，我们将这些方法集成到一个“keyes_Bit_Turtle_Car.py”库文件中，这使得您更容易通过Python代码来控制Micro:bit
迷你智能乌龟车。这就像MakeCode代码中的扩展库文件一样。

导入“keyes_Bit_Turtle_Car.py“文件

Mu保存文件的默认目录是“Mu_code”，它位于用户目录的根目录中。参考文献链接：[https://codewith.mu/en/tutorials/1.0/文件](https://codewith.mu/en/tutorials/1.0/files)

例如，在windows系统中，假设您的系统安装在电脑C驱动器上，则用户名为“Administrator”，那么“mu_code”目录的路径是“C:\Users\Administrator\mu\_
code”。在Linux系统上，“mu_code”目录的路径是“~/home/mu_code”

进入“mu_code”文件夹。

![](media/d271a92404720dbd8cf7c858732b7767.png)

拷贝“keyes_Bit_Car_Driver.py“库文件到”mu_code“文件夹。代码路径如下：

|文件类型|Path|文件名|
|-|-|-|
|Python file|.. /Python Code/ Libraries|keyes_Bit_Turtle_Car.py|

复制成功，如下图：

![](media/b63f5b2b6c417aeef87456479f008eec.png)

先打开Mu软件并连接micro:bit到电脑，接着点击“文件”按钮，再拖着“keyes_Bit_Turtle_Car.py“库文件到micro:bit中。

![](media/6ce84eda6d9bd568fa24a648b17370cd.png)

几秒钟后，导入完成。导入成功后，您将在左侧方框中可以看到它。

![](media/ba98ac5518fffa5bde74363f4e851615.png)

库文件导入成功后，您还需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/3adda7cb5621e4e0b5d9c2d5f846f221.png)

但是，单击“检查”按钮来检查代码是否有错误时，即使代码没有错误时也会出现如下提示语，这提示语只是一些警告语，而不是代码错误提示语。也就是说整个代码是没有错误的。

![](media/b27eb6846ce642e80170ac3b8a26b2c5.png)

![](media/67ff667a61837491f09e864d2ca39957.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/101a29513dab67937d1266df38dd951d.png)

如果点击“刷入”按钮后程序错误或实验现象错误，请确认您是否已经导入好我们提供给micro:bit
的“keyes_Bit_Turtle_Car.py“库文件。

注意:

如果您在micro:bit板上下载了其他程序，但“keyes_Bit_Turtle_Car.py“库文件程序除外。在使用Micropython编程之前，您需要将“
keyes_Bit_Turtle_Car.py”库文件导入到micro：bit。

如果您始终使用相同的
micro：bit板进行Micropython编程，则无需多次将“keyes_Bit_Turtle_Car.py”库文件发送到micro：bit；反之，就需要再次将“keyes_Bit_Turtle_Car.py”库文件发送到micro：bit。

代码2：

RGB灯渐变显示不同颜色灯光

用Mu软件打开“microbit-RGB实验-2.py“，加载代码的路径如下：

|文件类型|路经|文件名|
|-|-|-|
|Python file|../Python code/8.14：RGB实验/2个RGB实验|microbit-RGB实验-2.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/e4b3daaabbe4869e256dd126e7e9930d.png)![](media/0e9f71ae90a13ab857ca15a383ec70f3.png)

单击“文件”按钮导入“keyes_Bit_Car_Driver.py“库文件到micro:bit
。如果micro:bit已经含有库文件，就不需要再添加库文件了。

![](media/98d20d763b985ce62240aa5490fda78f.png)

![](media/0e9f71ae90a13ab857ca15a383ec70f3.png)

确定库文件导入之后，您还需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/7cbd5efb710462fc6d9ff557ffe721a6.png)

![](media/0e9f71ae90a13ab857ca15a383ec70f3.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/d1271bb036f37fb0f7af0dc768c40a03.png)

![](media/0e9f71ae90a13ab857ca15a383ec70f3.png)

实验结果：

代码1成功下载到micro：bit之后，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，乌龟车上2个RGB灯循环亮起红、绿、蓝、青、深红、黄、白7种颜色灯光。

代码2成功下载到micro：bit之后，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，乌龟车上2个RGB灯渐变显示不同颜色灯光。

### 15：4个WS2812 RGB灯亮起

![](media/b6f9010d508b3d2dadb50ae5175bd4ea.png)

实验说明：

Micro:bit的电机驱动扩展板上自带4个WS2812 RGB灯，完全兼容micro bit控制板，是由micro bit的P8控制的。在这一课程中我们利用micro bit的P8控制端控制4个WS2812 RGB灯显示不同的状态。课程中，我们提供4个实验代码，让模块上4个WS2812 RGB灯分别显示3中不同的现象。

|实色效果|英文名称|RGB数值（R,G,B）|颜色代码（16色）|实色效果|英文名称|RGB数值（R,G,B）|颜色代码（16色）|
|-|-|-|-|-|-|-|-|
|![](media/8eb18c098e9fb43de8e4bc1d6bcbb998.png)|红色|255, 0, 0|#FF0000|![](media/a9a509e976933b06b2fdaf8f47b21f9f.png)|橙/桔色|255, 165, 0|#FFA500|
|![](media/02cfaa9a127b2757c4d3b9a76db06fb2.png)|黄色|255, 255, 0|#FFFF00|![](media/d97b84ea891c1f77c96f13ff06336b5d.png)|绿色|0, 255, 0|#00FF00|
|![](media/8e632fcb718937b3b391df553a830950.png)|蓝色|0, 255, 0|#0000FF|![](media/a3cdf397029f4625fffbb34c65d6e1c7.png)|靛蓝色|75, 0, 130|#4B0082|
|![](media/e7ceadb386175c67dea8f22bc891fdea.png)|紫罗兰色|238, 130, 238|#EE82EE|![](media/fb86ba2b7c59633c285d0cd2fc7d31c0.png)|紫色|160, 32, 240|#A020F0|
|![](media/9383aa73e392f24384c7fecaf9b58cd4.png)|黑色|0, 0, 0|#000000|![](media/648da100dfbc3c36e9e8e08a36ebeada.png)|白色|255, 255, 255|#FFFFFF|
|......|......|.......|......|......|......|......|......|

准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro：bit主板和电脑。

（5）打开离线版本的Mu软件。

实验代码：

代码1：

用Mu软件打开“microbit-4 WS2812 RGB lights-1.py“文件，加载代码的路径如下：

|文件类型|路经|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python 测试程序完整版\8.15：4个WS2812 RGB灯亮起|microbit-4 WS2812 RGB lights-1.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/c9d715c85aad3d59cd299d975a5223f5.png)

![](media/6ea65bcb7de4ae5014730d7bd19406cb.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/0d75f3d51d3f52efc4617c944351d6ae.png)

![](media/6ea65bcb7de4ae5014730d7bd19406cb.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/b2a8b5f07e61c340d394d0194d21b644.png)

![](media/6ea65bcb7de4ae5014730d7bd19406cb.png)

代码2：

用Mu软件打开“microbit-4 WS2812 RGB lights-2.py“文件，加载代码的路径如下：

|文件类型|路经|文件名|
|-|-|-|
|Python file|..\2. Python 教程\Python 测试程序完整版\8.15：4个WS2812 RGB灯亮起|microbit-4 WS2812 RGB lights-2.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/68747e0048abd9baee16b466290a57e8.png)

![](media/fc4826c9fa03eef207fa7df89bbc996f.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/aa0cdf3d541029228966abf1eae13212.png)

![](media/fc4826c9fa03eef207fa7df89bbc996f.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/0abda0655a8a5d013361e68045a2e40a.png)

![](media/fc4826c9fa03eef207fa7df89bbc996f.png)

代码3：

用Mu软件打开“microbit-4 WS2812 RGB lights-3.py“文件，加载代码的路径如下：

|文件类型|路经|文件名|
|-|-|-|
|Python file|..\2. Python 教程\Python 测试程序完整版\8.15：4个WS2812 RGB灯亮起|microbit-4 WS2812 RGB lights-3.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/59b9817e1e7d8db9ee2998dcbda19326.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/fee45fe08a681317de687d33f0f798a8.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/227ea3c864c23ec514eca42b5de10aa9.png)

实验结果：

代码1成功下载到micro：bit之后，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，micro:bit电机驱动扩展板上的4个WS2812RGB灯全亮，一种颜色变化，一直循环。

代码2成功下载到micro：bit之后，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，micro:bit电机驱动扩展板上的4个WS2812RGB灯以流水灯的形式点亮，一条线一种颜色，一直循环。

代码3成功下载到micro：bit之后，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，micro:bit电机驱动扩展板上的4个WS2812RGB灯以流水灯的形式点亮，每个灯亮起都是一种随机颜色，一直循环。

### 16：电机驱动 

![](media/f970c9eaf6017ca0ea2bad808d23b359.png)

实验说明：

 keyes Micro：bit迷你智能乌龟车上配有两个直流减速电机，即[齿轮减速电机](https://baike.baidu.com/item/%E9%BD%BF%E8%BD%AE%E5%87%8F%E9%80%9F%E7%94%B5%E6%9C%BA/3249233)，是在普通[直流电机](https://baike.baidu.com/item/%E7%9B%B4%E6%B5%81%E7%94%B5%E6%9C%BA/2404223)的基础上，加上配套齿轮减速箱。齿轮减速箱的作用是，提供较低的转速，较大的力矩。同时，[齿轮箱](https://baike.baidu.com/item/%E9%BD%BF%E8%BD%AE%E7%AE%B1/1059341)不同的[减速比](https://baike.baidu.com/item/%E5%87%8F%E9%80%9F%E6%AF%94/5341327)可以提供不同的转速和力矩。这大大提高了直流电机在自动化行业中的使用率。[减速电机](https://baike.baidu.com/item/%E5%87%8F%E9%80%9F%E7%94%B5%E6%9C%BA/3750851)是指[减速机](https://baike.baidu.com/item/%E5%87%8F%E9%80%9F%E6%9C%BA/873618)和电机（马达）的集成体。这种集成体通常也可称为[齿轮马达](https://baike.baidu.com/item/%E9%BD%BF%E8%BD%AE%E9%A9%AC%E8%BE%BE/7911602)或[齿轮电机](https://baike.baidu.com/item/%E9%BD%BF%E8%BD%AE%E7%94%B5%E6%9C%BA/3377578)。减速电机广泛应用于钢铁行业、机械行业等。使用减速电机的优点是简化设计、节省空间。

Micro:bit电机驱动扩展板上包含PCA9685PW芯片和TB6612FNG芯片等，为了节约IO口资源，我们使用PCA9685PW芯片部分引脚来控制TB6612FNG电机芯片，并且TB6612FNG电机芯片是用来控制两个直流减速电机的转动方向和速度。我们来看一下Micro:bit电机驱动扩展板的示意图和两个芯片的电路图：

![](media/b55acb08d80cfe3315b96b7f4cdc100d.png)

![](media/02e6c39452ef2e16b69eae1ba34b31e3.png)

![](media/8fe5e70058693bcfa59d040d71a328c9.png)

都已经插好在Micro:bit的电机驱动扩展板上（竖着方向），如下图所示，你们最好不要去改变它们的插入方向。这样，如果将我们提供的事例代码下载到microbit板后，电机转动的方向就与事例代码中设置的转动方向一致。

![](media/36c335fa3978a716de9f40996175be17.png)

但是，如果把8个跳线帽都横着插在Micro:bit的电机驱动扩展板上，如下图所示，这样就会导致电机转动方向和事例代码中设置的方向不一样，那这样就需要你自己更改代码了。

![](media/a491869c9cf3c40db4a7b813c925b880.png)

准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro:bit主板和电脑。

（5）打开离线版本的Mu软件。

实验代码：

代码1：

CarRun

用Mu软件打开“microbit-Motor Driving-1.py“文件，加载代码的路径如下：（[How to load the project code?](#AS)）

|文件类型|路经|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.16：电机驱动|microbit-Motor Driving-1.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/c46c2ed0b6a15570075e6658621548aa.png)

)。
如果micro:bit已经含有库文件，就不需要再添加库文件了。

![](media/1b8ee0060682a33c4c97487b5898c63d.png)

确定库文件导入之后，您还需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/a7e8247697d1aedad55b03be7052552b.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/c1faf9e6d656c040ea7d0cd1369d79fb.png)

代码2：

路线图

用Mu软件打开“microbit-Motor Driving-2.py“，加载代码的路径如下：

|文件类型|路经|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.16：电机驱动|microbit-Motor Driving-2.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/87fc0feea7ec79cbe5ee8ff5ffac987d.png)

单击“文件”按钮导入“keyes_Bit_Turtle_Car.py“库文件到micro:bit
。 如果micro:bit已经含有库文件，就不需要再添加库文件了。

![](media/2ce7464e97867aafbacc80eaca3bbf11.png)

![](media/f571a5c43fb9d5c54ac5ab8298e26d27.png)

![](media/a0ef1ac08287b2d4a13be07a0448213b.png)

确定库文件导入之后，您还需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/c59e7fc9cf1f3dee2394990e787ab22c.png)

![](media/f571a5c43fb9d5c54ac5ab8298e26d27.png)

![](media/a0ef1ac08287b2d4a13be07a0448213b.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/ca5ee855fd56458e0bf5cff2e4b5aef3.png)

![](media/f571a5c43fb9d5c54ac5ab8298e26d27.png)

![](media/a0ef1ac08287b2d4a13be07a0448213b.png)

实验结果：

代码1成功下载到micro：bit之后，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，我们可以看到乌龟车将前进1s，后退1s，左转1s，右转1s，原地左旋1s，原地左旋1s，停止1s，并且每种运动状态下LED点阵显示对应图案。一直循环。

代码2成功下载到micro：bit之后，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，当我们第一次按A键时，LED点阵会显示“L”图案，再按B键，可以看到乌龟车前进的路经是“L”；当我们第二次按A键时，LED点阵会显示“口”图案，再按B键，可以看到乌龟车前进的路经是“口”；当我们第三次按A键时，LED点阵会显示“L”，再按B键，可以看到乌龟车前进的路经是“L”；
........；保持循环处于这种状态。

### 17：循迹乌龟车

#### 8.17.1：循迹传感器测试

![](media/275ab53a16f10156f17312d704a97df2.jpg)

实验说明：

keyes Micro:bit迷你智能乌龟车上包含一个3路循迹传感器模块，并且传感器模块上自带有三个电位器，用于调节循迹传感器敏感度。循迹传感器其实也是红外传感器，这里的循迹传感器模块用到的元件是TCRT5000红外对管，TCRT5000红外对管具有一个高发射功率红外发射二极管和一个高灵敏度红外接收管。当发射管的红外信号经反射被接收管接收后，接收管的电阻会发生变化，在电路上一般以电压的变化体现出来。电阻的变化取决于接收管所接收的红外信号强度，常表现在反射面的颜色和反射面接收管的距离。在检测的时候，黑色高电平有效，白色是为低电平有效。

红外对管寻迹：

当乌龟车在白色底面行驶时，装在车下的红外发射管发射红外信号，经白色发射后，被接收管接收，一旦接收管接收到信号，输出端将输出低电平（0）；当乌龟车行驶到黑线时，红外线信号被黑色吸收后，将输出高电平（1），从而实现了通过红外线检测信号的功能。将检测到的信号送到单片机的I/O口，当I/O口检测到的信号为高电平（1）时，表明乌龟车处于黑色的引线上；同理，当I/O口检测到的信号为低电平（0）时，表明乌龟车处于白色地面上。

根据上面的接线图可知，乌龟车上的3路循迹传感器模块集成端口是接在micro:bit
电机驱动扩展板上G 5V P14 P15 P16集合端口，是由micro:bit的P14、P15和P16控制的。3路循迹传感器模块上的左边TCRT5000红外对管是由micro bit的P14控制，中间TCRT5000红外对管是由micro bit的P15控制，右边TCRT5000红外对管是由micro bit的P16控制。在乌龟车底部放上白纸，我们通过旋转3路循迹传感器模块上自带的三个电位器，当传感器模块上的指示灯亮起时，再拿起乌龟车使乌龟车上的两车轮离白纸的高度大概都是0.5cm，传感器模块上的指示灯熄灭，这时灵敏度就调节好了。

准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro：bit主板和电脑。

（5）打开离线版本的Mu软件。

实验代码：

代码1：

用Mu软件打开“microbit-Line tracking detection-1.py“文件，加载代码的路径如下：

|文件类型|路经|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.17：循迹乌龟车\8.17.1|microbit-Line tracking detection-1.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/5b9acbad1174cc31b1e2f43945c0521a.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/0380c263fd4a3f63409135bb6d89176c.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/481b77f110ed30d48548543f91e38f15.png)

代码1成功下载到micro：bit之后，micro USB数据线不能拔下来，利用micro USB数据线上电。先点击“REPL”按钮，再按一下micro:bit后面的复位按钮，这样，BBC microbit REPL窗口打印并显示了micro:bit迷你智能乌龟车上3路循迹传感器模块的左边TCRT5000红外对管检测到的数字信号，当左边TCRT5000红外对管检测到白色物体时，串口监视器窗口显示低电平（0），同时传感器模块对应的左边指示灯亮起；当左边TCRT5000红外对管检测到黑色物体或未检测到物体时，串口监视器窗口显示高电平（1），同时传感器模块对应的左边指示灯不亮，如下图：

![](media/eb9974630634e171c19f8aaa3cc124e0.png)

代码2：

迷你智能乌龟车上的3路循迹传感器传输的巡线值如下：

<td colspan="3">循迹传感器模块上的左、中、右TCRT5000红外对管（电平）|二进制|
|低电平（0）|低电平（0）|高电平（1）|001|
|低电平（0）|高电平（1）|低电平（0）|010|
|低电平（0）|高电平（1）|高电平（1）|011|
|高电平（1）|低电平（0）|低电平（0）|100|
|高电平（1）|低电平（0）|高电平（1）|101|
|高电平（1）|高电平（1）|低电平（0）|110|
|高电平（1）|高电平（1）|高电平（1）|111|
|低电平（0）|低电平（0）|低电平（0）|000|

用Mu软件打开“microbit-Line tracking detection-2.py“文件，加载代码的路径如下：

|文件类型|路经|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.17：循迹乌龟车\8.17.1|microbit-Line tracking detection-2.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/ed144c1677c8879969ea5c2c8f70b354.png)

您需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/152f8725819b0938b3788a57100739e9.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/87ac93978d5149f0c04130cb50ec5ca0.png)

实验结果：

代码2成功下载到micro：bit之后，确定已经开启Keyes Micro:bit迷你智能乌龟车上的电源（拨动POWER拨码开关到ON一端）。这样，乌龟车上的循迹传感器模块只有左边的TCRT5000红外对管检测到白色物体时，micro bit LED点阵左边显示“I”图案，同时循迹传感器模块左边的指示灯亮起；

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

#### 8.17.2：循迹乌龟车 

实验说明：

前面的部分我们学习了循迹传感器和电机驱动的原理和应用，下面我们要结合这两个基本的循迹传感器和电机驱动来做一款循迹乌龟车。

循迹，意思就是循着轨迹，也就是我们经常会看到的走黑线的循迹乌龟车，原理是利用循迹传感器对路面黑色轨迹进行检测，并将路面检测信号反馈给micro bit主板。micro bit主板对采集到的信号予以分析判断，及时控制驱动电机以调整乌龟车转向，从而使乌龟车能够沿着黑色轨迹自动行驶，实现循迹乌龟车自动寻迹的目的。

循迹乌龟车行驶原理：循迹乌龟车根据3路循迹传感器传输的巡线值采取不同的行动。

|循迹传感器模块上的左、中、右TCRT5000红外对管（电平）|二进制|乌龟车的行动|
|-|-|-|-|-|
|低电平（0）|低电平（0）|高电平（1）|001|向右转|
|低电平（0）|高电平（1）|低电平（0）|010|前进|
|低电平（0）|高电平（1）|高电平（1）|011|前进|
|高电平（1）|低电平（0）|低电平（0）|100|向左转|
|高电平（1）|低电平（0）|高电平（1）|101|前进|
|高电平（1）|高电平（1）|低电平（0）|110|前进|
|高电平（1）|高电平（1）|高电平（1）|111|前进|
|低电平（0）|低电平（0）|低电平（0）|000|停止|

![](media/7abb567990baeeb9bb4694b578c1f670.png)

根据上面的接线图可知，乌龟车上的3路循迹传感器模块集成端口是接在micro:bit
电机驱动扩展板上G 5V P14 P15 P16集合端口，是由micro:bit的P14、P15和P16控制的。

准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro：bit主板和电脑。

（5）打开离线版本的Mu软件。

警告：3路循迹传感器应避免在阳光等有红外干扰的环境中使用。阳光中含有大量的不可见光，如红外线和紫外线。在阳光强烈的环境下，3路循迹传感器不能正常工作。](#M11)

编程思路：

程序流程图：

![](media/7e620e084d9c76cf9732c45d18a6727d.png)

实验代码：

用Mu软件打开“microbit- Line tracking car.py“文件，加载代码的路径如下：

<table style="width:100%;">

|文件类型|路经|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.17：循迹乌龟车\8.17.2|microbit- Line tracking car.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/041e340f60041e33a045ccf7d5cbf81d.png)

![](media/89ba87bf5fee4c4635becba29883e9a5.png)

)
如果micro:bit已经含有库文件，就不需要再添加库文件了。

![](media/dbdde9314e0cb5245de3e16ebe87cd32.png)

![](media/89ba87bf5fee4c4635becba29883e9a5.png)

确定库文件导入之后，您还需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/1890091d1bc5e4a9b7541504de32f288.png)

![](media/89ba87bf5fee4c4635becba29883e9a5.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后单击“刷入”按钮将代码下载到micro:bit。

![](media/e8df84134d7b65775c9305a7c435fb1d.png)

![](media/89ba87bf5fee4c4635becba29883e9a5.png)

实验结果：

代码成功下载到micro：bit之后，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，循迹乌龟车能随着黑色轨迹前行，同时，点亮4个WS2812 RGB灯。

特别注意：（1）乌龟车循迹轨道，黑线的宽度必须大于等于3路循迹传感器模块宽度。

测试乌龟车时，不要在阳光明媚的太阳底下测试。测试过程中，如果出现问题，可在暗一点的环境中测试。

### 18：超声波跟随乌龟车

#### 8.18.1：超声波测距

实验说明：

![](media/9810ae67a9c903f3dff413e21fe2d585.jpg)自然界有一种叫蝙蝠的动物，蝙蝠在夜间飞行不是靠眼睛看的，而是靠耳朵和发音器官飞行的。蝙蝠在飞行时，会发出一种尖叫声，这是一种超声波信号，是人类无法听到的，因为它的音频很高。这些超声波的信号若在飞行路线上碰到其他物体，就会立刻反射回来，在接收到返回的信息之后，蝙蝠于振翅之间就完成了听、看、计算与绕开障碍物的全部过程。

![](media/0180b169a1c3b228394b43df704fac32.png)超声波传感器模块的原理跟上面的原理是一样的，超声波传感器模块一触发信号后发射超声波，当超声波投射到物体而反射回来时，模块输出一回响信号，以触发信号和回响信号间的时间差，来判定物体的距离。超声波传感器有敏感范围大，无视觉盲区，不受障碍物干扰等特点，这项技术已经在商业和安全领域被使用25年多了，已经被证明是检测小物体运动最有效的方法。

我们看下超声波传感器模块的图片，两个像眼睛一样的东西，一个就是信号发射端（TRIG），一个就是信号接收端（ECHO）。

![](media/7d1365ccda9dfeff4ba6624f9413877c.png)

根据上面的接线图可知，超声波传感器模块集成端口是接在micro:bit
电机驱动扩展板上5V G P1 P2集合端口，Trig（T）引脚是接在P1处，对应的是micro:bit的P1控制的；Echo（E）引脚是接在P2处，对应的是micro:bit的P2控制的。

工作原理：

![](media/8ff02741199a0f03d8d814a4b72f27d7.png)

10us
的高电平信号去触发；

40KHZ
的方波，并自动检测是否有信号返回；

ECHO（E）
输出一个高电平，高电平持续的时间便是超声波从发射到接收的时间。那么测试距离=高电平持续时间\*340m/s\*0.5。

规格参数：

工作电压：3-5.5V（DC）

工作电流：15mA

工作频率：40khz

最大探测距离：3m左右

最小探测距离：2-3cm

高精度可达 0.2cm

感应角度：不大于15度

输入触发脉冲：10us 的 TTL 电平

TTL
电平信号（高），与射程成正比

准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro:bit主板和电脑。

（5）打开离线版本的Mu软件。

实验代码：

用Mu软件打开“microbit- Ultrasonic Ranging.py“文件，加载代码的路径如下：

|文件类型|路经|文件名|
|-|-|-|
|Python file|..\2. Python 教程\Python测试程序完整版\8.18：超声波跟随乌龟车\8.18.1：超声波测距|microbit- Ultrasonic Ranging.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/961697111d1d5ac8289cd343816b2e5e.png)

单击“文件”按钮导入“keyes_Bit_Turtle_Car.py“库文件到micro:bit
。如果micro:bit已经含有库文件，就不需要再添加库文件了。

![](media/76e1bab2b21ec099a5634d55e3aa16c0.png)

确定库文件导入之后，您还需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/561a1ac9e3a3b618f3508920e70c00ac.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后再单击“刷入”按钮将代码下载到micro:bit。

![](media/99d77d849b9c08608f524343d24cf16a.png)

实验结果：

代码成功下载到micro：bit之后，micro USB数据线不能从micro：bit上拔下来，然后先点击“REPL”按钮，再按一下micro:bit后面的复位按钮，这样，BBC microbit REPL窗口打印并显示了micro:bit mini smart robot car扩展板上的超声波传感器模块与障碍物之间的距离（如下图），并且当障碍物与超声波传感器模块的距离小于10cm时，小车控制板上无源蜂鸣器响起声音。

![](media/879d530b92041805cfaa1199a12736d1.png)

![](media/02b470544ebea01927a5a12c4678d9bc.png)

#### 8.18.2：超声波避障乌龟车

![](media/830318dfa0c756e4b811f26a3acf976d.jpg)

实验说明：

前面的课程我们结合了循迹传感器和乌龟车等结合，制作了一款循迹乌龟车；在这课程中，我们利用超声波传感器模块和乌龟车等结合，制作一个超声波避障乌龟车。它的原理就是，通过超声波传感器测量乌龟车与前方障碍物之间的距离，
根据测试距离控制乌龟车的避障动作。这样，当乌龟车靠近前方障碍物时，让其转弯避开障碍物行走。

准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro:bit主板和电脑。

（5）打开离线版本的Mu软件。

编程思路：

程序流程图：

![](media/61e2c216330939d99f57ec9588dc2f45.png)

实验代码：

用Mu软件打开“microbit-Ultrasonic Avoiding Smart Turtle Car.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.18：超声波跟随乌龟车\8.18.2：超声波避障乌龟车|microbit-Ultrasonic Avoiding Smart Turtle Car.py|

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代码。（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

![](media/60584e0cd6d5539007e740b55dba2c07.png)

单击“文件”按钮导入“keyes_Bit_Turtle_Car.py“库文件到micro:bit。如果micro:bit已经含有库文件，就不需要再添加库文件了。

![](media/4c7a70d74b74f024a0ef2e9f327735ae.png)

确定库文件导入之后，您还需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/3aabbb9f12e68fb99ebb173f4e40fb5f.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后再单击“刷入”按钮将代码下载到micro:bit。

![](media/45a382176f035c835514e99b245e597e.png)

实验结果：

代码成功下载到micro：bit之后，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，乌龟车在离前方障碍物的距离大于15cm时，乌龟车向前走，同时2个RGB灯亮绿色灯；反之，乌龟车向左转，同时2个RGB亮蓝色灯。

#### 8.18.3：超声波跟随乌龟车

实验说明：

前面的课程我们结合了循迹传感器和乌龟车等结合，制作了一款循迹乌龟车；在这课程中，我们利用超声波模块和乌龟车等结合，制作一个超声波跟随乌龟车。它的原理就是，通过超声波传感器模块，测试出乌龟车和前方障碍物的距离，然后根据测试距离控制乌龟车运动状态。

准备：

（1）将micro：bit主板正确插入keyes Micro:bit迷你智能乌龟车。

（2）将电池装入keyes Micro:bit迷你智能乌龟车。

（3）将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端，开启电源。

（4）通过micro USB线连接micro：bit主板和电脑。

（5）打开离线版本的Mu软件。

编程思路：

程序流程图：

![](media/dec69f0ffaf8837f30418e0a9ba25981.png)

实验代码：

用Mu软件打开“microbit-Ultrasonic Follow Smart Turtle Car.py“文件，加载代码的路径如下：

|文件类型|路径|文件名|
|-|-|-|
|Python file|../2. Python 教程\Python测试程序完整版\8.18：超声波跟随乌龟车\8.18.3：超声波跟随乌龟车|microbit-Ultrasonic Follow Smart Turtle Car.py|

![](media/c88d1e2fb30d6549d6c80594f94c8b37.png)

加载完成后，如下图所示。你也可以打开Mu软件，在编辑窗口输入代（注意！所有英文及符号均须以英文填写，最后一行必须有空格。）

单击“文件”按钮导入“keyes_Bit_Turtle_Car.py“库文件到micro:bit
。如果micro:bit已经含有库文件，就不需要再添加库文件了。

![](media/4127908d2ae62581005154438d3c68b1.png)

确定库文件导入之后，您还需要单击“检查”按钮来检查代码是否有错误。如果一行出现光标或下划线，则表明该行的程序有错误。

![](media/9b68d914640d660f5a67f67031f78da8.png)

确定程序代码无误之后，你还需要确定micro USB线已连接到micro:bit和电脑，然后再单击“刷入”按钮将代码下载到micro:bit。

![](media/9260bc4c62a2b30143451f08b597b734.png)

实验结果：

代码成功下载到micro：bit之后，确定已经将Micro:bit的电机驱动扩展板上的POWER拨码开关拨到ON一端。这样，乌龟车可以跟随前方障碍物的移动而移动。乌龟车不同的运动状态，4个WS2812 RGB灯亮起不同的颜色。

注意：障碍物只能在乌龟车的正前方移动，不能拐弯。

## 相关资料链接

BBC microbit MicroPython的官方说明链接：

[https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html)

MicroPython 语言的官方链接：

[https://docs.openmv.io/reference/index.html](https://docs.openmv.io/reference/index.html)

ustruct 库链接：

[https://docs.openmv.io/library/ustruct.html](https://docs.openmv.io/library/ustruct.html)

math 库链接：

[https://docs.openmv.io/library/math.html](https://docs.openmv.io/library/math.html)

utime(sleep_us,tick_us) 库文件链接：

[https://docs.openmv.io/library/utime.html#](https://docs.openmv.io/library/utime.html)
