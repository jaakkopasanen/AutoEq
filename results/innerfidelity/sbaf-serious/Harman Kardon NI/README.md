# Harman Kardon NI
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.2; 25 -11.3; 28 -11.2; 31 -11.2; 34 -11.1; 37 -11.0; 41 -10.9; 45 -10.8; 49 -10.7; 54 -10.6; 60 -10.5; 66 -10.4; 72 -10.3; 79 -10.3; 87 -10.2; 96 -10.1; 106 -9.9; 116 -9.6; 128 -9.4; 141 -9.2; 155 -8.8; 170 -8.5; 187 -8.0; 206 -7.7; 227 -7.1; 249 -6.7; 274 -6.2; 302 -5.7; 332 -5.2; 365 -4.8; 402 -4.3; 442 -3.8; 486 -3.6; 535 -3.2; 588 -2.6; 647 -2.5; 712 -2.6; 783 -2.5; 861 -2.6; 947 -2.8; 1042 -3.2; 1146 -3.6; 1261 -4.3; 1387 -5.2; 1526 -6.3; 1678 -7.3; 1846 -8.1; 2031 -9.1; 2234 -10.5; 2457 -12.1; 2703 -12.3; 2973 -9.0; 3270 -5.5; 3597 -3.6; 3957 -4.4; 4353 -7.8; 4788 -12.0; 5267 -14.3; 5793 -6.8; 6373 -1.6; 7010 -0.5; 7711 -2.7; 8482 -3.0; 9330 -3.0; 10263 -3.0; 11289 -3.0; 12418 -3.0; 13660 -3.0; 15026 -3.0; 16529 -3.6; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Harman Kardon NI GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Harman Kardon NI ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.1  | -8.1 dB  |
| Peaking | 621 Hz  | 1.09 | 1.9 dB   |
| Peaking | 2387 Hz | 1.96 | -9.1 dB  |
| Peaking | 5161 Hz | 4.98 | -12.6 dB |
| Peaking | 6641 Hz | 3.98 | 4.8 dB   |
| Peaking | 1714 Hz | 2.24 | -3.4 dB  |
| Peaking | 2133 Hz | 1.23 | 2.9 dB   |
| Peaking | 2750 Hz | 4.72 | -4.1 dB  |
| Peaking | 3643 Hz | 3.6  | 2.9 dB   |
| Peaking | 4531 Hz | 5.31 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | -4.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Harman%20Kardon%20NI/Harman%20Kardon%20NI.png)