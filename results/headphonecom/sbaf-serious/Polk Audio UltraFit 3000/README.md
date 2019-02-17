# Polk Audio UltraFit 3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.4; 23 -16.5; 25 -16.6; 28 -16.7; 31 -16.8; 34 -16.9; 37 -16.9; 41 -16.9; 45 -17.0; 49 -17.0; 54 -17.2; 60 -17.3; 66 -17.4; 72 -17.5; 79 -17.5; 87 -17.6; 96 -17.5; 106 -17.4; 116 -17.3; 128 -17.2; 141 -17.0; 155 -16.8; 170 -16.4; 187 -16.1; 206 -15.6; 227 -15.1; 249 -14.5; 274 -13.9; 302 -13.2; 332 -12.5; 365 -11.7; 402 -11.0; 442 -10.4; 486 -9.7; 535 -9.0; 588 -8.3; 647 -7.7; 712 -7.2; 783 -6.7; 861 -6.4; 947 -6.5; 1042 -6.4; 1146 -6.5; 1261 -7.0; 1387 -7.7; 1526 -8.4; 1678 -8.9; 1846 -9.2; 2031 -9.3; 2234 -8.9; 2457 -8.0; 2703 -6.3; 2973 -4.3; 3270 -2.4; 3597 -1.8; 3957 -2.7; 4353 -3.7; 4788 -3.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.22 | -10.2 dB |
| Peaking | 188 Hz  | 0.64 | -5.0 dB  |
| Peaking | 2059 Hz | 2.22 | -3.5 dB  |
| Peaking | 3480 Hz | 2.8  | 4.8 dB   |
| Peaking | 5758 Hz | 2.99 | 6.4 dB   |
| Peaking | 390 Hz  | 1.41 | -0.8 dB  |
| Peaking | 881 Hz  | 1.22 | 1.3 dB   |
| Peaking | 1550 Hz | 4.26 | -1.1 dB  |
| Peaking | 8214 Hz | 4.7  | -1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.2 dB |
| Peaking | 62 Hz    | 1.41 | -7.9 dB  |
| Peaking | 125 Hz   | 1.41 | -8.8 dB  |
| Peaking | 250 Hz   | 1.41 | -6.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%203000/Polk%20Audio%20UltraFit%203000.png)