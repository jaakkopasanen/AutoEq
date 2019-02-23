# MrSpeakers Alpha Dog 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.4; 25 -6.5; 28 -6.6; 31 -6.6; 34 -6.6; 37 -6.5; 41 -6.3; 45 -6.1; 49 -6.0; 54 -5.6; 60 -5.7; 66 -5.6; 72 -4.8; 79 -4.7; 87 -5.2; 96 -5.8; 106 -5.9; 116 -6.1; 128 -6.5; 141 -7.0; 155 -6.9; 170 -7.6; 187 -8.6; 206 -8.9; 227 -9.1; 249 -9.3; 274 -9.3; 302 -9.3; 332 -9.3; 365 -8.3; 402 -8.0; 442 -8.2; 486 -8.4; 535 -8.5; 588 -6.6; 647 -5.5; 712 -5.1; 783 -4.8; 861 -5.5; 947 -6.3; 1042 -6.2; 1146 -4.6; 1261 -4.5; 1387 -5.0; 1526 -4.9; 1678 -4.7; 1846 -3.7; 2031 -3.7; 2234 -2.9; 2457 -2.7; 2703 -2.3; 2973 -2.4; 3270 -2.2; 3597 -1.2; 3957 -0.5; 4353 -0.8; 4788 -1.4; 5267 -1.9; 5793 -3.9; 6373 -4.3; 7010 -3.0; 7711 -4.9; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Alpha Dog 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Alpha Dog 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.59 | -1.6 dB |
| Peaking | 263 Hz  | 1.06 | -4.4 dB |
| Peaking | 505 Hz  | 4.74 | -2.3 dB |
| Peaking | 4292 Hz | 0.88 | 6.3 dB  |
| Peaking | 5827 Hz | 0.75 | -2.6 dB |
| Peaking | 79 Hz   | 5.51 | 1.1 dB  |
| Peaking | 737 Hz  | 4.79 | 1.1 dB  |
| Peaking | 986 Hz  | 7.17 | -1.5 dB |
| Peaking | 2834 Hz | 2.09 | 1.0 dB  |
| Peaking | 3150 Hz | 4.37 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Alpha%20Dog%202014/MrSpeakers%20Alpha%20Dog%202014.png)