# Dita Audio Fidelity
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -7.9; 25 -7.8; 28 -7.7; 31 -7.6; 34 -7.4; 37 -7.3; 41 -7.1; 45 -7.0; 49 -6.8; 54 -6.6; 60 -6.5; 66 -6.4; 72 -6.4; 79 -6.5; 87 -6.5; 96 -6.7; 106 -6.7; 116 -6.7; 128 -7.0; 141 -7.0; 155 -7.1; 170 -7.6; 187 -7.3; 206 -7.0; 227 -6.8; 249 -6.7; 274 -6.4; 302 -6.1; 332 -5.8; 365 -5.4; 402 -5.1; 442 -4.8; 486 -4.4; 535 -4.0; 588 -3.6; 647 -3.2; 712 -2.8; 783 -2.4; 861 -2.1; 947 -2.0; 1042 -2.3; 1146 -2.9; 1261 -3.4; 1387 -3.4; 1526 -2.9; 1678 -2.4; 1846 -2.0; 2031 -1.4; 2234 -0.8; 2457 -0.5; 2703 -0.6; 2973 -1.1; 3270 -2.2; 3597 -3.6; 3957 -5.3; 4353 -7.4; 4788 -8.6; 5267 -6.9; 5793 -3.5; 6373 -1.1; 7010 -1.8; 7711 -4.3; 8482 -7.0; 9330 -6.3; 10263 -5.1; 11289 -6.1; 12418 -8.0; 13660 -12.1; 15026 -17.4; 16529 -20.9; 18182 -23.1; 20000 -23.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Fidelity GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Fidelity ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.22 | -3.6 dB  |
| Peaking | 186 Hz   | 0.91 | -2.8 dB  |
| Peaking | 4606 Hz  | 2.58 | -8.9 dB  |
| Peaking | 8544 Hz  | 0.26 | 11.9 dB  |
| Peaking | 17939 Hz | 0.26 | -24.6 dB |
| Peaking | 862 Hz   | 2.02 | 1.5 dB   |
| Peaking | 1368 Hz  | 3.15 | -1.6 dB  |
| Peaking | 6580 Hz  | 6.39 | 3.1 dB   |
| Peaking | 8553 Hz  | 3.95 | -3.6 dB  |
| Peaking | 11395 Hz | 2.7  | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 16000 Hz | 1.41 | -22.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dita%20Audio%20Fidelity/Dita%20Audio%20Fidelity.png)