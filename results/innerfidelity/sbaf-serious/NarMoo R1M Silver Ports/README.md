# NarMoo R1M Silver Ports
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.3; 25 -8.3; 28 -8.4; 31 -8.4; 34 -8.5; 37 -8.5; 41 -8.6; 45 -8.7; 49 -8.8; 54 -9.0; 60 -9.2; 66 -9.4; 72 -9.7; 79 -10.0; 87 -10.3; 96 -10.6; 106 -10.7; 116 -10.8; 128 -11.0; 141 -11.1; 155 -11.1; 170 -11.0; 187 -10.8; 206 -10.6; 227 -10.2; 249 -10.0; 274 -9.5; 302 -9.1; 332 -8.5; 365 -8.0; 402 -7.4; 442 -6.7; 486 -6.2; 535 -5.6; 588 -4.7; 647 -4.2; 712 -3.8; 783 -3.2; 861 -3.3; 947 -3.1; 1042 -2.7; 1146 -2.6; 1261 -2.6; 1387 -3.0; 1526 -3.3; 1678 -3.5; 1846 -3.4; 2031 -3.1; 2234 -3.0; 2457 -2.6; 2703 -2.9; 2973 -3.2; 3270 -3.5; 3597 -4.1; 3957 -5.3; 4353 -8.3; 4788 -10.8; 5267 -10.0; 5793 -5.5; 6373 -1.7; 7010 -0.5; 7711 -2.4; 8482 -2.7; 9330 -2.7; 10263 -2.7; 11289 -2.7; 12418 -2.7; 13660 -2.7; 15026 -2.7; 16529 -4.8; 18182 -3.5; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo R1M Silver Ports GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Silver Ports ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.18 | -5.2 dB |
| Peaking | 153 Hz   | 0.67 | -5.0 dB |
| Peaking | 320 Hz   | 1.14 | -2.8 dB |
| Peaking | 4957 Hz  | 3.18 | -9.3 dB |
| Peaking | 6676 Hz  | 4.14 | 4.2 dB  |
| Peaking | 497 Hz   | 4.03 | -0.6 dB |
| Peaking | 1217 Hz  | 1.15 | 1.1 dB  |
| Peaking | 1644 Hz  | 1.81 | -1.2 dB |
| Peaking | 2559 Hz  | 2.69 | 0.6 dB  |
| Peaking | 17043 Hz | 3.22 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.7 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Silver%20Ports/NarMoo%20R1M%20Silver%20Ports.png)