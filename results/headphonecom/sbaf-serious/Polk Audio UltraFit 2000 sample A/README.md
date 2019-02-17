# Polk Audio UltraFit 2000 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.2; 60 -2.7; 66 -4.0; 72 -5.1; 79 -6.2; 87 -7.2; 96 -8.0; 106 -8.5; 116 -8.7; 128 -8.9; 141 -9.1; 155 -9.0; 170 -8.8; 187 -8.4; 206 -8.0; 227 -7.6; 249 -7.2; 274 -6.8; 302 -6.1; 332 -5.5; 365 -4.9; 402 -4.1; 442 -4.0; 486 -3.4; 535 -3.0; 588 -2.4; 647 -2.1; 712 -2.2; 783 -3.0; 861 -4.6; 947 -6.3; 1042 -6.4; 1146 -7.4; 1261 -7.7; 1387 -7.4; 1526 -9.1; 1678 -9.2; 1846 -7.9; 2031 -6.0; 2234 -3.8; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.43 | 8.5 dB  |
| Peaking | 108 Hz  | 0.66 | -6.9 dB |
| Peaking | 599 Hz  | 1.15 | 4.7 dB  |
| Peaking | 1619 Hz | 1.29 | -6.9 dB |
| Peaking | 3219 Hz | 0.7  | 8.1 dB  |
| Peaking | 958 Hz  | 9.23 | -1.2 dB |
| Peaking | 2546 Hz | 6.81 | 1.5 dB  |
| Peaking | 3562 Hz | 2.81 | -1.2 dB |
| Peaking | 6241 Hz | 2.1  | 5.5 dB  |
| Peaking | 7446 Hz | 1.45 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 4.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%202000%20sample%20A/Polk%20Audio%20UltraFit%202000%20sample%20A.png)