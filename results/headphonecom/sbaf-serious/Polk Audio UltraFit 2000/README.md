# Polk Audio UltraFit 2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -2.3; 66 -3.5; 72 -4.7; 79 -5.8; 87 -6.7; 96 -7.5; 106 -8.0; 116 -8.2; 128 -8.5; 141 -8.7; 155 -8.6; 170 -8.4; 187 -8.0; 206 -7.7; 227 -7.3; 249 -6.9; 274 -6.5; 302 -5.7; 332 -4.8; 365 -4.4; 402 -3.6; 442 -3.1; 486 -2.7; 535 -2.3; 588 -1.7; 647 -1.4; 712 -1.4; 783 -2.1; 861 -3.6; 947 -5.8; 1042 -6.9; 1146 -8.2; 1261 -8.7; 1387 -8.9; 1526 -9.9; 1678 -10.1; 1846 -9.6; 2031 -8.4; 2234 -6.5; 2457 -4.0; 2703 -1.9; 2973 -0.6; 3270 -0.6; 3597 -1.8; 3957 -2.3; 4353 -0.8; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -9.2; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.65 | 7.9 dB   |
| Peaking | 577 Hz   | 0.51 | 17.7 dB  |
| Peaking | 885 Hz   | 0.13 | -12.9 dB |
| Peaking | 2973 Hz  | 1.94 | 10.5 dB  |
| Peaking | 5298 Hz  | 1.28 | 11.8 dB  |
| Peaking | 103 Hz   | 3.89 | -0.8 dB  |
| Peaking | 798 Hz   | 2.97 | 3.2 dB   |
| Peaking | 861 Hz   | 1.09 | -1.6 dB  |
| Peaking | 9186 Hz  | 3.76 | -3.8 dB  |
| Peaking | 10399 Hz | 0.95 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 5.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFit%202000/Polk%20Audio%20UltraFit%202000.png)