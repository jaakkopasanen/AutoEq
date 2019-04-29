# Stealthsonics U2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.5; 25 -11.7; 28 -11.8; 31 -11.9; 34 -12.0; 37 -12.1; 41 -12.2; 45 -12.3; 49 -12.3; 54 -12.5; 60 -12.6; 66 -12.8; 72 -12.9; 79 -13.1; 87 -13.3; 96 -13.5; 106 -13.6; 116 -13.7; 128 -13.7; 141 -13.7; 155 -13.6; 170 -13.3; 187 -13.0; 206 -12.6; 227 -12.2; 249 -11.8; 274 -11.2; 302 -10.6; 332 -9.8; 365 -9.1; 402 -8.5; 442 -7.8; 486 -7.1; 535 -6.3; 588 -5.6; 647 -4.9; 712 -4.2; 783 -3.4; 861 -3.0; 947 -2.7; 1042 -3.0; 1146 -3.7; 1261 -4.4; 1387 -4.8; 1526 -4.9; 1678 -4.8; 1846 -4.3; 2031 -2.9; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -2.5; 4353 -5.5; 4788 -5.6; 5267 -5.4; 5793 -8.5; 6373 -11.9; 7010 -7.1; 7711 -6.1; 8482 -6.9; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -15.7; 16529 -15.8; 18182 -14.1; 20000 -22.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stealthsonics U2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stealthsonics U2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.32 | -4.4 dB |
| Peaking | 161 Hz  | 0.53 | -5.8 dB |
| Peaking | 848 Hz  | 1.28 | 4.2 dB  |
| Peaking | 2834 Hz | 1.79 | 6.9 dB  |
| Peaking | 1043 Hz | 5.83 | 0.4 dB  |
| Peaking | 1478 Hz | 4.07 | -0.5 dB |
| Peaking | 3691 Hz | 9.02 | 2.8 dB  |
| Peaking | 5414 Hz | 7.76 | 1.1 dB  |
| Peaking | 6250 Hz | 6.1  | -6.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -10.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Stealthsonics%20U2/Stealthsonics%20U2.png)