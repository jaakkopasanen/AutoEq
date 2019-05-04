# Grado GW100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -3.7; 25 -5.3; 28 -7.2; 31 -8.5; 34 -9.2; 37 -9.5; 41 -9.3; 45 -8.8; 49 -8.2; 54 -7.8; 60 -7.9; 66 -8.1; 72 -8.2; 79 -8.2; 87 -8.3; 96 -8.5; 106 -8.9; 116 -9.5; 128 -10.1; 141 -10.7; 155 -11.3; 170 -11.7; 187 -11.7; 206 -11.5; 227 -11.2; 249 -10.4; 274 -9.4; 302 -8.7; 332 -8.3; 365 -7.8; 402 -7.4; 442 -7.2; 486 -7.0; 535 -6.6; 588 -6.1; 647 -5.5; 712 -4.7; 783 -4.1; 861 -3.4; 947 -2.9; 1042 -2.5; 1146 -2.4; 1261 -2.7; 1387 -3.3; 1526 -4.4; 1678 -6.1; 1846 -9.7; 2031 -12.6; 2234 -12.2; 2457 -8.9; 2703 -5.8; 2973 -3.8; 3270 -2.9; 3597 -3.1; 3957 -3.3; 4353 -1.5; 4788 -0.5; 5267 -0.6; 5793 -0.5; 6373 -1.5; 7010 -4.0; 7711 -6.3; 8482 -10.1; 9330 -10.2; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GW100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GW100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 181 Hz   | 0.8  | -5.2 dB  |
| Peaking | 1208 Hz  | 0.97 | 5.2 dB   |
| Peaking | 2109 Hz  | 2.67 | -10.1 dB |
| Peaking | 3185 Hz  | 1.95 | 3.7 dB   |
| Peaking | 5321 Hz  | 2.62 | 6.4 dB   |
| Peaking | 18 Hz    | 1.83 | 6.3 dB   |
| Peaking | 34 Hz    | 1.92 | -3.7 dB  |
| Peaking | 6521 Hz  | 5.43 | 2.4 dB   |
| Peaking | 8963 Hz  | 3.92 | -5.9 dB  |
| Peaking | 10439 Hz | 3.59 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20GW100/Grado%20GW100.png)