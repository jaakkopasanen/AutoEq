# Polk Audio UltraFit 2000 sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.8; 66 -3.1; 72 -4.3; 79 -5.3; 87 -6.3; 96 -6.9; 106 -7.5; 116 -7.8; 128 -8.1; 141 -8.2; 155 -8.1; 170 -8.0; 187 -7.6; 206 -7.3; 227 -7.0; 249 -6.6; 274 -6.2; 302 -5.4; 332 -4.1; 365 -3.9; 402 -3.1; 442 -2.2; 486 -2.0; 535 -1.6; 588 -1.0; 647 -0.7; 712 -0.6; 783 -1.2; 861 -2.7; 947 -5.3; 1042 -7.4; 1146 -9.0; 1261 -9.7; 1387 -10.3; 1526 -10.8; 1678 -11.1; 1846 -11.4; 2031 -10.8; 2234 -9.3; 2457 -6.7; 2703 -4.5; 2973 -2.8; 3270 -2.4; 3597 -3.2; 3957 -4.2; 4353 -2.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.2; 9330 -12.5; 10263 -9.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 1.05 | 7.3 dB   |
| Peaking | 663 Hz  | 1.3  | 7.6 dB   |
| Peaking | 1630 Hz | 1.04 | -8.0 dB  |
| Peaking | 5240 Hz | 0.56 | 7.2 dB   |
| Peaking | 9117 Hz | 2.53 | -10.5 dB |
| Peaking | 58 Hz   | 2.2  | 3.6 dB   |
| Peaking | 126 Hz  | 0.47 | -2.5 dB  |
| Peaking | 372 Hz  | 1.88 | 2.1 dB   |
| Peaking | 2983 Hz | 5.18 | 2.3 dB   |
| Peaking | 3915 Hz | 7    | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 6.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%202000%20sample%20B/Polk%20Audio%20UltraFit%202000%20sample%20B.png)