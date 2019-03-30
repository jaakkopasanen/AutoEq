# Westone Adv Alpha
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.4; 23 -19.2; 25 -19.1; 28 -18.9; 31 -18.7; 34 -18.5; 37 -18.3; 41 -18.0; 45 -17.8; 49 -17.5; 54 -17.3; 60 -16.9; 66 -16.5; 72 -16.2; 79 -15.8; 87 -15.3; 96 -14.9; 106 -14.4; 116 -13.9; 128 -13.3; 141 -12.8; 155 -12.2; 170 -11.6; 187 -11.1; 206 -10.5; 227 -9.8; 249 -9.2; 274 -8.7; 302 -8.1; 332 -7.5; 365 -6.9; 402 -6.3; 442 -5.8; 486 -5.4; 535 -4.9; 588 -4.4; 647 -4.0; 712 -3.6; 783 -3.2; 861 -2.9; 947 -2.7; 1042 -2.4; 1146 -2.4; 1261 -2.1; 1387 -2.1; 1526 -2.0; 1678 -1.8; 1846 -1.7; 2031 -1.8; 2234 -1.8; 2457 -1.7; 2703 -1.5; 2973 -1.3; 3270 -1.1; 3597 -1.5; 3957 -3.9; 4353 -7.9; 4788 -9.9; 5267 -9.2; 5793 -5.8; 6373 -0.5; 7010 -2.0; 7711 -4.2; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone Adv Alpha GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone Adv Alpha ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 43 Hz   | 0.22 | -12.1 dB |
| Peaking | 2108 Hz | 0.37 | 3.5 dB   |
| Peaking | 4935 Hz | 3.26 | -8.6 dB  |
| Peaking | 6519 Hz | 8.04 | 5.2 dB   |
| Peaking | 18 Hz   | 0.9  | -4.6 dB  |
| Peaking | 36 Hz   | 0.19 | -0.1 dB  |
| Peaking | 3221 Hz | 1.04 | -1.2 dB  |
| Peaking | 3382 Hz | 3.15 | 2.9 dB   |
| Peaking | 9554 Hz | 2.18 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -15.5 dB |
| Peaking | 62 Hz    | 1.41 | -8.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Westone%20Adv%20Alpha/Westone%20Adv%20Alpha.png)