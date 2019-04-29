# Kennerton Jimo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.6; 25 -12.8; 28 -13.0; 31 -13.1; 34 -13.2; 37 -13.4; 41 -13.6; 45 -13.8; 49 -13.9; 54 -14.1; 60 -14.3; 66 -14.6; 72 -14.8; 79 -15.0; 87 -15.3; 96 -15.6; 106 -15.8; 116 -15.9; 128 -16.0; 141 -16.0; 155 -16.0; 170 -15.9; 187 -15.7; 206 -15.3; 227 -15.0; 249 -14.6; 274 -14.1; 302 -13.5; 332 -12.8; 365 -12.1; 402 -11.4; 442 -10.8; 486 -10.0; 535 -9.1; 588 -8.2; 647 -7.3; 712 -6.3; 783 -5.1; 861 -4.1; 947 -3.1; 1042 -2.2; 1146 -1.7; 1261 -2.3; 1387 -1.8; 1526 -0.9; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.9; 5267 -2.9; 5793 -6.5; 6373 -7.4; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.7; 15026 -21.6; 16529 -27.3; 18182 -25.4; 20000 -24.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kennerton Jimo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kennerton Jimo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.19 | -6.1 dB  |
| Peaking | 183 Hz   | 0.53 | -6.1 dB  |
| Peaking | 459 Hz   | 0.67 | -5.7 dB  |
| Peaking | 3370 Hz  | 0.08 | 7.6 dB   |
| Peaking | 17685 Hz | 0.56 | -26.0 dB |
| Peaking | 666 Hz   | 5.77 | -0.3 dB  |
| Peaking | 4758 Hz  | 2.91 | 2.0 dB   |
| Peaking | 6037 Hz  | 3.85 | -5.4 dB  |
| Peaking | 13165 Hz | 2.28 | 7.9 dB   |
| Peaking | 15521 Hz | 2.85 | -8.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB  |
| Peaking | 62 Hz    | 1.41 | -5.7 dB  |
| Peaking | 125 Hz   | 1.41 | -7.9 dB  |
| Peaking | 250 Hz   | 1.41 | -6.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -22.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kennerton%20Jimo/Kennerton%20Jimo.png)