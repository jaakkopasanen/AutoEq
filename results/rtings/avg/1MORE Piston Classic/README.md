# 1MORE Piston Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.6; 25 -3.2; 28 -4.0; 31 -4.6; 34 -5.2; 37 -5.7; 41 -6.3; 45 -6.9; 49 -7.3; 54 -7.8; 60 -8.4; 66 -9.0; 72 -9.5; 79 -9.9; 87 -10.5; 96 -11.0; 106 -11.4; 116 -11.8; 128 -12.1; 141 -12.3; 155 -12.4; 170 -12.4; 187 -12.3; 206 -12.2; 227 -11.9; 249 -11.7; 274 -11.6; 302 -11.4; 332 -11.0; 365 -10.5; 402 -9.9; 442 -9.3; 486 -8.5; 535 -7.4; 588 -6.4; 647 -5.5; 712 -4.7; 783 -4.3; 861 -4.4; 947 -4.4; 1042 -4.1; 1146 -3.6; 1261 -3.2; 1387 -2.7; 1526 -1.9; 1678 -1.1; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.1; 3270 -4.1; 3597 -6.0; 3957 -6.6; 4353 -7.4; 4788 -8.2; 5267 -8.3; 5793 -7.7; 6373 -6.1; 7010 -4.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Piston Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Piston Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.92 | 5.2 dB  |
| Peaking | 111 Hz  | 0.74 | -2.2 dB |
| Peaking | 307 Hz  | 0.36 | -5.9 dB |
| Peaking | 784 Hz  | 0.71 | 5.3 dB  |
| Peaking | 2152 Hz | 1.57 | 6.4 dB  |
| Peaking | 1613 Hz | 2.45 | 1.8 dB  |
| Peaking | 2799 Hz | 0.9  | -2.5 dB |
| Peaking | 2842 Hz | 3.54 | 4.9 dB  |
| Peaking | 5212 Hz | 2.13 | -2.0 dB |
| Peaking | 6883 Hz | 4.42 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Piston%20Classic/1MORE%20Piston%20Classic.png)