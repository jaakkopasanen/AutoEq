# AKG K271 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.2; 45 -1.9; 49 -2.5; 54 -3.2; 60 -3.6; 66 -3.6; 72 -2.9; 79 -1.8; 87 -0.7; 96 -0.7; 106 -3.1; 116 -4.1; 128 -4.5; 141 -5.5; 155 -5.0; 170 -4.8; 187 -5.3; 206 -5.3; 227 -6.0; 249 -6.7; 274 -6.9; 302 -7.1; 332 -7.2; 365 -7.2; 402 -7.4; 442 -7.4; 486 -7.7; 535 -8.1; 588 -8.3; 647 -9.2; 712 -7.0; 783 -5.2; 861 -5.8; 947 -6.0; 1042 -6.7; 1146 -7.0; 1261 -7.5; 1387 -8.2; 1526 -9.2; 1678 -9.7; 1846 -8.9; 2031 -5.9; 2234 -5.9; 2457 -4.4; 2703 -4.3; 2973 -3.6; 3270 -2.8; 3597 -1.7; 3957 -1.9; 4353 -3.7; 4788 -2.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.8; 8482 -12.1; 9330 -14.1; 10263 -11.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K271 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.74 | 6.4 dB  |
| Peaking | 91 Hz   | 2.77 | 4.9 dB  |
| Peaking | 3532 Hz | 3.13 | 4.1 dB  |
| Peaking | 5887 Hz | 2.11 | 6.9 dB  |
| Peaking | 9127 Hz | 3.4  | -9.6 dB |
| Peaking | 176 Hz  | 3.88 | 1.1 dB  |
| Peaking | 682 Hz  | 1.6  | -4.4 dB |
| Peaking | 785 Hz  | 2.73 | 4.8 dB  |
| Peaking | 1710 Hz | 2.59 | -4.7 dB |
| Peaking | 2168 Hz | 2.04 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | 2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K271%20MKII/AKG%20K271%20MKII.png)