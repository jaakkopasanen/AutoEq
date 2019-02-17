# Sennheiser HD 219
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.7; 25 -4.3; 28 -5.1; 31 -5.8; 34 -6.4; 37 -6.9; 41 -7.6; 45 -8.1; 49 -8.5; 54 -9.0; 60 -9.5; 66 -9.8; 72 -10.0; 79 -10.2; 87 -10.2; 96 -10.4; 106 -10.5; 116 -10.2; 128 -9.8; 141 -9.0; 155 -9.0; 170 -8.9; 187 -9.1; 206 -8.4; 227 -7.5; 249 -7.3; 274 -6.5; 302 -5.3; 332 -4.2; 365 -3.8; 402 -3.4; 442 -3.4; 486 -3.7; 535 -4.0; 588 -4.4; 647 -4.3; 712 -3.4; 783 -4.0; 861 -4.6; 947 -5.1; 1042 -5.5; 1146 -5.6; 1261 -5.7; 1387 -5.6; 1526 -5.2; 1678 -6.5; 1846 -6.9; 2031 -6.6; 2234 -6.0; 2457 -5.5; 2703 -5.1; 2973 -5.0; 3270 -4.5; 3597 -3.8; 3957 -5.0; 4353 -7.2; 4788 -6.1; 5267 -3.3; 5793 -1.2; 6373 -0.5; 7010 -2.9; 7711 -6.7; 8482 -10.0; 9330 -10.1; 10263 -5.8; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.9; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 219 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 219 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 85 Hz   | 0.98 | -5.3 dB |
| Peaking | 179 Hz  | 2.81 | -2.4 dB |
| Peaking | 6295 Hz | 3.89 | 6.1 dB  |
| Peaking | 8777 Hz | 3.99 | -6.3 dB |
| Peaking | 20 Hz   | 2.92 | 3.0 dB  |
| Peaking | 418 Hz  | 2.48 | 2.6 dB  |
| Peaking | 726 Hz  | 4.36 | 1.9 dB  |
| Peaking | 1863 Hz | 4.92 | -1.8 dB |
| Peaking | 4485 Hz | 9.57 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20219/Sennheiser%20HD%20219.png)