# HiSoundAudio Wooduo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.1; 23 -15.1; 25 -15.0; 28 -15.0; 31 -14.9; 34 -14.9; 37 -14.8; 41 -14.8; 45 -14.7; 49 -14.7; 54 -14.6; 60 -14.6; 66 -14.6; 72 -14.6; 79 -14.6; 87 -14.6; 96 -14.6; 106 -14.4; 116 -14.2; 128 -14.0; 141 -13.6; 155 -13.3; 170 -12.9; 187 -12.4; 206 -11.9; 227 -11.2; 249 -10.6; 274 -9.8; 302 -9.2; 332 -8.4; 365 -7.6; 402 -6.8; 442 -6.0; 486 -5.3; 535 -4.5; 588 -3.5; 647 -2.8; 712 -2.1; 783 -2.4; 861 -0.5; 947 -0.5; 1042 -0.8; 1146 -0.8; 1261 -0.9; 1387 -1.3; 1526 -1.7; 1678 -2.0; 1846 -1.9; 2031 -1.8; 2234 -1.8; 2457 -1.7; 2703 -1.5; 2973 -1.2; 3270 -1.2; 3597 -1.4; 3957 -2.4; 4353 -4.9; 4788 -6.8; 5267 -9.0; 5793 -10.5; 6373 -5.2; 7010 -2.7; 7711 -4.9; 8482 -5.1; 9330 -5.1; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiSoundAudio Wooduo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Wooduo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.41 | -8.4 dB |
| Peaking | 121 Hz  | 0.39 | -7.9 dB |
| Peaking | 897 Hz  | 0.78 | 4.9 dB  |
| Peaking | 3586 Hz | 0.7  | 3.7 dB  |
| Peaking | 5366 Hz | 3.56 | -8.3 dB |
| Peaking | 4526 Hz | 4.96 | -3.5 dB |
| Peaking | 5093 Hz | 1.83 | 3.9 dB  |
| Peaking | 5857 Hz | 7.36 | -3.8 dB |
| Peaking | 6810 Hz | 7.65 | 3.6 dB  |
| Peaking | 6895 Hz | 0.89 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB  |
| Peaking | 125 Hz   | 1.41 | -7.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Wooduo/HiSoundAudio%20Wooduo.png)