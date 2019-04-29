# Whizzer A-HE03 Kylin
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.1; 25 -10.2; 28 -10.4; 31 -10.6; 34 -10.7; 37 -10.8; 41 -11.0; 45 -11.1; 49 -11.2; 54 -11.4; 60 -11.6; 66 -11.9; 72 -12.1; 79 -12.4; 87 -12.7; 96 -13.0; 106 -13.3; 116 -13.5; 128 -13.7; 141 -13.9; 155 -13.9; 170 -13.8; 187 -13.7; 206 -13.5; 227 -13.3; 249 -12.9; 274 -12.5; 302 -12.0; 332 -11.4; 365 -10.8; 402 -10.1; 442 -9.4; 486 -8.7; 535 -7.9; 588 -7.1; 647 -6.2; 712 -5.3; 783 -4.4; 861 -3.6; 947 -3.1; 1042 -3.2; 1146 -3.7; 1261 -4.3; 1387 -4.6; 1526 -4.5; 1678 -4.1; 1846 -3.6; 2031 -3.0; 2234 -2.2; 2457 -1.7; 2703 -1.5; 2973 -1.4; 3270 -1.6; 3597 -2.3; 3957 -3.7; 4353 -5.1; 4788 -4.3; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -14.9; 15026 -24.7; 16529 -28.2; 18182 -26.2; 20000 -22.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Whizzer A-HE03 Kylin GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Whizzer A-HE03 Kylin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 62 Hz    | 0.25 | -4.3 dB  |
| Peaking | 216 Hz   | 0.58 | -5.0 dB  |
| Peaking | 6875 Hz  | 0.23 | 20.9 dB  |
| Peaking | 12418 Hz | 1.73 | 12.8 dB  |
| Peaking | 15594 Hz | 0.24 | -36.1 dB |
| Peaking | 937 Hz   | 3.09 | 1.8 dB   |
| Peaking | 1512 Hz  | 2.03 | -2.0 dB  |
| Peaking | 4520 Hz  | 2.62 | -8.5 dB  |
| Peaking | 5328 Hz  | 1.08 | 6.6 dB   |
| Peaking | 7696 Hz  | 2.44 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 16000 Hz | 1.41 | -26.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Whizzer%20A-HE03%20Kylin/Whizzer%20A-HE03%20Kylin.png)