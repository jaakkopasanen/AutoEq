# Ikko OH-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.4; 25 -6.4; 28 -6.5; 31 -6.6; 34 -6.7; 37 -6.8; 41 -6.8; 45 -6.8; 49 -6.9; 54 -7.0; 60 -7.1; 66 -7.1; 72 -7.2; 79 -7.3; 87 -7.4; 96 -7.4; 106 -7.4; 116 -7.3; 128 -7.2; 141 -7.1; 155 -7.1; 170 -6.9; 187 -6.7; 206 -6.4; 227 -6.1; 249 -5.7; 274 -5.4; 302 -5.0; 332 -4.5; 365 -4.0; 402 -3.7; 442 -3.5; 486 -3.3; 535 -2.9; 588 -2.7; 647 -2.5; 712 -2.2; 783 -2.0; 861 -1.9; 947 -2.0; 1042 -2.4; 1146 -3.0; 1261 -3.4; 1387 -3.7; 1526 -3.8; 1678 -3.9; 1846 -4.0; 2031 -4.1; 2234 -4.3; 2457 -4.1; 2703 -3.5; 2973 -2.7; 3270 -2.3; 3597 -2.6; 3957 -3.7; 4353 -4.8; 4788 -5.0; 5267 -3.9; 5793 -1.5; 6373 -0.5; 7010 -2.2; 7711 -3.5; 8482 -3.7; 9330 -3.8; 10263 -3.8; 11289 -3.8; 12418 -3.9; 13660 -8.8; 15026 -14.7; 16529 -15.4; 18182 -9.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ikko OH-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ikko OH-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.31 | -2.9 dB  |
| Peaking | 153 Hz   | 0.74 | -2.0 dB  |
| Peaking | 737 Hz   | 1.23 | 2.1 dB   |
| Peaking | 6496 Hz  | 4.27 | 3.8 dB   |
| Peaking | 16194 Hz | 1.69 | -13.6 dB |
| Peaking | 2326 Hz  | 1.75 | -1.2 dB  |
| Peaking | 3279 Hz  | 2.25 | 2.1 dB   |
| Peaking | 4545 Hz  | 4.17 | -2.1 dB  |
| Peaking | 12308 Hz | 2.11 | 3.0 dB   |
| Peaking | 14428 Hz | 3.76 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -12.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Ikko%20OH-1/Ikko%20OH-1.png)