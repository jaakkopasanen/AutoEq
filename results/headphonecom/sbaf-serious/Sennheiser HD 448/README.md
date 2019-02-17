# Sennheiser HD 448
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -1.0; 116 -1.9; 128 -2.9; 141 -4.5; 155 -6.6; 170 -6.9; 187 -5.9; 206 -4.2; 227 -2.9; 249 -4.4; 274 -4.6; 302 -3.9; 332 -4.5; 365 -4.5; 402 -4.1; 442 -4.2; 486 -4.0; 535 -4.7; 588 -5.0; 647 -5.3; 712 -6.2; 783 -6.7; 861 -6.4; 947 -5.9; 1042 -6.6; 1146 -6.3; 1261 -7.4; 1387 -7.2; 1526 -7.8; 1678 -8.1; 1846 -8.7; 2031 -9.0; 2234 -7.3; 2457 -5.4; 2703 -5.7; 2973 -5.2; 3270 -4.9; 3597 -5.0; 3957 -3.8; 4353 -0.5; 4788 -0.5; 5267 -3.6; 5793 -3.3; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 448 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 448 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.51 | 6.3 dB  |
| Peaking | 91 Hz    | 1.87 | 3.9 dB  |
| Peaking | 378 Hz   | 1.32 | 2.3 dB  |
| Peaking | 4804 Hz  | 2.06 | 5.7 dB  |
| Peaking | 22050 Hz | 2.34 | 2.2 dB  |
| Peaking | 166 Hz   | 5.39 | -2.8 dB |
| Peaking | 222 Hz   | 6.52 | 2.3 dB  |
| Peaking | 1851 Hz  | 3.1  | -2.8 dB |
| Peaking | 6372 Hz  | 2.33 | -2.8 dB |
| Peaking | 6464 Hz  | 5.68 | 6.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.8 dB  |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20448/Sennheiser%20HD%20448.png)