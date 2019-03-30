# JBL Everest 110
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.0; 25 -4.0; 28 -4.1; 31 -4.1; 34 -4.2; 37 -4.2; 41 -4.2; 45 -4.2; 49 -4.2; 54 -4.4; 60 -4.7; 66 -5.2; 72 -5.5; 79 -5.9; 87 -6.4; 96 -6.9; 106 -7.4; 116 -8.0; 128 -8.5; 141 -8.8; 155 -9.0; 170 -9.1; 187 -9.1; 206 -9.0; 227 -8.8; 249 -8.5; 274 -8.3; 302 -7.9; 332 -7.4; 365 -6.9; 402 -6.3; 442 -5.7; 486 -5.1; 535 -4.3; 588 -3.6; 647 -2.7; 712 -1.9; 783 -1.3; 861 -0.8; 947 -0.6; 1042 -0.7; 1146 -1.3; 1261 -1.8; 1387 -2.2; 1526 -2.4; 1678 -2.4; 1846 -2.4; 2031 -2.2; 2234 -1.4; 2457 -0.5; 2703 -0.6; 2973 -1.8; 3270 -3.5; 3597 -4.6; 3957 -5.2; 4353 -6.0; 4788 -6.3; 5267 -5.5; 5793 -4.3; 6373 -4.4; 7010 -3.1; 7711 -4.4; 8482 -4.6; 9330 -6.0; 10263 -7.3; 11289 -6.9; 12418 -4.9; 13660 -4.7; 15026 -4.7; 16529 -5.5; 18182 -9.6; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest 110 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest 110 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 200 Hz   | 0.69 | -4.8 dB |
| Peaking | 927 Hz   | 1.1  | 4.5 dB  |
| Peaking | 2529 Hz  | 3.29 | 4.1 dB  |
| Peaking | 10543 Hz | 4.34 | -3.0 dB |
| Peaking | 18833 Hz | 1.48 | -5.9 dB |
| Peaking | 46 Hz    | 0.37 | 1.0 dB  |
| Peaking | 113 Hz   | 1.5  | -1.1 dB |
| Peaking | 4584 Hz  | 3.75 | -2.2 dB |
| Peaking | 7059 Hz  | 5.06 | 1.6 dB  |
| Peaking | 17669 Hz | 8.16 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Everest%20110/JBL%20Everest%20110.png)