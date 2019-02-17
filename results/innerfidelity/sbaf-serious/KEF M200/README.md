# KEF M200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.1; 23 -15.1; 25 -15.0; 28 -14.7; 31 -14.5; 34 -14.4; 37 -14.3; 41 -14.1; 45 -13.8; 49 -13.6; 54 -13.4; 60 -13.2; 66 -13.0; 72 -12.9; 79 -12.7; 87 -12.6; 96 -12.5; 106 -12.1; 116 -11.9; 128 -11.6; 141 -11.3; 155 -10.9; 170 -10.6; 187 -10.1; 206 -9.7; 227 -9.1; 249 -8.8; 274 -8.1; 302 -7.7; 332 -7.1; 365 -6.5; 402 -6.0; 442 -5.3; 486 -5.2; 535 -4.6; 588 -4.1; 647 -3.9; 712 -4.0; 783 -4.0; 861 -4.4; 947 -4.9; 1042 -5.5; 1146 -6.1; 1261 -7.0; 1387 -8.5; 1526 -10.1; 1678 -11.4; 1846 -12.4; 2031 -12.1; 2234 -10.7; 2457 -7.6; 2703 -2.0; 2973 -1.9; 3270 -3.4; 3597 -3.7; 3957 -4.1; 4353 -4.4; 4788 -3.1; 5267 -1.2; 5793 -0.5; 6373 -2.1; 7010 -4.3; 7711 -7.6; 8482 -10.3; 9330 -8.7; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -9.4; 16529 -10.8; 18182 -7.9; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KEF M200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.19 | -9.6 dB  |
| Peaking | 158 Hz   | 0.64 | -3.3 dB  |
| Peaking | 1865 Hz  | 1.16 | -17.9 dB |
| Peaking | 2370 Hz  | 0.39 | 11.4 dB  |
| Peaking | 15520 Hz | 0.14 | -3.6 dB  |
| Peaking | 2846 Hz  | 5.1  | 4.2 dB   |
| Peaking | 4790 Hz  | 0.89 | -3.9 dB  |
| Peaking | 5782 Hz  | 2.24 | 6.8 dB   |
| Peaking | 8523 Hz  | 3.7  | -5.6 dB  |
| Peaking | 11663 Hz | 1.85 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -4.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KEF%20M200/KEF%20M200.png)