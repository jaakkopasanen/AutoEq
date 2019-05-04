# Tin Audio T2 (Foam Eartips)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.9; 31 -2.3; 34 -2.7; 37 -3.1; 41 -3.5; 45 -3.8; 49 -4.2; 54 -4.6; 60 -5.0; 66 -5.4; 72 -5.9; 79 -6.3; 87 -6.8; 96 -7.4; 106 -7.8; 116 -8.3; 128 -8.7; 141 -9.0; 155 -9.3; 170 -9.6; 187 -9.7; 206 -9.9; 227 -9.9; 249 -10.0; 274 -10.0; 302 -9.9; 332 -9.7; 365 -9.5; 402 -9.4; 442 -9.2; 486 -9.0; 535 -8.7; 588 -8.4; 647 -8.1; 712 -7.7; 783 -7.3; 861 -7.2; 947 -7.5; 1042 -7.0; 1146 -7.0; 1261 -6.7; 1387 -6.2; 1526 -5.5; 1678 -4.8; 1846 -4.0; 2031 -3.4; 2234 -2.9; 2457 -3.0; 2703 -3.2; 2973 -2.6; 3270 -1.6; 3597 -1.2; 3957 -1.6; 4353 -2.8; 4788 -4.8; 5267 -5.5; 5793 -3.2; 6373 -1.4; 7010 -4.2; 7711 -6.5; 8482 -9.3; 9330 -10.1; 10263 -12.2; 11289 -14.7; 12418 -17.0; 13660 -21.2; 15026 -22.7; 16529 -19.9; 18182 -17.6; 20000 -15.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 (Foam Eartips) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 (Foam Eartips) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 1.25 | 6.1 dB   |
| Peaking | 2182 Hz  | 2.61 | 3.4 dB   |
| Peaking | 3573 Hz  | 2.32 | 5.8 dB   |
| Peaking | 6689 Hz  | 1.69 | 7.8 dB   |
| Peaking | 15700 Hz | 0.47 | -15.5 dB |
| Peaking | 54 Hz    | 1.25 | 1.7 dB   |
| Peaking | 241 Hz   | 0.53 | -3.5 dB  |
| Peaking | 10167 Hz | 4.04 | 1.5 dB   |
| Peaking | 14074 Hz | 5.82 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB   |
| Peaking | 62 Hz    | 1.41 | 0.9 dB   |
| Peaking | 125 Hz   | 1.41 | -1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -23.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Tin%20Audio%20T2%20(Foam%20Eartips)/Tin%20Audio%20T2%20(Foam%20Eartips).png)