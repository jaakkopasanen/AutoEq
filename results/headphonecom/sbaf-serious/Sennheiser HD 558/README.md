# Sennheiser HD 558
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.3; 45 -1.9; 49 -2.3; 54 -2.9; 60 -3.4; 66 -3.8; 72 -4.1; 79 -4.5; 87 -3.4; 96 -4.6; 106 -5.9; 116 -6.4; 128 -6.6; 141 -7.0; 155 -7.4; 170 -7.5; 187 -7.6; 206 -7.4; 227 -7.5; 249 -7.6; 274 -7.6; 302 -7.5; 332 -7.2; 365 -7.0; 402 -6.9; 442 -6.7; 486 -6.6; 535 -6.3; 588 -5.7; 647 -5.7; 712 -5.8; 783 -5.2; 861 -5.2; 947 -5.2; 1042 -5.5; 1146 -5.4; 1261 -5.5; 1387 -5.7; 1526 -5.7; 1678 -5.5; 1846 -6.3; 2031 -7.1; 2234 -7.2; 2457 -6.8; 2703 -8.1; 2973 -8.6; 3270 -9.0; 3597 -7.6; 3957 -6.6; 4353 -8.9; 4788 -8.6; 5267 -6.2; 5793 -4.0; 6373 -3.0; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.3; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 558 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 558 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.98 | 5.8 dB  |
| Peaking | 49 Hz   | 1.25 | 2.5 dB  |
| Peaking | 3093 Hz | 4.3  | -2.7 dB |
| Peaking | 4605 Hz | 5.92 | -3.2 dB |
| Peaking | 6219 Hz | 4    | 3.9 dB  |
| Peaking | 88 Hz   | 5.43 | 2.3 dB  |
| Peaking | 207 Hz  | 0.69 | -1.4 dB |
| Peaking | 903 Hz  | 1.06 | 1.5 dB  |
| Peaking | 9170 Hz | 6.83 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20558/Sennheiser%20HD%20558.png)