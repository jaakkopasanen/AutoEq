# Polk Audio UltraFit 2000 sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.7; 60 -3.2; 66 -4.5; 72 -5.7; 79 -6.8; 87 -7.7; 96 -8.4; 106 -9.0; 116 -9.3; 128 -9.6; 141 -9.7; 155 -9.6; 170 -9.5; 187 -9.1; 206 -8.8; 227 -8.4; 249 -8.0; 274 -7.7; 302 -6.8; 332 -5.6; 365 -5.3; 402 -4.5; 442 -3.7; 486 -3.5; 535 -3.1; 588 -2.5; 647 -2.1; 712 -2.1; 783 -2.6; 861 -4.1; 947 -6.7; 1042 -8.9; 1146 -10.4; 1261 -11.2; 1387 -11.8; 1526 -12.2; 1678 -12.5; 1846 -12.9; 2031 -12.3; 2234 -10.8; 2457 -8.2; 2703 -5.9; 2973 -4.2; 3270 -3.9; 3597 -4.7; 3957 -5.6; 4353 -4.1; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.4; 8482 -11.7; 9330 -14.0; 10263 -10.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 1.36 | 7.4 dB   |
| Peaking | 686 Hz  | 1.69 | 6.7 dB   |
| Peaking | 1603 Hz | 1.03 | -8.1 dB  |
| Peaking | 6288 Hz | 0.72 | 8.5 dB   |
| Peaking | 9038 Hz | 2.29 | -13.5 dB |
| Peaking | 53 Hz   | 2.22 | 3.9 dB   |
| Peaking | 140 Hz  | 0.69 | -3.7 dB  |
| Peaking | 413 Hz  | 2.12 | 2.1 dB   |
| Peaking | 3027 Hz | 5.05 | 2.5 dB   |
| Peaking | 4010 Hz | 6.83 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 5.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -7.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%202000%20sample%20B/Polk%20Audio%20UltraFit%202000%20sample%20B.png)