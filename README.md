<h1 align="center">
  EbSynth Auto Runer
</h1>
<p align="center">
<a href="https://github.com/Littleor/ebsynth-auto-runer/blob/master/LICENSE" target="blank">
<img src="https://img.shields.io/github/license/Littleor/ebsynth-auto-runer?style=flat-square" alt="github-profile-readme-generator license" />
</a>
<a href="https://github.com/Littleor/ebsynth-auto-runer/fork" target="blank">
<img src="https://img.shields.io/github/forks/Littleor/ebsynth-auto-runer?style=flat-square" alt="github-profile-readme-generator forks"/>
</a>
<a href="https://github.com/Littleor/ebsynth-auto-runer/stargazers" target="blank">
<img src="https://img.shields.io/github/stars/Littleor/ebsynth-auto-runer?style=flat-square" alt="github-profile-readme-generator stars"/>
</a>
<a href="https://github.com/Littleor/ebsynth-auto-runer/issues" target="blank">
<img src="https://img.shields.io/github/issues/Littleor/ebsynth-auto-runer?style=flat-square" alt="github-profile-readme-generator issues"/>
</a>
<a href="https://github.com/Littleor/ebsynth-auto-runer/pulls" target="blank">
<img src="https://img.shields.io/github/issues-pr/Littleor/ebsynth-auto-runer?style=flat-square" alt="github-profile-readme-generator pull-requests"/>
</a>
</p>

---

This is a tool that can help you automate running [EbSynth](https://ebsynth.com/) on your Mac to process the `.ebs`
files generated in the [ebsynth_utility](https://github.com/s9roll7/ebsynth_utility) extension.

## 🛠️ Installation

First, you need to install [EbSynth](https://ebsynth.com/) on your Mac, and move the `EbSynth` to the `/Applications`
folder

Then, all you need is Python 3.6+ and pip, and just run the following commands in you Terminal:

```bash
# Clone and cd
git clone https://github.com/Littleor/ebsynth-auto-runer.git
cd ebsynth-auto-runer

# If you want to use venv
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## 🚀 Usage

With the `ebsynth_utility` extension, you can generate the keyframes and `.ebs` files, and then run the following
command in your Terminal to start the automation:

> Note:
>
> You can freely to use your Mac while the `EbSynth` is running, but you
> should make the `EbSynth` window show on the top of the screen when the `EbSynth` ends the current `ebs` file
> processing.

```bash
# You should replace the /path/to/your/project with your own path which is also the `ebsynth_utility` project path
python main.py /path/to/your/project
```

If you want to know more about the arguments, just run the following command in your Terminal:

```bash
python main.py --help
```

## 📝 TODO

* Add a GUI
* Support Windows
* Support Linux? (If the `EbSynth` supports Linux)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

## 📚 License

This project is Apache-2.0 licensed.






