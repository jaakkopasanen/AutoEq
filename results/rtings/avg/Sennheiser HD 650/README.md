# Sennheiser HD 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.0; 45 -1.5; 49 -1.9; 54 -2.4; 60 -3.0; 66 -3.5; 72 -3.9; 79 -4.4; 87 -5.0; 96 -5.5; 106 -6.0; 116 -6.5; 128 -6.9; 141 -7.3; 155 -7.5; 170 -7.6; 187 -7.6; 206 -7.6; 227 -7.4; 249 -7.3; 274 -7.2; 302 -7.3; 332 -7.2; 365 -7.1; 402 -7.1; 442 -7.1; 486 -7.1; 535 -7.1; 588 -7.0; 647 -6.8; 712 -6.7; 783 -6.6; 861 -6.5; 947 -6.0; 1042 -6.1; 1146 -6.6; 1261 -6.9; 1387 -7.3; 1526 -7.5; 1678 -7.7; 1846 -8.0; 2031 -8.2; 2234 -8.0; 2457 -7.7; 2703 -7.5; 2973 -7.5; 3270 -7.3; 3597 -7.0; 3957 -6.1; 4353 -5.4; 4788 -6.3; 5267 -6.1; 5793 -4.4; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.0; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.43 | 6.3 dB  |
| Peaking | 154 Hz  | 0.78 | -2.0 dB |
| Peaking | 489 Hz  | 3.05 | -0.4 dB |
| Peaking | 2092 Hz | 1.75 | -1.8 dB |
| Peaking | 6410 Hz | 5.04 | 4.7 dB  |
| Peaking | 995 Hz  | 6.18 | 0.9 dB  |
| Peaking | 3948 Hz | 1.34 | -0.5 dB |
| Peaking | 4255 Hz | 6.62 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)