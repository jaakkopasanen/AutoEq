# Eternal Melody EM6W
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.7; 25 -6.9; 28 -7.3; 31 -7.5; 34 -7.8; 37 -8.1; 41 -8.4; 45 -8.6; 49 -8.8; 54 -9.1; 60 -9.4; 66 -9.8; 72 -10.1; 79 -10.5; 87 -10.9; 96 -11.4; 106 -11.8; 116 -12.1; 128 -12.3; 141 -12.6; 155 -12.8; 170 -12.9; 187 -12.9; 206 -12.9; 227 -12.7; 249 -12.6; 274 -12.3; 302 -11.9; 332 -11.5; 365 -10.9; 402 -10.5; 442 -10.0; 486 -9.4; 535 -8.8; 588 -8.1; 647 -7.4; 712 -6.6; 783 -5.9; 861 -5.2; 947 -4.8; 1042 -4.9; 1146 -5.2; 1261 -5.7; 1387 -5.9; 1526 -5.8; 1678 -5.5; 1846 -5.0; 2031 -4.0; 2234 -2.7; 2457 -1.6; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.3; 5793 -2.4; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.7; 15026 -19.2; 16529 -17.6; 18182 -15.5; 20000 -21.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Eternal Melody EM6W GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Eternal Melody EM6W ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 138 Hz   | 0.54 | -5.4 dB  |
| Peaking | 300 Hz   | 1.01 | -2.8 dB  |
| Peaking | 4894 Hz  | 0.52 | 9.4 dB   |
| Peaking | 12082 Hz | 2.09 | 8.7 dB   |
| Peaking | 17010 Hz | 0.23 | -13.1 dB |
| Peaking | 920 Hz   | 3.18 | 1.6 dB   |
| Peaking | 1589 Hz  | 3.11 | -1.7 dB  |
| Peaking | 15398 Hz | 3.09 | -5.9 dB  |
| Peaking | 18145 Hz | 0.71 | 4.2 dB   |
| Peaking | 19926 Hz | 1.63 | -6.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -14.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Eternal%20Melody%20EM6W/Eternal%20Melody%20EM6W.png)