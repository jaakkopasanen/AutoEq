# Fender Ten 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.7; 25 -7.1; 28 -7.6; 31 -7.9; 34 -8.2; 37 -8.5; 41 -8.7; 45 -8.9; 49 -9.1; 54 -9.2; 60 -9.5; 66 -9.7; 72 -9.8; 79 -10.0; 87 -10.2; 96 -10.3; 106 -10.5; 116 -10.5; 128 -10.5; 141 -10.5; 155 -10.3; 170 -10.1; 187 -9.8; 206 -9.6; 227 -9.2; 249 -8.9; 274 -8.5; 302 -8.0; 332 -7.5; 365 -7.1; 402 -6.7; 442 -6.4; 486 -6.0; 535 -5.7; 588 -5.5; 647 -5.3; 712 -5.2; 783 -5.0; 861 -5.1; 947 -5.6; 1042 -6.5; 1146 -7.8; 1261 -9.0; 1387 -9.7; 1526 -9.7; 1678 -8.7; 1846 -6.9; 2031 -4.8; 2234 -3.1; 2457 -2.5; 2703 -3.1; 2973 -4.3; 3270 -5.1; 3597 -4.6; 3957 -2.7; 4353 -0.8; 4788 -1.7; 5267 -3.0; 5793 -1.2; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.8; 15026 -12.1; 16529 -11.5; 18182 -9.1; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fender Ten 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fender Ten 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 74 Hz    | 0.57 | -3.6 dB |
| Peaking | 173 Hz   | 1.07 | -2.7 dB |
| Peaking | 1456 Hz  | 3.35 | -5.1 dB |
| Peaking | 4768 Hz  | 0.74 | 4.2 dB  |
| Peaking | 16171 Hz | 1.34 | -6.7 dB |
| Peaking | 717 Hz   | 2.49 | 1.3 dB  |
| Peaking | 2411 Hz  | 5.22 | 2.5 dB  |
| Peaking | 3375 Hz  | 5.32 | -2.6 dB |
| Peaking | 6305 Hz  | 5.97 | 3.2 dB  |
| Peaking | 7851 Hz  | 3.26 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -6.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Fender%20Ten%205/Fender%20Ten%205.png)