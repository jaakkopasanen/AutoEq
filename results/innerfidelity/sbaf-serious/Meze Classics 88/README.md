# Meze Classics 88
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.3; 25 -7.5; 28 -7.7; 31 -7.9; 34 -8.0; 37 -8.2; 41 -8.3; 45 -8.4; 49 -8.5; 54 -8.6; 60 -8.7; 66 -8.8; 72 -8.9; 79 -9.2; 87 -9.8; 96 -10.3; 106 -10.4; 116 -10.7; 128 -11.2; 141 -11.4; 155 -11.5; 170 -11.4; 187 -11.6; 206 -11.7; 227 -11.4; 249 -11.0; 274 -10.6; 302 -10.5; 332 -10.4; 365 -10.1; 402 -9.6; 442 -8.4; 486 -7.0; 535 -5.5; 588 -5.2; 647 -6.7; 712 -8.4; 783 -9.4; 861 -10.7; 947 -11.7; 1042 -11.2; 1146 -12.8; 1261 -13.4; 1387 -13.6; 1526 -12.9; 1678 -11.4; 1846 -9.1; 2031 -7.1; 2234 -5.1; 2457 -2.7; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.6; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze Classics 88 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Classics 88 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 119 Hz  | 0.64 | -3.8 dB |
| Peaking | 237 Hz  | 1.31 | -3.0 dB |
| Peaking | 1382 Hz | 1.4  | -8.9 dB |
| Peaking | 3177 Hz | 1.12 | 7.7 dB  |
| Peaking | 5838 Hz | 3.53 | 4.5 dB  |
| Peaking | 33 Hz   | 1.81 | -0.8 dB |
| Peaking | 380 Hz  | 3.65 | -1.6 dB |
| Peaking | 566 Hz  | 3.57 | 3.5 dB  |
| Peaking | 878 Hz  | 4.15 | -1.7 dB |
| Peaking | 8383 Hz | 3.6  | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%20Classics%2088/Meze%20Classics%2088.png)