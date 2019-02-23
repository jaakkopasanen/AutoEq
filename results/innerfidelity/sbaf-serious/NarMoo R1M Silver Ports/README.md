# NarMoo R1M Silver Ports
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.1; 25 -7.2; 28 -7.2; 31 -7.3; 34 -7.3; 37 -7.4; 41 -7.4; 45 -7.5; 49 -7.7; 54 -7.8; 60 -8.0; 66 -8.3; 72 -8.5; 79 -8.8; 87 -9.1; 96 -9.5; 106 -9.6; 116 -9.7; 128 -9.8; 141 -9.9; 155 -9.9; 170 -9.8; 187 -9.7; 206 -9.5; 227 -9.1; 249 -8.8; 274 -8.3; 302 -7.9; 332 -7.4; 365 -6.8; 402 -6.3; 442 -5.5; 486 -5.1; 535 -4.5; 588 -3.6; 647 -3.1; 712 -2.7; 783 -2.1; 861 -2.1; 947 -1.9; 1042 -1.5; 1146 -1.5; 1261 -1.5; 1387 -1.9; 1526 -2.2; 1678 -2.4; 1846 -2.2; 2031 -2.0; 2234 -1.9; 2457 -1.4; 2703 -1.7; 2973 -2.0; 3270 -2.3; 3597 -2.9; 3957 -4.1; 4353 -7.2; 4788 -9.6; 5267 -8.8; 5793 -4.4; 6373 -0.5; 7010 -2.1; 7711 -4.4; 8482 -4.6; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo R1M Silver Ports GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Silver Ports ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.11 | -2.1 dB |
| Peaking | 202 Hz  | 0.45 | -4.7 dB |
| Peaking | 1120 Hz | 0.27 | 3.8 dB  |
| Peaking | 4934 Hz | 3.59 | -7.6 dB |
| Peaking | 6438 Hz | 5.95 | 5.1 dB  |
| Peaking | 1133 Hz | 1.53 | 0.6 dB  |
| Peaking | 1667 Hz | 1.93 | -1.3 dB |
| Peaking | 2800 Hz | 1.75 | 0.7 dB  |
| Peaking | 8865 Hz | 2.12 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Silver%20Ports/NarMoo%20R1M%20Silver%20Ports.png)