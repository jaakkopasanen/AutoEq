# NarMoo R1M Gunmetal Port
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -11.5; 25 -11.3; 28 -10.9; 31 -10.7; 34 -10.4; 37 -10.2; 41 -9.9; 45 -9.7; 49 -9.6; 54 -9.5; 60 -9.4; 66 -9.4; 72 -9.3; 79 -9.4; 87 -9.5; 96 -9.6; 106 -9.6; 116 -9.5; 128 -9.5; 141 -9.5; 155 -9.4; 170 -9.3; 187 -9.1; 206 -8.8; 227 -8.5; 249 -8.2; 274 -7.8; 302 -7.3; 332 -6.9; 365 -6.3; 402 -5.8; 442 -5.2; 486 -4.9; 535 -4.2; 588 -3.4; 647 -2.9; 712 -2.5; 783 -2.0; 861 -2.0; 947 -1.7; 1042 -1.6; 1146 -1.5; 1261 -1.5; 1387 -1.9; 1526 -2.3; 1678 -2.4; 1846 -2.3; 2031 -2.0; 2234 -1.9; 2457 -1.5; 2703 -1.8; 2973 -2.1; 3270 -2.3; 3597 -2.7; 3957 -3.8; 4353 -6.8; 4788 -9.2; 5267 -8.7; 5793 -4.4; 6373 -0.5; 7010 -2.0; 7711 -4.2; 8482 -4.4; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.9; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo R1M Gunmetal Port GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Gunmetal Port ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.31 | -7.3 dB |
| Peaking | 184 Hz   | 0.41 | -5.3 dB |
| Peaking | 1124 Hz  | 0.28 | 3.6 dB  |
| Peaking | 4959 Hz  | 3.64 | -7.3 dB |
| Peaking | 6458 Hz  | 5.84 | 5.0 dB  |
| Peaking | 850 Hz   | 1.85 | 0.5 dB  |
| Peaking | 1692 Hz  | 3.07 | -1.1 dB |
| Peaking | 3156 Hz  | 2.08 | 0.7 dB  |
| Peaking | 8744 Hz  | 2.26 | -0.5 dB |
| Peaking | 17706 Hz | 3.8  | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Gunmetal%20Port/NarMoo%20R1M%20Gunmetal%20Port.png)