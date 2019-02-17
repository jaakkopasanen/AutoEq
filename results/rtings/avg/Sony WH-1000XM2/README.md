# Sony WH-1000XM2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.4; 25 -10.1; 28 -9.7; 31 -9.5; 34 -9.2; 37 -9.0; 41 -8.7; 45 -8.5; 49 -8.4; 54 -8.4; 60 -8.5; 66 -8.7; 72 -8.9; 79 -9.1; 87 -9.3; 96 -9.5; 106 -9.8; 116 -10.0; 128 -10.1; 141 -10.2; 155 -10.2; 170 -10.0; 187 -9.8; 206 -9.3; 227 -8.8; 249 -8.7; 274 -8.4; 302 -8.0; 332 -7.5; 365 -7.1; 402 -6.7; 442 -6.4; 486 -6.0; 535 -5.6; 588 -5.1; 647 -4.6; 712 -3.9; 783 -1.8; 861 -0.5; 947 -0.6; 1042 -1.3; 1146 -3.1; 1261 -5.3; 1387 -8.1; 1526 -9.8; 1678 -11.2; 1846 -12.6; 2031 -12.0; 2234 -9.7; 2457 -8.3; 2703 -8.5; 2973 -7.8; 3270 -7.7; 3597 -8.6; 3957 -9.7; 4353 -7.8; 4788 -5.6; 5267 -7.9; 5793 -8.6; 6373 -4.8; 7010 -5.5; 7711 -7.3; 8482 -7.9; 9330 -4.8; 10263 -1.8; 11289 -2.0; 12418 -3.1; 13660 -1.4; 15026 -0.8; 16529 -0.8; 18182 -0.8; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 1.05 | -9.8 dB |
| Peaking | 41 Hz    | 0.16 | -6.5 dB |
| Peaking | 210 Hz   | 0.55 | -4.9 dB |
| Peaking | 1838 Hz  | 2.34 | -9.4 dB |
| Peaking | 4714 Hz  | 0.57 | -6.9 dB |
| Peaking | 885 Hz   | 0.92 | -3.6 dB |
| Peaking | 923 Hz   | 2.19 | 7.3 dB  |
| Peaking | 6589 Hz  | 7.54 | 2.9 dB  |
| Peaking | 8390 Hz  | 4.07 | -3.6 dB |
| Peaking | 10332 Hz | 4.58 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.2 dB  |
| Peaking | 62 Hz    | 1.41 | -4.7 dB  |
| Peaking | 125 Hz   | 1.41 | -7.8 dB  |
| Peaking | 250 Hz   | 1.41 | -6.3 dB  |
| Peaking | 500 Hz   | 1.41 | -3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.1 dB |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.3 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-1000XM2/Sony%20WH-1000XM2.png)