# Astell & Kern T8iE Mk1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.3; 25 -12.4; 28 -12.5; 31 -12.6; 34 -12.6; 37 -12.7; 41 -12.7; 45 -12.8; 49 -12.9; 54 -13.0; 60 -13.1; 66 -13.3; 72 -13.5; 79 -13.7; 87 -13.9; 96 -14.1; 106 -14.2; 116 -14.4; 128 -14.4; 141 -14.4; 155 -14.3; 170 -14.1; 187 -13.9; 206 -13.5; 227 -13.1; 249 -12.7; 274 -12.2; 302 -11.6; 332 -10.9; 365 -10.3; 402 -9.7; 442 -9.1; 486 -8.4; 535 -7.8; 588 -7.1; 647 -6.5; 712 -5.8; 783 -5.2; 861 -4.7; 947 -4.6; 1042 -4.8; 1146 -5.2; 1261 -5.6; 1387 -5.7; 1526 -5.3; 1678 -4.8; 1846 -4.2; 2031 -3.2; 2234 -2.0; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -2.5; 4788 -4.8; 5267 -2.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.8; 15026 -13.0; 16529 -17.6; 18182 -16.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astell & Kern T8iE Mk1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astell & Kern T8iE Mk1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.25 | -5.7 dB  |
| Peaking | 143 Hz   | 0.78 | -4.7 dB  |
| Peaking | 279 Hz   | 1.32 | -2.7 dB  |
| Peaking | 3452 Hz  | 0.62 | 5.9 dB   |
| Peaking | 17273 Hz | 1.31 | -13.0 dB |
| Peaking | 845 Hz   | 4.16 | 1.7 dB   |
| Peaking | 4865 Hz  | 4.74 | -5.6 dB  |
| Peaking | 6079 Hz  | 1.8  | 5.3 dB   |
| Peaking | 7604 Hz  | 2.29 | -4.0 dB  |
| Peaking | 12905 Hz | 4.65 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -10.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Astell%20&%20Kern%20T8iE%20Mk1/Astell%20&%20Kern%20T8iE%20Mk1.png)