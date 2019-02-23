# Sennheiser HD 205 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.9; 25 -8.0; 28 -8.0; 31 -8.0; 34 -8.2; 37 -8.5; 41 -8.7; 45 -8.8; 49 -9.0; 54 -9.1; 60 -8.9; 66 -8.6; 72 -9.4; 79 -10.3; 87 -10.7; 96 -11.1; 106 -11.1; 116 -11.2; 128 -10.9; 141 -10.0; 155 -10.2; 170 -10.1; 187 -10.2; 206 -9.9; 227 -10.1; 249 -9.6; 274 -9.5; 302 -8.9; 332 -7.7; 365 -6.3; 402 -5.0; 442 -4.8; 486 -5.8; 535 -7.1; 588 -7.2; 647 -5.5; 712 -3.0; 783 -3.3; 861 -5.2; 947 -6.7; 1042 -7.7; 1146 -8.5; 1261 -8.9; 1387 -9.3; 1526 -9.8; 1678 -9.7; 1846 -9.1; 2031 -8.5; 2234 -7.4; 2457 -5.8; 2703 -3.7; 2973 -3.1; 3270 -2.5; 3597 -1.3; 3957 -0.8; 4353 -0.5; 4788 -2.2; 5267 -4.4; 5793 -1.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.8; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 205 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 205 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 4.24 | 1.4 dB  |
| Peaking | 576 Hz  | 0.58 | 8.8 dB  |
| Peaking | 640 Hz  | 0.1  | -7.4 dB |
| Peaking | 3733 Hz | 1.21 | 10.7 dB |
| Peaking | 6361 Hz | 4.98 | 5.8 dB  |
| Peaking | 420 Hz  | 4.39 | 2.2 dB  |
| Peaking | 583 Hz  | 2.71 | -3.8 dB |
| Peaking | 736 Hz  | 3.26 | 4.4 dB  |
| Peaking | 1472 Hz | 1.23 | -1.1 dB |
| Peaking | 2670 Hz | 5.66 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20205%20II/Sennheiser%20HD%20205%20II.png)