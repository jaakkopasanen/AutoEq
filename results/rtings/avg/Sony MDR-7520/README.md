# Sony MDR-7520
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.5; 25 -7.0; 28 -7.7; 31 -8.3; 34 -8.8; 37 -9.2; 41 -9.7; 45 -10.0; 49 -10.3; 54 -10.6; 60 -11.1; 66 -11.6; 72 -12.1; 79 -12.5; 87 -13.0; 96 -13.4; 106 -13.6; 116 -13.8; 128 -13.8; 141 -13.5; 155 -12.8; 170 -12.2; 187 -11.5; 206 -10.3; 227 -8.9; 249 -7.4; 274 -8.3; 302 -5.9; 332 -5.1; 365 -5.7; 402 -6.8; 442 -7.7; 486 -8.1; 535 -8.2; 588 -8.0; 647 -7.6; 712 -7.4; 783 -7.1; 861 -6.7; 947 -6.4; 1042 -6.4; 1146 -6.8; 1261 -7.4; 1387 -8.1; 1526 -9.0; 1678 -10.1; 1846 -11.4; 2031 -12.2; 2234 -11.8; 2457 -11.9; 2703 -13.2; 2973 -13.9; 3270 -12.1; 3597 -9.0; 3957 -4.4; 4353 -0.7; 4788 -0.5; 5267 -5.6; 5793 -7.7; 6373 -4.8; 7010 -5.3; 7711 -10.8; 8482 -17.1; 9330 -19.6; 10263 -16.3; 11289 -10.0; 12418 -6.3; 13660 -6.3; 15026 -7.8; 16529 -12.2; 18182 -11.4; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7520 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7520 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 104 Hz   | 0.76 | -7.8 dB  |
| Peaking | 2998 Hz  | 1.14 | -10.0 dB |
| Peaking | 4407 Hz  | 2.2  | 11.6 dB  |
| Peaking | 9297 Hz  | 3.47 | -14.7 dB |
| Peaking | 17406 Hz | 1.99 | -7.0 dB  |
| Peaking | 332 Hz   | 5.09 | 3.1 dB   |
| Peaking | 1980 Hz  | 4.29 | -2.9 dB  |
| Peaking | 2042 Hz  | 1.94 | 1.3 dB   |
| Peaking | 17942 Hz | 3.58 | 0.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-7520/Sony%20MDR-7520.png)