# JBL Free
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.6; 28 -8.6; 31 -8.7; 34 -8.7; 37 -8.7; 41 -8.6; 45 -8.6; 49 -8.6; 54 -8.5; 60 -8.5; 66 -8.5; 72 -8.4; 79 -8.3; 87 -8.2; 96 -8.1; 106 -7.8; 116 -7.5; 128 -7.1; 141 -6.6; 155 -6.1; 170 -5.6; 187 -5.2; 206 -4.9; 227 -4.6; 249 -4.5; 274 -4.3; 302 -4.2; 332 -4.0; 365 -3.9; 402 -3.6; 442 -3.3; 486 -3.0; 535 -2.5; 588 -2.0; 647 -1.4; 712 -0.8; 783 -0.5; 861 -0.7; 947 -1.2; 1042 -1.9; 1146 -2.7; 1261 -3.2; 1387 -3.6; 1526 -3.7; 1678 -3.6; 1846 -3.6; 2031 -3.8; 2234 -3.8; 2457 -3.6; 2703 -3.8; 2973 -3.8; 3270 -3.4; 3597 -2.7; 3957 -2.0; 4353 -1.5; 4788 -1.4; 5267 -1.0; 5793 -0.9; 6373 -2.6; 7010 -6.2; 7711 -4.8; 8482 -3.4; 9330 -3.4; 10263 -3.4; 11289 -6.4; 12418 -7.9; 13660 -5.5; 15026 -5.6; 16529 -9.7; 18182 -10.3; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Free GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Free ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.29 | -5.6 dB |
| Peaking | 783 Hz   | 1.56 | 3.4 dB  |
| Peaking | 4950 Hz  | 1.63 | 4.2 dB  |
| Peaking | 7971 Hz  | 0.2  | -1.7 dB |
| Peaking | 17728 Hz | 1.39 | -7.1 dB |
| Peaking | 6044 Hz  | 8.94 | 1.4 dB  |
| Peaking | 7095 Hz  | 5.68 | -3.7 dB |
| Peaking | 11241 Hz | 1.18 | 4.0 dB  |
| Peaking | 12037 Hz | 3.05 | -6.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -6.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Free/JBL%20Free.png)