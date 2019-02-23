# Final Audio Adagio III
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.9; 23 -14.9; 25 -14.9; 28 -14.8; 31 -14.8; 34 -14.9; 37 -14.9; 41 -15.0; 45 -15.0; 49 -15.1; 54 -15.2; 60 -15.3; 66 -15.5; 72 -15.7; 79 -15.9; 87 -16.1; 96 -16.3; 106 -16.3; 116 -16.3; 128 -16.4; 141 -16.3; 155 -16.1; 170 -15.8; 187 -15.5; 206 -15.1; 227 -14.5; 249 -14.0; 274 -13.3; 302 -12.5; 332 -11.7; 365 -10.8; 402 -9.8; 442 -8.6; 486 -7.6; 535 -6.4; 588 -4.7; 647 -3.6; 712 -2.6; 783 -1.8; 861 -2.3; 947 -3.5; 1042 -4.8; 1146 -5.3; 1261 -5.0; 1387 -4.8; 1526 -4.7; 1678 -4.7; 1846 -5.0; 2031 -5.5; 2234 -6.7; 2457 -7.5; 2703 -7.1; 2973 -4.1; 3270 -0.9; 3597 -0.5; 3957 -0.6; 4353 -3.2; 4788 -5.9; 5267 -6.3; 5793 -2.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Adagio III GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Adagio III ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.26 | -7.5 dB |
| Peaking | 148 Hz   | 0.37 | -9.1 dB |
| Peaking | 736 Hz   | 1.25 | 6.7 dB  |
| Peaking | 3719 Hz  | 2.81 | 6.5 dB  |
| Peaking | 21348 Hz | 2.48 | 2.3 dB  |
| Peaking | 1104 Hz  | 7.25 | -0.7 dB |
| Peaking | 1599 Hz  | 3.36 | 1.7 dB  |
| Peaking | 3794 Hz  | 0.35 | -0.7 dB |
| Peaking | 5134 Hz  | 6.4  | -2.7 dB |
| Peaking | 6177 Hz  | 4.15 | 6.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB |
| Peaking | 125 Hz   | 1.41 | -8.2 dB |
| Peaking | 250 Hz   | 1.41 | -7.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Adagio%20III/Final%20Audio%20Adagio%20III.png)