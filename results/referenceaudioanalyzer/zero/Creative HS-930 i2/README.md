# Creative HS-930 i2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.8; 23 -18.0; 25 -18.1; 28 -18.3; 31 -18.4; 34 -18.5; 37 -18.4; 41 -18.3; 45 -18.1; 49 -17.9; 54 -17.6; 60 -17.3; 66 -16.9; 72 -16.5; 79 -16.0; 87 -15.4; 96 -14.8; 106 -14.1; 116 -13.4; 128 -12.6; 141 -12.0; 155 -11.8; 170 -12.0; 187 -12.4; 206 -12.3; 227 -11.8; 249 -11.2; 274 -10.6; 302 -10.0; 332 -9.4; 365 -8.7; 402 -8.0; 442 -7.4; 486 -6.9; 535 -6.4; 588 -5.9; 647 -5.5; 712 -5.2; 783 -5.0; 861 -4.8; 947 -4.7; 1042 -4.7; 1146 -4.5; 1261 -4.4; 1387 -4.9; 1526 -5.6; 1678 -6.4; 1846 -7.4; 2031 -8.5; 2234 -9.5; 2457 -9.9; 2703 -9.5; 2973 -8.0; 3270 -5.7; 3597 -3.3; 3957 -1.1; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.9; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative HS-930 i2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative HS-930 i2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.41 | -8.7 dB |
| Peaking | 119 Hz  | 0.16 | -5.0 dB |
| Peaking | 831 Hz  | 0.54 | 4.3 dB  |
| Peaking | 2471 Hz | 1.77 | -6.0 dB |
| Peaking | 4710 Hz | 1.51 | 7.5 dB  |
| Peaking | 145 Hz  | 3.45 | 1.3 dB  |
| Peaking | 209 Hz  | 2.94 | -1.1 dB |
| Peaking | 4850 Hz | 8.87 | -1.2 dB |
| Peaking | 6266 Hz | 5.77 | 2.6 dB  |
| Peaking | 9507 Hz | 2.53 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.6 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Creative%20HS-930%20i2/Creative%20HS-930%20i2.png)