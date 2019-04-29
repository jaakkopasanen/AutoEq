# Jomo Jazz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.5; 25 -6.7; 28 -7.0; 31 -7.3; 34 -7.5; 37 -7.7; 41 -7.9; 45 -8.1; 49 -8.2; 54 -8.5; 60 -8.8; 66 -9.1; 72 -9.4; 79 -9.7; 87 -10.1; 96 -10.6; 106 -10.9; 116 -11.2; 128 -11.4; 141 -11.7; 155 -11.8; 170 -11.9; 187 -11.9; 206 -11.8; 227 -11.7; 249 -11.7; 274 -11.5; 302 -11.1; 332 -10.7; 365 -10.2; 402 -9.8; 442 -9.4; 486 -8.9; 535 -8.5; 588 -8.0; 647 -7.5; 712 -7.1; 783 -6.6; 861 -6.4; 947 -6.5; 1042 -7.2; 1146 -8.3; 1261 -9.6; 1387 -10.8; 1526 -11.1; 1678 -9.5; 1846 -6.9; 2031 -4.5; 2234 -2.7; 2457 -1.4; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -1.7; 4788 -4.0; 5267 -8.0; 5793 -4.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.2; 16529 -8.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Jazz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Jazz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 142 Hz   | 0.54 | -4.5 dB  |
| Peaking | 304 Hz   | 0.94 | -2.3 dB  |
| Peaking | 1548 Hz  | 1.85 | -10.0 dB |
| Peaking | 2289 Hz  | 0.74 | 7.5 dB   |
| Peaking | 3732 Hz  | 3.29 | 2.5 dB   |
| Peaking | 14 Hz    | 2.02 | 0.7 dB   |
| Peaking | 5345 Hz  | 7.79 | -5.2 dB  |
| Peaking | 6245 Hz  | 6.55 | 5.2 dB   |
| Peaking | 15671 Hz | 4.11 | -5.7 dB  |
| Peaking | 17267 Hz | 2.2  | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Jazz/Jomo%20Jazz.png)