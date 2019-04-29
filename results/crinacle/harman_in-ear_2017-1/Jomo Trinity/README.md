# Jomo Trinity
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.8; 25 -7.0; 28 -7.2; 31 -7.3; 34 -7.4; 37 -7.5; 41 -7.5; 45 -7.6; 49 -7.6; 54 -7.7; 60 -7.8; 66 -7.8; 72 -7.9; 79 -8.0; 87 -8.1; 96 -8.2; 106 -8.3; 116 -8.2; 128 -8.1; 141 -8.0; 155 -7.8; 170 -7.5; 187 -7.2; 206 -6.8; 227 -6.4; 249 -6.0; 274 -5.5; 302 -5.0; 332 -4.4; 365 -3.9; 402 -3.5; 442 -3.1; 486 -2.7; 535 -2.3; 588 -2.0; 647 -1.8; 712 -1.6; 783 -1.5; 861 -1.7; 947 -2.1; 1042 -3.0; 1146 -4.3; 1261 -5.5; 1387 -6.5; 1526 -6.9; 1678 -7.0; 1846 -6.6; 2031 -6.4; 2234 -6.0; 2457 -4.7; 2703 -3.7; 2973 -3.2; 3270 -3.5; 3597 -4.5; 3957 -6.0; 4353 -6.7; 4788 -5.3; 5267 -2.9; 5793 -1.3; 6373 -0.5; 7010 -2.1; 7711 -4.2; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.6; 13660 -9.2; 15026 -13.9; 16529 -18.6; 18182 -21.1; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Trinity GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Trinity ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.39 | -2.9 dB  |
| Peaking | 139 Hz   | 0.93 | -2.4 dB  |
| Peaking | 640 Hz   | 1.59 | 3.5 dB   |
| Peaking | 11523 Hz | 0.61 | 7.7 dB   |
| Peaking | 17555 Hz | 0.53 | -19.4 dB |
| Peaking | 943 Hz   | 2.94 | 2.2 dB   |
| Peaking | 1709 Hz  | 1.21 | -4.2 dB  |
| Peaking | 4432 Hz  | 2.18 | -9.5 dB  |
| Peaking | 5288 Hz  | 0.73 | 8.7 dB   |
| Peaking | 8417 Hz  | 1.49 | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 16000 Hz | 1.41 | -16.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Trinity/Jomo%20Trinity.png)