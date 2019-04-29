# Vsonic VC02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.8; 25 -7.1; 28 -7.5; 31 -7.9; 34 -8.1; 37 -8.4; 41 -8.6; 45 -8.8; 49 -9.0; 54 -9.3; 60 -9.6; 66 -9.9; 72 -10.3; 79 -10.7; 87 -11.0; 96 -11.4; 106 -11.7; 116 -12.0; 128 -12.4; 141 -12.6; 155 -12.7; 170 -12.8; 187 -12.8; 206 -12.7; 227 -12.6; 249 -12.5; 274 -12.3; 302 -12.0; 332 -11.6; 365 -11.2; 402 -10.9; 442 -10.6; 486 -10.2; 535 -9.7; 588 -9.2; 647 -8.8; 712 -8.2; 783 -7.7; 861 -7.4; 947 -7.2; 1042 -7.2; 1146 -7.8; 1261 -8.6; 1387 -8.8; 1526 -7.9; 1678 -6.4; 1846 -4.1; 2031 -4.2; 2234 -2.7; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.8; 9330 -11.5; 10263 -9.1; 11289 -6.7; 12418 -7.5; 13660 -15.1; 15026 -23.8; 16529 -24.6; 18182 -18.2; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vsonic VC02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vsonic VC02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 176 Hz   | 0.53 | -4.3 dB  |
| Peaking | 341 Hz   | 0.11 | -2.2 dB  |
| Peaking | 3715 Hz  | 0.77 | 8.1 dB   |
| Peaking | 15343 Hz | 2.94 | -10.5 dB |
| Peaking | 17095 Hz | 0.98 | -14.5 dB |
| Peaking | 1345 Hz  | 1.1  | 3.1 dB   |
| Peaking | 1389 Hz  | 2.45 | -5.5 dB  |
| Peaking | 6211 Hz  | 4.57 | 3.1 dB   |
| Peaking | 9057 Hz  | 3.5  | -5.7 dB  |
| Peaking | 11793 Hz | 3.82 | 4.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -21.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vsonic%20VC02/Vsonic%20VC02.png)