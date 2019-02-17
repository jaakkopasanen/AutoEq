# AKG K240 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.0; 28 -2.9; 31 -3.6; 34 -4.3; 37 -5.0; 41 -5.7; 45 -6.1; 49 -6.5; 54 -7.2; 60 -7.1; 66 -7.4; 72 -8.9; 79 -10.0; 87 -10.9; 96 -11.6; 106 -12.1; 116 -12.5; 128 -12.7; 141 -12.9; 155 -12.6; 170 -12.3; 187 -12.1; 206 -11.8; 227 -11.3; 249 -10.9; 274 -10.8; 302 -10.6; 332 -10.4; 365 -10.0; 402 -9.7; 442 -9.6; 486 -9.5; 535 -6.1; 588 -7.2; 647 -7.3; 712 -7.1; 783 -6.9; 861 -6.6; 947 -6.3; 1042 -6.0; 1146 -5.7; 1261 -5.7; 1387 -6.4; 1526 -7.2; 1678 -7.9; 1846 -9.1; 2031 -9.3; 2234 -10.1; 2457 -9.6; 2703 -7.7; 2973 -6.9; 3270 -5.0; 3597 -4.2; 3957 -5.7; 4353 -6.7; 4788 -7.0; 5267 -4.6; 5793 -4.5; 6373 -6.5; 7010 -8.6; 7711 -11.4; 8482 -15.1; 9330 -15.7; 10263 -11.7; 11289 -7.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 15 Hz   | 0.15 | 6.6 dB   |
| Peaking | 119 Hz  | 0.37 | -8.9 dB  |
| Peaking | 2169 Hz | 1.79 | -6.1 dB  |
| Peaking | 4169 Hz | 0.21 | 2.6 dB   |
| Peaking | 8948 Hz | 2.37 | -12.6 dB |
| Peaking | 64 Hz   | 6.53 | 1.5 dB   |
| Peaking | 2909 Hz | 4.2  | -0.7 dB  |
| Peaking | 3499 Hz | 3.16 | 2.6 dB   |
| Peaking | 4642 Hz | 2.09 | -3.3 dB  |
| Peaking | 5512 Hz | 4.59 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K240%20MKII/AKG%20K240%20MKII.png)