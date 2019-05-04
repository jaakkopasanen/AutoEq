# Sony MDR-7506
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.4; 25 -6.9; 28 -7.6; 31 -8.1; 34 -8.4; 37 -8.6; 41 -8.8; 45 -8.8; 49 -8.7; 54 -8.6; 60 -8.4; 66 -8.2; 72 -7.9; 79 -7.7; 87 -7.6; 96 -7.6; 106 -7.5; 116 -7.2; 128 -6.7; 141 -6.2; 155 -5.8; 170 -5.1; 187 -4.2; 206 -3.2; 227 -1.9; 249 -0.5; 274 -1.2; 302 -3.5; 332 -4.3; 365 -4.4; 402 -4.5; 442 -4.7; 486 -4.8; 535 -4.6; 588 -4.4; 647 -4.1; 712 -3.8; 783 -3.6; 861 -3.1; 947 -2.8; 1042 -3.0; 1146 -3.3; 1261 -3.8; 1387 -4.2; 1526 -4.9; 1678 -5.7; 1846 -6.6; 2031 -7.5; 2234 -7.4; 2457 -7.2; 2703 -7.7; 2973 -8.4; 3270 -8.0; 3597 -7.1; 3957 -7.8; 4353 -9.9; 4788 -8.4; 5267 -4.4; 5793 -1.1; 6373 -0.8; 7010 -3.9; 7711 -6.6; 8482 -7.4; 9330 -8.5; 10263 -10.5; 11289 -8.4; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7506 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 0.51 | -3.6 dB |
| Peaking | 249 Hz   | 2.37 | 5.0 dB  |
| Peaking | 4870 Hz  | 1.05 | -6.3 dB |
| Peaking | 5964 Hz  | 2.94 | 10.4 dB |
| Peaking | 10232 Hz | 3.59 | -5.2 dB |
| Peaking | 1047 Hz  | 1.36 | 2.8 dB  |
| Peaking | 2177 Hz  | 1.24 | -1.6 dB |
| Peaking | 3702 Hz  | 8.55 | 2.2 dB  |
| Peaking | 8078 Hz  | 7.75 | -1.0 dB |
| Peaking | 12478 Hz | 4.66 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | 4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-7506/Sony%20MDR-7506.png)