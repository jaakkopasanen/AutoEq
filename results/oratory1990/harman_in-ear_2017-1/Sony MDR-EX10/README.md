# Sony MDR-EX10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.4; 25 -12.5; 28 -12.6; 31 -12.7; 34 -12.7; 37 -12.7; 41 -12.8; 45 -12.8; 49 -12.8; 54 -12.7; 60 -12.8; 66 -12.8; 72 -12.8; 79 -12.8; 87 -12.9; 96 -12.9; 106 -12.8; 116 -12.8; 128 -12.6; 141 -12.3; 155 -12.0; 170 -11.6; 187 -11.1; 206 -10.4; 227 -10.3; 249 -10.6; 274 -10.0; 302 -9.2; 332 -8.5; 365 -7.8; 402 -7.2; 442 -6.7; 486 -6.1; 535 -5.5; 588 -5.0; 647 -4.5; 712 -4.0; 783 -3.6; 861 -3.5; 947 -3.5; 1042 -3.9; 1146 -4.1; 1261 -3.9; 1387 -3.6; 1526 -3.3; 1678 -2.9; 1846 -2.7; 2031 -2.8; 2234 -2.5; 2457 -2.1; 2703 -2.1; 2973 -2.4; 3270 -2.7; 3597 -3.0; 3957 -3.7; 4353 -4.2; 4788 -4.3; 5267 -3.7; 5793 -2.2; 6373 -0.5; 7010 -3.2; 7711 -5.4; 8482 -5.6; 9330 -8.6; 10263 -8.0; 11289 -5.7; 12418 -5.7; 13660 -9.2; 15026 -22.6; 16529 -27.1; 18182 -21.2; 20000 -14.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 15 Hz    |  0.35 | -5.4 dB  |
| Peaking | 150 Hz   |  0.28 | -7.7 dB  |
| Peaking | 1990 Hz  |  0.09 | 4.4 dB   |
| Peaking | 12634 Hz |  2.27 | 10.0 dB  |
| Peaking | 16428 Hz |  0.86 | -25.6 dB |
| Peaking | 1318 Hz  |  2.94 | -1.2 dB  |
| Peaking | 4559 Hz  |  2.92 | -1.5 dB  |
| Peaking | 6419 Hz  |  4.57 | 4.5 dB   |
| Peaking | 9707 Hz  | 10.07 | -2.8 dB  |
| Peaking | 19605 Hz |  1    | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.0 dB  |
| Peaking | 62 Hz    | 1.41 | -5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 16000 Hz | 1.41 | -22.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20MDR-EX10/Sony%20MDR-EX10.png)