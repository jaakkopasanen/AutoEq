# Pioneer HDJ-2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.4; 31 -2.5; 34 -3.7; 37 -4.7; 41 -6.0; 45 -7.0; 49 -7.8; 54 -8.7; 60 -9.6; 66 -10.2; 72 -10.6; 79 -10.9; 87 -11.4; 96 -11.8; 106 -11.8; 116 -11.7; 128 -11.7; 141 -11.9; 155 -12.0; 170 -11.7; 187 -11.8; 206 -11.8; 227 -11.8; 249 -11.8; 274 -11.7; 302 -11.2; 332 -10.7; 365 -9.8; 402 -8.7; 442 -7.4; 486 -6.7; 535 -6.7; 588 -6.3; 647 -6.3; 712 -6.8; 783 -7.2; 861 -7.1; 947 -6.7; 1042 -6.9; 1146 -7.7; 1261 -8.1; 1387 -8.5; 1526 -9.2; 1678 -9.1; 1846 -8.3; 2031 -6.8; 2234 -4.0; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.8; 3597 -3.7; 3957 -5.9; 4353 -3.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  1.02 | 7.3 dB  |
| Peaking | 102 Hz  |  0.5  | -5.6 dB |
| Peaking | 265 Hz  |  1.73 | -3.1 dB |
| Peaking | 2847 Hz |  3.53 | 6.8 dB  |
| Peaking | 5511 Hz |  2.63 | 6.7 dB  |
| Peaking | 557 Hz  |  2.72 | 1.4 dB  |
| Peaking | 1625 Hz |  2.21 | -3.4 dB |
| Peaking | 2407 Hz |  6.18 | 2.8 dB  |
| Peaking | 3977 Hz | 14.49 | -2.0 dB |
| Peaking | 9246 Hz |  5.11 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Pioneer%20HDJ-2000/Pioneer%20HDJ-2000.png)