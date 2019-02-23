# KEF M200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.7; 23 -14.6; 25 -14.5; 28 -14.3; 31 -14.1; 34 -14.0; 37 -13.8; 41 -13.6; 45 -13.4; 49 -13.1; 54 -12.9; 60 -12.7; 66 -12.6; 72 -12.4; 79 -12.3; 87 -12.2; 96 -12.0; 106 -11.7; 116 -11.4; 128 -11.2; 141 -10.8; 155 -10.5; 170 -10.1; 187 -9.7; 206 -9.2; 227 -8.7; 249 -8.4; 274 -7.7; 302 -7.2; 332 -6.6; 365 -6.0; 402 -5.6; 442 -4.9; 486 -4.8; 535 -4.2; 588 -3.6; 647 -3.5; 712 -3.6; 783 -3.5; 861 -4.0; 947 -4.4; 1042 -5.1; 1146 -5.7; 1261 -6.6; 1387 -8.0; 1526 -9.6; 1678 -11.0; 1846 -12.0; 2031 -11.7; 2234 -10.2; 2457 -7.2; 2703 -1.6; 2973 -1.5; 3270 -2.9; 3597 -3.3; 3957 -3.6; 4353 -3.9; 4788 -2.7; 5267 -0.7; 5793 -0.5; 6373 -1.6; 7010 -3.9; 7711 -7.2; 8482 -9.8; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.9; 16529 -10.4; 18182 -7.4; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KEF M200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.39 | -8.0 dB |
| Peaking | 121 Hz   | 1.17 | -3.1 dB |
| Peaking | 1997 Hz  | 2.71 | -8.1 dB |
| Peaking | 2908 Hz  | 2.06 | 6.1 dB  |
| Peaking | 5641 Hz  | 3.47 | 6.4 dB  |
| Peaking | 226 Hz   | 1.73 | -1.2 dB |
| Peaking | 690 Hz   | 0.92 | 3.4 dB  |
| Peaking | 1557 Hz  | 3.49 | -2.3 dB |
| Peaking | 8633 Hz  | 6.17 | -4.5 dB |
| Peaking | 16219 Hz | 2.54 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KEF%20M200/KEF%20M200.png)