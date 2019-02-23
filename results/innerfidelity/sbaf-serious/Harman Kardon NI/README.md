# Harman Kardon NI
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.1; 25 -10.1; 28 -10.1; 31 -10.1; 34 -10.0; 37 -9.9; 41 -9.8; 45 -9.7; 49 -9.5; 54 -9.4; 60 -9.3; 66 -9.3; 72 -9.2; 79 -9.1; 87 -9.1; 96 -9.0; 106 -8.7; 116 -8.5; 128 -8.3; 141 -8.1; 155 -7.7; 170 -7.4; 187 -6.9; 206 -6.5; 227 -6.0; 249 -5.6; 274 -5.1; 302 -4.6; 332 -4.1; 365 -3.6; 402 -3.2; 442 -2.6; 486 -2.4; 535 -2.1; 588 -1.5; 647 -1.4; 712 -1.5; 783 -1.3; 861 -1.4; 947 -1.7; 1042 -2.0; 1146 -2.5; 1261 -3.2; 1387 -4.1; 1526 -5.2; 1678 -6.1; 1846 -7.0; 2031 -7.9; 2234 -9.3; 2457 -11.0; 2703 -11.2; 2973 -7.9; 3270 -4.3; 3597 -2.5; 3957 -3.3; 4353 -6.7; 4788 -10.9; 5267 -13.2; 5793 -5.7; 6373 -0.5; 7010 -2.0; 7711 -4.3; 8482 -4.5; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Harman Kardon NI GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Harman Kardon NI ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.11 | -5.4 dB  |
| Peaking | 686 Hz  | 0.65 | 3.9 dB   |
| Peaking | 2556 Hz | 1.48 | -12.5 dB |
| Peaking | 3826 Hz | 0.83 | 8.6 dB   |
| Peaking | 5029 Hz | 4.41 | -14.3 dB |
| Peaking | 1054 Hz | 4.78 | 0.4 dB   |
| Peaking | 3553 Hz | 5.01 | 1.5 dB   |
| Peaking | 4197 Hz | 7.83 | -1.2 dB  |
| Peaking | 6428 Hz | 5.31 | 6.1 dB   |
| Peaking | 7109 Hz | 1.08 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Harman%20Kardon%20NI/Harman%20Kardon%20NI.png)