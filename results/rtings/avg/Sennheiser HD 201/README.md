# Sennheiser HD 201
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.0; 41 -1.3; 45 -1.5; 49 -1.6; 54 -1.7; 60 -1.8; 66 -2.0; 72 -2.2; 79 -2.5; 87 -2.8; 96 -3.1; 106 -3.4; 116 -3.6; 128 -3.9; 141 -4.1; 155 -4.2; 170 -4.1; 187 -4.2; 206 -4.1; 227 -4.0; 249 -3.8; 274 -3.8; 302 -5.2; 332 -5.9; 365 -6.5; 402 -7.1; 442 -7.8; 486 -8.3; 535 -8.4; 588 -8.1; 647 -7.8; 712 -7.8; 783 -8.0; 861 -8.2; 947 -8.5; 1042 -8.7; 1146 -8.9; 1261 -8.5; 1387 -8.9; 1526 -9.7; 1678 -7.1; 1846 -9.1; 2031 -10.2; 2234 -10.0; 2457 -8.6; 2703 -7.2; 2973 -7.2; 3270 -8.2; 3597 -8.4; 3957 -6.0; 4353 -0.5; 4788 -0.5; 5267 -6.6; 5793 -3.9; 6373 -4.4; 7010 -7.7; 7711 -10.3; 8482 -10.2; 9330 -8.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 201 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.16 | 5.9 dB  |
| Peaking | 252 Hz  | 2.29 | 2.5 dB  |
| Peaking | 1368 Hz | 0.32 | -2.6 dB |
| Peaking | 4593 Hz | 4.31 | 8.0 dB  |
| Peaking | 8140 Hz | 5.37 | -4.5 dB |
| Peaking | 483 Hz  | 3.41 | -1.1 dB |
| Peaking | 1066 Hz | 0.35 | 0.4 dB  |
| Peaking | 2114 Hz | 6.8  | -2.2 dB |
| Peaking | 5948 Hz | 2.32 | -2.9 dB |
| Peaking | 6049 Hz | 5.42 | 6.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)