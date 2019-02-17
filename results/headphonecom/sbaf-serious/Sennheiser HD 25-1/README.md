# Sennheiser HD 25-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -1.8; 28 -2.4; 31 -2.5; 34 -2.6; 37 -3.3; 41 -4.6; 45 -5.1; 49 -4.8; 54 -4.0; 60 -3.5; 66 -3.8; 72 -5.3; 79 -6.8; 87 -7.1; 96 -8.7; 106 -8.5; 116 -7.8; 128 -8.1; 141 -8.4; 155 -6.8; 170 -6.7; 187 -7.4; 206 -8.6; 227 -8.3; 249 -7.5; 274 -7.2; 302 -6.5; 332 -6.0; 365 -5.7; 402 -5.4; 442 -5.4; 486 -5.6; 535 -5.6; 588 -5.7; 647 -5.9; 712 -6.2; 783 -6.4; 861 -6.5; 947 -6.8; 1042 -7.0; 1146 -7.2; 1261 -7.7; 1387 -8.5; 1526 -9.5; 1678 -10.1; 1846 -10.6; 2031 -10.8; 2234 -10.1; 2457 -8.5; 2703 -6.5; 2973 -4.8; 3270 -4.4; 3597 -4.1; 3957 -5.0; 4353 -4.3; 4788 -2.4; 5267 -0.9; 5793 -1.0; 6373 -1.5; 7010 -4.4; 7711 -6.6; 8482 -11.1; 9330 -13.5; 10263 -10.1; 11289 -8.6; 12418 -8.4; 13660 -6.9; 15026 -6.9; 16529 -6.9; 18182 -6.9; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.24 | 6.1 dB   |
| Peaking | 62 Hz   | 5.18 | 3.2 dB   |
| Peaking | 1936 Hz | 2.28 | -5.1 dB  |
| Peaking | 6173 Hz | 0.97 | 7.7 dB   |
| Peaking | 9063 Hz | 2.15 | -10.5 dB |
| Peaking | 104 Hz  | 2.64 | -2.1 dB  |
| Peaking | 221 Hz  | 3.79 | -2.0 dB  |
| Peaking | 457 Hz  | 1.16 | 1.6 dB   |
| Peaking | 3165 Hz | 3.07 | 3.8 dB   |
| Peaking | 3221 Hz | 1.59 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%2025-1/Sennheiser%20HD%2025-1.png)