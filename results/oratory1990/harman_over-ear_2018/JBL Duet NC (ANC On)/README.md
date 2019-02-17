# JBL Duet NC (ANC On)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.4; 25 -12.9; 28 -12.2; 31 -11.6; 34 -11.0; 37 -10.6; 41 -10.1; 45 -9.7; 49 -9.5; 54 -9.3; 60 -9.2; 66 -8.9; 72 -8.8; 79 -8.6; 87 -8.3; 96 -8.7; 106 -8.9; 116 -8.9; 128 -8.8; 141 -8.2; 155 -7.6; 170 -6.8; 187 -6.1; 206 -5.4; 227 -4.7; 249 -3.9; 274 -3.0; 302 -2.1; 332 -1.5; 365 -1.4; 402 -1.3; 442 -1.1; 486 -0.5; 535 -0.9; 588 -1.1; 647 -1.3; 712 -2.1; 783 -3.0; 861 -4.2; 947 -5.7; 1042 -7.1; 1146 -8.1; 1261 -8.0; 1387 -8.2; 1526 -8.8; 1678 -7.1; 1846 -5.5; 2031 -4.3; 2234 -3.3; 2457 -3.5; 2703 -4.4; 2973 -3.6; 3270 -0.7; 3597 -1.7; 3957 -6.6; 4353 -6.7; 4788 -5.6; 5267 -0.7; 5793 -6.8; 6373 -3.4; 7010 -4.9; 7711 -8.4; 8482 -8.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Duet NC (ANC On) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Duet NC (ANC On) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 437 Hz   | 1.06 | 6.5 dB  |
| Peaking | 2308 Hz  | 5.58 | 3.1 dB  |
| Peaking | 3343 Hz  | 5.34 | 6.1 dB  |
| Peaking | 22042 Hz | 2.28 | 1.0 dB  |
| Peaking | 13 Hz    | 0.38 | -8.5 dB |
| Peaking | 121 Hz   | 1.83 | -2.4 dB |
| Peaking | 1335 Hz  | 2.79 | -3.2 dB |
| Peaking | 6983 Hz  | 2.13 | 4.6 dB  |
| Peaking | 7786 Hz  | 3.82 | -5.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | 2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 7.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/JBL%20Duet%20NC%20(ANC%20On)/JBL%20Duet%20NC%20(ANC%20On).png)