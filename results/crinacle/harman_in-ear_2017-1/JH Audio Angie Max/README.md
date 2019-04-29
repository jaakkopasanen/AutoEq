# JH Audio Angie Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -11.9; 25 -12.0; 28 -12.0; 31 -12.1; 34 -12.2; 37 -12.2; 41 -12.3; 45 -12.4; 49 -12.5; 54 -12.6; 60 -12.7; 66 -12.9; 72 -13.1; 79 -13.3; 87 -13.5; 96 -13.7; 106 -13.9; 116 -13.9; 128 -13.9; 141 -13.9; 155 -13.8; 170 -13.7; 187 -13.4; 206 -13.1; 227 -12.7; 249 -12.4; 274 -12.0; 302 -11.5; 332 -11.0; 365 -10.5; 402 -10.1; 442 -9.7; 486 -9.2; 535 -8.8; 588 -8.4; 647 -8.0; 712 -7.6; 783 -7.3; 861 -7.3; 947 -7.8; 1042 -9.0; 1146 -10.3; 1261 -11.1; 1387 -11.2; 1526 -10.3; 1678 -8.6; 1846 -6.4; 2031 -4.1; 2234 -2.1; 2457 -0.9; 2703 -0.9; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -13.2; 16529 -20.9; 18182 -27.2; 20000 -27.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Angie Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Angie Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.9  | -3.4 dB  |
| Peaking | 118 Hz   | 0.23 | -7.0 dB  |
| Peaking | 4507 Hz  | 0.82 | 7.4 dB   |
| Peaking | 18984 Hz | 0.92 | -24.6 dB |
| Peaking | 909 Hz   | 0.88 | 5.0 dB   |
| Peaking | 1337 Hz  | 1.06 | -8.9 dB  |
| Peaking | 2326 Hz  | 2    | 5.2 dB   |
| Peaking | 13612 Hz | 1.54 | 10.9 dB  |
| Peaking | 15500 Hz | 0.71 | -7.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -5.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -15.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%20Angie%20Max/JH%20Audio%20Angie%20Max.png)