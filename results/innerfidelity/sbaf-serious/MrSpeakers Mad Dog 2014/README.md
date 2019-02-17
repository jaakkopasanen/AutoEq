# MrSpeakers Mad Dog 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.4; 25 -3.8; 28 -4.1; 31 -4.4; 34 -4.7; 37 -4.9; 41 -5.1; 45 -5.2; 49 -5.4; 54 -5.6; 60 -5.9; 66 -6.0; 72 -6.1; 79 -6.3; 87 -6.6; 96 -7.2; 106 -7.8; 116 -8.5; 128 -9.3; 141 -9.7; 155 -9.6; 170 -9.2; 187 -9.9; 206 -10.1; 227 -10.0; 249 -9.8; 274 -9.6; 302 -9.4; 332 -9.3; 365 -8.9; 402 -7.7; 442 -7.1; 486 -7.0; 535 -5.2; 588 -4.9; 647 -6.4; 712 -6.6; 783 -5.4; 861 -6.1; 947 -6.2; 1042 -6.0; 1146 -6.4; 1261 -5.9; 1387 -6.3; 1526 -5.9; 1678 -5.0; 1846 -4.4; 2031 -3.4; 2234 -1.9; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -1.3; 5267 -1.5; 5793 -3.8; 6373 -5.5; 7010 -5.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Mad Dog 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Mad Dog 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.33 | 3.9 dB  |
| Peaking | 80 Hz   | 1.35 | 2.1 dB  |
| Peaking | 203 Hz  | 0.33 | -4.1 dB |
| Peaking | 553 Hz  | 1.72 | 3.4 dB  |
| Peaking | 3322 Hz | 0.98 | 6.9 dB  |
| Peaking | 1452 Hz | 6.97 | -1.3 dB |
| Peaking | 2419 Hz | 5.65 | 1.5 dB  |
| Peaking | 3284 Hz | 4.23 | -0.8 dB |
| Peaking | 5083 Hz | 3.12 | 2.6 dB  |
| Peaking | 6686 Hz | 0.91 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Mad%20Dog%202014/MrSpeakers%20Mad%20Dog%202014.png)