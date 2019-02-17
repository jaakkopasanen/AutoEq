# Sony MDR-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -9.1; 25 -9.4; 28 -9.6; 31 -9.8; 34 -9.8; 37 -9.8; 41 -9.7; 45 -9.5; 49 -9.4; 54 -9.4; 60 -9.4; 66 -9.6; 72 -9.8; 79 -10.1; 87 -10.5; 96 -10.9; 106 -11.3; 116 -11.5; 128 -11.7; 141 -11.8; 155 -11.8; 170 -11.6; 187 -11.3; 206 -10.8; 227 -10.3; 249 -10.2; 274 -10.2; 302 -9.7; 332 -8.7; 365 -7.6; 402 -7.4; 442 -7.8; 486 -8.0; 535 -7.8; 588 -6.4; 647 -6.7; 712 -7.9; 783 -4.4; 861 -3.3; 947 -2.5; 1042 -2.0; 1146 -0.5; 1261 -2.5; 1387 -4.5; 1526 -7.3; 1678 -9.3; 1846 -10.2; 2031 -9.6; 2234 -7.7; 2457 -7.0; 2703 -6.9; 2973 -6.5; 3270 -6.4; 3597 -6.8; 3957 -9.7; 4353 -10.4; 4788 -8.6; 5267 -10.3; 5793 -14.7; 6373 -7.7; 7010 -4.3; 7711 -6.0; 8482 -6.0; 9330 -3.2; 10263 -2.1; 11289 -4.6; 12418 -8.2; 13660 -7.9; 15026 -2.3; 16529 -2.0; 18182 -2.0; 20000 -2.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.13 | -6.9 dB |
| Peaking | 193 Hz   | 0.64 | -6.0 dB |
| Peaking | 543 Hz   | 2.1  | -3.1 dB |
| Peaking | 1885 Hz  | 3.07 | -7.5 dB |
| Peaking | 5154 Hz  | 1.08 | -8.8 dB |
| Peaking | 710 Hz   | 9.49 | -3.5 dB |
| Peaking | 1164 Hz  | 2.24 | 3.5 dB  |
| Peaking | 1512 Hz  | 4.11 | -2.8 dB |
| Peaking | 10073 Hz | 3.99 | 3.0 dB  |
| Peaking | 12907 Hz | 3.24 | -6.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -8.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.1 dB |
| Peaking | 500 Hz   | 1.41 | -4.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | -6.2 dB |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-1000X/Sony%20MDR-1000X.png)