# Polk Audio UltraFit 2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.4; 54 -2.8; 60 -4.3; 66 -5.6; 72 -6.7; 79 -7.8; 87 -8.8; 96 -9.5; 106 -10.1; 116 -10.3; 128 -10.6; 141 -10.7; 155 -10.6; 170 -10.4; 187 -10.0; 206 -9.7; 227 -9.3; 249 -8.9; 274 -8.6; 302 -7.8; 332 -6.8; 365 -6.4; 402 -5.6; 442 -5.2; 486 -4.8; 535 -4.3; 588 -3.7; 647 -3.4; 712 -3.4; 783 -4.1; 861 -5.7; 947 -7.8; 1042 -9.0; 1146 -10.2; 1261 -10.7; 1387 -10.9; 1526 -12.0; 1678 -12.2; 1846 -11.7; 2031 -10.5; 2234 -8.6; 2457 -6.1; 2703 -4.0; 2973 -2.6; 3270 -2.5; 3597 -3.8; 3957 -4.4; 4353 -2.9; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.1; 9330 -11.3; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.65 | 7.2 dB  |
| Peaking | 121 Hz  | 0.95 | -5.8 dB |
| Peaking | 1665 Hz | 1.98 | -6.7 dB |
| Peaking | 3023 Hz | 2.95 | 4.7 dB  |
| Peaking | 5398 Hz | 2.7  | 6.9 dB  |
| Peaking | 242 Hz  | 1.96 | -1.6 dB |
| Peaking | 723 Hz  | 1.05 | 4.9 dB  |
| Peaking | 1060 Hz | 1.94 | -4.4 dB |
| Peaking | 6524 Hz | 6.45 | 2.4 dB  |
| Peaking | 9208 Hz | 4.35 | -5.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%202000/Polk%20Audio%20UltraFit%202000.png)