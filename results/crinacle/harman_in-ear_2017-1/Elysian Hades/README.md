# Elysian Hades
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.6; 25 -5.0; 28 -5.4; 31 -5.7; 34 -6.0; 37 -6.2; 41 -6.5; 45 -6.7; 49 -7.0; 54 -7.3; 60 -7.6; 66 -8.0; 72 -8.4; 79 -8.7; 87 -9.1; 96 -9.6; 106 -9.9; 116 -10.4; 128 -10.7; 141 -10.9; 155 -11.1; 170 -11.3; 187 -11.4; 206 -11.4; 227 -11.4; 249 -11.3; 274 -11.1; 302 -10.9; 332 -10.5; 365 -10.1; 402 -9.8; 442 -9.4; 486 -9.0; 535 -8.5; 588 -8.0; 647 -7.4; 712 -6.7; 783 -6.1; 861 -5.5; 947 -5.2; 1042 -5.2; 1146 -5.5; 1261 -5.6; 1387 -5.3; 1526 -4.6; 1678 -3.8; 1846 -3.0; 2031 -2.2; 2234 -1.5; 2457 -1.2; 2703 -1.3; 2973 -1.2; 3270 -0.8; 3597 -0.5; 3957 -0.7; 4353 -1.8; 4788 -4.1; 5267 -5.9; 5793 -4.0; 6373 -2.4; 7010 -4.1; 7711 -6.1; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.4; 13660 -12.9; 15026 -22.3; 16529 -28.2; 18182 -26.2; 20000 -13.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Elysian Hades GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Elysian Hades ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.63 | 3.2 dB   |
| Peaking | 204 Hz   | 0.46 | -5.3 dB  |
| Peaking | 3867 Hz  | 0.46 | 7.0 dB   |
| Peaking | 12078 Hz | 1.25 | 12.0 dB  |
| Peaking | 16677 Hz | 0.58 | -26.3 dB |
| Peaking | 894 Hz   | 3.21 | 1.0 dB   |
| Peaking | 1355 Hz  | 3.05 | -1.4 dB  |
| Peaking | 5241 Hz  | 3.83 | -6.8 dB  |
| Peaking | 5952 Hz  | 1.39 | 4.9 dB   |
| Peaking | 7741 Hz  | 1.55 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 16000 Hz | 1.41 | -23.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Elysian%20Hades/Elysian%20Hades.png)