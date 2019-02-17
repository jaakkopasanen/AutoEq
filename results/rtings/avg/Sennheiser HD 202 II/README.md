# Sennheiser HD 202 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.6; 25 -3.2; 28 -4.0; 31 -4.7; 34 -5.3; 37 -5.8; 41 -6.4; 45 -7.0; 49 -7.5; 54 -8.2; 60 -8.8; 66 -9.3; 72 -9.5; 79 -9.6; 87 -9.8; 96 -9.9; 106 -9.8; 116 -9.4; 128 -8.9; 141 -8.3; 155 -7.8; 170 -7.0; 187 -6.1; 206 -5.1; 227 -4.0; 249 -2.9; 274 -1.9; 302 -1.7; 332 -2.7; 365 -2.8; 402 -2.9; 442 -3.3; 486 -4.0; 535 -4.7; 588 -5.3; 647 -5.6; 712 -5.7; 783 -5.9; 861 -6.1; 947 -6.4; 1042 -6.6; 1146 -7.1; 1261 -7.4; 1387 -8.1; 1526 -8.3; 1678 -8.1; 1846 -7.6; 2031 -6.5; 2234 -5.4; 2457 -4.4; 2703 -3.0; 2973 -1.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.6; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.3; 13660 -11.1; 15026 -8.2; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 3.14 | 4.6 dB  |
| Peaking | 343 Hz   | 1.57 | 4.9 dB  |
| Peaking | 3343 Hz  | 1.53 | 7.4 dB  |
| Peaking | 5552 Hz  | 0.26 | -4.3 dB |
| Peaking | 5774 Hz  | 1.17 | 8.3 dB  |
| Peaking | 67 Hz    | 2.41 | -1.8 dB |
| Peaking | 106 Hz   | 1.28 | -3.4 dB |
| Peaking | 250 Hz   | 3.49 | 2.0 dB  |
| Peaking | 11331 Hz | 3.22 | 2.5 dB  |
| Peaking | 13298 Hz | 4    | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | 4.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20202%20II/Sennheiser%20HD%20202%20II.png)