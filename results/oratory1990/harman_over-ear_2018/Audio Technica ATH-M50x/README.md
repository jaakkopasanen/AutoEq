# Audio Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.6; 34 -2.5; 37 -3.3; 41 -3.9; 45 -4.2; 49 -4.3; 54 -4.2; 60 -4.4; 66 -4.7; 72 -4.5; 79 -4.4; 87 -5.3; 96 -6.1; 106 -6.8; 116 -6.9; 128 -7.2; 141 -7.6; 155 -7.7; 170 -7.7; 187 -7.5; 206 -6.9; 227 -5.8; 249 -4.6; 274 -3.5; 302 -3.3; 332 -3.7; 365 -4.0; 402 -4.7; 442 -5.2; 486 -5.6; 535 -5.8; 588 -5.9; 647 -5.8; 712 -5.8; 783 -5.7; 861 -5.7; 947 -5.6; 1042 -5.7; 1146 -5.9; 1261 -6.2; 1387 -6.1; 1526 -5.9; 1678 -6.0; 1846 -6.4; 2031 -6.9; 2234 -7.8; 2457 -8.7; 2703 -8.8; 2973 -8.8; 3270 -7.6; 3597 -6.1; 3957 -7.8; 4353 -10.3; 4788 -7.9; 5267 -5.0; 5793 -2.9; 6373 -5.1; 7010 -9.2; 7711 -11.0; 8482 -9.7; 9330 -6.9; 10263 -6.5; 11289 -8.6; 12418 -14.5; 13660 -17.8; 15026 -17.7; 16529 -14.8; 18182 -12.6; 20000 -16.4
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
| Peaking | 23 Hz    | 0.87 | 6.2 dB   |
| Peaking | 323 Hz   | 2.4  | 3.3 dB   |
| Peaking | 5060 Hz  | 1.27 | -3.3 dB  |
| Peaking | 5726 Hz  | 4.29 | 8.0 dB   |
| Peaking | 15493 Hz | 0.89 | -11.4 dB |
| Peaking | 158 Hz   | 2.69 | -2.0 dB  |
| Peaking | 6519 Hz  | 4.61 | 1.6 dB   |
| Peaking | 7621 Hz  | 3.46 | -3.3 dB  |
| Peaking | 10220 Hz | 3.93 | 4.9 dB   |
| Peaking | 19990 Hz | 2.05 | -8.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.1 dB   |
| Peaking | 62 Hz    | 1.41 | 1.7 dB   |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | 2.0 dB   |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -14.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M50x/Audio%20Technica%20ATH-M50x.png)