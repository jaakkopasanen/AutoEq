# Stax SR-404 S 2742
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.8; 37 -0.9; 41 -1.0; 45 -1.1; 49 -1.1; 54 -1.2; 60 -1.5; 66 -1.9; 72 -2.2; 79 -2.5; 87 -2.7; 96 -3.1; 106 -3.5; 116 -3.7; 128 -3.9; 141 -4.1; 155 -4.2; 170 -4.2; 187 -4.4; 206 -4.4; 227 -4.4; 249 -4.5; 274 -4.5; 302 -4.5; 332 -4.5; 365 -4.4; 402 -4.4; 442 -4.3; 486 -4.6; 535 -4.8; 588 -4.5; 647 -4.8; 712 -5.0; 783 -5.0; 861 -5.5; 947 -6.0; 1042 -6.6; 1146 -7.0; 1261 -8.1; 1387 -9.0; 1526 -9.6; 1678 -10.4; 1846 -9.0; 2031 -6.1; 2234 -3.7; 2457 -2.2; 2703 -3.6; 2973 -5.6; 3270 -5.4; 3597 -4.8; 3957 -3.4; 4353 -3.4; 4788 -4.3; 5267 -4.3; 5793 -6.0; 6373 -6.1; 7010 -4.1; 7711 -6.2; 8482 -8.6; 9330 -10.7; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.3; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-404 S 2742 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-404 S 2742 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.44 | 4.3 dB  |
| Peaking | 64 Hz   | 0.06 | 1.8 dB  |
| Peaking | 1617 Hz | 1.55 | -9.3 dB |
| Peaking | 2114 Hz | 0.68 | 5.8 dB  |
| Peaking | 9264 Hz | 5.63 | -5.2 dB |
| Peaking | 1016 Hz | 4.08 | -0.6 dB |
| Peaking | 1838 Hz | 6.47 | -1.2 dB |
| Peaking | 2450 Hz | 3.47 | 3.2 dB  |
| Peaking | 3023 Hz | 2.99 | -3.4 dB |
| Peaking | 4194 Hz | 3.63 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-404%20S%202742/Stax%20SR-404%20S%202742.png)