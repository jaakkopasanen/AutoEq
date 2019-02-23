# Westone UM3X RC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.3; 25 -6.6; 28 -7.0; 31 -7.3; 34 -7.6; 37 -7.8; 41 -8.1; 45 -8.3; 49 -8.6; 54 -8.9; 60 -9.4; 66 -9.7; 72 -10.0; 79 -10.4; 87 -10.8; 96 -11.1; 106 -11.4; 116 -11.6; 128 -11.9; 141 -12.0; 155 -12.2; 170 -12.4; 187 -12.3; 206 -12.4; 227 -12.2; 249 -12.2; 274 -12.0; 302 -11.7; 332 -11.3; 365 -10.9; 402 -10.5; 442 -10.2; 486 -9.8; 535 -9.3; 588 -8.8; 647 -8.5; 712 -8.2; 783 -7.8; 861 -7.9; 947 -8.0; 1042 -8.3; 1146 -8.6; 1261 -8.9; 1387 -9.3; 1526 -9.8; 1678 -9.8; 1846 -8.9; 2031 -7.4; 2234 -5.5; 2457 -3.1; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -11.1; 10263 -10.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM3X RC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM3X RC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 89 Hz   | 0.72 | -1.7 dB |
| Peaking | 230 Hz  | 0.46 | -5.4 dB |
| Peaking | 1688 Hz | 1.18 | -9.1 dB |
| Peaking | 3186 Hz | 0.46 | 8.9 dB  |
| Peaking | 9504 Hz | 2.86 | -7.8 dB |
| Peaking | 19 Hz   | 2.12 | 1.0 dB  |
| Peaking | 2780 Hz | 5.54 | 1.6 dB  |
| Peaking | 4759 Hz | 0.86 | -1.4 dB |
| Peaking | 6453 Hz | 1.65 | 3.0 dB  |
| Peaking | 7382 Hz | 5.51 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20UM3X%20RC/Westone%20UM3X%20RC.png)