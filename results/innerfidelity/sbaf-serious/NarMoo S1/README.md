# NarMoo S1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.5; 25 -12.6; 28 -12.6; 31 -12.7; 34 -12.7; 37 -12.7; 41 -12.7; 45 -12.8; 49 -12.8; 54 -12.8; 60 -12.9; 66 -13.0; 72 -13.0; 79 -13.1; 87 -13.2; 96 -13.3; 106 -13.2; 116 -13.0; 128 -12.9; 141 -12.8; 155 -12.4; 170 -12.1; 187 -11.7; 206 -11.2; 227 -10.7; 249 -10.1; 274 -9.5; 302 -8.8; 332 -8.1; 365 -7.3; 402 -6.5; 442 -5.6; 486 -4.9; 535 -4.0; 588 -2.9; 647 -2.2; 712 -1.7; 783 -1.1; 861 -1.0; 947 -0.8; 1042 -1.1; 1146 -1.1; 1261 -1.4; 1387 -2.2; 1526 -3.4; 1678 -4.0; 1846 -4.5; 2031 -4.8; 2234 -5.5; 2457 -6.5; 2703 -8.5; 2973 -10.3; 3270 -6.5; 3597 -3.7; 3957 -5.0; 4353 -8.6; 4788 -11.7; 5267 -6.9; 5793 -1.2; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.5; 10263 -6.9; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo S1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo S1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.4  | -5.4 dB |
| Peaking | 132 Hz  | 0.35 | -6.7 dB |
| Peaking | 944 Hz  | 0.58 | 7.3 dB  |
| Peaking | 3184 Hz | 0.47 | -3.4 dB |
| Peaking | 6261 Hz | 4.68 | 8.4 dB  |
| Peaking | 2180 Hz | 5.48 | 0.5 dB  |
| Peaking | 2990 Hz | 4.46 | -6.0 dB |
| Peaking | 3597 Hz | 2.69 | 6.4 dB  |
| Peaking | 4786 Hz | 4.94 | -6.5 dB |
| Peaking | 5657 Hz | 8.69 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20S1/NarMoo%20S1.png)