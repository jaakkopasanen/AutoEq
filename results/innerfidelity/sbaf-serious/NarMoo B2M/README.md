# NarMoo B2M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.4; 23 -14.3; 25 -14.3; 28 -14.2; 31 -14.0; 34 -13.8; 37 -13.6; 41 -13.5; 45 -13.3; 49 -13.1; 54 -13.0; 60 -12.8; 66 -12.7; 72 -12.6; 79 -12.6; 87 -12.5; 96 -12.5; 106 -12.3; 116 -12.2; 128 -12.0; 141 -11.9; 155 -11.7; 170 -11.5; 187 -11.2; 206 -11.0; 227 -10.6; 249 -10.4; 274 -10.1; 302 -9.8; 332 -9.5; 365 -9.2; 402 -8.9; 442 -8.5; 486 -8.4; 535 -8.0; 588 -7.5; 647 -7.2; 712 -7.2; 783 -6.8; 861 -6.7; 947 -6.9; 1042 -7.2; 1146 -7.2; 1261 -7.3; 1387 -7.7; 1526 -8.0; 1678 -8.3; 1846 -6.8; 2031 -6.6; 2234 -6.5; 2457 -6.1; 2703 -5.2; 2973 -3.3; 3270 -0.8; 3597 -0.5; 3957 -0.5; 4353 -2.4; 4788 -4.7; 5267 -2.4; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo B2M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo B2M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.27 | -7.6 dB |
| Peaking | 156 Hz  | 0.49 | -4.0 dB |
| Peaking | 3584 Hz | 1.99 | 8.9 dB  |
| Peaking | 3653 Hz | 0.54 | -2.7 dB |
| Peaking | 6022 Hz | 3.27 | 7.0 dB  |
| Peaking | 828 Hz  | 3.08 | 0.8 dB  |
| Peaking | 1666 Hz | 4.48 | -1.7 dB |
| Peaking | 1838 Hz | 4.55 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20B2M/NarMoo%20B2M.png)