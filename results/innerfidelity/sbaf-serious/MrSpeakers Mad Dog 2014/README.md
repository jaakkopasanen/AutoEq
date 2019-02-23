# MrSpeakers Mad Dog 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.5; 25 -4.8; 28 -5.2; 31 -5.5; 34 -5.7; 37 -6.0; 41 -6.2; 45 -6.3; 49 -6.4; 54 -6.7; 60 -7.0; 66 -7.1; 72 -7.2; 79 -7.3; 87 -7.7; 96 -8.2; 106 -8.8; 116 -9.5; 128 -10.3; 141 -10.8; 155 -10.7; 170 -10.3; 187 -11.0; 206 -11.2; 227 -11.0; 249 -10.9; 274 -10.6; 302 -10.4; 332 -10.3; 365 -10.0; 402 -8.7; 442 -8.1; 486 -8.0; 535 -6.3; 588 -5.9; 647 -7.4; 712 -7.7; 783 -6.5; 861 -7.2; 947 -7.2; 1042 -7.1; 1146 -7.4; 1261 -7.0; 1387 -7.4; 1526 -7.0; 1678 -6.1; 1846 -5.5; 2031 -4.5; 2234 -2.9; 2457 -1.5; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.7; 4788 -2.4; 5267 -2.5; 5793 -4.8; 6373 -6.5; 7010 -6.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Mad Dog 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Mad Dog 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.72 | 3.5 dB  |
| Peaking | 169 Hz  | 0.94 | -4.2 dB |
| Peaking | 313 Hz  | 1.87 | -2.5 dB |
| Peaking | 1420 Hz | 1.68 | -2.0 dB |
| Peaking | 3237 Hz | 1.13 | 6.8 dB  |
| Peaking | 560 Hz  | 6.92 | 1.9 dB  |
| Peaking | 1910 Hz | 0.56 | 1.8 dB  |
| Peaking | 2626 Hz | 0.3  | -1.8 dB |
| Peaking | 5379 Hz | 2.15 | 2.7 dB  |
| Peaking | 6130 Hz | 3.87 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Mad%20Dog%202014/MrSpeakers%20Mad%20Dog%202014.png)