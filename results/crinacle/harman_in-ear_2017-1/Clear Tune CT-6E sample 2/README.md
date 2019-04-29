# Clear Tune CT-6E sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.9; 25 -3.1; 28 -3.3; 31 -3.5; 34 -3.6; 37 -3.8; 41 -4.0; 45 -4.2; 49 -4.5; 54 -4.7; 60 -4.9; 66 -5.3; 72 -5.7; 79 -6.0; 87 -6.4; 96 -6.9; 106 -7.3; 116 -7.6; 128 -8.0; 141 -8.5; 155 -8.8; 170 -9.0; 187 -9.0; 206 -9.1; 227 -9.3; 249 -9.3; 274 -9.3; 302 -9.2; 332 -9.0; 365 -8.7; 402 -8.6; 442 -8.5; 486 -8.3; 535 -8.0; 588 -7.8; 647 -7.5; 712 -7.2; 783 -6.9; 861 -6.8; 947 -6.9; 1042 -7.4; 1146 -8.2; 1261 -9.0; 1387 -9.5; 1526 -10.0; 1678 -10.7; 1846 -11.1; 2031 -10.0; 2234 -7.9; 2457 -5.5; 2703 -4.0; 2973 -3.8; 3270 -4.3; 3597 -4.5; 3957 -5.2; 4353 -4.8; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -13.3; 16529 -15.5; 18182 -9.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-6E sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-6E sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.23 | 3.7 dB   |
| Peaking | 212 Hz   | 0.54 | -3.2 dB  |
| Peaking | 1704 Hz  | 2.72 | -5.0 dB  |
| Peaking | 5462 Hz  | 1.81 | 6.5 dB   |
| Peaking | 16345 Hz | 2.13 | -10.5 dB |
| Peaking | 2074 Hz  | 4.65 | -2.0 dB  |
| Peaking | 2771 Hz  | 2.57 | 2.9 dB   |
| Peaking | 4167 Hz  | 7.88 | -2.5 dB  |
| Peaking | 7954 Hz  | 5.44 | -1.7 dB  |
| Peaking | 13419 Hz | 5.51 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -8.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Clear%20Tune%20CT-6E%20sample%202/Clear%20Tune%20CT-6E%20sample%202.png)