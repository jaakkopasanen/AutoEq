# Polk Audio UltraFit 1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.5; 66 -2.4; 72 -3.3; 79 -4.0; 87 -4.8; 96 -5.4; 106 -6.1; 116 -6.6; 128 -7.2; 141 -7.9; 155 -8.4; 170 -8.8; 187 -9.3; 206 -9.7; 227 -10.0; 249 -10.3; 274 -10.5; 302 -10.6; 332 -10.5; 365 -10.6; 402 -10.4; 442 -10.3; 486 -9.9; 535 -9.9; 588 -10.0; 647 -10.1; 712 -10.1; 783 -10.1; 861 -10.0; 947 -8.9; 1042 -5.2; 1146 -7.0; 1261 -7.7; 1387 -8.5; 1526 -8.9; 1678 -8.1; 1846 -5.9; 2031 -3.3; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 36 Hz   |  0.43 | 6.9 dB  |
| Peaking | 280 Hz  |  0.41 | -4.8 dB |
| Peaking | 786 Hz  |  2.88 | -2.6 dB |
| Peaking | 1571 Hz |  2.92 | -5.9 dB |
| Peaking | 3092 Hz |  0.61 | 7.3 dB  |
| Peaking | 1062 Hz | 12.37 | 2.8 dB  |
| Peaking | 2298 Hz |  5.19 | 1.8 dB  |
| Peaking | 5491 Hz |  0.38 | -1.6 dB |
| Peaking | 6297 Hz |  1.63 | 5.9 dB  |
| Peaking | 7565 Hz |  2.13 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%201000/Polk%20Audio%20UltraFit%201000.png)