# Polk Audio UltraFit 500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.1; 106 -1.7; 116 -2.3; 128 -3.0; 141 -3.5; 155 -4.0; 170 -4.5; 187 -4.9; 206 -5.2; 227 -5.5; 249 -5.8; 274 -5.9; 302 -6.2; 332 -6.2; 365 -6.2; 402 -6.4; 442 -6.6; 486 -6.8; 535 -7.0; 588 -7.1; 647 -7.3; 712 -7.4; 783 -7.4; 861 -7.3; 947 -6.9; 1042 -6.2; 1146 -4.6; 1261 -3.5; 1387 -3.8; 1526 -3.0; 1678 -1.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.26 | 6.7 dB  |
| Peaking | 1211 Hz | 0.1  | -2.2 dB |
| Peaking | 1995 Hz | 1.01 | 6.9 dB  |
| Peaking | 3986 Hz | 1.18 | 5.6 dB  |
| Peaking | 5919 Hz | 2.91 | 4.6 dB  |
| Peaking | 86 Hz   | 5.59 | 0.8 dB  |
| Peaking | 405 Hz  | 3.1  | 0.6 dB  |
| Peaking | 856 Hz  | 4.59 | -0.8 dB |
| Peaking | 7714 Hz | 7.51 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 3.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%20500/Polk%20Audio%20UltraFit%20500.png)