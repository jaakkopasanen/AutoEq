# JBL Everest 710
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.7; 28 -3.6; 31 -3.5; 34 -3.3; 37 -3.1; 41 -2.8; 45 -2.6; 49 -2.5; 54 -2.4; 60 -2.5; 66 -2.7; 72 -3.1; 79 -3.6; 87 -4.2; 96 -4.6; 106 -4.7; 116 -4.7; 128 -4.6; 141 -4.2; 155 -3.5; 170 -2.7; 187 -2.7; 206 -2.3; 227 -1.8; 249 -1.7; 274 -1.9; 302 -2.2; 332 -2.5; 365 -2.3; 402 -2.8; 442 -4.6; 486 -5.5; 535 -5.6; 588 -5.7; 647 -5.8; 712 -6.2; 783 -6.6; 861 -6.9; 947 -7.0; 1042 -6.7; 1146 -7.0; 1261 -7.4; 1387 -7.9; 1526 -8.2; 1678 -8.2; 1846 -7.6; 2031 -6.1; 2234 -4.9; 2457 -4.2; 2703 -3.3; 2973 -3.7; 3270 -4.0; 3597 -3.4; 3957 -3.1; 4353 -1.3; 4788 -0.5; 5267 -2.0; 5793 -5.6; 6373 -6.6; 7010 -6.5; 7711 -7.1; 8482 -8.0; 9330 -8.3; 10263 -8.9; 11289 -10.1; 12418 -10.2; 13660 -8.3; 15026 -7.0; 16529 -5.6; 18182 -4.8; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest 710 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest 710 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 1.33 | 2.5 dB  |
| Peaking | 263 Hz   | 1.37 | 3.5 dB  |
| Peaking | 1228 Hz  | 0.93 | -3.1 dB |
| Peaking | 4555 Hz  | 2.17 | 5.1 dB  |
| Peaking | 11143 Hz | 0.86 | -5.2 dB |
| Peaking | 21 Hz    | 1.59 | 0.9 dB  |
| Peaking | 504 Hz   | 6.3  | -1.0 dB |
| Peaking | 1719 Hz  | 4.88 | -1.6 dB |
| Peaking | 2600 Hz  | 3.61 | 2.0 dB  |
| Peaking | 6077 Hz  | 7.96 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Everest%20710/JBL%20Everest%20710.png)