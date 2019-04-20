# JBL Duet NC (ANC On)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.8; 23 -14.3; 25 -13.8; 28 -13.1; 31 -12.5; 34 -11.9; 37 -11.5; 41 -11.0; 45 -10.6; 49 -10.4; 54 -10.2; 60 -10.0; 66 -9.8; 72 -9.6; 79 -9.4; 87 -9.2; 96 -9.6; 106 -9.8; 116 -9.8; 128 -9.6; 141 -9.1; 155 -8.5; 170 -7.7; 187 -6.9; 206 -6.3; 227 -5.6; 249 -4.8; 274 -3.8; 302 -3.0; 332 -2.4; 365 -2.2; 402 -2.2; 442 -2.0; 486 -1.3; 535 -1.7; 588 -2.0; 647 -2.2; 712 -3.0; 783 -3.9; 861 -5.1; 947 -6.5; 1042 -8.0; 1146 -9.0; 1261 -8.9; 1387 -9.2; 1526 -9.7; 1678 -8.0; 1846 -6.4; 2031 -5.1; 2234 -4.2; 2457 -4.4; 2703 -5.3; 2973 -4.5; 3270 -0.5; 3597 -2.0; 3957 -7.4; 4353 -7.6; 4788 -6.1; 5267 -1.6; 5793 -7.1; 6373 -4.4; 7010 -5.6; 7711 -9.3; 8482 -9.2; 9330 -5.7; 10263 -5.6; 11289 -5.6; 12418 -6.4; 13660 -5.9; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Duet NC (ANC On) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Duet NC (ANC On) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 15 Hz   |  0.68 | -8.3 dB |
| Peaking | 30 Hz   |  0.41 | -3.0 dB |
| Peaking | 138 Hz  |  0.77 | -4.9 dB |
| Peaking | 692 Hz  |  0.29 | 6.3 dB  |
| Peaking | 1245 Hz |  1.19 | -9.6 dB |
| Peaking | 1555 Hz |  9.78 | -1.5 dB |
| Peaking | 3431 Hz |  6.61 | 7.2 dB  |
| Peaking | 4111 Hz |  2.87 | -4.3 dB |
| Peaking | 5221 Hz | 10.99 | 5.0 dB  |
| Peaking | 8080 Hz |  6.06 | -5.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 5.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/JBL%20Duet%20NC%20(ANC%20On)/JBL%20Duet%20NC%20(ANC%20On).png)