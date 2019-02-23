# AKG K271 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.1; 72 -1.9; 79 -2.6; 87 -3.1; 96 -3.3; 106 -3.1; 116 -2.4; 128 -1.7; 141 -0.6; 155 -0.8; 170 -2.5; 187 -4.3; 206 -5.6; 227 -6.8; 249 -7.5; 274 -8.1; 302 -8.3; 332 -8.4; 365 -8.4; 402 -8.4; 442 -8.5; 486 -8.7; 535 -9.0; 588 -9.8; 647 -11.9; 712 -7.8; 783 -5.8; 861 -6.4; 947 -7.2; 1042 -7.9; 1146 -8.5; 1261 -9.1; 1387 -9.8; 1526 -10.6; 1678 -11.1; 1846 -11.3; 2031 -9.6; 2234 -6.7; 2457 -5.9; 2703 -4.2; 2973 -3.1; 3270 -4.0; 3597 -3.9; 3957 -1.6; 4353 -0.5; 4788 -0.5; 5267 -1.0; 5793 -4.8; 6373 -7.3; 7010 -10.8; 7711 -11.6; 8482 -10.6; 9330 -7.0; 10263 -6.5; 11289 -8.8; 12418 -12.6; 13660 -9.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K271 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.36 | 6.9 dB  |
| Peaking | 150 Hz   | 2.33 | 5.9 dB  |
| Peaking | 1506 Hz  | 0.05 | -3.0 dB |
| Peaking | 4590 Hz  | 1.18 | 9.8 dB  |
| Peaking | 7314 Hz  | 2.94 | -6.3 dB |
| Peaking | 841 Hz   | 4.6  | 3.5 dB  |
| Peaking | 1763 Hz  | 3.16 | -3.6 dB |
| Peaking | 2697 Hz  | 3.93 | 2.5 dB  |
| Peaking | 10222 Hz | 4.48 | 3.0 dB  |
| Peaking | 12452 Hz | 4.8  | -5.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K271%20MKII/AKG%20K271%20MKII.png)