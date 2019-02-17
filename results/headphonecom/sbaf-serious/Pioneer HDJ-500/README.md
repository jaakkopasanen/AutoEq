# Pioneer HDJ-500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -2.1; 34 -3.7; 37 -5.1; 41 -6.6; 45 -7.7; 49 -8.4; 54 -9.0; 60 -9.4; 66 -9.5; 72 -9.4; 79 -9.2; 87 -9.5; 96 -9.7; 106 -9.8; 116 -9.8; 128 -10.2; 141 -10.5; 155 -10.7; 170 -10.8; 187 -11.1; 206 -11.1; 227 -11.3; 249 -11.1; 274 -10.8; 302 -11.1; 332 -11.2; 365 -11.8; 402 -12.0; 442 -11.2; 486 -10.9; 535 -9.9; 588 -8.8; 647 -8.0; 712 -7.6; 783 -7.4; 861 -7.0; 947 -6.9; 1042 -6.2; 1146 -5.4; 1261 -4.9; 1387 -4.5; 1526 -3.9; 1678 -3.3; 1846 -2.1; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -4.5; 5267 -8.5; 5793 -7.0; 6373 -1.3; 7010 -6.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.5; 18182 -8.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.28 | 8.6 dB  |
| Peaking | 104 Hz   | 0.25 | -3.9 dB |
| Peaking | 393 Hz   | 1.28 | -3.2 dB |
| Peaking | 2374 Hz  | 1.13 | 6.4 dB  |
| Peaking | 3961 Hz  | 3.84 | 4.2 dB  |
| Peaking | 203 Hz   | 4.21 | -0.7 dB |
| Peaking | 4502 Hz  | 8.89 | 4.1 dB  |
| Peaking | 5450 Hz  | 3.7  | -6.4 dB |
| Peaking | 6183 Hz  | 7.67 | 7.8 dB  |
| Peaking | 17700 Hz | 1.96 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Pioneer%20HDJ-500/Pioneer%20HDJ-500.png)