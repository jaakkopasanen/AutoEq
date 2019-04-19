# Sony MDR-7506
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.9; 28 -2.9; 31 -3.7; 34 -4.3; 37 -4.8; 41 -5.4; 45 -5.8; 49 -6.1; 54 -6.3; 60 -6.3; 66 -5.8; 72 -5.0; 79 -5.2; 87 -5.0; 96 -5.0; 106 -6.5; 116 -7.2; 128 -6.9; 141 -6.9; 155 -6.6; 170 -6.1; 187 -5.0; 206 -3.5; 227 -3.2; 249 -4.1; 274 -4.9; 302 -5.2; 332 -5.0; 365 -4.7; 402 -4.5; 442 -4.2; 486 -4.0; 535 -3.8; 588 -3.6; 647 -3.3; 712 -3.2; 783 -2.7; 861 -2.6; 947 -2.6; 1042 -2.1; 1146 -2.4; 1261 -2.3; 1387 -2.3; 1526 -2.7; 1678 -3.1; 1846 -3.6; 2031 -3.7; 2234 -4.1; 2457 -5.6; 2703 -7.5; 2973 -7.9; 3270 -6.5; 3597 -4.6; 3957 -4.5; 4353 -9.6; 4788 -10.0; 5267 -8.6; 5793 -9.1; 6373 -10.4; 7010 -9.7; 7711 -6.8; 8482 -5.2; 9330 -5.4; 10263 -5.3; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7506 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 2.49 | 4.9 dB  |
| Peaking | 128 Hz  | 2.8  | -2.4 dB |
| Peaking | 2562 Hz | 0.23 | 3.4 dB  |
| Peaking | 2782 Hz | 3.55 | -4.7 dB |
| Peaking | 5686 Hz | 1.22 | -7.8 dB |
| Peaking | 54 Hz   | 2.41 | -1.5 dB |
| Peaking | 85 Hz   | 2.81 | 0.7 dB  |
| Peaking | 3839 Hz | 9.13 | 3.0 dB  |
| Peaking | 4491 Hz | 9.53 | -3.2 dB |
| Peaking | 8376 Hz | 9.12 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-7506/Sony%20MDR-7506.png)