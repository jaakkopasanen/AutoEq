# Ivery IS-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.4; 23 -14.5; 25 -14.6; 28 -14.6; 31 -14.7; 34 -14.8; 37 -14.8; 41 -15.0; 45 -15.1; 49 -15.2; 54 -15.3; 60 -15.5; 66 -15.7; 72 -15.9; 79 -16.1; 87 -16.4; 96 -16.6; 106 -16.6; 116 -16.5; 128 -16.6; 141 -16.5; 155 -16.4; 170 -16.2; 187 -15.9; 206 -15.5; 227 -14.9; 249 -14.5; 274 -13.8; 302 -13.3; 332 -12.6; 365 -11.9; 402 -11.1; 442 -10.2; 486 -9.5; 535 -8.7; 588 -7.5; 647 -6.8; 712 -5.8; 783 -4.7; 861 -4.5; 947 -4.1; 1042 -2.6; 1146 -2.1; 1261 -2.0; 1387 -1.8; 1526 -1.3; 1678 -0.7; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -1.6; 5267 -1.2; 5793 -1.4; 6373 -4.3; 7010 -9.9; 7711 -11.9; 8482 -7.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ivery IS-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ivery IS-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.22 | -6.7 dB |
| Peaking | 170 Hz  | 0.41 | -8.4 dB |
| Peaking | 1598 Hz | 0.61 | 6.2 dB  |
| Peaking | 3993 Hz | 1.75 | 4.3 dB  |
| Peaking | 1478 Hz | 3.69 | -1.1 dB |
| Peaking | 3898 Hz | 0.72 | 1.9 dB  |
| Peaking | 4156 Hz | 1.55 | -2.7 dB |
| Peaking | 5781 Hz | 2.98 | 3.9 dB  |
| Peaking | 7448 Hz | 3.94 | -8.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB |
| Peaking | 125 Hz   | 1.41 | -8.4 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ivery%20IS-1/Ivery%20IS-1.png)