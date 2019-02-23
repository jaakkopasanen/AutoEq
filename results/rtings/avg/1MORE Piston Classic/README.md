# 1MORE Piston Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.1; 41 -1.7; 45 -2.2; 49 -2.7; 54 -3.3; 60 -4.2; 66 -5.0; 72 -5.7; 79 -6.4; 87 -7.2; 96 -8.1; 106 -9.0; 116 -9.8; 128 -10.5; 141 -11.2; 155 -11.7; 170 -12.0; 187 -12.2; 206 -12.3; 227 -12.2; 249 -12.0; 274 -11.8; 302 -11.7; 332 -11.3; 365 -10.8; 402 -10.2; 442 -9.5; 486 -8.7; 535 -7.6; 588 -6.6; 647 -5.6; 712 -4.8; 783 -4.5; 861 -4.5; 947 -4.5; 1042 -4.2; 1146 -3.7; 1261 -3.3; 1387 -2.7; 1526 -2.0; 1678 -1.2; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.2; 3270 -4.5; 3597 -6.6; 3957 -7.1; 4353 -8.0; 4788 -8.0; 5267 -8.3; 5793 -8.0; 6373 -7.3; 7010 -5.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Piston Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Piston Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.33 | 7.1 dB  |
| Peaking | 184 Hz  | 0.4  | -7.5 dB |
| Peaking | 702 Hz  | 1.78 | 2.7 dB  |
| Peaking | 2610 Hz | 0.68 | 9.7 dB  |
| Peaking | 4120 Hz | 1.13 | -7.9 dB |
| Peaking | 2936 Hz | 6.08 | 2.5 dB  |
| Peaking | 3315 Hz | 2.24 | -2.3 dB |
| Peaking | 4093 Hz | 2.18 | 1.7 dB  |
| Peaking | 6196 Hz | 1.77 | -1.3 dB |
| Peaking | 7054 Hz | 6.27 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Piston%20Classic/1MORE%20Piston%20Classic.png)