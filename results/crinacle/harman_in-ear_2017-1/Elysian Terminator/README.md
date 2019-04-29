# Elysian Terminator
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.6; 25 -7.0; 28 -7.4; 31 -7.8; 34 -8.0; 37 -8.2; 41 -8.5; 45 -8.7; 49 -8.9; 54 -9.2; 60 -9.5; 66 -9.7; 72 -10.0; 79 -10.3; 87 -10.6; 96 -10.9; 106 -11.2; 116 -11.5; 128 -11.7; 141 -11.7; 155 -11.8; 170 -11.8; 187 -11.7; 206 -11.6; 227 -11.4; 249 -11.1; 274 -10.9; 302 -10.5; 332 -10.1; 365 -9.6; 402 -9.3; 442 -8.9; 486 -8.4; 535 -8.0; 588 -7.5; 647 -7.0; 712 -6.5; 783 -6.0; 861 -5.6; 947 -5.5; 1042 -5.8; 1146 -6.5; 1261 -7.0; 1387 -7.1; 1526 -6.9; 1678 -6.6; 1846 -6.4; 2031 -5.9; 2234 -5.2; 2457 -4.3; 2703 -3.7; 2973 -2.7; 3270 -1.0; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.1; 6373 -2.5; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.3; 15026 -26.6; 16529 -32.5; 18182 -21.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Elysian Terminator GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Elysian Terminator ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 168 Hz   | 0.37 | -5.5 dB  |
| Peaking | 864 Hz   | 2.4  | 0.9 dB   |
| Peaking | 1705 Hz  | 0.99 | -5.9 dB  |
| Peaking | 5082 Hz  | 0.2  | 8.0 dB   |
| Peaking | 16351 Hz | 1.44 | -32.4 dB |
| Peaking | 2638 Hz  | 3.28 | -1.3 dB  |
| Peaking | 5232 Hz  | 0.77 | 1.5 dB   |
| Peaking | 7864 Hz  | 2.1  | -4.2 dB  |
| Peaking | 12907 Hz | 2.54 | 7.2 dB   |
| Peaking | 14977 Hz | 3.1  | -7.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 16000 Hz | 1.41 | -24.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Elysian%20Terminator/Elysian%20Terminator.png)