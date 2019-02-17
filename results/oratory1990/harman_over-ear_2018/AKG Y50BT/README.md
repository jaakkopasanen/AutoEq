# AKG Y50BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.6; 31 -2.3; 34 -2.9; 37 -3.3; 41 -3.8; 45 -4.2; 49 -4.4; 54 -4.6; 60 -4.9; 66 -5.1; 72 -5.3; 79 -5.4; 87 -5.6; 96 -5.8; 106 -5.8; 116 -5.6; 128 -5.1; 141 -4.1; 155 -2.8; 170 -1.2; 187 -0.6; 206 -1.6; 227 -3.3; 249 -4.5; 274 -5.6; 302 -6.8; 332 -7.7; 365 -7.7; 402 -7.2; 442 -6.7; 486 -6.5; 535 -6.5; 588 -6.6; 647 -6.9; 712 -7.3; 783 -7.8; 861 -8.3; 947 -8.1; 1042 -6.9; 1146 -8.6; 1261 -9.5; 1387 -9.5; 1526 -9.3; 1678 -8.5; 1846 -7.1; 2031 -5.9; 2234 -4.5; 2457 -2.5; 2703 -1.3; 2973 -2.9; 3270 -6.7; 3597 -5.1; 3957 -4.2; 4353 -5.8; 4788 -7.2; 5267 -8.6; 5793 -8.9; 6373 -7.8; 7010 -5.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -9.7; 15026 -11.3; 16529 -11.7; 18182 -10.9; 20000 -9.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Y50BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Y50BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.73 | 6.0 dB  |
| Peaking | 185 Hz   | 2.82 | 6.3 dB  |
| Peaking | 1413 Hz  | 1.21 | -3.2 dB |
| Peaking | 2610 Hz  | 2.87 | 6.1 dB  |
| Peaking | 17191 Hz | 0.86 | -5.7 dB |
| Peaking | 239 Hz   | 4.27 | 0.7 dB  |
| Peaking | 343 Hz   | 3.95 | -1.8 dB |
| Peaking | 3929 Hz  | 9.85 | 2.5 dB  |
| Peaking | 5613 Hz  | 3.61 | -3.2 dB |
| Peaking | 8423 Hz  | 1.08 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20Y50BT/AKG%20Y50BT.png)