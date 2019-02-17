# AKG K271 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -1.4; 87 -1.9; 96 -2.1; 106 -1.9; 116 -1.2; 128 -0.5; 141 -0.5; 155 -0.5; 170 -1.3; 187 -3.1; 206 -4.4; 227 -5.6; 249 -6.3; 274 -6.9; 302 -7.1; 332 -7.2; 365 -7.2; 402 -7.2; 442 -7.3; 486 -7.5; 535 -7.8; 588 -8.6; 647 -10.7; 712 -6.6; 783 -4.6; 861 -5.2; 947 -6.0; 1042 -6.8; 1146 -7.3; 1261 -7.9; 1387 -8.6; 1526 -9.4; 1678 -9.9; 1846 -10.1; 2031 -8.4; 2234 -5.5; 2457 -4.7; 2703 -3.0; 2973 -1.9; 3270 -2.8; 3597 -2.7; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.7; 6373 -6.1; 7010 -9.6; 7711 -10.4; 8482 -9.4; 9330 -6.6; 10263 -6.5; 11289 -7.8; 12418 -11.4; 13660 -8.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K271 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.45 | 6.6 dB  |
| Peaking | 145 Hz   | 2.4  | 4.8 dB  |
| Peaking | 2902 Hz  | 2.03 | 7.4 dB  |
| Peaking | 4234 Hz  | 0.38 | -7.2 dB |
| Peaking | 4714 Hz  | 1.59 | 12.8 dB |
| Peaking | 683 Hz   | 2.2  | -8.8 dB |
| Peaking | 770 Hz   | 2.68 | 10.0 dB |
| Peaking | 7696 Hz  | 3.13 | -4.6 dB |
| Peaking | 11154 Hz | 0.98 | 5.6 dB  |
| Peaking | 12460 Hz | 2.8  | -8.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K271%20MKII/AKG%20K271%20MKII.png)