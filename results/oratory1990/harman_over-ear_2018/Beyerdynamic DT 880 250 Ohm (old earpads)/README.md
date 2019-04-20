# Beyerdynamic DT 880 250 Ohm (old earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.9; 72 -1.5; 79 -2.2; 87 -2.9; 96 -3.6; 106 -4.3; 116 -4.8; 128 -5.3; 141 -5.8; 155 -6.2; 170 -6.5; 187 -6.7; 206 -7.0; 227 -7.1; 249 -7.1; 274 -7.1; 302 -7.0; 332 -6.9; 365 -6.9; 402 -6.8; 442 -6.7; 486 -6.5; 535 -6.5; 588 -6.5; 647 -6.6; 712 -6.7; 783 -6.8; 861 -7.0; 947 -7.1; 1042 -7.1; 1146 -6.9; 1261 -6.8; 1387 -6.7; 1526 -6.7; 1678 -6.9; 1846 -7.0; 2031 -7.0; 2234 -7.0; 2457 -7.1; 2703 -7.3; 2973 -7.1; 3270 -6.1; 3597 -5.0; 3957 -4.8; 4353 -4.5; 4788 -3.6; 5267 -4.7; 5793 -8.5; 6373 -9.2; 7010 -7.5; 7711 -7.6; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.8; 13660 -6.6; 15026 -6.5; 16529 -9.6; 18182 -13.8; 20000 -14.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm (old earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm (old earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.29 | 7.2 dB  |
| Peaking | 155 Hz   | 0.57 | -3.8 dB |
| Peaking | 4951 Hz  | 2.78 | 4.5 dB  |
| Peaking | 6040 Hz  | 3.4  | -4.6 dB |
| Peaking | 19224 Hz | 1.04 | -9.1 dB |
| Peaking | 2831 Hz  | 1.23 | -1.1 dB |
| Peaking | 3629 Hz  | 4.16 | 1.7 dB  |
| Peaking | 15243 Hz | 2.88 | 2.0 dB  |
| Peaking | 17487 Hz | 2.99 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20880%20250%20Ohm%20(old%20earpads)/Beyerdynamic%20DT%20880%20250%20Ohm%20(old%20earpads).png)