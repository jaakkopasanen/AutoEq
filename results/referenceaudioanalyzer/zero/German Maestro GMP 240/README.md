# German Maestro GMP 240
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.7; 45 -2.7; 49 -3.4; 54 -4.4; 60 -5.7; 66 -7.1; 72 -8.1; 79 -8.8; 87 -9.3; 96 -9.9; 106 -10.1; 116 -10.1; 128 -10.1; 141 -9.7; 155 -9.3; 170 -8.9; 187 -8.4; 206 -7.9; 227 -7.3; 249 -6.7; 274 -6.2; 302 -5.8; 332 -5.4; 365 -5.1; 402 -4.8; 442 -4.5; 486 -4.1; 535 -3.8; 588 -3.5; 647 -3.3; 712 -3.3; 783 -3.3; 861 -3.1; 947 -3.0; 1042 -3.3; 1146 -3.5; 1261 -3.6; 1387 -3.6; 1526 -3.6; 1678 -3.0; 1846 -2.4; 2031 -2.9; 2234 -3.8; 2457 -4.3; 2703 -4.7; 2973 -7.5; 3270 -10.3; 3597 -11.4; 3957 -10.8; 4353 -8.7; 4788 -4.6; 5267 -2.2; 5793 -6.9; 6373 -10.8; 7010 -12.3; 7711 -13.0; 8482 -12.9; 9330 -12.4; 10263 -12.4; 11289 -12.3; 12418 -11.0; 13660 -9.3; 15026 -8.1; 16529 -6.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`German Maestro GMP 240 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `German Maestro GMP 240 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.51 | 7.9 dB  |
| Peaking | 96 Hz    | 0.62 | -6.7 dB |
| Peaking | 1942 Hz  | 0.16 | 4.1 dB  |
| Peaking | 3534 Hz  | 3.5  | -8.3 dB |
| Peaking | 9133 Hz  | 0.97 | -9.4 dB |
| Peaking | 4235 Hz  | 6.33 | -2.8 dB |
| Peaking | 5219 Hz  | 4.4  | 7.1 dB  |
| Peaking | 6618 Hz  | 2.14 | -3.7 dB |
| Peaking | 9445 Hz  | 2.22 | 2.2 dB  |
| Peaking | 11720 Hz | 2.59 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/German%20Maestro%20GMP%20240/German%20Maestro%20GMP%20240.png)