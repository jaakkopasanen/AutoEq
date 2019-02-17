# Sennheiser RS 165
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.4; 25 -8.3; 28 -8.3; 31 -8.1; 34 -7.8; 37 -7.5; 41 -7.0; 45 -6.6; 49 -6.2; 54 -5.8; 60 -5.6; 66 -6.0; 72 -6.4; 79 -6.9; 87 -7.7; 96 -8.5; 106 -9.2; 116 -9.6; 128 -9.7; 141 -9.6; 155 -9.2; 170 -8.7; 187 -7.9; 206 -6.8; 227 -5.6; 249 -4.6; 274 -4.5; 302 -4.8; 332 -4.5; 365 -3.5; 402 -2.3; 442 -1.8; 486 -2.2; 535 -2.8; 588 -3.4; 647 -3.8; 712 -3.6; 783 -4.5; 861 -5.3; 947 -6.2; 1042 -6.5; 1146 -6.2; 1261 -6.5; 1387 -6.4; 1526 -5.9; 1678 -4.9; 1846 -4.8; 2031 -4.5; 2234 -3.9; 2457 -3.4; 2703 -3.2; 2973 -2.5; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -4.4; 5793 -4.3; 6373 -6.3; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 2.2  | -2.2 dB |
| Peaking | 136 Hz  | 1.57 | -3.7 dB |
| Peaking | 249 Hz  | 4.67 | 1.7 dB  |
| Peaking | 465 Hz  | 1.41 | 4.7 dB  |
| Peaking | 3766 Hz | 1.48 | 6.4 dB  |
| Peaking | 58 Hz   | 3.64 | 1.5 dB  |
| Peaking | 739 Hz  | 4.47 | 1.5 dB  |
| Peaking | 1472 Hz | 0.77 | -1.2 dB |
| Peaking | 1721 Hz | 3.35 | 1.6 dB  |
| Peaking | 2350 Hz | 4.02 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20165/Sennheiser%20RS%20165.png)