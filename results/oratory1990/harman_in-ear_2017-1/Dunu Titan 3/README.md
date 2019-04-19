# Dunu Titan 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.1; 25 -1.2; 28 -1.4; 31 -1.5; 34 -1.5; 37 -1.6; 41 -1.7; 45 -1.8; 49 -2.0; 54 -2.3; 60 -2.8; 66 -3.2; 72 -3.5; 79 -4.0; 87 -4.1; 96 -4.1; 106 -4.7; 116 -4.8; 128 -5.4; 141 -5.5; 155 -5.7; 170 -6.0; 187 -6.4; 206 -6.7; 227 -6.9; 249 -7.1; 274 -7.3; 302 -7.5; 332 -7.4; 365 -6.1; 402 -7.3; 442 -7.5; 486 -7.4; 535 -7.3; 588 -7.0; 647 -6.7; 712 -6.0; 783 -5.5; 861 -5.2; 947 -5.1; 1042 -5.3; 1146 -6.0; 1261 -6.7; 1387 -7.1; 1526 -7.2; 1678 -7.1; 1846 -7.0; 2031 -7.1; 2234 -7.3; 2457 -7.7; 2703 -7.6; 2973 -6.4; 3270 -5.0; 3597 -4.2; 3957 -4.6; 4353 -6.2; 4788 -9.8; 5267 -10.2; 5793 -4.2; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -11.4; 15026 -16.2; 16529 -16.3; 18182 -15.4; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Titan 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.93 | 4.5 dB   |
| Peaking | 52 Hz    | 1.29 | 2.6 dB   |
| Peaking | 5161 Hz  | 4.8  | -9.4 dB  |
| Peaking | 6126 Hz  | 2.16 | 7.0 dB   |
| Peaking | 17445 Hz | 0.8  | -11.8 dB |
| Peaking | 271 Hz   | 1.94 | -1.7 dB  |
| Peaking | 490 Hz   | 3.01 | -1.6 dB  |
| Peaking | 2086 Hz  | 1.89 | -1.8 dB  |
| Peaking | 12396 Hz | 2.39 | 4.5 dB   |
| Peaking | 14463 Hz | 2.94 | -5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB   |
| Peaking | 62 Hz    | 1.41 | 2.2 dB   |
| Peaking | 125 Hz   | 1.41 | 0.4 dB   |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -13.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Dunu%20Titan%203/Dunu%20Titan%203.png)