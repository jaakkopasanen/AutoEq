# RHA MA450i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.7; 23 -14.7; 25 -14.6; 28 -14.5; 31 -14.4; 34 -14.2; 37 -14.1; 41 -14.0; 45 -13.8; 49 -13.7; 54 -13.6; 60 -13.5; 66 -13.4; 72 -13.3; 79 -13.3; 87 -13.2; 96 -13.1; 106 -12.9; 116 -12.6; 128 -12.3; 141 -12.1; 155 -11.7; 170 -11.2; 187 -10.9; 206 -10.3; 227 -9.8; 249 -9.2; 274 -8.5; 302 -8.0; 332 -7.2; 365 -6.7; 402 -6.1; 442 -5.3; 486 -5.1; 535 -4.4; 588 -3.8; 647 -3.3; 712 -3.1; 783 -2.9; 861 -2.6; 947 -2.9; 1042 -3.0; 1146 -3.3; 1261 -3.5; 1387 -4.0; 1526 -4.6; 1678 -4.7; 1846 -4.7; 2031 -4.4; 2234 -4.2; 2457 -3.9; 2703 -4.0; 2973 -4.0; 3270 -4.2; 3597 -4.5; 3957 -5.7; 4353 -9.0; 4788 -12.8; 5267 -14.3; 5793 -6.9; 6373 -1.8; 7010 -0.5; 7711 -2.6; 8482 -2.9; 9330 -2.9; 10263 -2.9; 11289 -2.9; 12418 -2.9; 13660 -2.9; 15026 -5.0; 16529 -3.0; 18182 -2.9; 20000 -2.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA MA450i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA MA450i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.16 | -11.4 dB |
| Peaking | 172 Hz   | 0.68 | -4.1 dB  |
| Peaking | 1769 Hz  | 3.14 | -1.7 dB  |
| Peaking | 5097 Hz  | 3.36 | -13.3 dB |
| Peaking | 6602 Hz  | 3.77 | 5.8 dB   |
| Peaking | 91 Hz    | 4.07 | -0.4 dB  |
| Peaking | 333 Hz   | 2.21 | -0.6 dB  |
| Peaking | 778 Hz   | 2.03 | 1.1 dB   |
| Peaking | 14913 Hz | 4.4  | -2.3 dB  |
| Peaking | 15969 Hz | 1.25 | 0.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.1 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB  |
| Peaking | 125 Hz   | 1.41 | -7.7 dB  |
| Peaking | 250 Hz   | 1.41 | -5.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20MA450i/RHA%20MA450i.png)