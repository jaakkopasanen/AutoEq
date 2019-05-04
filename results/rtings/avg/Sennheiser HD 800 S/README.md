# Sennheiser HD 800 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.2; 31 -1.4; 34 -1.5; 37 -1.6; 41 -1.7; 45 -1.9; 49 -2.2; 54 -2.5; 60 -2.9; 66 -3.3; 72 -3.7; 79 -4.1; 87 -4.6; 96 -5.1; 106 -5.6; 116 -6.1; 128 -6.5; 141 -6.9; 155 -7.2; 170 -7.4; 187 -7.4; 206 -7.5; 227 -7.5; 249 -7.5; 274 -7.6; 302 -7.6; 332 -7.6; 365 -7.6; 402 -7.6; 442 -7.6; 486 -7.6; 535 -7.6; 588 -7.4; 647 -7.3; 712 -7.0; 783 -6.7; 861 -6.3; 947 -6.2; 1042 -6.0; 1146 -5.6; 1261 -5.4; 1387 -5.2; 1526 -4.9; 1678 -4.9; 1846 -6.2; 2031 -7.1; 2234 -6.6; 2457 -6.0; 2703 -4.9; 2973 -4.7; 3270 -4.5; 3597 -6.5; 3957 -7.0; 4353 -5.5; 4788 -5.6; 5267 -7.0; 5793 -8.6; 6373 -9.0; 7010 -8.6; 7711 -8.9; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -10.0; 13660 -8.0; 15026 -6.5; 16529 -6.5; 18182 -8.0; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.98 | 5.7 dB  |
| Peaking | 54 Hz    | 1.53 | 3.1 dB  |
| Peaking | 3261 Hz  | 0.74 | 1.3 dB  |
| Peaking | 6616 Hz  | 2.12 | -3.1 dB |
| Peaking | 19951 Hz | 1.3  | -6.4 dB |
| Peaking | 337 Hz   | 0.52 | -1.6 dB |
| Peaking | 1589 Hz  | 1.53 | 1.7 dB  |
| Peaking | 2047 Hz  | 3.61 | -2.6 dB |
| Peaking | 2068 Hz  | 0.01 | 0.3 dB  |
| Peaking | 12890 Hz | 5.59 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20800%20S/Sennheiser%20HD%20800%20S.png)