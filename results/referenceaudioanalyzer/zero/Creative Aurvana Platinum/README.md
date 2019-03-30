# Creative Aurvana Platinum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -7.2; 25 -7.8; 28 -8.7; 31 -9.6; 34 -10.3; 37 -10.9; 41 -11.6; 45 -12.1; 49 -12.6; 54 -13.2; 60 -13.7; 66 -14.1; 72 -14.4; 79 -14.7; 87 -15.1; 96 -15.4; 106 -15.7; 116 -16.0; 128 -16.1; 141 -16.0; 155 -16.0; 170 -16.0; 187 -15.8; 206 -15.4; 227 -14.6; 249 -13.7; 274 -12.6; 302 -11.2; 332 -10.0; 365 -8.8; 402 -7.3; 442 -5.7; 486 -4.0; 535 -2.3; 588 -0.8; 647 -0.5; 712 -0.5; 783 -0.9; 861 -1.2; 947 -2.0; 1042 -3.1; 1146 -3.7; 1261 -3.8; 1387 -3.3; 1526 -2.0; 1678 -0.6; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -2.6; 3270 -6.2; 3597 -10.1; 3957 -12.7; 4353 -13.1; 4788 -11.7; 5267 -9.5; 5793 -7.0; 6373 -4.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Platinum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Platinum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 64 Hz   | 0.7  | -4.6 dB  |
| Peaking | 177 Hz  | 0.58 | -8.8 dB  |
| Peaking | 622 Hz  | 1.33 | 7.6 dB   |
| Peaking | 2762 Hz | 0.74 | 9.1 dB   |
| Peaking | 4061 Hz | 2.04 | -14.1 dB |
| Peaking | 17 Hz   | 2.36 | 1.5 dB   |
| Peaking | 1267 Hz | 2.77 | -3.5 dB  |
| Peaking | 1323 Hz | 1.33 | 2.1 dB   |
| Peaking | 6360 Hz | 1.39 | -2.3 dB  |
| Peaking | 6644 Hz | 4.02 | 5.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -6.1 dB |
| Peaking | 125 Hz   | 1.41 | -8.2 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB |
| Peaking | 500 Hz   | 1.41 | 5.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Creative%20Aurvana%20Platinum/Creative%20Aurvana%20Platinum.png)