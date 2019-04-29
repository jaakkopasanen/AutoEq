# Advanced Elise
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.7; 25 -12.0; 28 -12.3; 31 -12.5; 34 -12.7; 37 -12.9; 41 -13.1; 45 -13.3; 49 -13.5; 54 -13.6; 60 -13.8; 66 -14.0; 72 -14.3; 79 -14.5; 87 -14.7; 96 -15.0; 106 -15.3; 116 -15.3; 128 -15.4; 141 -15.4; 155 -15.3; 170 -15.1; 187 -14.9; 206 -14.5; 227 -14.1; 249 -13.7; 274 -13.2; 302 -12.6; 332 -11.8; 365 -11.1; 402 -10.4; 442 -9.7; 486 -8.9; 535 -8.1; 588 -7.3; 647 -6.4; 712 -5.5; 783 -4.5; 861 -3.6; 947 -2.9; 1042 -2.6; 1146 -2.5; 1261 -2.6; 1387 -2.6; 1526 -2.5; 1678 -2.3; 1846 -1.6; 2031 -0.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.8; 4788 -0.9; 5267 -0.9; 5793 -1.6; 6373 -3.9; 7010 -7.9; 7711 -7.5; 8482 -6.5; 9330 -6.7; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -12.1; 15026 -21.3; 16529 -27.1; 18182 -28.3; 20000 -22.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced Elise GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced Elise ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 0.26 | -5.7 dB  |
| Peaking | 203 Hz   | 0.49 | -5.8 dB  |
| Peaking | 5971 Hz  | 0.16 | 8.2 dB   |
| Peaking | 17797 Hz | 0.56 | -28.0 dB |
| Peaking | 1627 Hz  | 4.92 | -1.3 dB  |
| Peaking | 5875 Hz  | 2.65 | 2.4 dB   |
| Peaking | 7107 Hz  | 3.35 | -5.6 dB  |
| Peaking | 12559 Hz | 2.3  | 6.5 dB   |
| Peaking | 15222 Hz | 2.37 | -5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB  |
| Peaking | 62 Hz    | 1.41 | -5.4 dB  |
| Peaking | 125 Hz   | 1.41 | -7.5 dB  |
| Peaking | 250 Hz   | 1.41 | -6.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 16000 Hz | 1.41 | -23.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20Elise/Advanced%20Elise.png)