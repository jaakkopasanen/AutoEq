# Jabra Elite 45e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.7; 25 -5.2; 28 -5.9; 31 -6.5; 34 -7.0; 37 -7.4; 41 -7.9; 45 -8.3; 49 -8.7; 54 -9.1; 60 -9.6; 66 -10.1; 72 -10.5; 79 -10.7; 87 -11.0; 96 -11.2; 106 -11.3; 116 -11.5; 128 -12.0; 141 -12.2; 155 -12.1; 170 -12.0; 187 -11.9; 206 -11.7; 227 -11.4; 249 -11.2; 274 -11.0; 302 -10.6; 332 -10.3; 365 -9.9; 402 -9.6; 442 -9.2; 486 -8.7; 535 -8.0; 588 -7.2; 647 -6.4; 712 -5.5; 783 -4.7; 861 -4.2; 947 -4.6; 1042 -5.7; 1146 -6.5; 1261 -7.0; 1387 -7.2; 1526 -7.2; 1678 -6.6; 1846 -5.9; 2031 -5.1; 2234 -3.5; 2457 -1.7; 2703 -0.7; 2973 -0.5; 3270 -0.6; 3597 -0.7; 3957 -1.4; 4353 -2.9; 4788 -2.7; 5267 -1.5; 5793 -1.6; 6373 -4.6; 7010 -7.1; 7711 -5.0; 8482 -5.2; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -7.4; 13660 -12.7; 15026 -13.5; 16529 -10.7; 18182 -7.2; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 45e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 45e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 75 Hz    | 0.79 | -2.9 dB  |
| Peaking | 199 Hz   | 0.52 | -6.1 dB  |
| Peaking | 3480 Hz  | 1.37 | 5.2 dB   |
| Peaking | 11610 Hz | 1.8  | 4.9 dB   |
| Peaking | 14424 Hz | 1.11 | -10.2 dB |
| Peaking | 18 Hz    | 2.23 | 1.8 dB   |
| Peaking | 854 Hz   | 1.88 | 4.2 dB   |
| Peaking | 1896 Hz  | 0.47 | -4.0 dB  |
| Peaking | 2594 Hz  | 1.75 | 4.8 dB   |
| Peaking | 5534 Hz  | 5.06 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -8.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2045e/Jabra%20Elite%2045e.png)