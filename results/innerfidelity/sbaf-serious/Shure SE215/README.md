# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -8.6; 25 -8.6; 28 -8.7; 31 -8.8; 34 -8.8; 37 -8.9; 41 -9.0; 45 -9.2; 49 -9.3; 54 -9.5; 60 -9.7; 66 -10.0; 72 -10.1; 79 -10.5; 87 -10.7; 96 -11.0; 106 -11.2; 116 -11.2; 128 -11.3; 141 -11.3; 155 -11.3; 170 -11.1; 187 -10.9; 206 -10.6; 227 -10.2; 249 -9.9; 274 -9.5; 302 -9.0; 332 -8.5; 365 -7.9; 402 -7.4; 442 -6.7; 486 -6.3; 535 -5.7; 588 -4.9; 647 -4.5; 712 -4.3; 783 -3.8; 861 -3.9; 947 -4.2; 1042 -4.5; 1146 -4.7; 1261 -5.3; 1387 -6.4; 1526 -7.4; 1678 -8.2; 1846 -8.8; 2031 -9.3; 2234 -9.3; 2457 -7.9; 2703 -5.8; 2973 -2.7; 3270 -0.7; 3597 -0.5; 3957 -2.5; 4353 -7.8; 4788 -12.4; 5267 -7.2; 5793 -1.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 0.52 | -3.3 dB |
| Peaking | 172 Hz  | 1.15 | -3.5 dB |
| Peaking | 3549 Hz | 3.89 | 7.6 dB  |
| Peaking | 4795 Hz | 4.71 | -8.5 dB |
| Peaking | 6029 Hz | 3.97 | 7.4 dB  |
| Peaking | 19 Hz   | 2.23 | -1.1 dB |
| Peaking | 319 Hz  | 1.66 | -1.3 dB |
| Peaking | 851 Hz  | 0.91 | 3.2 dB  |
| Peaking | 2049 Hz | 1.63 | -4.2 dB |
| Peaking | 3005 Hz | 4.98 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE215/Shure%20SE215.png)