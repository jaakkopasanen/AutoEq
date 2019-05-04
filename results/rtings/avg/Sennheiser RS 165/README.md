# Sennheiser RS 165
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.0; 25 -10.0; 28 -9.9; 31 -9.8; 34 -9.5; 37 -9.2; 41 -8.8; 45 -8.3; 49 -7.9; 54 -7.5; 60 -7.4; 66 -7.6; 72 -8.1; 79 -8.7; 87 -9.4; 96 -10.3; 106 -10.8; 116 -11.2; 128 -11.3; 141 -11.2; 155 -11.0; 170 -10.5; 187 -9.7; 206 -8.6; 227 -7.4; 249 -6.4; 274 -6.3; 302 -6.6; 332 -6.3; 365 -5.3; 402 -4.1; 442 -3.7; 486 -4.2; 535 -4.7; 588 -5.4; 647 -5.8; 712 -5.8; 783 -6.5; 861 -7.2; 947 -8.2; 1042 -8.5; 1146 -8.3; 1261 -8.7; 1387 -8.5; 1526 -8.0; 1678 -7.1; 1846 -7.0; 2031 -6.9; 2234 -6.6; 2457 -6.3; 2703 -5.7; 2973 -4.4; 3270 -3.0; 3597 -1.9; 3957 -1.1; 4353 -0.5; 4788 -1.8; 5267 -6.9; 5793 -6.0; 6373 -7.2; 7010 -7.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.9; 12418 -7.4; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 165 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 165 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.23 | -3.7 dB |
| Peaking | 132 Hz   | 1.22 | -5.2 dB |
| Peaking | 461 Hz   | 1.49 | 3.1 dB  |
| Peaking | 1188 Hz  | 1.5  | -2.5 dB |
| Peaking | 4022 Hz  | 2.75 | 6.5 dB  |
| Peaking | 181 Hz   | 6.84 | -0.5 dB |
| Peaking | 3261 Hz  | 4.86 | 1.7 dB  |
| Peaking | 4630 Hz  | 6.83 | 5.6 dB  |
| Peaking | 4800 Hz  | 2.13 | -3.4 dB |
| Peaking | 11665 Hz | 6.58 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20165/Sennheiser%20RS%20165.png)