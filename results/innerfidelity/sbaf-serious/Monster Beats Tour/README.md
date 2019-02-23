# Monster Beats Tour
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.3; 25 -13.2; 28 -13.1; 31 -13.0; 34 -12.9; 37 -12.8; 41 -12.6; 45 -12.5; 49 -12.4; 54 -12.3; 60 -12.1; 66 -12.0; 72 -12.0; 79 -11.9; 87 -11.8; 96 -11.7; 106 -11.5; 116 -11.1; 128 -10.9; 141 -10.7; 155 -10.3; 170 -9.8; 187 -9.4; 206 -8.9; 227 -8.3; 249 -7.8; 274 -7.2; 302 -6.6; 332 -6.0; 365 -5.4; 402 -4.9; 442 -4.2; 486 -3.8; 535 -3.3; 588 -2.6; 647 -2.3; 712 -2.1; 783 -1.8; 861 -2.1; 947 -2.4; 1042 -2.9; 1146 -3.2; 1261 -3.8; 1387 -4.7; 1526 -5.8; 1678 -6.8; 1846 -7.7; 2031 -8.7; 2234 -10.1; 2457 -10.4; 2703 -8.9; 2973 -5.1; 3270 -1.9; 3597 -0.5; 3957 -1.6; 4353 -5.2; 4788 -9.4; 5267 -14.5; 5793 -7.7; 6373 -2.1; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Tour GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Tour ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.2  | -7.3 dB  |
| Peaking | 144 Hz  | 0.68 | -3.0 dB  |
| Peaking | 1954 Hz | 0.31 | 7.2 dB   |
| Peaking | 2120 Hz | 1.42 | -11.5 dB |
| Peaking | 5229 Hz | 6.55 | -13.0 dB |
| Peaking | 2676 Hz | 4.99 | -4.0 dB  |
| Peaking | 3639 Hz | 1.89 | 5.1 dB   |
| Peaking | 4491 Hz | 5.83 | -2.7 dB  |
| Peaking | 6539 Hz | 5.69 | 5.4 dB   |
| Peaking | 6823 Hz | 0.78 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Tour/Monster%20Beats%20Tour.png)