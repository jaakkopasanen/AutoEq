# MrSpeakers Alpha Dog 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.4; 25 -6.5; 28 -6.6; 31 -6.6; 34 -6.6; 37 -6.5; 41 -6.3; 45 -6.1; 49 -6.0; 54 -5.6; 60 -5.7; 66 -5.6; 72 -4.8; 79 -4.7; 87 -5.2; 96 -5.8; 106 -5.9; 116 -6.1; 128 -6.5; 141 -7.0; 155 -6.9; 170 -7.6; 187 -8.6; 206 -8.9; 227 -9.1; 249 -9.3; 274 -9.3; 302 -9.3; 332 -9.3; 365 -8.3; 402 -8.0; 442 -8.2; 486 -8.4; 535 -8.5; 588 -6.6; 647 -5.5; 712 -5.1; 783 -4.8; 861 -5.5; 947 -6.3; 1042 -6.2; 1146 -4.6; 1261 -4.5; 1387 -5.0; 1526 -4.9; 1678 -4.7; 1846 -3.7; 2031 -3.7; 2234 -2.9; 2457 -2.7; 2703 -2.3; 2973 -2.4; 3270 -2.2; 3597 -1.2; 3957 -0.5; 4353 -0.8; 4788 -1.4; 5267 -1.9; 5793 -3.9; 6373 -4.3; 7010 -4.0; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Alpha Dog 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Alpha Dog 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 266 Hz  | 1.61 | -3.3 dB |
| Peaking | 508 Hz  | 2.98 | -2.1 dB |
| Peaking | 707 Hz  | 3.11 | 1.9 dB  |
| Peaking | 2432 Hz | 0.97 | 2.8 dB  |
| Peaking | 4340 Hz | 1.66 | 4.8 dB  |
| Peaking | 78 Hz   | 1.93 | 1.7 dB  |
| Peaking | 191 Hz  | 6.72 | -1.0 dB |
| Peaking | 1006 Hz | 7.79 | -1.1 dB |
| Peaking | 1201 Hz | 7.4  | 1.3 dB  |
| Peaking | 8789 Hz | 3.77 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Alpha%20Dog%202014/MrSpeakers%20Alpha%20Dog%202014.png)