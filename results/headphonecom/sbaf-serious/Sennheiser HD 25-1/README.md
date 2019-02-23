# Sennheiser HD 25-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.4; 25 -1.9; 28 -2.4; 31 -2.6; 34 -2.7; 37 -3.4; 41 -4.7; 45 -5.2; 49 -4.9; 54 -4.1; 60 -3.6; 66 -3.9; 72 -5.4; 79 -6.9; 87 -7.2; 96 -8.7; 106 -8.6; 116 -7.8; 128 -8.2; 141 -8.5; 155 -6.9; 170 -6.7; 187 -7.5; 206 -8.6; 227 -8.4; 249 -7.6; 274 -7.3; 302 -6.6; 332 -6.1; 365 -5.8; 402 -5.5; 442 -5.5; 486 -5.7; 535 -5.7; 588 -5.8; 647 -6.0; 712 -6.2; 783 -6.4; 861 -6.6; 947 -6.8; 1042 -7.1; 1146 -7.3; 1261 -7.7; 1387 -8.6; 1526 -9.5; 1678 -10.2; 1846 -10.7; 2031 -10.9; 2234 -10.1; 2457 -8.6; 2703 -6.6; 2973 -4.9; 3270 -4.4; 3597 -4.2; 3957 -5.1; 4353 -4.4; 4788 -2.5; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -11.2; 9330 -13.6; 10263 -10.2; 11289 -8.6; 12418 -8.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 1.96 | 5.2 dB   |
| Peaking | 35 Hz   | 1.73 | 2.7 dB   |
| Peaking | 1904 Hz | 2.02 | -5.3 dB  |
| Peaking | 6120 Hz | 1.18 | 7.7 dB   |
| Peaking | 9094 Hz | 2.24 | -10.3 dB |
| Peaking | 63 Hz   | 3.75 | 3.1 dB   |
| Peaking | 102 Hz  | 1.59 | -2.5 dB  |
| Peaking | 221 Hz  | 3.76 | -2.2 dB  |
| Peaking | 445 Hz  | 1.68 | 1.2 dB   |
| Peaking | 3072 Hz | 6.5  | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%2025-1/Sennheiser%20HD%2025-1.png)