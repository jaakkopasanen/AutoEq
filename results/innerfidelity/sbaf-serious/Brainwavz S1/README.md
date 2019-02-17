# Brainwavz S1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.6; 25 -10.7; 28 -10.8; 31 -10.8; 34 -10.9; 37 -11.0; 41 -11.1; 45 -11.2; 49 -11.3; 54 -11.4; 60 -11.6; 66 -11.8; 72 -11.9; 79 -12.1; 87 -12.3; 96 -12.5; 106 -12.5; 116 -12.4; 128 -12.4; 141 -12.3; 155 -12.1; 170 -11.8; 187 -11.4; 206 -11.0; 227 -10.5; 249 -10.1; 274 -9.4; 302 -8.8; 332 -8.2; 365 -7.5; 402 -6.8; 442 -6.0; 486 -5.4; 535 -4.6; 588 -3.7; 647 -3.1; 712 -2.6; 783 -1.9; 861 -1.7; 947 -1.5; 1042 -1.3; 1146 -1.1; 1261 -0.9; 1387 -1.2; 1526 -2.5; 1678 -4.1; 1846 -4.3; 2031 -4.0; 2234 -3.9; 2457 -3.5; 2703 -3.5; 2973 -3.5; 3270 -3.7; 3597 -4.3; 3957 -5.7; 4353 -8.8; 4788 -10.5; 5267 -10.9; 5793 -6.8; 6373 -2.9; 7010 -0.5; 7711 -1.1; 8482 -1.4; 9330 -2.6; 10263 -6.6; 11289 -5.7; 12418 -2.3; 13660 -5.4; 15026 -7.8; 16529 -2.5; 18182 -1.4; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz S1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.21 | -8.8 dB |
| Peaking | 146 Hz   | 0.63 | -6.0 dB |
| Peaking | 310 Hz   | 1.14 | -3.0 dB |
| Peaking | 4824 Hz  | 2.58 | -9.8 dB |
| Peaking | 14672 Hz | 1.91 | -6.1 dB |
| Peaking | 1340 Hz  | 1.43 | 3.5 dB  |
| Peaking | 1772 Hz  | 1.58 | -4.5 dB |
| Peaking | 7270 Hz  | 3.71 | 3.2 dB  |
| Peaking | 10659 Hz | 4.81 | -5.3 dB |
| Peaking | 12676 Hz | 5.11 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.2 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB |
| Peaking | 125 Hz   | 1.41 | -9.1 dB |
| Peaking | 250 Hz   | 1.41 | -7.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | -6.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -4.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S1/Brainwavz%20S1.png)