# Beyerdynamic DT 1770 (Leatherette Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.5; 25 -10.6; 28 -10.6; 31 -10.4; 34 -10.1; 37 -9.8; 41 -9.6; 45 -9.3; 49 -9.0; 54 -9.2; 60 -10.0; 66 -11.0; 72 -12.1; 79 -12.8; 87 -13.2; 96 -13.9; 106 -14.4; 116 -14.9; 128 -15.1; 141 -14.4; 155 -14.1; 170 -13.3; 187 -11.3; 206 -8.8; 227 -6.8; 249 -5.7; 274 -5.7; 302 -6.3; 332 -6.8; 365 -7.0; 402 -7.1; 442 -7.2; 486 -7.2; 535 -7.0; 588 -6.8; 647 -6.3; 712 -6.2; 783 -6.3; 861 -6.5; 947 -6.5; 1042 -6.4; 1146 -6.2; 1261 -5.8; 1387 -5.3; 1526 -4.5; 1678 -3.1; 1846 -1.7; 2031 -1.2; 2234 -0.6; 2457 -1.0; 2703 -1.1; 2973 -0.5; 3270 -0.8; 3597 -0.9; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.2; 5793 -6.3; 6373 -7.1; 7010 -4.6; 7711 -8.2; 8482 -9.6; 9330 -7.7; 10263 -7.7; 11289 -8.7; 12418 -7.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1770 (Leatherette Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1770 (Leatherette Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.17 | -3.7 dB |
| Peaking | 121 Hz   | 1.34 | -8.3 dB |
| Peaking | 3535 Hz  | 0.71 | 7.4 dB  |
| Peaking | 8298 Hz  | 0.84 | -4.0 dB |
| Peaking | 14233 Hz | 2.76 | 0.8 dB  |
| Peaking | 172 Hz   | 5.16 | -2.4 dB |
| Peaking | 250 Hz   | 3    | 3.1 dB  |
| Peaking | 1551 Hz  | 0.8  | -1.9 dB |
| Peaking | 1937 Hz  | 2.3  | 3.3 dB  |
| Peaking | 16922 Hz | 2.55 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -9.8 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%201770%20(Leatherette%20Earpads)/Beyerdynamic%20DT%201770%20(Leatherette%20Earpads).png)