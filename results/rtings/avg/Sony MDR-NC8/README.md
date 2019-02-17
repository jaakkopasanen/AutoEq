# Sony MDR-NC8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.5; 72 -2.3; 79 -3.1; 87 -3.9; 96 -4.6; 106 -5.4; 116 -5.9; 128 -5.6; 141 -4.9; 155 -3.7; 170 -2.7; 187 -3.1; 206 -3.9; 227 -3.7; 249 -3.4; 274 -2.8; 302 -2.0; 332 -1.5; 365 -1.0; 402 -0.6; 442 -0.5; 486 -0.9; 535 -1.7; 588 -2.2; 647 -1.9; 712 -3.3; 783 -4.5; 861 -3.7; 947 -5.7; 1042 -6.4; 1146 -4.8; 1261 -3.1; 1387 -2.5; 1526 -2.2; 1678 -1.8; 1846 -1.7; 2031 -1.3; 2234 -0.6; 2457 -1.2; 2703 -1.7; 2973 -2.2; 3270 -2.1; 3597 -1.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.8; 8482 -11.1; 9330 -8.9; 10263 -6.5; 11289 -6.5; 12418 -7.0; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-NC8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-NC8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.64 | 6.8 dB  |
| Peaking | 175 Hz  | 5.41 | 2.2 dB  |
| Peaking | 420 Hz  | 1.13 | 5.9 dB  |
| Peaking | 2158 Hz | 1.13 | 5.1 dB  |
| Peaking | 4878 Hz | 1.92 | 6.0 dB  |
| Peaking | 62 Hz   | 4.07 | 1.4 dB  |
| Peaking | 115 Hz  | 4.11 | -1.6 dB |
| Peaking | 1014 Hz | 8.55 | -2.5 dB |
| Peaking | 6428 Hz | 4.79 | 3.4 dB  |
| Peaking | 8459 Hz | 4.05 | -6.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 5.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-NC8/Sony%20MDR-NC8.png)