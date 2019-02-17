# Polk Audio UltraFit 3000 sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.1; 23 -17.2; 25 -17.3; 28 -17.4; 31 -17.5; 34 -17.5; 37 -17.5; 41 -17.6; 45 -17.6; 49 -17.7; 54 -17.7; 60 -17.8; 66 -17.8; 72 -17.9; 79 -17.9; 87 -17.8; 96 -17.7; 106 -17.5; 116 -17.3; 128 -17.1; 141 -16.9; 155 -16.6; 170 -16.1; 187 -15.7; 206 -15.2; 227 -14.6; 249 -14.0; 274 -13.4; 302 -12.6; 332 -11.9; 365 -11.1; 402 -10.3; 442 -9.7; 486 -9.1; 535 -8.3; 588 -7.8; 647 -7.1; 712 -6.7; 783 -6.3; 861 -5.8; 947 -6.2; 1042 -6.5; 1146 -6.7; 1261 -7.3; 1387 -8.0; 1526 -9.0; 1678 -9.7; 1846 -10.2; 2031 -10.7; 2234 -10.8; 2457 -10.2; 2703 -8.9; 2973 -7.3; 3270 -5.7; 3597 -5.2; 3957 -5.2; 4353 -3.4; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 3000 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 3000 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.38 | -8.1 dB |
| Peaking | 117 Hz  | 0.31 | -9.8 dB |
| Peaking | 770 Hz  | 0.86 | 2.7 dB  |
| Peaking | 2055 Hz | 1.53 | -5.0 dB |
| Peaking | 5339 Hz | 2.03 | 7.1 dB  |
| Peaking | 2552 Hz | 5.63 | -0.6 dB |
| Peaking | 3295 Hz | 5.66 | 1.2 dB  |
| Peaking | 6523 Hz | 5.25 | 3.2 dB  |
| Peaking | 7278 Hz | 1.78 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.1 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB  |
| Peaking | 125 Hz   | 1.41 | -8.7 dB  |
| Peaking | 250 Hz   | 1.41 | -6.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%203000%20sample%20B/Polk%20Audio%20UltraFit%203000%20sample%20B.png)