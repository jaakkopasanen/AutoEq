# Stealthsonics U4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.0; 25 -10.1; 28 -10.3; 31 -10.4; 34 -10.5; 37 -10.6; 41 -10.7; 45 -10.8; 49 -10.9; 54 -11.1; 60 -11.3; 66 -11.6; 72 -11.9; 79 -12.2; 87 -12.5; 96 -12.9; 106 -13.2; 116 -13.5; 128 -13.6; 141 -13.9; 155 -14.0; 170 -14.0; 187 -14.0; 206 -13.8; 227 -13.6; 249 -13.4; 274 -13.0; 302 -12.5; 332 -12.0; 365 -11.4; 402 -10.9; 442 -10.4; 486 -9.7; 535 -9.0; 588 -8.2; 647 -7.4; 712 -6.5; 783 -5.5; 861 -4.7; 947 -4.2; 1042 -4.0; 1146 -4.2; 1261 -4.3; 1387 -4.0; 1526 -3.6; 1678 -3.4; 1846 -3.4; 2031 -2.4; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -1.6; 5267 -3.4; 5793 -7.7; 6373 -10.6; 7010 -8.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.8; 18182 -12.7; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stealthsonics U4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stealthsonics U4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.29 | -3.8 dB |
| Peaking | 165 Hz   | 0.77 | -5.2 dB |
| Peaking | 331 Hz   | 1.37 | -3.1 dB |
| Peaking | 2733 Hz  | 0.87 | 6.6 dB  |
| Peaking | 19115 Hz | 1.19 | -7.3 dB |
| Peaking | 979 Hz   | 1.71 | 2.9 dB  |
| Peaking | 1634 Hz  | 0.32 | -1.2 dB |
| Peaking | 4782 Hz  | 1.59 | 3.8 dB  |
| Peaking | 6201 Hz  | 3.83 | -7.5 dB |
| Peaking | 15434 Hz | 3.75 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -6.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Stealthsonics%20U4/Stealthsonics%20U4.png)