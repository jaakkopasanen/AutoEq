# ADV Sound M4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.6; 25 -12.8; 28 -13.1; 31 -13.3; 34 -13.4; 37 -13.6; 41 -13.8; 45 -14.0; 49 -14.2; 54 -14.4; 60 -14.6; 66 -14.9; 72 -15.2; 79 -15.4; 87 -15.7; 96 -16.0; 106 -16.1; 116 -16.1; 128 -16.2; 141 -16.2; 155 -16.1; 170 -15.9; 187 -15.7; 206 -15.4; 227 -14.9; 249 -14.5; 274 -14.0; 302 -13.4; 332 -12.9; 365 -12.2; 402 -11.6; 442 -10.8; 486 -10.3; 535 -9.6; 588 -8.6; 647 -8.1; 712 -7.6; 783 -7.0; 861 -6.8; 947 -6.7; 1042 -6.3; 1146 -6.1; 1261 -6.3; 1387 -6.6; 1526 -6.9; 1678 -6.9; 1846 -6.4; 2031 -5.9; 2234 -5.5; 2457 -5.9; 2703 -6.0; 2973 -3.5; 3270 -1.4; 3597 -0.5; 3957 -0.8; 4353 -2.7; 4788 -3.3; 5267 -3.1; 5793 -4.3; 6373 -8.1; 7010 -12.4; 7711 -11.7; 8482 -8.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ADV Sound M4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ADV Sound M4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.27 | -6.4 dB |
| Peaking | 147 Hz  | 0.66 | -5.4 dB |
| Peaking | 308 Hz  | 1.06 | -3.2 dB |
| Peaking | 3902 Hz | 1.7  | 6.1 dB  |
| Peaking | 7285 Hz | 4.48 | -7.7 dB |
| Peaking | 1002 Hz | 2.53 | 0.9 dB  |
| Peaking | 2684 Hz | 5.57 | -1.7 dB |
| Peaking | 3394 Hz | 2.62 | 3.1 dB  |
| Peaking | 4139 Hz | 1.25 | -2.4 dB |
| Peaking | 5471 Hz | 4.51 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.0 dB |
| Peaking | 125 Hz   | 1.41 | -8.1 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ADV%20Sound%20M4/ADV%20Sound%20M4.png)