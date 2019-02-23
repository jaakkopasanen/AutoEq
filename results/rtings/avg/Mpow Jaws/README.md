# Mpow Jaws
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.4; 25 -8.5; 28 -8.5; 31 -8.6; 34 -8.6; 37 -8.7; 41 -8.7; 45 -8.8; 49 -8.9; 54 -9.1; 60 -9.6; 66 -10.0; 72 -10.4; 79 -10.8; 87 -11.4; 96 -11.9; 106 -12.6; 116 -13.1; 128 -13.7; 141 -14.1; 155 -14.3; 170 -14.4; 187 -14.4; 206 -14.2; 227 -14.1; 249 -13.9; 274 -13.3; 302 -12.3; 332 -11.1; 365 -10.4; 402 -10.3; 442 -10.1; 486 -9.5; 535 -8.8; 588 -7.9; 647 -6.9; 712 -6.0; 783 -5.3; 861 -5.2; 947 -5.5; 1042 -5.4; 1146 -5.7; 1261 -5.8; 1387 -5.3; 1526 -4.7; 1678 -4.3; 1846 -3.7; 2031 -3.0; 2234 -1.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.1; 3957 -2.1; 4353 -3.2; 4788 -3.2; 5267 -0.6; 5793 -2.5; 6373 -3.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Jaws GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Jaws ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.15 | -1.6 dB |
| Peaking | 140 Hz  | 0.82 | -5.4 dB |
| Peaking | 257 Hz  | 1.03 | -4.3 dB |
| Peaking | 2841 Hz | 1.05 | 6.3 dB  |
| Peaking | 5548 Hz | 4.61 | 4.0 dB  |
| Peaking | 491 Hz  | 3.5  | -1.3 dB |
| Peaking | 810 Hz  | 2.18 | 1.7 dB  |
| Peaking | 1340 Hz | 2.17 | -0.6 dB |
| Peaking | 6738 Hz | 9.79 | 2.9 dB  |
| Peaking | 7808 Hz | 1.66 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20Jaws/Mpow%20Jaws.png)