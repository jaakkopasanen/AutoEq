# Light Harmonic Stella
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.0; 25 -8.2; 28 -8.3; 31 -8.5; 34 -8.6; 37 -8.7; 41 -8.9; 45 -9.1; 49 -9.2; 54 -9.4; 60 -9.6; 66 -9.9; 72 -10.1; 79 -10.4; 87 -10.7; 96 -11.1; 106 -11.4; 116 -11.6; 128 -11.8; 141 -12.0; 155 -12.0; 170 -12.0; 187 -11.9; 206 -11.8; 227 -11.5; 249 -11.2; 274 -10.9; 302 -10.5; 332 -10.0; 365 -9.5; 402 -9.0; 442 -8.5; 486 -8.0; 535 -7.4; 588 -6.8; 647 -6.3; 712 -5.7; 783 -5.2; 861 -4.8; 947 -4.8; 1042 -5.1; 1146 -6.0; 1261 -6.8; 1387 -7.2; 1526 -7.4; 1678 -6.9; 1846 -5.7; 2031 -4.1; 2234 -2.6; 2457 -1.3; 2703 -0.7; 2973 -0.8; 3270 -1.7; 3597 -2.5; 3957 -1.1; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -9.2; 8482 -11.5; 9330 -10.1; 10263 -7.6; 11289 -6.5; 12418 -6.9; 13660 -10.2; 15026 -12.0; 16529 -11.9; 18182 -11.8; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Light Harmonic Stella GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Light Harmonic Stella ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 143 Hz   | 0.49 | -5.7 dB  |
| Peaking | 2664 Hz  | 3.52 | 3.7 dB   |
| Peaking | 6758 Hz  | 0.69 | 10.4 dB  |
| Peaking | 8303 Hz  | 2.31 | -13.1 dB |
| Peaking | 16862 Hz | 0.53 | -6.8 dB  |
| Peaking | 29 Hz    | 1.51 | -1.0 dB  |
| Peaking | 320 Hz   | 1.65 | -0.8 dB  |
| Peaking | 867 Hz   | 1.43 | 2.3 dB   |
| Peaking | 1470 Hz  | 2.79 | -2.6 dB  |
| Peaking | 14597 Hz | 7.09 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -7.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Light%20Harmonic%20Stella/Light%20Harmonic%20Stella.png)