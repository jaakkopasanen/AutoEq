# Final Audio Adagio III
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.5; 23 -16.5; 25 -16.5; 28 -16.4; 31 -16.4; 34 -16.5; 37 -16.5; 41 -16.6; 45 -16.6; 49 -16.7; 54 -16.8; 60 -16.9; 66 -17.1; 72 -17.3; 79 -17.5; 87 -17.7; 96 -18.0; 106 -17.9; 116 -17.9; 128 -18.0; 141 -17.9; 155 -17.7; 170 -17.4; 187 -17.1; 206 -16.7; 227 -16.1; 249 -15.6; 274 -14.9; 302 -14.1; 332 -13.3; 365 -12.4; 402 -11.4; 442 -10.2; 486 -9.2; 535 -8.0; 588 -6.3; 647 -5.2; 712 -4.2; 783 -3.4; 861 -3.9; 947 -5.1; 1042 -6.4; 1146 -6.9; 1261 -6.7; 1387 -6.4; 1526 -6.3; 1678 -6.3; 1846 -6.6; 2031 -7.1; 2234 -8.3; 2457 -9.1; 2703 -8.7; 2973 -5.7; 3270 -2.5; 3597 -0.8; 3957 -1.8; 4353 -4.8; 4788 -7.5; 5267 -7.9; 5793 -3.9; 6373 -0.5; 7010 -3.3; 7711 -5.6; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Adagio III GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Adagio III ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.24 | -10.7 dB |
| Peaking | 191 Hz  | 0.79 | -6.9 dB  |
| Peaking | 3655 Hz | 3.16 | 11.8 dB  |
| Peaking | 3706 Hz | 1.06 | -5.9 dB  |
| Peaking | 6398 Hz | 5.3  | 7.2 dB   |
| Peaking | 16 Hz   | 2.23 | -1.4 dB  |
| Peaking | 363 Hz  | 2.34 | -1.7 dB  |
| Peaking | 754 Hz  | 2.42 | 4.1 dB   |
| Peaking | 2539 Hz | 4.65 | -2.2 dB  |
| Peaking | 3125 Hz | 7.74 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -7.8 dB  |
| Peaking | 125 Hz   | 1.41 | -9.8 dB  |
| Peaking | 250 Hz   | 1.41 | -8.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Adagio%20III/Final%20Audio%20Adagio%20III.png)