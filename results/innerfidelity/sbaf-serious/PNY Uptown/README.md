# PNY Uptown
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -15.4; 25 -15.3; 28 -15.1; 31 -15.0; 34 -14.8; 37 -14.7; 41 -14.5; 45 -14.3; 49 -14.1; 54 -13.9; 60 -13.7; 66 -13.5; 72 -13.4; 79 -13.3; 87 -13.2; 96 -13.0; 106 -12.7; 116 -12.4; 128 -12.1; 141 -11.8; 155 -11.4; 170 -11.0; 187 -10.5; 206 -10.0; 227 -9.4; 249 -8.9; 274 -8.3; 302 -7.8; 332 -7.3; 365 -6.7; 402 -6.1; 442 -5.5; 486 -5.2; 535 -4.7; 588 -4.1; 647 -3.8; 712 -3.8; 783 -2.9; 861 -3.1; 947 -3.7; 1042 -4.2; 1146 -4.7; 1261 -5.4; 1387 -6.3; 1526 -7.4; 1678 -8.8; 1846 -10.3; 2031 -11.2; 2234 -11.3; 2457 -9.3; 2703 -6.2; 2973 -2.2; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -2.6; 5267 -4.1; 5793 -9.2; 6373 -12.0; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PNY Uptown GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PNY Uptown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.2  | -8.8 dB  |
| Peaking | 141 Hz   | 0.86 | -2.8 dB  |
| Peaking | 2071 Hz  | 1.49 | -17.4 dB |
| Peaking | 2516 Hz  | 0.45 | 12.0 dB  |
| Peaking | 6244 Hz  | 4.08 | -10.5 dB |
| Peaking | 741 Hz   | 1.5  | 1.3 dB   |
| Peaking | 1520 Hz  | 1.41 | -3.6 dB  |
| Peaking | 2281 Hz  | 1.01 | 4.8 dB   |
| Peaking | 2522 Hz  | 3.6  | -5.8 dB  |
| Peaking | 10075 Hz | 1.36 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PNY%20Uptown/PNY%20Uptown.png)