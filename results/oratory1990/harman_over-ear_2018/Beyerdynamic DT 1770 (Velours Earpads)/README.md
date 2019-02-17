# Beyerdynamic DT 1770 (Velours Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.7; 25 -9.8; 28 -10.0; 31 -10.1; 34 -10.0; 37 -9.8; 41 -9.6; 45 -9.5; 49 -9.5; 54 -8.8; 60 -7.4; 66 -7.6; 72 -9.1; 79 -10.0; 87 -10.7; 96 -11.3; 106 -11.7; 116 -12.2; 128 -12.0; 141 -11.6; 155 -10.7; 170 -10.0; 187 -8.4; 206 -6.3; 227 -4.7; 249 -4.1; 274 -4.4; 302 -5.2; 332 -5.9; 365 -6.3; 402 -6.7; 442 -6.9; 486 -6.9; 535 -6.8; 588 -6.4; 647 -5.8; 712 -5.7; 783 -5.6; 861 -5.8; 947 -6.3; 1042 -6.4; 1146 -5.9; 1261 -5.1; 1387 -4.3; 1526 -3.4; 1678 -1.8; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -4.5; 5267 -7.8; 5793 -9.4; 6373 -9.9; 7010 -9.5; 7711 -11.3; 8482 -10.7; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1770 (Velours Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1770 (Velours Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.2  | -3.6 dB |
| Peaking | 128 Hz  | 0.95 | -6.0 dB |
| Peaking | 241 Hz  | 2.4  | 4.8 dB  |
| Peaking | 3483 Hz | 0.65 | 8.6 dB  |
| Peaking | 6518 Hz | 1.26 | -8.6 dB |
| Peaking | 1095 Hz | 2.58 | -1.6 dB |
| Peaking | 1867 Hz | 3.74 | 2.1 dB  |
| Peaking | 3421 Hz | 2.39 | -1.5 dB |
| Peaking | 4456 Hz | 4.04 | 4.0 dB  |
| Peaking | 5051 Hz | 5.58 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | 3.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%201770%20(Velours%20Earpads)/Beyerdynamic%20DT%201770%20(Velours%20Earpads).png)