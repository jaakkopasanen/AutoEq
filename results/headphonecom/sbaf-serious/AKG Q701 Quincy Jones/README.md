# AKG Q701 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.9; 41 -1.6; 45 -2.1; 49 -2.7; 54 -3.4; 60 -4.1; 66 -4.5; 72 -4.7; 79 -4.5; 87 -5.5; 96 -6.5; 106 -6.8; 116 -6.3; 128 -7.2; 141 -7.7; 155 -8.0; 170 -7.9; 187 -8.3; 206 -8.3; 227 -8.3; 249 -8.3; 274 -8.1; 302 -7.9; 332 -7.5; 365 -7.3; 402 -7.2; 442 -6.7; 486 -6.5; 535 -6.1; 588 -4.9; 647 -5.2; 712 -5.0; 783 -4.8; 861 -4.8; 947 -4.4; 1042 -4.0; 1146 -3.8; 1261 -4.2; 1387 -5.2; 1526 -6.7; 1678 -7.3; 1846 -9.0; 2031 -9.7; 2234 -8.2; 2457 -6.9; 2703 -5.1; 2973 -3.8; 3270 -2.6; 3597 -2.1; 3957 -3.6; 4353 -5.5; 4788 -5.3; 5267 -6.8; 5793 -10.0; 6373 -10.7; 7010 -8.6; 7711 -8.8; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 29 Hz   |  1.01 | 6.8 dB  |
| Peaking | 1100 Hz |  1.65 | 3.1 dB  |
| Peaking | 2006 Hz |  2.46 | -4.5 dB |
| Peaking | 3440 Hz |  1.92 | 4.9 dB  |
| Peaking | 6231 Hz |  3.17 | -5.0 dB |
| Peaking | 69 Hz   |  1.29 | 1.1 dB  |
| Peaking | 201 Hz  |  0.71 | -2.1 dB |
| Peaking | 615 Hz  |  3.06 | 1.4 dB  |
| Peaking | 5041 Hz | 14.77 | 1.5 dB  |
| Peaking | 7896 Hz | 10.44 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20Q701%20Quincy%20Jones/AKG%20Q701%20Quincy%20Jones.png)