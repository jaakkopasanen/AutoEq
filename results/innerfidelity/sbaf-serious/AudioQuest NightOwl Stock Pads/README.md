# AudioQuest NightOwl Stock Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.6; 25 -7.5; 28 -7.4; 31 -7.4; 34 -7.3; 37 -7.2; 41 -7.1; 45 -7.0; 49 -6.9; 54 -6.8; 60 -6.6; 66 -6.6; 72 -6.8; 79 -7.3; 87 -8.0; 96 -9.3; 106 -9.4; 116 -9.4; 128 -10.2; 141 -10.4; 155 -9.8; 170 -9.6; 187 -10.1; 206 -9.8; 227 -9.4; 249 -9.2; 274 -8.8; 302 -8.4; 332 -8.1; 365 -7.7; 402 -7.5; 442 -7.1; 486 -7.2; 535 -7.1; 588 -6.8; 647 -6.6; 712 -6.2; 783 -6.0; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.1; 1261 -5.6; 1387 -5.3; 1526 -4.7; 1678 -3.4; 1846 -1.9; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.7; 3597 -1.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.1; 6373 -3.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AudioQuest NightOwl Stock Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioQuest NightOwl Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.15 | -0.8 dB |
| Peaking | 67 Hz   | 1.59 | 2.2 dB  |
| Peaking | 136 Hz  | 0.79 | -2.1 dB |
| Peaking | 148 Hz  | 0.36 | -1.9 dB |
| Peaking | 3255 Hz | 0.73 | 6.8 dB  |
| Peaking | 1300 Hz | 1.85 | -1.2 dB |
| Peaking | 2018 Hz | 3.89 | 2.1 dB  |
| Peaking | 3422 Hz | 4.58 | -1.6 dB |
| Peaking | 5409 Hz | 2.9  | 2.5 dB  |
| Peaking | 8539 Hz | 1.62 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioQuest%20NightOwl%20Stock%20Pads/AudioQuest%20NightOwl%20Stock%20Pads.png)