# Sennheiser HD 280 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.1; 25 -7.5; 28 -7.9; 31 -8.3; 34 -8.5; 37 -8.5; 41 -8.3; 45 -8.1; 49 -7.7; 54 -7.2; 60 -6.6; 66 -6.1; 72 -5.6; 79 -5.1; 87 -4.8; 96 -4.6; 106 -4.5; 116 -4.1; 128 -3.5; 141 -2.6; 155 -1.8; 170 -1.7; 187 -2.7; 206 -4.1; 227 -5.5; 249 -6.3; 274 -7.1; 302 -7.6; 332 -8.0; 365 -8.3; 402 -8.8; 442 -8.7; 486 -8.2; 535 -7.9; 588 -7.6; 647 -7.2; 712 -6.8; 783 -6.6; 861 -6.3; 947 -5.7; 1042 -5.5; 1146 -5.7; 1261 -5.7; 1387 -5.6; 1526 -5.5; 1678 -5.6; 1846 -5.7; 2031 -5.9; 2234 -5.2; 2457 -3.4; 2703 -1.6; 2973 -0.5; 3270 -2.3; 3597 -3.4; 3957 -2.3; 4353 -1.3; 4788 -4.4; 5267 -4.0; 5793 -4.4; 6373 -5.2; 7010 -3.5; 7711 -5.1; 8482 -8.4; 9330 -8.3; 10263 -5.4; 11289 -5.5; 12418 -5.6; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 1.16 | -3.6 dB |
| Peaking | 165 Hz  | 1.62 | 4.8 dB  |
| Peaking | 376 Hz  | 0.8  | -3.8 dB |
| Peaking | 2918 Hz | 4.77 | 5.0 dB  |
| Peaking | 4178 Hz | 4.91 | 3.7 dB  |
| Peaking | 86 Hz   | 4.95 | 0.4 dB  |
| Peaking | 992 Hz  | 6.19 | 0.5 dB  |
| Peaking | 2031 Hz | 6.42 | -1.0 dB |
| Peaking | 7119 Hz | 5.37 | 2.0 dB  |
| Peaking | 8807 Hz | 4.7  | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | 3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)