# RHA MA450i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.4; 25 -13.3; 28 -13.2; 31 -13.0; 34 -12.9; 37 -12.8; 41 -12.7; 45 -12.5; 49 -12.4; 54 -12.3; 60 -12.2; 66 -12.1; 72 -12.0; 79 -12.0; 87 -11.9; 96 -11.8; 106 -11.6; 116 -11.3; 128 -11.0; 141 -10.8; 155 -10.4; 170 -9.9; 187 -9.6; 206 -9.0; 227 -8.4; 249 -7.9; 274 -7.2; 302 -6.7; 332 -5.9; 365 -5.4; 402 -4.7; 442 -4.0; 486 -3.7; 535 -3.1; 588 -2.5; 647 -2.0; 712 -1.8; 783 -1.6; 861 -1.3; 947 -1.6; 1042 -1.7; 1146 -1.9; 1261 -2.1; 1387 -2.7; 1526 -3.3; 1678 -3.4; 1846 -3.4; 2031 -3.1; 2234 -2.9; 2457 -2.6; 2703 -2.7; 2973 -2.7; 3270 -2.9; 3597 -3.2; 3957 -4.4; 4353 -7.6; 4788 -11.5; 5267 -13.0; 5793 -5.6; 6373 -0.5; 7010 -2.0; 7711 -4.3; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA MA450i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA MA450i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.33 | -8.1 dB  |
| Peaking | 147 Hz  | 0.39 | -6.2 dB  |
| Peaking | 687 Hz  | 0.35 | 3.9 dB   |
| Peaking | 5102 Hz | 4.69 | -10.9 dB |
| Peaking | 6467 Hz | 5.01 | 6.0 dB   |
| Peaking | 811 Hz  | 2.5  | 0.6 dB   |
| Peaking | 1644 Hz | 2.37 | -1.4 dB  |
| Peaking | 3534 Hz | 1.44 | 1.6 dB   |
| Peaking | 4459 Hz | 5.69 | -2.1 dB  |
| Peaking | 8024 Hz | 2.5  | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20MA450i/RHA%20MA450i.png)