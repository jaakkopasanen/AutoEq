# Beats Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.0; 23 -15.6; 25 -16.2; 28 -16.8; 31 -17.3; 34 -17.7; 37 -17.9; 41 -18.0; 45 -18.0; 49 -17.8; 54 -17.7; 60 -17.7; 66 -17.8; 72 -17.8; 79 -17.7; 87 -17.6; 96 -17.3; 106 -17.0; 116 -16.6; 128 -16.1; 141 -15.6; 155 -14.9; 170 -13.9; 187 -12.7; 206 -11.4; 227 -9.8; 249 -8.1; 274 -5.9; 302 -3.0; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -1.3; 712 -3.3; 783 -4.3; 861 -4.3; 947 -3.9; 1042 -3.6; 1146 -3.4; 1261 -3.1; 1387 -3.0; 1526 -3.3; 1678 -4.0; 1846 -5.3; 2031 -6.9; 2234 -8.7; 2457 -10.7; 2703 -12.4; 2973 -12.8; 3270 -11.5; 3597 -8.7; 3957 -6.2; 4353 -6.2; 4788 -6.2; 5267 -4.1; 5793 -1.7; 6373 -1.9; 7010 -4.0; 7711 -6.9; 8482 -11.3; 9330 -13.9; 10263 -14.0; 11289 -12.9; 12418 -11.5; 13660 -9.8; 15026 -7.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 113 Hz   | 0.09 | -20.6 dB |
| Peaking | 244 Hz   | 0.17 | -17.5 dB |
| Peaking | 380 Hz   | 0.18 | 41.7 dB  |
| Peaking | 2888 Hz  | 1.36 | -15.4 dB |
| Peaking | 10273 Hz | 1.31 | -13.4 dB |
| Peaking | 613 Hz   | 5.13 | 2.2 dB   |
| Peaking | 803 Hz   | 3.79 | -1.7 dB  |
| Peaking | 4855 Hz  | 4.44 | -3.4 dB  |
| Peaking | 6105 Hz  | 2.35 | 3.4 dB   |
| Peaking | 8621 Hz  | 5.36 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -8.4 dB  |
| Peaking | 125 Hz   | 1.41 | -9.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB   |
| Peaking | 500 Hz   | 1.41 | 7.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -2.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beats%20Pro/Beats%20Pro.png)