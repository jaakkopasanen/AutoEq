# Sennheiser Game One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.0; 45 -1.5; 49 -1.9; 54 -2.4; 60 -3.0; 66 -3.6; 72 -4.1; 79 -4.6; 87 -5.2; 96 -5.8; 106 -6.3; 116 -6.8; 128 -7.3; 141 -7.6; 155 -7.8; 170 -7.9; 187 -7.9; 206 -7.8; 227 -7.6; 249 -7.6; 274 -7.6; 302 -7.6; 332 -7.6; 365 -7.5; 402 -7.5; 442 -7.6; 486 -7.6; 535 -7.4; 588 -7.3; 647 -7.1; 712 -6.6; 783 -6.4; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -6.4; 1261 -6.7; 1387 -6.8; 1526 -6.4; 1678 -6.7; 1846 -7.0; 2031 -7.8; 2234 -8.1; 2457 -7.6; 2703 -7.2; 2973 -6.9; 3270 -6.4; 3597 -5.6; 3957 -4.0; 4353 -5.1; 4788 -6.6; 5267 -5.0; 5793 -4.9; 6373 -6.4; 7010 -6.9; 7711 -7.0; 8482 -7.8; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.3; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Game One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Game One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.34 | 7.0 dB  |
| Peaking | 123 Hz  | 0.45 | -3.6 dB |
| Peaking | 2254 Hz | 3.39 | -1.6 dB |
| Peaking | 4004 Hz | 7.19 | 2.9 dB  |
| Peaking | 5594 Hz | 7.94 | 1.9 dB  |
| Peaking | 247 Hz  | 4.23 | 0.3 dB  |
| Peaking | 553 Hz  | 1.69 | -0.8 dB |
| Peaking | 770 Hz  | 1.51 | 0.7 dB  |
| Peaking | 8370 Hz | 5.21 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Game%20One/Sennheiser%20Game%20One.png)