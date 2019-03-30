# German Maestro GMP 250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.4; 49 -2.3; 54 -3.3; 60 -4.1; 66 -4.8; 72 -5.5; 79 -6.2; 87 -6.5; 96 -6.6; 106 -6.8; 116 -6.8; 128 -6.7; 141 -6.5; 155 -6.2; 170 -5.9; 187 -5.4; 206 -5.0; 227 -4.5; 249 -4.2; 274 -4.0; 302 -3.9; 332 -3.9; 365 -3.9; 402 -4.0; 442 -4.3; 486 -4.7; 535 -5.3; 588 -5.9; 647 -6.5; 712 -7.1; 783 -7.6; 861 -7.7; 947 -7.3; 1042 -7.1; 1146 -7.1; 1261 -7.3; 1387 -7.6; 1526 -8.2; 1678 -8.9; 1846 -9.4; 2031 -9.4; 2234 -8.8; 2457 -6.9; 2703 -4.7; 2973 -6.7; 3270 -9.2; 3597 -9.1; 3957 -7.4; 4353 -4.5; 4788 -0.6; 5267 -5.5; 5793 -11.4; 6373 -12.3; 7010 -9.8; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -8.8; 11289 -11.6; 12418 -11.8; 13660 -8.4; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`German Maestro GMP 250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `German Maestro GMP 250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.9  | 6.8 dB  |
| Peaking | 1856 Hz  | 2.33 | -3.0 dB |
| Peaking | 4851 Hz  | 7.12 | 8.2 dB  |
| Peaking | 6117 Hz  | 4.05 | -6.9 dB |
| Peaking | 11966 Hz | 3.38 | -6.3 dB |
| Peaking | 104 Hz   | 1.69 | -1.4 dB |
| Peaking | 317 Hz   | 1.33 | 3.0 dB  |
| Peaking | 2745 Hz  | 7.62 | 3.3 dB  |
| Peaking | 3418 Hz  | 4.7  | -3.2 dB |
| Peaking | 8345 Hz  | 4.34 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/German%20Maestro%20GMP%20250/German%20Maestro%20GMP%20250.png)