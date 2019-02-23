# Behringer HPS5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.9; 87 -3.1; 96 -3.8; 106 -4.6; 116 -5.2; 128 -5.8; 141 -6.1; 155 -6.5; 170 -6.7; 187 -6.8; 206 -7.0; 227 -7.0; 249 -7.0; 274 -6.7; 302 -6.2; 332 -6.3; 365 -6.3; 402 -6.4; 442 -7.4; 486 -7.5; 535 -7.5; 588 -7.3; 647 -7.5; 712 -7.9; 783 -8.4; 861 -9.5; 947 -10.5; 1042 -11.0; 1146 -11.6; 1261 -11.4; 1387 -12.7; 1526 -14.5; 1678 -14.5; 1846 -13.3; 2031 -10.7; 2234 -8.1; 2457 -5.1; 2703 -2.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -5.5; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.5; 8482 -9.7; 9330 -9.8; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Behringer HPS5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Behringer HPS5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 38 Hz    |  0.62 | 7.0 dB   |
| Peaking | 1729 Hz  |  1.02 | -11.5 dB |
| Peaking | 3016 Hz  |  1.15 | 10.7 dB  |
| Peaking | 6111 Hz  |  3.45 | 5.4 dB   |
| Peaking | 8663 Hz  |  3.3  | -5.0 dB  |
| Peaking | 41 Hz    |  2.89 | -1.1 dB  |
| Peaking | 71 Hz    |  3.1  | 2.0 dB   |
| Peaking | 157 Hz   |  1.45 | -1.2 dB  |
| Peaking | 1312 Hz  | 10.32 | 1.1 dB   |
| Peaking | 10620 Hz |  5.44 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.5 dB |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Behringer%20HPS5000/Behringer%20HPS5000.png)