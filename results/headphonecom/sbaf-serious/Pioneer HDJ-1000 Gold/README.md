# Pioneer HDJ-1000 Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -2.0; 79 -3.9; 87 -5.7; 96 -7.0; 106 -7.7; 116 -8.2; 128 -8.5; 141 -8.5; 155 -8.4; 170 -8.2; 187 -8.0; 206 -8.0; 227 -8.0; 249 -7.8; 274 -7.4; 302 -7.3; 332 -7.2; 365 -7.0; 402 -6.8; 442 -6.4; 486 -6.9; 535 -7.1; 588 -5.9; 647 -6.1; 712 -6.7; 783 -7.5; 861 -8.2; 947 -8.9; 1042 -9.2; 1146 -9.8; 1261 -10.7; 1387 -11.8; 1526 -12.5; 1678 -12.1; 1846 -10.6; 2031 -8.6; 2234 -6.5; 2457 -4.5; 2703 -3.4; 2973 -2.8; 3270 -2.2; 3597 -0.8; 3957 -4.9; 4353 -4.8; 4788 -1.1; 5267 -1.9; 5793 -3.8; 6373 -6.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-1000 Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-1000 Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 59 Hz   |  0.38 | 10.3 dB |
| Peaking | 117 Hz  |  0.68 | -9.5 dB |
| Peaking | 1561 Hz |  1.54 | -7.1 dB |
| Peaking | 3041 Hz |  1.5  | 5.5 dB  |
| Peaking | 5090 Hz |  5.53 | 4.9 dB  |
| Peaking | 62 Hz   |  1.35 | -1.4 dB |
| Peaking | 66 Hz   |  3.6  | 2.7 dB  |
| Peaking | 623 Hz  |  6.03 | 1.3 dB  |
| Peaking | 6874 Hz | 10.97 | 2.9 dB  |
| Peaking | 7286 Hz |  1.22 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Pioneer%20HDJ-1000%20Gold/Pioneer%20HDJ-1000%20Gold.png)