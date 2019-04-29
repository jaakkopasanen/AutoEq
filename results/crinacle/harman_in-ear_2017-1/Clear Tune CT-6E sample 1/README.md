# Clear Tune CT-6E sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -6.9; 25 -6.9; 28 -7.0; 31 -7.1; 34 -7.2; 37 -7.3; 41 -7.4; 45 -7.5; 49 -7.7; 54 -7.8; 60 -8.0; 66 -8.3; 72 -8.7; 79 -9.1; 87 -9.5; 96 -10.0; 106 -10.3; 116 -10.7; 128 -11.0; 141 -11.3; 155 -11.6; 170 -11.7; 187 -11.8; 206 -11.8; 227 -11.8; 249 -11.7; 274 -11.6; 302 -11.3; 332 -10.9; 365 -10.4; 402 -10.0; 442 -9.5; 486 -8.8; 535 -8.0; 588 -6.9; 647 -5.6; 712 -3.8; 783 -1.3; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -3.8; 1387 -7.2; 1526 -9.5; 1678 -11.5; 1846 -12.9; 2031 -12.2; 2234 -10.1; 2457 -7.9; 2703 -6.2; 2973 -5.5; 3270 -5.4; 3597 -5.4; 3957 -6.9; 4353 -6.0; 4788 -2.4; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.9; 15026 -16.9; 16529 -13.9; 18182 -8.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-6E sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-6E sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 254 Hz   | 0.37 | -5.9 dB  |
| Peaking | 965 Hz   | 1.17 | 10.0 dB  |
| Peaking | 1783 Hz  | 2.21 | -9.1 dB  |
| Peaking | 5704 Hz  | 2.55 | 6.9 dB   |
| Peaking | 15580 Hz | 2.39 | -11.6 dB |
| Peaking | 2989 Hz  | 3.14 | 3.3 dB   |
| Peaking | 3037 Hz  | 1.35 | -1.6 dB  |
| Peaking | 8172 Hz  | 4.63 | -0.9 dB  |
| Peaking | 13168 Hz | 3.37 | 3.3 dB   |
| Peaking | 15009 Hz | 4.02 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 16000 Hz | 1.41 | -9.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Clear%20Tune%20CT-6E%20sample%201/Clear%20Tune%20CT-6E%20sample%201.png)