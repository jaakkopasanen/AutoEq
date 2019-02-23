# NarMoo R1M Black Ports
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.1; 23 -14.1; 25 -14.1; 28 -14.0; 31 -13.9; 34 -13.8; 37 -13.8; 41 -13.7; 45 -13.6; 49 -13.5; 54 -13.5; 60 -13.5; 66 -13.4; 72 -13.4; 79 -13.4; 87 -13.4; 96 -13.3; 106 -13.1; 116 -12.8; 128 -12.6; 141 -12.3; 155 -11.9; 170 -11.5; 187 -10.9; 206 -10.4; 227 -9.7; 249 -9.1; 274 -8.4; 302 -7.6; 332 -6.8; 365 -6.0; 402 -5.3; 442 -4.2; 486 -3.5; 535 -2.6; 588 -1.6; 647 -1.0; 712 -0.9; 783 -0.7; 861 -1.2; 947 -1.1; 1042 -1.3; 1146 -1.5; 1261 -1.6; 1387 -2.0; 1526 -2.4; 1678 -2.5; 1846 -2.4; 2031 -2.1; 2234 -2.0; 2457 -1.6; 2703 -1.9; 2973 -2.1; 3270 -2.3; 3597 -2.7; 3957 -3.9; 4353 -6.8; 4788 -9.3; 5267 -8.8; 5793 -4.4; 6373 -0.5; 7010 -2.2; 7711 -4.4; 8482 -4.7; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo R1M Black Ports GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Black Ports ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 16 Hz   |  0.43 | -7.6 dB  |
| Peaking | 116 Hz  |  0.31 | -7.7 dB  |
| Peaking | 691 Hz  |  0.62 | 5.4 dB   |
| Peaking | 4652 Hz |  0.87 | 4.8 dB   |
| Peaking | 4828 Hz |  3.31 | -10.5 dB |
| Peaking | 2478 Hz |  5.19 | 0.9 dB   |
| Peaking | 5429 Hz | 10.02 | -2.0 dB  |
| Peaking | 6490 Hz |  4.69 | 4.6 dB   |
| Peaking | 7815 Hz |  1.54 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Black%20Ports/NarMoo%20R1M%20Black%20Ports.png)