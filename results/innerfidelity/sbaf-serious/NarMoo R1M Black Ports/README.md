# NarMoo R1M Black Ports
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -15.5; 25 -15.5; 28 -15.4; 31 -15.3; 34 -15.3; 37 -15.2; 41 -15.1; 45 -15.1; 49 -15.0; 54 -14.9; 60 -14.9; 66 -14.9; 72 -14.8; 79 -14.8; 87 -14.8; 96 -14.8; 106 -14.5; 116 -14.2; 128 -14.1; 141 -13.7; 155 -13.3; 170 -12.9; 187 -12.4; 206 -11.8; 227 -11.1; 249 -10.5; 274 -9.8; 302 -9.0; 332 -8.2; 365 -7.4; 402 -6.7; 442 -5.7; 486 -5.0; 535 -4.0; 588 -3.1; 647 -2.5; 712 -2.3; 783 -2.2; 861 -2.6; 947 -2.5; 1042 -2.7; 1146 -2.9; 1261 -3.1; 1387 -3.4; 1526 -3.8; 1678 -4.0; 1846 -3.9; 2031 -3.6; 2234 -3.5; 2457 -3.0; 2703 -3.3; 2973 -3.6; 3270 -3.7; 3597 -4.1; 3957 -5.3; 4353 -8.2; 4788 -10.7; 5267 -10.3; 5793 -5.8; 6373 -1.9; 7010 -0.5; 7711 -2.4; 8482 -2.7; 9330 -2.7; 10263 -2.7; 11289 -2.7; 12418 -2.7; 13660 -2.7; 15026 -2.7; 16529 -5.2; 18182 -4.4; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo R1M Black Ports GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Black Ports ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.2  | -12.5 dB |
| Peaking | 169 Hz   | 0.7  | -5.3 dB  |
| Peaking | 5021 Hz  | 2.75 | -10.0 dB |
| Peaking | 6515 Hz  | 2.6  | 4.3 dB   |
| Peaking | 17274 Hz | 2.68 | -3.3 dB  |
| Peaking | 44 Hz    | 2.51 | 0.3 dB   |
| Peaking | 348 Hz   | 1.8  | -1.1 dB  |
| Peaking | 690 Hz   | 1.55 | 1.9 dB   |
| Peaking | 1676 Hz  | 2.89 | -1.1 dB  |
| Peaking | 3587 Hz  | 6.11 | 0.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.1 dB |
| Peaking | 62 Hz    | 1.41 | -8.5 dB  |
| Peaking | 125 Hz   | 1.41 | -9.2 dB  |
| Peaking | 250 Hz   | 1.41 | -6.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -1.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Black%20Ports/NarMoo%20R1M%20Black%20Ports.png)