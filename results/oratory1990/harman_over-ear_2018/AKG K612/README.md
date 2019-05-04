# AKG K612
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.8; 41 -1.1; 45 -1.3; 49 -1.2; 54 -0.9; 60 -0.8; 66 -1.5; 72 -2.4; 79 -2.9; 87 -3.6; 96 -4.2; 106 -4.7; 116 -5.2; 128 -5.6; 141 -5.9; 155 -6.2; 170 -6.4; 187 -6.6; 206 -6.7; 227 -6.8; 249 -6.8; 274 -6.7; 302 -6.4; 332 -6.1; 365 -6.0; 402 -5.9; 442 -5.7; 486 -5.5; 535 -5.3; 588 -5.1; 647 -4.7; 712 -4.5; 783 -5.1; 861 -5.7; 947 -5.8; 1042 -5.9; 1146 -5.7; 1261 -5.8; 1387 -6.4; 1526 -7.5; 1678 -8.6; 1846 -9.2; 2031 -9.3; 2234 -9.1; 2457 -9.5; 2703 -9.1; 2973 -8.8; 3270 -7.5; 3597 -7.3; 3957 -6.2; 4353 -5.3; 4788 -6.2; 5267 -7.0; 5793 -8.6; 6373 -8.5; 7010 -8.6; 7711 -8.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.4; 13660 -6.7; 15026 -6.5; 16529 -8.7; 18182 -13.0; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K612 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K612 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.7  | 5.9 dB  |
| Peaking | 61 Hz    | 1.46 | 3.5 dB  |
| Peaking | 2286 Hz  | 2.2  | -3.3 dB |
| Peaking | 6805 Hz  | 3.34 | -2.3 dB |
| Peaking | 18795 Hz | 1.27 | -7.5 dB |
| Peaking | 664 Hz   | 2.06 | 1.9 dB  |
| Peaking | 1317 Hz  | 2.39 | 1.5 dB  |
| Peaking | 1632 Hz  | 2.75 | -1.7 dB |
| Peaking | 4342 Hz  | 6.49 | 1.8 dB  |
| Peaking | 22050 Hz | 3.52 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K612/AKG%20K612.png)