# HiSoundAudio Wooduo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.1; 23 -15.1; 25 -15.1; 28 -15.0; 31 -15.0; 34 -14.9; 37 -14.9; 41 -14.8; 45 -14.8; 49 -14.7; 54 -14.7; 60 -14.7; 66 -14.6; 72 -14.6; 79 -14.7; 87 -14.7; 96 -14.7; 106 -14.5; 116 -14.2; 128 -14.0; 141 -13.7; 155 -13.3; 170 -13.0; 187 -12.4; 206 -11.9; 227 -11.2; 249 -10.7; 274 -9.9; 302 -9.2; 332 -8.5; 365 -7.7; 402 -6.9; 442 -6.0; 486 -5.3; 535 -4.6; 588 -3.6; 647 -2.9; 712 -2.2; 783 -2.4; 861 -0.6; 947 -0.5; 1042 -0.8; 1146 -0.8; 1261 -0.9; 1387 -1.3; 1526 -1.8; 1678 -2.0; 1846 -2.0; 2031 -1.9; 2234 -1.9; 2457 -1.7; 2703 -1.5; 2973 -1.3; 3270 -1.2; 3597 -1.5; 3957 -2.4; 4353 -4.9; 4788 -6.8; 5267 -9.1; 5793 -10.5; 6373 -5.2; 7010 -0.8; 7711 -0.5; 8482 -0.8; 9330 -0.8; 10263 -0.8; 11289 -0.8; 12418 -0.8; 13660 -0.8; 15026 -0.8; 16529 -1.8; 18182 -0.8; 20000 -0.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiSoundAudio Wooduo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Wooduo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 0.35 | -12.5 dB |
| Peaking | 101 Hz  | 0.27 | -11.9 dB |
| Peaking | 194 Hz  | 0.86 | -1.0 dB  |
| Peaking | 853 Hz  | 1.55 | 2.2 dB   |
| Peaking | 5469 Hz | 3.55 | -10.3 dB |
| Peaking | 1959 Hz | 2.34 | -0.8 dB  |
| Peaking | 3603 Hz | 3.48 | 0.8 dB   |
| Peaking | 4455 Hz | 6.32 | -1.8 dB  |
| Peaking | 7354 Hz | 6.28 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.7 dB |
| Peaking | 62 Hz    | 1.41 | -9.7 dB  |
| Peaking | 125 Hz   | 1.41 | -10.5 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Wooduo/HiSoundAudio%20Wooduo.png)