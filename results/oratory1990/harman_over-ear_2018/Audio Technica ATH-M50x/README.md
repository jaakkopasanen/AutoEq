# Audio Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.5; 31 -2.6; 34 -3.4; 37 -4.1; 41 -4.7; 45 -5.1; 49 -5.0; 54 -4.8; 60 -4.7; 66 -5.3; 72 -5.4; 79 -5.1; 87 -5.7; 96 -6.8; 106 -7.6; 116 -7.7; 128 -7.9; 141 -8.4; 155 -8.6; 170 -8.6; 187 -8.2; 206 -7.3; 227 -6.0; 249 -4.4; 274 -3.0; 302 -2.5; 332 -3.0; 365 -3.4; 402 -4.1; 442 -4.7; 486 -5.1; 535 -5.4; 588 -5.4; 647 -5.4; 712 -5.4; 783 -5.4; 861 -5.3; 947 -5.3; 1042 -5.5; 1146 -5.8; 1261 -6.1; 1387 -6.1; 1526 -6.0; 1678 -6.1; 1846 -6.5; 2031 -7.1; 2234 -8.0; 2457 -8.8; 2703 -9.0; 2973 -9.0; 3270 -7.8; 3597 -6.0; 3957 -7.6; 4353 -10.4; 4788 -7.8; 5267 -5.2; 5793 -4.2; 6373 -6.8; 7010 -9.6; 7711 -10.5; 8482 -8.5; 9330 -6.5; 10263 -6.5; 11289 -7.8; 12418 -12.9; 13660 -16.5; 15026 -17.4; 16529 -15.3; 18182 -13.7; 20000 -18.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.32 | 6.3 dB   |
| Peaking | 332 Hz   | 2.36 | 4.1 dB   |
| Peaking | 2725 Hz  | 3.22 | -2.8 dB  |
| Peaking | 14662 Hz | 1.72 | -9.6 dB  |
| Peaking | 20145 Hz | 0.51 | -10.5 dB |
| Peaking | 158 Hz   | 2.17 | -2.9 dB  |
| Peaking | 2274 Hz  | 0.28 | 2.0 dB   |
| Peaking | 2805 Hz  | 0.64 | -2.2 dB  |
| Peaking | 7489 Hz  | 5.57 | -4.2 dB  |
| Peaking | 10236 Hz | 4.21 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB   |
| Peaking | 62 Hz    | 1.41 | 1.4 dB   |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | 2.2 dB   |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -14.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M50x/Audio%20Technica%20ATH-M50x.png)