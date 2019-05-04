# Sennheiser HD 598 Cs
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.5; 25 -3.7; 28 -3.9; 31 -4.0; 34 -4.1; 37 -4.1; 41 -4.1; 45 -4.1; 49 -4.2; 54 -4.4; 60 -4.8; 66 -5.1; 72 -5.3; 79 -5.6; 87 -6.0; 96 -6.5; 106 -6.9; 116 -7.3; 128 -7.5; 141 -7.6; 155 -7.6; 170 -7.4; 187 -6.9; 206 -6.1; 227 -5.2; 249 -4.6; 274 -4.0; 302 -4.0; 332 -4.5; 365 -5.3; 402 -6.3; 442 -7.4; 486 -8.2; 535 -8.3; 588 -8.2; 647 -8.2; 712 -8.3; 783 -8.3; 861 -8.1; 947 -8.0; 1042 -7.9; 1146 -7.8; 1261 -7.7; 1387 -7.8; 1526 -7.9; 1678 -8.0; 1846 -8.3; 2031 -8.4; 2234 -8.0; 2457 -6.8; 2703 -5.5; 2973 -5.5; 3270 -7.0; 3597 -7.9; 3957 -5.9; 4353 -4.9; 4788 -3.6; 5267 -1.2; 5793 -0.5; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -8.7; 18182 -11.9; 20000 -16.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 Cs GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 Cs ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.46 | 3.6 dB  |
| Peaking | 294 Hz   | 1.58 | 5.3 dB  |
| Peaking | 298 Hz   | 0.19 | -2.8 dB |
| Peaking | 5702 Hz  | 3.11 | 6.8 dB  |
| Peaking | 19696 Hz | 0.95 | -9.4 dB |
| Peaking | 2144 Hz  | 2.25 | -3.8 dB |
| Peaking | 2631 Hz  | 1.23 | 3.5 dB  |
| Peaking | 3515 Hz  | 4.88 | -3.4 dB |
| Peaking | 8570 Hz  | 5.8  | -2.4 dB |
| Peaking | 14327 Hz | 2.42 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20598%20Cs/Sennheiser%20HD%20598%20Cs.png)