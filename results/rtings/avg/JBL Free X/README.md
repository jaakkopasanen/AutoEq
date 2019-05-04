# JBL Free X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.3; 25 -9.3; 28 -9.3; 31 -9.2; 34 -9.2; 37 -9.1; 41 -9.0; 45 -8.9; 49 -8.8; 54 -8.7; 60 -8.5; 66 -8.4; 72 -8.3; 79 -8.1; 87 -7.9; 96 -7.7; 106 -7.3; 116 -6.9; 128 -6.5; 141 -5.9; 155 -5.3; 170 -4.8; 187 -4.3; 206 -4.0; 227 -3.7; 249 -3.5; 274 -3.3; 302 -3.2; 332 -3.0; 365 -2.9; 402 -2.7; 442 -2.4; 486 -2.0; 535 -1.5; 588 -1.1; 647 -0.7; 712 -0.5; 783 -0.5; 861 -0.6; 947 -1.1; 1042 -1.9; 1146 -2.8; 1261 -3.3; 1387 -3.6; 1526 -3.7; 1678 -4.0; 1846 -4.4; 2031 -4.9; 2234 -5.1; 2457 -5.2; 2703 -5.6; 2973 -5.7; 3270 -4.8; 3597 -3.5; 3957 -2.5; 4353 -1.9; 4788 -1.6; 5267 -1.0; 5793 -0.7; 6373 -1.8; 7010 -5.8; 7711 -6.5; 8482 -3.7; 9330 -3.4; 10263 -4.0; 11289 -8.5; 12418 -10.4; 13660 -7.4; 15026 -6.3; 16529 -10.0; 18182 -11.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Free X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Free X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.34 | -6.1 dB |
| Peaking | 681 Hz   | 1.5  | 3.3 dB  |
| Peaking | 5454 Hz  | 4.5  | 3.3 dB  |
| Peaking | 12161 Hz | 3.57 | -6.5 dB |
| Peaking | 17912 Hz | 1.14 | -8.5 dB |
| Peaking | 929 Hz   | 4.6  | 1.1 dB  |
| Peaking | 3067 Hz  | 1.16 | -4.3 dB |
| Peaking | 3940 Hz  | 1.48 | 3.6 dB  |
| Peaking | 7438 Hz  | 6.9  | -3.9 dB |
| Peaking | 9561 Hz  | 4.25 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -8.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Free%20X/JBL%20Free%20X.png)