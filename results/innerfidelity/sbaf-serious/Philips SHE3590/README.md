# Philips SHE3590
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.7; 25 -12.6; 28 -12.3; 31 -12.0; 34 -11.8; 37 -11.6; 41 -11.3; 45 -11.0; 49 -10.7; 54 -10.4; 60 -10.2; 66 -10.0; 72 -9.8; 79 -9.6; 87 -9.4; 96 -9.3; 106 -8.9; 116 -8.5; 128 -8.3; 141 -7.9; 155 -7.6; 170 -7.1; 187 -6.8; 206 -6.3; 227 -5.7; 249 -5.3; 274 -4.8; 302 -4.3; 332 -3.8; 365 -3.3; 402 -2.9; 442 -2.3; 486 -2.1; 535 -1.7; 588 -1.2; 647 -1.0; 712 -1.1; 783 -0.9; 861 -0.9; 947 -1.2; 1042 -1.9; 1146 -2.5; 1261 -3.3; 1387 -4.3; 1526 -5.5; 1678 -6.5; 1846 -7.3; 2031 -8.0; 2234 -9.3; 2457 -10.1; 2703 -9.4; 2973 -5.9; 3270 -2.2; 3597 -0.5; 3957 -0.9; 4353 -3.5; 4788 -5.8; 5267 -7.1; 5793 -5.5; 6373 -3.5; 7010 -1.7; 7711 -1.4; 8482 -1.6; 9330 -1.7; 10263 -2.0; 11289 -1.6; 12418 -1.6; 13660 -1.6; 15026 -1.6; 16529 -1.6; 18182 -1.6; 20000 -1.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHE3590 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHE3590 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.21 | -10.9 dB |
| Peaking | 148 Hz  | 0.87 | -3.1 dB  |
| Peaking | 2432 Hz | 1.61 | -9.4 dB  |
| Peaking | 3567 Hz | 3.05 | 5.6 dB   |
| Peaking | 5201 Hz | 3.8  | -5.4 dB  |
| Peaking | 87 Hz   | 3.74 | -0.5 dB  |
| Peaking | 285 Hz  | 1.79 | -0.8 dB  |
| Peaking | 784 Hz  | 1.05 | 1.7 dB   |
| Peaking | 1556 Hz | 3.16 | -1.7 dB  |
| Peaking | 7488 Hz | 6.57 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20SHE3590/Philips%20SHE3590.png)