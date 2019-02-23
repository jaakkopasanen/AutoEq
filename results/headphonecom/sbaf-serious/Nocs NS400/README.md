# Nocs NS400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.3; 23 -15.2; 25 -15.2; 28 -15.1; 31 -15.0; 34 -15.0; 37 -14.9; 41 -14.8; 45 -14.7; 49 -14.6; 54 -14.6; 60 -14.5; 66 -14.4; 72 -14.4; 79 -14.3; 87 -14.2; 96 -13.9; 106 -13.7; 116 -13.4; 128 -13.2; 141 -12.9; 155 -12.5; 170 -12.1; 187 -11.6; 206 -11.1; 227 -10.4; 249 -9.9; 274 -9.2; 302 -8.5; 332 -7.8; 365 -7.1; 402 -6.4; 442 -5.8; 486 -5.2; 535 -4.6; 588 -3.9; 647 -3.4; 712 -3.0; 783 -2.8; 861 -2.7; 947 -2.9; 1042 -3.3; 1146 -3.6; 1261 -4.1; 1387 -4.7; 1526 -5.3; 1678 -5.8; 1846 -6.3; 2031 -7.0; 2234 -7.8; 2457 -7.9; 2703 -7.2; 2973 -5.3; 3270 -2.3; 3597 -0.5; 3957 -0.5; 4353 -1.9; 4788 -3.1; 5267 -3.7; 5793 -6.1; 6373 -10.1; 7010 -8.5; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.26 | -8.3 dB |
| Peaking | 133 Hz  | 0.57 | -4.3 dB |
| Peaking | 756 Hz  | 1.11 | 4.5 dB  |
| Peaking | 3956 Hz | 2.9  | 6.6 dB  |
| Peaking | 6526 Hz | 7.44 | -4.9 dB |
| Peaking | 413 Hz  | 4.11 | 0.5 dB  |
| Peaking | 1320 Hz | 1.86 | 1.2 dB  |
| Peaking | 2795 Hz | 1.17 | -3.3 dB |
| Peaking | 3310 Hz | 4.04 | 4.2 dB  |
| Peaking | 5198 Hz | 5.21 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS400/Nocs%20NS400.png)