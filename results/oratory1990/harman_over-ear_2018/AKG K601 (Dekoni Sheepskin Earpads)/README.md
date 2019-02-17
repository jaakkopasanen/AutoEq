# AKG K601 (Dekoni Sheepskin Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.6; 25 -2.1; 28 -2.8; 31 -3.4; 34 -3.9; 37 -4.4; 41 -4.9; 45 -5.3; 49 -5.7; 54 -6.1; 60 -6.6; 66 -7.0; 72 -7.4; 79 -7.8; 87 -8.2; 96 -8.6; 106 -9.0; 116 -9.3; 128 -9.7; 141 -10.1; 155 -10.3; 170 -10.5; 187 -10.7; 206 -10.8; 227 -10.8; 249 -10.7; 274 -10.4; 302 -10.0; 332 -9.4; 365 -8.8; 402 -8.4; 442 -7.7; 486 -7.0; 535 -6.4; 588 -5.7; 647 -4.8; 712 -4.3; 783 -4.1; 861 -4.9; 947 -6.1; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.1; 1526 -7.2; 1678 -7.6; 1846 -8.2; 2031 -9.2; 2234 -10.2; 2457 -10.3; 2703 -8.9; 2973 -5.3; 3270 -0.5; 3597 -0.5; 3957 -1.2; 4353 -2.2; 4788 -5.9; 5267 -7.4; 5793 -8.5; 6373 -6.8; 7010 -5.9; 7711 -8.0; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -8.2; 12418 -9.5; 13660 -6.6; 15026 -6.5; 16529 -10.7; 18182 -14.8; 20000 -13.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 (Dekoni Sheepskin Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 (Dekoni Sheepskin Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.08 | 5.5 dB  |
| Peaking | 185 Hz   | 0.87 | -4.7 dB |
| Peaking | 2442 Hz  | 2.41 | -5.7 dB |
| Peaking | 3504 Hz  | 2.83 | 8.4 dB  |
| Peaking | 18878 Hz | 0.95 | -9.2 dB |
| Peaking | 732 Hz   | 3.09 | 3.2 dB  |
| Peaking | 4292 Hz  | 9.34 | 2.2 dB  |
| Peaking | 5547 Hz  | 5.35 | -2.9 dB |
| Peaking | 11985 Hz | 6.4  | -3.1 dB |
| Peaking | 14588 Hz | 3.1  | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K601%20(Dekoni%20Sheepskin%20Earpads)/AKG%20K601%20(Dekoni%20Sheepskin%20Earpads).png)