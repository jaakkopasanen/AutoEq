# Simgot EN700 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -11.8; 25 -11.6; 28 -11.5; 31 -11.2; 34 -11.0; 37 -10.8; 41 -10.5; 45 -10.3; 49 -10.1; 54 -9.8; 60 -9.5; 66 -9.2; 72 -9.0; 79 -8.8; 87 -8.6; 96 -8.5; 106 -8.3; 116 -8.1; 128 -7.9; 141 -7.6; 155 -7.2; 170 -6.8; 187 -6.4; 206 -6.1; 227 -5.6; 249 -5.1; 274 -4.7; 302 -4.2; 332 -3.8; 365 -3.3; 402 -2.9; 442 -2.5; 486 -2.2; 535 -1.9; 588 -1.6; 647 -1.3; 712 -1.0; 783 -0.7; 861 -0.5; 947 -0.5; 1042 -1.0; 1146 -1.7; 1261 -2.6; 1387 -3.0; 1526 -3.2; 1678 -3.1; 1846 -3.0; 2031 -3.4; 2234 -4.0; 2457 -5.1; 2703 -6.2; 2973 -6.3; 3270 -5.4; 3597 -4.5; 3957 -4.1; 4353 -4.7; 4788 -6.7; 5267 -8.6; 5793 -6.5; 6373 -3.1; 7010 -3.0; 7711 -5.2; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -4.0; 18182 -4.0; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Simgot EN700 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Simgot EN700 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.41 | -7.5 dB |
| Peaking | 121 Hz  | 0.54 | -3.0 dB |
| Peaking | 1166 Hz | 0.47 | 5.1 dB  |
| Peaking | 1333 Hz | 2.89 | -2.1 dB |
| Peaking | 2810 Hz | 0.63 | -3.9 dB |
| Peaking | 2891 Hz | 3.84 | -2.0 dB |
| Peaking | 4091 Hz | 1.64 | 2.6 dB  |
| Peaking | 4953 Hz | 3.84 | -1.1 dB |
| Peaking | 5311 Hz | 3.98 | -4.2 dB |
| Peaking | 6540 Hz | 6.11 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Simgot%20EN700%20Pro/Simgot%20EN700%20Pro.png)