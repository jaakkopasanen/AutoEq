# Focal Spirit One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -11.0; 25 -11.0; 28 -11.0; 31 -11.1; 34 -11.1; 37 -11.0; 41 -10.9; 45 -10.8; 49 -10.7; 54 -10.7; 60 -10.8; 66 -10.7; 72 -10.4; 79 -9.9; 87 -10.6; 96 -12.4; 106 -13.0; 116 -12.9; 128 -12.6; 141 -12.7; 155 -12.5; 170 -12.1; 187 -11.8; 206 -11.2; 227 -10.3; 249 -9.6; 274 -8.7; 302 -7.9; 332 -7.9; 365 -7.8; 402 -8.6; 442 -8.6; 486 -8.7; 535 -8.7; 588 -8.2; 647 -8.3; 712 -8.3; 783 -7.8; 861 -7.6; 947 -7.0; 1042 -6.7; 1146 -7.0; 1261 -6.7; 1387 -6.9; 1526 -7.1; 1678 -7.0; 1846 -6.3; 2031 -5.5; 2234 -4.5; 2457 -3.2; 2703 -2.3; 2973 -0.7; 3270 -1.0; 3597 -0.5; 3957 -3.5; 4353 -5.9; 4788 -6.5; 5267 -6.4; 5793 -2.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.52 | -4.4 dB |
| Peaking | 136 Hz  | 0.95 | -5.7 dB |
| Peaking | 1630 Hz | 0.15 | -1.2 dB |
| Peaking | 3104 Hz | 1.91 | 7.3 dB  |
| Peaking | 6311 Hz | 5.63 | 6.5 dB  |
| Peaking | 319 Hz  | 2.97 | 1.6 dB  |
| Peaking | 649 Hz  | 0.5  | -1.0 dB |
| Peaking | 1024 Hz | 1.81 | 1.5 dB  |
| Peaking | 4627 Hz | 1.48 | 2.1 dB  |
| Peaking | 4773 Hz | 3.21 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One/Focal%20Spirit%20One.png)