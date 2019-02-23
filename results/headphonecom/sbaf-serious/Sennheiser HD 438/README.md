# Sennheiser HD 438
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.7; 25 -2.3; 28 -3.2; 31 -3.9; 34 -4.5; 37 -5.0; 41 -5.6; 45 -6.1; 49 -6.4; 54 -6.3; 60 -6.5; 66 -7.4; 72 -7.8; 79 -6.2; 87 -4.6; 96 -6.9; 106 -7.7; 116 -8.1; 128 -8.4; 141 -8.6; 155 -8.3; 170 -8.4; 187 -7.5; 206 -7.2; 227 -6.7; 249 -6.4; 274 -6.7; 302 -6.2; 332 -6.4; 365 -7.1; 402 -7.5; 442 -7.5; 486 -8.0; 535 -8.5; 588 -8.9; 647 -8.8; 712 -8.8; 783 -9.2; 861 -10.1; 947 -11.0; 1042 -10.6; 1146 -10.2; 1261 -10.6; 1387 -11.2; 1526 -10.0; 1678 -9.0; 1846 -7.9; 2031 -6.6; 2234 -5.5; 2457 -2.9; 2703 -3.1; 2973 -3.7; 3270 -3.8; 3597 -4.1; 3957 -1.4; 4353 -0.5; 4788 -0.6; 5267 -3.5; 5793 -3.0; 6373 -4.2; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 438 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 438 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.18 | 6.0 dB  |
| Peaking | 413 Hz  | 0.03 | -0.7 dB |
| Peaking | 1210 Hz | 0.98 | -4.1 dB |
| Peaking | 2523 Hz | 2.9  | 4.4 dB  |
| Peaking | 4486 Hz | 1.78 | 6.6 dB  |
| Peaking | 87 Hz   | 6.98 | 3.5 dB  |
| Peaking | 197 Hz  | 0.58 | -2.9 dB |
| Peaking | 264 Hz  | 1.11 | 3.8 dB  |
| Peaking | 3719 Hz | 8.8  | -2.2 dB |
| Peaking | 3900 Hz | 5.08 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -4.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20438/Sennheiser%20HD%20438.png)