# SkullCandy SkullCrushers Max Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.8; 25 -4.1; 28 -7.0; 31 -5.8; 34 -1.9; 37 -0.8; 41 -2.8; 45 -6.3; 49 -8.1; 54 -8.7; 60 -8.7; 66 -11.0; 72 -17.4; 79 -23.7; 87 -27.7; 96 -21.2; 106 -15.4; 116 -11.0; 128 -7.0; 141 -5.2; 155 -0.5; 170 -3.4; 187 -1.7; 206 -1.8; 227 -2.9; 249 -5.5; 274 -6.7; 302 -6.6; 332 -6.5; 365 -7.3; 402 -7.2; 442 -8.0; 486 -8.8; 535 -9.2; 588 -9.0; 647 -9.1; 712 -9.0; 783 -9.0; 861 -9.1; 947 -9.3; 1042 -9.6; 1146 -9.9; 1261 -10.3; 1387 -10.6; 1526 -10.8; 1678 -10.7; 1846 -12.7; 2031 -14.2; 2234 -11.5; 2457 -7.3; 2703 -3.5; 2973 -0.7; 3270 -0.5; 3597 -6.0; 3957 -8.8; 4353 -6.1; 4788 -2.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.1; 9330 -11.8; 10263 -10.0; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SkullCandy SkullCrushers Max Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SkullCandy SkullCrushers Max Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 87 Hz    | 3.51 | -23.8 dB |
| Peaking | 170 Hz   | 1.82 | 7.7 dB   |
| Peaking | 3030 Hz  | 2.96 | 14.7 dB  |
| Peaking | 3415 Hz  | 0.37 | -9.8 dB  |
| Peaking | 5648 Hz  | 1.89 | 14.4 dB  |
| Peaking | 21 Hz    | 0.5  | 4.3 dB   |
| Peaking | 77 Hz    | 6.49 | -5.0 dB  |
| Peaking | 2032 Hz  | 9.26 | -3.4 dB  |
| Peaking | 9374 Hz  | 2.95 | -7.2 dB  |
| Peaking | 10288 Hz | 0.9  | 3.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 8.7 dB   |
| Peaking | 62 Hz    | 1.41 | -12.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB  |
| Peaking | 250 Hz   | 1.41 | 5.2 dB   |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/SkullCandy%20SkullCrushers%20Max%20Bass/SkullCandy%20SkullCrushers%20Max%20Bass.png)