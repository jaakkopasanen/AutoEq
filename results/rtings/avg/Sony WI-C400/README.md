# Sony WI-C400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.2; 66 -2.1; 72 -2.9; 79 -3.7; 87 -4.6; 96 -5.5; 106 -6.2; 116 -6.9; 128 -7.4; 141 -7.9; 155 -8.2; 170 -8.4; 187 -8.4; 206 -8.3; 227 -8.0; 249 -7.8; 274 -7.7; 302 -7.6; 332 -7.2; 365 -6.7; 402 -6.1; 442 -5.5; 486 -4.9; 535 -4.3; 588 -3.7; 647 -3.2; 712 -2.7; 783 -2.2; 861 -2.2; 947 -2.8; 1042 -3.5; 1146 -4.4; 1261 -5.3; 1387 -5.8; 1526 -5.9; 1678 -6.3; 1846 -6.8; 2031 -7.2; 2234 -7.1; 2457 -6.7; 2703 -6.6; 2973 -6.8; 3270 -7.3; 3597 -7.7; 3957 -8.2; 4353 -9.0; 4788 -10.3; 5267 -10.8; 5793 -9.6; 6373 -7.3; 7010 -6.4; 7711 -6.7; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.2; 18182 -7.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-C400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-C400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.34 | 7.5 dB  |
| Peaking | 140 Hz   | 0.62 | -5.4 dB |
| Peaking | 768 Hz   | 1.39 | 4.8 dB  |
| Peaking | 5015 Hz  | 2.63 | -4.5 dB |
| Peaking | 17304 Hz | 3.19 | -2.7 dB |
| Peaking | 34 Hz    | 2.95 | -0.2 dB |
| Peaking | 717 Hz   | 3.51 | -1.7 dB |
| Peaking | 731 Hz   | 1.72 | 1.3 dB  |
| Peaking | 1993 Hz  | 2.7  | -1.0 dB |
| Peaking | 6958 Hz  | 7.24 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-C400/Sony%20WI-C400.png)