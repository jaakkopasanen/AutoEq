# Pioneer HDJ-500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.2; 31 -2.6; 34 -4.3; 37 -5.7; 41 -7.2; 45 -8.3; 49 -9.0; 54 -9.6; 60 -10.0; 66 -10.1; 72 -9.9; 79 -9.8; 87 -10.1; 96 -10.3; 106 -10.4; 116 -10.4; 128 -10.8; 141 -11.1; 155 -11.3; 170 -11.4; 187 -11.7; 206 -11.7; 227 -11.9; 249 -11.7; 274 -11.4; 302 -11.7; 332 -11.7; 365 -12.4; 402 -12.6; 442 -11.8; 486 -11.5; 535 -10.4; 588 -9.4; 647 -8.6; 712 -8.2; 783 -8.0; 861 -7.6; 947 -7.5; 1042 -6.8; 1146 -6.0; 1261 -5.5; 1387 -5.1; 1526 -4.5; 1678 -3.8; 1846 -2.7; 2031 -1.2; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -5.0; 5267 -9.1; 5793 -7.6; 6373 -1.5; 7010 -6.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -9.1; 18182 -9.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.27 | 9.3 dB  |
| Peaking | 96 Hz    | 0.21 | -4.5 dB |
| Peaking | 397 Hz   | 1.15 | -3.1 dB |
| Peaking | 2750 Hz  | 1.02 | 7.0 dB  |
| Peaking | 17733 Hz | 1.59 | -3.4 dB |
| Peaking | 17 Hz    | 2.93 | 1.9 dB  |
| Peaking | 2827 Hz  | 6.55 | -1.0 dB |
| Peaking | 4452 Hz  | 3.06 | 7.0 dB  |
| Peaking | 5325 Hz  | 2.68 | -9.6 dB |
| Peaking | 6244 Hz  | 8.04 | 8.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -4.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Pioneer%20HDJ-500/Pioneer%20HDJ-500.png)