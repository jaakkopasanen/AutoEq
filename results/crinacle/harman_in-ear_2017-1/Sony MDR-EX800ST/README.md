# Sony MDR-EX800ST
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.9; 25 -2.3; 28 -2.7; 31 -3.0; 34 -3.3; 37 -3.5; 41 -3.8; 45 -4.0; 49 -4.3; 54 -4.6; 60 -4.9; 66 -5.3; 72 -5.7; 79 -6.1; 87 -6.6; 96 -7.1; 106 -7.6; 116 -8.0; 128 -8.3; 141 -8.7; 155 -9.1; 170 -9.3; 187 -9.6; 206 -9.7; 227 -9.8; 249 -9.9; 274 -9.9; 302 -9.9; 332 -9.7; 365 -9.6; 402 -9.5; 442 -9.4; 486 -9.1; 535 -8.8; 588 -8.6; 647 -8.2; 712 -7.7; 783 -7.5; 861 -6.6; 947 -6.4; 1042 -6.9; 1146 -7.5; 1261 -8.1; 1387 -8.7; 1526 -8.8; 1678 -8.6; 1846 -8.0; 2031 -6.8; 2234 -4.9; 2457 -2.8; 2703 -0.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -3.8; 5267 -8.3; 5793 -6.4; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.3; 18182 -14.5; 20000 -15.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX800ST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX800ST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.24 | 5.1 dB   |
| Peaking | 244 Hz   | 0.53 | -3.7 dB  |
| Peaking | 1697 Hz  | 2.04 | -3.6 dB  |
| Peaking | 2975 Hz  | 1.67 | 6.7 dB   |
| Peaking | 4133 Hz  | 5.06 | 3.9 dB   |
| Peaking | 515 Hz   | 2.77 | -0.4 dB  |
| Peaking | 908 Hz   | 6.14 | 1.4 dB   |
| Peaking | 5428 Hz  | 8.25 | -4.6 dB  |
| Peaking | 6507 Hz  | 6.47 | 4.8 dB   |
| Peaking | 19224 Hz | 1.23 | -10.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MDR-EX800ST/Sony%20MDR-EX800ST.png)