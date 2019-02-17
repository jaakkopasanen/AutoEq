# PNY Uptown
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.0; 23 -17.9; 25 -17.8; 28 -17.7; 31 -17.5; 34 -17.3; 37 -17.2; 41 -17.0; 45 -16.8; 49 -16.6; 54 -16.4; 60 -16.3; 66 -16.1; 72 -15.9; 79 -15.8; 87 -15.7; 96 -15.6; 106 -15.2; 116 -14.9; 128 -14.6; 141 -14.3; 155 -13.9; 170 -13.5; 187 -13.0; 206 -12.5; 227 -11.9; 249 -11.5; 274 -10.9; 302 -10.3; 332 -9.8; 365 -9.2; 402 -8.7; 442 -8.0; 486 -7.7; 535 -7.2; 588 -6.6; 647 -6.3; 712 -6.3; 783 -5.5; 861 -5.7; 947 -6.2; 1042 -6.8; 1146 -7.2; 1261 -7.9; 1387 -8.8; 1526 -9.9; 1678 -11.3; 1846 -12.8; 2031 -13.7; 2234 -13.9; 2457 -11.8; 2703 -8.8; 2973 -4.7; 3270 -1.9; 3597 -0.5; 3957 -0.8; 4353 -3.1; 4788 -5.1; 5267 -6.6; 5793 -11.7; 6373 -14.5; 7010 -8.9; 7711 -6.3; 8482 -6.5; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PNY Uptown GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PNY Uptown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 0.19 | -11.2 dB |
| Peaking | 158 Hz  | 0.78 | -3.6 dB  |
| Peaking | 2163 Hz | 2    | -9.5 dB  |
| Peaking | 3601 Hz | 1.97 | 8.4 dB   |
| Peaking | 6196 Hz | 5.61 | -10.1 dB |
| Peaking | 309 Hz  | 2.41 | -0.7 dB  |
| Peaking | 799 Hz  | 1.71 | 1.8 dB   |
| Peaking | 1599 Hz | 3.68 | -1.1 dB  |
| Peaking | 7689 Hz | 8.23 | 1.2 dB   |
| Peaking | 9348 Hz | 9.34 | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -8.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PNY%20Uptown/PNY%20Uptown.png)