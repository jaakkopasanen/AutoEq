# Sony MDRV-SA5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.3; 72 -2.3; 79 -3.2; 87 -4.1; 96 -4.8; 106 -5.1; 116 -5.2; 128 -5.1; 141 -5.1; 155 -5.3; 170 -4.7; 187 -4.4; 206 -4.3; 227 -4.0; 249 -3.7; 274 -3.3; 302 -3.1; 332 -2.8; 365 -3.7; 402 -4.9; 442 -3.8; 486 -4.0; 535 -4.4; 588 -4.6; 647 -4.8; 712 -5.6; 783 -6.2; 861 -7.0; 947 -7.0; 1042 -5.9; 1146 -4.5; 1261 -3.4; 1387 -3.5; 1526 -4.2; 1678 -5.1; 1846 -6.1; 2031 -7.4; 2234 -9.3; 2457 -10.3; 2703 -9.4; 2973 -7.1; 3270 -4.2; 3597 -0.6; 3957 -0.7; 4353 -3.6; 4788 -2.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.4; 9330 -10.7; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDRV-SA5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDRV-SA5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.62 | 6.8 dB  |
| Peaking | 339 Hz  | 0.92 | 3.0 dB  |
| Peaking | 3744 Hz | 6.86 | 5.9 dB  |
| Peaking | 5776 Hz | 2.59 | 6.8 dB  |
| Peaking | 8986 Hz | 4.66 | -5.5 dB |
| Peaking | 62 Hz   | 3.73 | 1.6 dB  |
| Peaking | 102 Hz  | 2.1  | -1.0 dB |
| Peaking | 942 Hz  | 2.63 | -3.7 dB |
| Peaking | 1238 Hz | 1.31 | 3.9 dB  |
| Peaking | 2424 Hz | 3.42 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | 2.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDRV-SA5000/Sony%20MDRV-SA5000.png)