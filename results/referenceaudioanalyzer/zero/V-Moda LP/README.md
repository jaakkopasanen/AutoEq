# V-Moda LP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -1.0; 28 -2.4; 31 -4.2; 34 -5.7; 37 -6.9; 41 -8.2; 45 -9.1; 49 -9.7; 54 -10.2; 60 -10.7; 66 -11.2; 72 -11.7; 79 -12.2; 87 -12.5; 96 -12.8; 106 -13.0; 116 -13.3; 128 -13.3; 141 -13.5; 155 -13.6; 170 -13.6; 187 -13.3; 206 -12.5; 227 -11.7; 249 -11.1; 274 -10.9; 302 -10.6; 332 -9.9; 365 -8.5; 402 -6.5; 442 -4.3; 486 -2.2; 535 -0.6; 588 -0.5; 647 -1.3; 712 -2.8; 783 -4.0; 861 -4.7; 947 -4.7; 1042 -4.6; 1146 -4.9; 1261 -5.5; 1387 -6.0; 1526 -6.2; 1678 -6.1; 1846 -6.0; 2031 -6.1; 2234 -6.8; 2457 -7.9; 2703 -8.0; 2973 -8.0; 3270 -9.8; 3597 -10.8; 3957 -9.0; 4353 -5.0; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda LP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.07 | 9.6 dB   |
| Peaking | 332 Hz  | 0.41 | -12.1 dB |
| Peaking | 406 Hz  | 0.06 | -7.1 dB  |
| Peaking | 537 Hz  | 0.49 | 22.4 dB  |
| Peaking | 5650 Hz | 2.25 | 9.8 dB   |
| Peaking | 242 Hz  | 6.36 | 1.2 dB   |
| Peaking | 815 Hz  | 5.5  | -1.4 dB  |
| Peaking | 1967 Hz | 2.24 | 1.5 dB   |
| Peaking | 3645 Hz | 4.41 | -3.9 dB  |
| Peaking | 4691 Hz | 6.84 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -6.1 dB |
| Peaking | 500 Hz   | 1.41 | 5.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/V-Moda%20LP/V-Moda%20LP.png)