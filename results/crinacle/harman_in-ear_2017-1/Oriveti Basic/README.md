# Oriveti Basic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.5; 25 -13.5; 28 -13.6; 31 -13.6; 34 -13.7; 37 -13.7; 41 -13.7; 45 -13.8; 49 -13.8; 54 -13.8; 60 -13.9; 66 -14.0; 72 -14.1; 79 -14.2; 87 -14.3; 96 -14.5; 106 -14.6; 116 -14.6; 128 -14.6; 141 -14.5; 155 -14.4; 170 -14.2; 187 -14.0; 206 -13.7; 227 -13.3; 249 -12.9; 274 -12.7; 302 -12.3; 332 -11.7; 365 -11.2; 402 -10.8; 442 -10.4; 486 -10.1; 535 -9.6; 588 -9.2; 647 -8.8; 712 -8.3; 783 -7.9; 861 -7.5; 947 -7.4; 1042 -7.4; 1146 -7.5; 1261 -7.3; 1387 -6.5; 1526 -5.4; 1678 -4.1; 1846 -2.6; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.8; 4353 -3.0; 4788 -3.7; 5267 -3.5; 5793 -1.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.4; 15026 -23.6; 16529 -25.7; 18182 -26.8; 20000 -25.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriveti Basic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriveti Basic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.11 | -6.5 dB  |
| Peaking | 276 Hz   | 0.32 | -4.6 dB  |
| Peaking | 1224 Hz  | 2.11 | -3.8 dB  |
| Peaking | 9005 Hz  | 0.18 | 19.0 dB  |
| Peaking | 17324 Hz | 0.25 | -34.2 dB |
| Peaking | 2377 Hz  | 2.55 | 1.5 dB   |
| Peaking | 4715 Hz  | 5.56 | -2.7 dB  |
| Peaking | 8067 Hz  | 4.77 | -2.9 dB  |
| Peaking | 12665 Hz | 2.61 | 7.2 dB   |
| Peaking | 14648 Hz | 2.92 | -6.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 16000 Hz | 1.41 | -24.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Oriveti%20Basic/Oriveti%20Basic.png)