# Klipsch Image S2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.4; 25 -11.5; 28 -11.6; 31 -11.8; 34 -11.8; 37 -11.8; 41 -11.8; 45 -11.8; 49 -11.9; 54 -11.9; 60 -11.9; 66 -12.0; 72 -12.0; 79 -12.0; 87 -11.9; 96 -11.8; 106 -11.6; 116 -11.4; 128 -11.2; 141 -11.0; 155 -10.7; 170 -10.4; 187 -10.0; 206 -9.5; 227 -9.1; 249 -8.6; 274 -8.1; 302 -7.5; 332 -6.9; 365 -6.3; 402 -5.7; 442 -5.2; 486 -4.8; 535 -4.3; 588 -4.0; 647 -3.6; 712 -3.4; 783 -3.5; 861 -3.7; 947 -4.3; 1042 -5.1; 1146 -6.0; 1261 -7.2; 1387 -7.9; 1526 -7.5; 1678 -7.8; 1846 -8.8; 2031 -9.8; 2234 -10.8; 2457 -11.1; 2703 -9.4; 2973 -5.8; 3270 -2.4; 3597 -0.5; 3957 -1.3; 4353 -4.1; 4788 -6.6; 5267 -10.3; 5793 -11.4; 6373 -4.1; 7010 -3.7; 7711 -6.0; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.3; 15026 -7.3; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image S2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.38 | -5.7 dB  |
| Peaking | 139 Hz   | 1.02 | -3.0 dB  |
| Peaking | 2280 Hz  | 1.31 | -16.9 dB |
| Peaking | 2730 Hz  | 0.55 | 12.1 dB  |
| Peaking | 5493 Hz  | 4.91 | -10.6 dB |
| Peaking | 682 Hz   | 1.47 | 2.2 dB   |
| Peaking | 1321 Hz  | 3.65 | -2.8 dB  |
| Peaking | 2741 Hz  | 7.91 | -2.3 dB  |
| Peaking | 3599 Hz  | 5.55 | 3.0 dB   |
| Peaking | 10204 Hz | 1.37 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S2/Klipsch%20Image%20S2.png)