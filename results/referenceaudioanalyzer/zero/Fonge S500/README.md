# Fonge S500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.9; 23 -19.8; 25 -19.7; 28 -19.6; 31 -19.4; 34 -19.3; 37 -19.3; 41 -19.1; 45 -19.0; 49 -18.8; 54 -18.5; 60 -18.2; 66 -17.9; 72 -17.6; 79 -17.3; 87 -16.9; 96 -16.5; 106 -16.0; 116 -15.5; 128 -15.0; 141 -14.3; 155 -13.7; 170 -13.1; 187 -12.4; 206 -12.0; 227 -11.5; 249 -10.9; 274 -10.3; 302 -9.7; 332 -9.0; 365 -8.3; 402 -7.6; 442 -6.9; 486 -6.2; 535 -5.5; 588 -4.8; 647 -4.2; 712 -3.6; 783 -3.2; 861 -2.8; 947 -2.6; 1042 -2.6; 1146 -2.4; 1261 -2.3; 1387 -2.4; 1526 -2.8; 1678 -3.5; 1846 -4.4; 2031 -5.3; 2234 -6.6; 2457 -8.0; 2703 -8.5; 2973 -8.1; 3270 -7.3; 3597 -7.0; 3957 -8.0; 4353 -8.8; 4788 -8.6; 5267 -7.0; 5793 -4.0; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fonge S500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fonge S500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 46 Hz   | 0.21 | -11.9 dB |
| Peaking | 1361 Hz | 0.55 | 7.1 dB   |
| Peaking | 2719 Hz | 0.59 | -6.1 dB  |
| Peaking | 6421 Hz | 4.89 | 7.2 dB   |
| Peaking | 17 Hz   | 0.91 | -4.2 dB  |
| Peaking | 40 Hz   | 0.96 | -0.5 dB  |
| Peaking | 2666 Hz | 2.95 | -2.3 dB  |
| Peaking | 3724 Hz | 1.27 | 3.2 dB   |
| Peaking | 4478 Hz | 2.7  | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.7 dB |
| Peaking | 62 Hz    | 1.41 | -8.7 dB  |
| Peaking | 125 Hz   | 1.41 | -7.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fonge%20S500/Fonge%20S500.png)