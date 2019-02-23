# Thinksound On1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.3; 25 -8.8; 28 -9.4; 31 -9.8; 34 -10.2; 37 -10.5; 41 -10.8; 45 -11.0; 49 -11.1; 54 -11.2; 60 -11.1; 66 -11.5; 72 -11.9; 79 -12.1; 87 -12.1; 96 -11.8; 106 -11.2; 116 -10.6; 128 -10.1; 141 -9.3; 155 -8.9; 170 -7.5; 187 -7.4; 206 -6.3; 227 -5.0; 249 -4.2; 274 -4.1; 302 -4.4; 332 -5.1; 365 -5.5; 402 -5.8; 442 -6.1; 486 -6.5; 535 -6.8; 588 -6.7; 647 -6.9; 712 -7.2; 783 -7.2; 861 -7.5; 947 -7.6; 1042 -7.6; 1146 -7.5; 1261 -7.3; 1387 -7.5; 1526 -7.4; 1678 -7.3; 1846 -6.3; 2031 -4.3; 2234 -4.1; 2457 -3.3; 2703 -1.6; 2973 -2.0; 3270 -3.6; 3597 -3.9; 3957 -3.1; 4353 -3.7; 4788 -2.7; 5267 -0.5; 5793 -4.2; 6373 -5.0; 7010 -7.3; 7711 -7.9; 8482 -9.2; 9330 -7.5; 10263 -6.1; 11289 -6.1; 12418 -7.3; 13660 -8.6; 15026 -6.2; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksound On1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound On1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.86 | -4.4 dB |
| Peaking | 94 Hz    | 1.52 | -4.7 dB |
| Peaking | 2801 Hz  | 3.37 | 4.6 dB  |
| Peaking | 5134 Hz  | 2.99 | 5.2 dB  |
| Peaking | 8193 Hz  | 2.48 | -3.2 dB |
| Peaking | 149 Hz   | 3.16 | -1.3 dB |
| Peaking | 268 Hz   | 2.14 | 2.8 dB  |
| Peaking | 1152 Hz  | 0.88 | -1.8 dB |
| Peaking | 2138 Hz  | 5.43 | 1.9 dB  |
| Peaking | 13585 Hz | 6.19 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20On1/Thinksound%20On1.png)