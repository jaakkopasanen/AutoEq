# JBL Everest 110
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.6; 28 -8.7; 31 -8.7; 34 -8.7; 37 -8.8; 41 -8.8; 45 -8.9; 49 -8.9; 54 -9.0; 60 -9.0; 66 -9.2; 72 -9.3; 79 -9.5; 87 -9.7; 96 -9.8; 106 -9.9; 116 -10.0; 128 -10.0; 141 -9.9; 155 -9.8; 170 -9.5; 187 -9.2; 206 -8.9; 227 -8.5; 249 -8.2; 274 -8.0; 302 -7.7; 332 -7.2; 365 -6.6; 402 -6.1; 442 -5.5; 486 -4.9; 535 -4.1; 588 -3.4; 647 -2.6; 712 -1.9; 783 -1.2; 861 -0.7; 947 -0.5; 1042 -0.7; 1146 -1.3; 1261 -1.8; 1387 -2.2; 1526 -2.4; 1678 -2.4; 1846 -2.5; 2031 -2.4; 2234 -2.0; 2457 -1.2; 2703 -0.9; 2973 -1.6; 3270 -3.0; 3597 -4.1; 3957 -4.7; 4353 -5.4; 4788 -6.4; 5267 -5.7; 5793 -3.9; 6373 -3.3; 7010 -2.9; 7711 -4.4; 8482 -4.7; 9330 -4.7; 10263 -6.5; 11289 -7.7; 12418 -5.0; 13660 -4.7; 15026 -4.7; 16529 -5.4; 18182 -9.0; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest 110 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest 110 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.64 | -2.6 dB |
| Peaking | 133 Hz   | 0.38 | -5.1 dB |
| Peaking | 909 Hz   | 0.97 | 4.8 dB  |
| Peaking | 2621 Hz  | 3.17 | 3.5 dB  |
| Peaking | 12 Hz    | 1    | -0.8 dB |
| Peaking | 4966 Hz  | 3.19 | -3.4 dB |
| Peaking | 6080 Hz  | 1.83 | 2.3 dB  |
| Peaking | 11003 Hz | 4.78 | -3.4 dB |
| Peaking | 18485 Hz | 1.88 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Everest%20110/JBL%20Everest%20110.png)