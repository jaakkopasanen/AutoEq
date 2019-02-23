# JBL Duet NC (ANC Off)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -11.2; 25 -11.6; 28 -11.8; 31 -11.9; 34 -12.1; 37 -12.4; 41 -12.5; 45 -12.2; 49 -11.9; 54 -11.3; 60 -10.4; 66 -9.8; 72 -8.7; 79 -7.4; 87 -7.4; 96 -8.0; 106 -8.4; 116 -8.1; 128 -8.4; 141 -9.3; 155 -9.8; 170 -9.2; 187 -7.9; 206 -6.3; 227 -4.1; 249 -2.1; 274 -0.8; 302 -0.5; 332 -1.1; 365 -1.8; 402 -2.7; 442 -3.4; 486 -4.2; 535 -5.9; 588 -6.7; 647 -7.3; 712 -8.1; 783 -8.8; 861 -9.4; 947 -9.6; 1042 -9.6; 1146 -9.1; 1261 -8.4; 1387 -8.5; 1526 -8.2; 1678 -6.9; 1846 -5.8; 2031 -4.9; 2234 -4.1; 2457 -4.1; 2703 -4.6; 2973 -1.6; 3270 -2.5; 3597 -8.3; 3957 -9.0; 4353 -7.9; 4788 -6.8; 5267 -1.4; 5793 -7.7; 6373 -5.0; 7010 -6.5; 7711 -8.6; 8482 -7.8; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -8.6; 13660 -8.5; 15026 -6.2; 16529 -6.8; 18182 -8.3; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Duet NC (ANC Off) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Duet NC (ANC Off) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.78 | -6.6 dB |
| Peaking | 167 Hz   | 1.83 | -5.2 dB |
| Peaking | 294 Hz   | 1.19 | 7.0 dB  |
| Peaking | 920 Hz   | 1.34 | -4.2 dB |
| Peaking | 3030 Hz  | 6.93 | 5.7 dB  |
| Peaking | 2246 Hz  | 4.18 | 2.5 dB  |
| Peaking | 3820 Hz  | 6.48 | -4.0 dB |
| Peaking | 12863 Hz | 6.62 | -1.9 dB |
| Peaking | 13291 Hz | 4.92 | -1.7 dB |
| Peaking | 18795 Hz | 1.3  | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/JBL%20Duet%20NC%20(ANC%20Off)/JBL%20Duet%20NC%20(ANC%20Off).png)