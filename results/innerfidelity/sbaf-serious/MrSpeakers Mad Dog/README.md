# MrSpeakers Mad Dog
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.2; 25 -2.3; 28 -2.3; 31 -2.4; 34 -2.2; 37 -1.9; 41 -1.2; 45 -0.8; 49 -0.9; 54 -0.9; 60 -2.3; 66 -3.2; 72 -3.4; 79 -5.8; 87 -8.5; 96 -9.5; 106 -9.4; 116 -9.1; 128 -8.8; 141 -8.5; 155 -7.8; 170 -8.3; 187 -8.2; 206 -8.0; 227 -7.6; 249 -7.5; 274 -7.4; 302 -7.2; 332 -7.1; 365 -7.3; 402 -7.4; 442 -7.8; 486 -8.7; 535 -9.0; 588 -7.6; 647 -7.1; 712 -7.6; 783 -8.7; 861 -9.3; 947 -9.1; 1042 -8.2; 1146 -8.2; 1261 -7.9; 1387 -7.7; 1526 -7.4; 1678 -6.8; 1846 -5.8; 2031 -4.2; 2234 -3.2; 2457 -1.8; 2703 -1.4; 2973 -1.2; 3270 -1.1; 3597 -0.9; 3957 -1.1; 4353 -2.5; 4788 -2.2; 5267 -0.5; 5793 -1.2; 6373 -4.3; 7010 -6.4; 7711 -8.4; 8482 -10.4; 9330 -10.8; 10263 -6.7; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Mad Dog GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Mad Dog ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.62 | 4.5 dB  |
| Peaking | 49 Hz   | 2.97 | 5.8 dB  |
| Peaking | 3158 Hz | 1.88 | 5.9 dB  |
| Peaking | 5428 Hz | 3.02 | 5.4 dB  |
| Peaking | 8706 Hz | 3.31 | -5.5 dB |
| Peaking | 119 Hz  | 1.57 | -3.2 dB |
| Peaking | 500 Hz  | 3.13 | -2.1 dB |
| Peaking | 877 Hz  | 3.84 | -2.3 dB |
| Peaking | 1357 Hz | 1.26 | -1.8 dB |
| Peaking | 2279 Hz | 3.31 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Mad%20Dog/MrSpeakers%20Mad%20Dog.png)