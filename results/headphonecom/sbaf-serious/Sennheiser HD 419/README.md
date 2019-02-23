# Sennheiser HD 419
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.3; 25 -11.5; 28 -11.7; 31 -11.9; 34 -12.1; 37 -12.2; 41 -12.4; 45 -12.5; 49 -12.5; 54 -12.6; 60 -12.7; 66 -12.7; 72 -12.8; 79 -12.3; 87 -10.1; 96 -10.4; 106 -13.6; 116 -14.4; 128 -14.3; 141 -14.6; 155 -14.7; 170 -14.4; 187 -15.0; 206 -14.8; 227 -14.7; 249 -13.8; 274 -12.6; 302 -11.4; 332 -10.4; 365 -9.0; 402 -7.5; 442 -6.8; 486 -6.8; 535 -7.6; 588 -7.5; 647 -6.5; 712 -5.9; 783 -6.0; 861 -5.3; 947 -5.0; 1042 -4.7; 1146 -5.6; 1261 -5.1; 1387 -6.1; 1526 -6.6; 1678 -6.7; 1846 -7.0; 2031 -6.1; 2234 -4.2; 2457 -3.1; 2703 -3.1; 2973 -2.6; 3270 -2.6; 3597 -2.8; 3957 -1.3; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 419 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 419 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.82 | -4.6 dB  |
| Peaking | 55 Hz   | 1.76 | -2.7 dB  |
| Peaking | 197 Hz  | 0.63 | -10.3 dB |
| Peaking | 428 Hz  | 0.54 | 3.5 dB   |
| Peaking | 4646 Hz | 1.22 | 6.5 dB   |
| Peaking | 1864 Hz | 2.36 | -5.3 dB  |
| Peaking | 2096 Hz | 1.32 | 4.2 dB   |
| Peaking | 6205 Hz | 2.74 | 6.1 dB   |
| Peaking | 6494 Hz | 1.15 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -6.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20419/Sennheiser%20HD%20419.png)