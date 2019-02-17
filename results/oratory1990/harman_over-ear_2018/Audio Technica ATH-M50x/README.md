# Audio Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.2; 28 -2.5; 31 -3.6; 34 -4.5; 37 -5.2; 41 -5.8; 45 -6.1; 49 -6.1; 54 -5.9; 60 -5.8; 66 -6.3; 72 -6.5; 79 -6.2; 87 -6.8; 96 -7.9; 106 -8.7; 116 -8.8; 128 -9.0; 141 -9.5; 155 -9.7; 170 -9.6; 187 -9.2; 206 -8.4; 227 -7.1; 249 -5.5; 274 -4.1; 302 -3.6; 332 -4.1; 365 -4.5; 402 -5.2; 442 -5.8; 486 -6.2; 535 -6.4; 588 -6.5; 647 -6.5; 712 -6.5; 783 -6.4; 861 -6.4; 947 -6.4; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.2; 1526 -7.1; 1678 -7.2; 1846 -7.6; 2031 -8.2; 2234 -9.0; 2457 -9.9; 2703 -10.1; 2973 -10.1; 3270 -8.9; 3597 -7.1; 3957 -8.6; 4353 -11.5; 4788 -8.9; 5267 -6.3; 5793 -5.3; 6373 -7.8; 7010 -10.7; 7711 -11.5; 8482 -9.5; 9330 -6.6; 10263 -6.5; 11289 -8.9; 12418 -14.0; 13660 -17.5; 15026 -18.5; 16529 -16.4; 18182 -14.8; 20000 -19.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 2.16 | 6.3 dB   |
| Peaking | 2633 Hz  | 2.37 | -3.8 dB  |
| Peaking | 4357 Hz  | 7.84 | -4.4 dB  |
| Peaking | 14606 Hz | 1.62 | -10.0 dB |
| Peaking | 20339 Hz | 0.43 | -11.8 dB |
| Peaking | 165 Hz   | 1.25 | -4.0 dB  |
| Peaking | 297 Hz   | 1.99 | 4.1 dB   |
| Peaking | 5760 Hz  | 4.81 | 3.6 dB   |
| Peaking | 7458 Hz  | 2.5  | -4.8 dB  |
| Peaking | 9917 Hz  | 3.42 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.5 dB   |
| Peaking | 62 Hz    | 1.41 | 0.6 dB   |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | 1.4 dB   |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -15.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M50x/Audio%20Technica%20ATH-M50x.png)