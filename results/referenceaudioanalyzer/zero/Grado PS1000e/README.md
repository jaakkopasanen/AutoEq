# Grado PS1000e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.6; 87 -3.4; 96 -5.3; 106 -7.2; 116 -8.9; 128 -10.3; 141 -10.9; 155 -10.6; 170 -9.8; 187 -8.7; 206 -7.6; 227 -6.4; 249 -5.5; 274 -4.7; 302 -4.0; 332 -3.7; 365 -3.5; 402 -3.1; 442 -2.8; 486 -2.5; 535 -2.3; 588 -2.1; 647 -1.9; 712 -1.8; 783 -1.8; 861 -1.8; 947 -1.8; 1042 -2.1; 1146 -2.4; 1261 -2.8; 1387 -3.4; 1526 -4.4; 1678 -5.5; 1846 -6.0; 2031 -6.2; 2234 -6.3; 2457 -6.8; 2703 -7.9; 2973 -9.0; 3270 -9.6; 3597 -9.2; 3957 -7.9; 4353 -8.8; 4788 -12.3; 5267 -15.3; 5793 -17.7; 6373 -17.4; 7010 -12.5; 7711 -6.9; 8482 -6.5; 9330 -6.5; 10263 -7.4; 11289 -9.4; 12418 -9.0; 13660 -6.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS1000e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 80 Hz    | 0.24 | 9.4 dB   |
| Peaking | 141 Hz   | 1    | -13.4 dB |
| Peaking | 837 Hz   | 0.77 | 4.2 dB   |
| Peaking | 3077 Hz  | 2.69 | -2.7 dB  |
| Peaking | 5887 Hz  | 2.97 | -12.5 dB |
| Peaking | 74 Hz    | 6.65 | 1.5 dB   |
| Peaking | 1798 Hz  | 6.49 | -0.9 dB  |
| Peaking | 8240 Hz  | 5.1  | 2.8 dB   |
| Peaking | 11906 Hz | 4.32 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 7.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.0 dB |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20PS1000e/Grado%20PS1000e.png)