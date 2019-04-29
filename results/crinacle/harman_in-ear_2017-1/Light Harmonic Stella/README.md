# Light Harmonic Stella
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.2; 25 -9.3; 28 -9.5; 31 -9.6; 34 -9.7; 37 -9.9; 41 -10.1; 45 -10.2; 49 -10.3; 54 -10.5; 60 -10.8; 66 -11.0; 72 -11.3; 79 -11.6; 87 -11.9; 96 -12.2; 106 -12.5; 116 -12.8; 128 -13.0; 141 -13.1; 155 -13.2; 170 -13.2; 187 -13.1; 206 -12.9; 227 -12.7; 249 -12.4; 274 -12.0; 302 -11.6; 332 -11.0; 365 -10.4; 402 -9.9; 442 -9.3; 486 -8.7; 535 -8.1; 588 -7.5; 647 -6.9; 712 -6.3; 783 -5.8; 861 -5.5; 947 -5.6; 1042 -6.0; 1146 -6.7; 1261 -7.3; 1387 -7.4; 1526 -7.4; 1678 -6.7; 1846 -5.5; 2031 -3.6; 2234 -1.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.5; 8482 -9.8; 9330 -11.0; 10263 -9.9; 11289 -7.2; 12418 -9.4; 13660 -19.2; 15026 -28.3; 16529 -30.7; 18182 -28.3; 20000 -21.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Light Harmonic Stella GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Light Harmonic Stella ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 62 Hz    | 0.28 | -3.3 dB  |
| Peaking | 196 Hz   | 0.63 | -4.7 dB  |
| Peaking | 4219 Hz  | 0.74 | 7.6 dB   |
| Peaking | 15810 Hz | 2.02 | -15.3 dB |
| Peaking | 18553 Hz | 0.69 | -20.1 dB |
| Peaking | 1579 Hz  | 3.06 | -2.8 dB  |
| Peaking | 2434 Hz  | 2.68 | 3.0 dB   |
| Peaking | 6378 Hz  | 2.17 | 5.9 dB   |
| Peaking | 9645 Hz  | 0.63 | -6.8 dB  |
| Peaking | 11737 Hz | 2.59 | 11.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 16000 Hz | 1.41 | -31.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Light%20Harmonic%20Stella/Light%20Harmonic%20Stella.png)