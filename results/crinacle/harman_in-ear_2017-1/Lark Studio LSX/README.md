# Lark Studio LSX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -9.1; 25 -9.4; 28 -9.9; 31 -10.2; 34 -10.4; 37 -10.5; 41 -10.7; 45 -10.9; 49 -11.1; 54 -11.4; 60 -11.5; 66 -11.8; 72 -12.0; 79 -12.3; 87 -12.6; 96 -12.8; 106 -13.2; 116 -13.3; 128 -13.4; 141 -13.5; 155 -13.5; 170 -13.4; 187 -13.3; 206 -13.1; 227 -12.8; 249 -12.5; 274 -12.2; 302 -11.7; 332 -11.1; 365 -10.5; 402 -10.1; 442 -9.5; 486 -9.0; 535 -8.4; 588 -7.9; 647 -7.3; 712 -6.8; 783 -6.3; 861 -5.9; 947 -5.9; 1042 -6.1; 1146 -6.6; 1261 -7.0; 1387 -7.4; 1526 -7.3; 1678 -6.7; 1846 -5.9; 2031 -5.0; 2234 -3.7; 2457 -1.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -2.7; 5793 -5.8; 6373 -5.7; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.9; 15026 -15.5; 16529 -19.1; 18182 -18.7; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lark Studio LSX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lark Studio LSX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 54 Hz    | 0.38 | -3.8 dB  |
| Peaking | 137 Hz   | 0.81 | -3.5 dB  |
| Peaking | 271 Hz   | 0.89 | -3.5 dB  |
| Peaking | 3634 Hz  | 1.14 | 7.0 dB   |
| Peaking | 17753 Hz | 0.98 | -14.5 dB |
| Peaking | 1525 Hz  | 0.88 | 3.4 dB   |
| Peaking | 1538 Hz  | 1.66 | -5.4 dB  |
| Peaking | 5959 Hz  | 9.83 | -2.6 dB  |
| Peaking | 12870 Hz | 2    | 4.0 dB   |
| Peaking | 15326 Hz | 2.59 | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -13.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lark%20Studio%20LSX/Lark%20Studio%20LSX.png)