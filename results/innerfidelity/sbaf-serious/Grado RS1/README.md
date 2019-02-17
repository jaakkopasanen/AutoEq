# Grado RS1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.7; 54 -3.0; 60 -4.3; 66 -5.4; 72 -6.5; 79 -7.5; 87 -8.5; 96 -9.2; 106 -9.7; 116 -9.8; 128 -9.9; 141 -9.8; 155 -9.6; 170 -9.3; 187 -9.0; 206 -8.7; 227 -8.1; 249 -8.2; 274 -8.1; 302 -7.8; 332 -7.5; 365 -7.1; 402 -7.4; 442 -7.1; 486 -7.0; 535 -6.7; 588 -6.5; 647 -6.4; 712 -6.5; 783 -6.1; 861 -6.2; 947 -6.5; 1042 -6.5; 1146 -6.6; 1261 -7.4; 1387 -8.5; 1526 -10.3; 1678 -11.6; 1846 -16.4; 2031 -14.9; 2234 -13.7; 2457 -11.9; 2703 -10.6; 2973 -8.3; 3270 -6.9; 3597 -5.6; 3957 -8.8; 4353 -16.3; 4788 -14.5; 5267 -11.8; 5793 -11.7; 6373 -14.9; 7010 -16.9; 7711 -14.5; 8482 -15.0; 9330 -15.6; 10263 -8.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -11.6; 18182 -13.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 1.53 | 7.5 dB  |
| Peaking | 1959 Hz  | 2.96 | -9.5 dB |
| Peaking | 7030 Hz  | 1.25 | -9.7 dB |
| Peaking | 17827 Hz | 2.37 | -8.5 dB |
| Peaking | 22050 Hz | 2.01 | -5.0 dB |
| Peaking | 136 Hz   | 1.1  | -3.9 dB |
| Peaking | 3642 Hz  | 5.42 | 4.9 dB  |
| Peaking | 4431 Hz  | 7.17 | -8.3 dB |
| Peaking | 9266 Hz  | 3.9  | -9.1 dB |
| Peaking | 10171 Hz | 1.35 | 5.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -9.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1/Grado%20RS1.png)