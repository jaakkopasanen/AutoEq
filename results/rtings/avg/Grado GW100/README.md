# Grado GW100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -4.9; 25 -6.5; 28 -8.4; 31 -9.7; 34 -10.5; 37 -10.7; 41 -10.5; 45 -10.0; 49 -9.3; 54 -8.9; 60 -9.0; 66 -9.3; 72 -9.4; 79 -9.5; 87 -9.6; 96 -9.8; 106 -10.2; 116 -10.7; 128 -11.3; 141 -11.9; 155 -12.5; 170 -12.9; 187 -12.9; 206 -12.7; 227 -12.3; 249 -11.5; 274 -10.5; 302 -9.8; 332 -9.4; 365 -8.9; 402 -8.5; 442 -8.2; 486 -8.0; 535 -7.6; 588 -7.1; 647 -6.4; 712 -5.7; 783 -5.0; 861 -4.3; 947 -3.8; 1042 -3.4; 1146 -3.3; 1261 -3.6; 1387 -4.1; 1526 -5.2; 1678 -6.8; 1846 -10.4; 2031 -13.2; 2234 -12.4; 2457 -9.0; 2703 -6.3; 2973 -4.8; 3270 -4.1; 3597 -4.3; 3957 -4.7; 4353 -2.9; 4788 -0.6; 5267 -1.2; 5793 -0.5; 6373 -3.4; 7010 -3.5; 7711 -5.7; 8482 -11.5; 9330 -13.1; 10263 -7.5; 11289 -3.6; 12418 -4.0; 13660 -5.3; 15026 -5.0; 16529 -4.9; 18182 -6.0; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GW100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GW100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 38 Hz   |  1.33 | -5.9 dB  |
| Peaking | 183 Hz  |  0.55 | -9.0 dB  |
| Peaking | 2107 Hz |  3.57 | -10.5 dB |
| Peaking | 5443 Hz |  2.67 | 3.8 dB   |
| Peaking | 9051 Hz |  3.9  | -11.0 dB |
| Peaking | 70 Hz   |  4.81 | -0.7 dB  |
| Peaking | 555 Hz  |  2.63 | -1.3 dB  |
| Peaking | 1122 Hz |  1.59 | 1.7 dB   |
| Peaking | 1859 Hz |  7.55 | -1.6 dB  |
| Peaking | 3969 Hz | 10.08 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -6.9 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20GW100/Grado%20GW100.png)